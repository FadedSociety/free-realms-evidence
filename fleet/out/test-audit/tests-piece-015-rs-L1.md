<!-- fleet job=test-audit id=tests-piece-015-rs-L1 status=done turns=4 usd=0.0039 tokens(read,write,in,out)=[20987, 14774, 10, 3592] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_015.rs lines 1-153 of 153

Window: `prototype/osfr-tools/tests/piece_015.rs` lines 1-153. Read against `prototype/osfr-tools/src/restoration/piece_015.rs` (all 282 lines).

- **[high] prototype/osfr-tools/tests/piece_015.rs:129 real_tables_match_the_recovered_catalogue_counts - the only check against shipped data returns early and passes whenever the lab is absent, which is the case in this repo.**
  - Why it cannot catch a regression: `lab_resources()` (lines 46-56) resolves `CARGO_MANIFEST_DIR/../../lab/working/...`. The repo root has no `lab/` directory (checked with `list` on the repo root: `.git`, `AGENTS.md`, `MODLOG.md`, `docs/`, `launcher/`, `notes/`, `prototype/`, `recovery-manifest.json`, `scripts/`, `setup-manifest.json`, `tests/`). So line 130-133 hits `eprintln!` and `return`, and the test reports ok. Any change to the parser, `launch_mode`, or `counts` that breaks the 783/22/20/610 counts or the row 139/802 lookups still passes on the integrator.
  - Fix: make the test fail (or be `#[ignore = "requires lab"]` and run in a lab-enabled job) when the fixture is absent on the gate. For example, panic when `CI`/a gate env var is set and `lab_resources()` is `None`, or ship a hash-pinned copy of the four tables under `tests/fixtures/` so the test never depends on the lab.

- **[medium] prototype/osfr-tools/tests/piece_015.rs:119-126 group_links_resolve_to_game_rows - the name claims links resolve to game rows, but the fixture has no dangling link, so the filter that drops links to unknown games is never exercised.**
  - Why it cannot catch a regression: `games_in_group` (src line 262-272) filters with `self.games.contains_key(&link.link_game)` and also dedups. Both `LINK_TABLE` rows (`1^5^0^1…` and `2^5^0^2…`) point at games 1 and 2, which exist. Deleting the `contains_key` predicate or the `dedup()` still returns `[1, 2]`, so the test passes. The only "unknown" case, `games_in_group(99)`, tests an unknown group, not an unknown game.
  - Fix: add a link row whose `LINK_GAME_ID` is not in `GAME_TABLE` (e.g. `3^5^0^99^…`) and a duplicate link (e.g. `4^5^0^1^…`), then assert `games_in_group(5) == vec![1, 2]`. This fails if the existence filter or dedup is removed.

No other problems in this window. I checked the `malformed_row_reports_source_and_line` header field count (14, including the trailing empty field), the line number 4, and the `duplicate_game_id` and `launch_mode` expectations against the parser, and they are correct.
