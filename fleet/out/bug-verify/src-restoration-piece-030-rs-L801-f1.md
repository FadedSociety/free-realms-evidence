<!-- fleet job=bug-verify id=src-restoration-piece-030-rs-L801-f1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[35965, 18347, 12, 3756] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_030.rs:1025

**Verdict:** refuted (the server-reachability premise fails; the logic slip itself is real but test-only)

**Severity if confirmed:** n/a. If anything, low: it affects only the acceptance-transcript checker.

**Evidence:**

1. **Module tree (decisive).** `piece_030.rs` is not in the server's module tree. A search of `prototype/osfr-tools/src/**/*.rs` for `piece_030`, `restoration` or `housing` shows no `mod`/`#[path]` that pulls it in. `src/lib.rs` does not mention `restoration`. The only includer is the integration test `prototype/osfr-tools/tests/piece_030.rs:26-28`, which does `#[path = "../src/restoration/piece_030.rs"] mod piece_030;`. The module-readiness notes say the same: "Lead registration: `src/restoration/piece_030.rs` is not in `src/lib.rs`", and "No (no `mod restoration`)". So `evaluate_transcript`, `evaluate_restart` and the replay code are test-only.

2. **No server caller.** `evaluate_transcript` is called only from the test file (`tests/piece_030.rs:96, 502, 514, 534`) and from `piece_030.rs:1460`, which is inside the same test-only module. No gateway, gameplay or save-load path reaches it, so no remote player input can reach `evaluate_restart`.

3. **The code claim is accurate, though.** I read the lines and the scenario holds:
   - `evaluate_restart` (1015-1083): `placed` (1025) and `expected` (1031-1035) come from `collect_fixtures(rows)` (614-648), which records `place_seq` for every `PlaceFixture` regardless of its seq relative to `restart.seq`.
   - Only the InstanceData search is filtered (`row.seq > restart.seq`, 1036-1039).
   - With the failure transcript, `placed == 1`, `expected == {F: None}`, and the listed-fixture checks (1048-1063) pass. The position check (1064) is skipped because `last_position()` is `None`. The gate returns `Pass` (1075-1082).
   - `validate_rows` (527-585) checks only ordering, opcode and house guid, as the claim says.

   So the missing `place_seq < restart.seq` filter is a real bug in the test-only evaluator. It is not a defect in the shipped server.

4. **Minor citation slips.** The claim cites "659-661" for `evaluate_gate`; the Restart arm is at 661 and the function starts at 650. The core line numbers (511, 1025, 1026-1030, 1031-1035) are correct.

**Corrected fix:** not needed for a server defect. If the acceptance harness is wired in later, the suggested filter is right: in `evaluate_restart`, count and collect only facts with `place_seq.is_some_and(|p| p < restart.seq)`, or restrict `collect_fixtures` to rows before `restart.seq`. Apply it to both `placed` and `expected`.
