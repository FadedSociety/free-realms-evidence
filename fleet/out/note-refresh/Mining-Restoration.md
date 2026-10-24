<!-- fleet job=note-refresh id=Mining-Restoration status=done turns=14 usd=0.0159 tokens(read,write,in,out)=[327574, 46468, 30, 13548] model=claude-haiku-5-5 -->
# notes/Research/Mining Restoration.md

**Verdict:** Stale in places. The file paths, the `Type8Engine` API, the `payload_packet` and `mining_spec()` names, and the `lib.rs` and `gameplay.rs` wiring all check out. Two statements are false (reward outputs, native status), one is a false description of how the tests link, and one integration step is already done.

**Corrections:**

1. `old:` Mining's original per-node reward grant schema is likewise unrecovered, so the default `mining.json` proposes **no** transaction (`outputs: []`) until root supplies a recovered or explicitly accepted mapping.
   `new:` Mining's original per-node reward grant schema is likewise unrecovered, so the default `mining.json` proposes two reconstructed outputs, value 601 -> definition 2739 x1 and value 602 -> definition 2739 x2 per cluster, labelled `reconstructed_rules: true` until root supplies a recovered or explicitly accepted mapping.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1020-1033 (`mining_spec()` outputs carry 601 and 602 with definition 2739); repo:prototype/osfr-tools/data/content/mining.json:36-49; repo:notes/Autopilot/F130.md:20-24 (outputs restored, new SHA-256 pinned). The `outputs: []` form only appears in the older review notes.

2. `old:` No native acceptance has been attempted.
   `new:` Native runs have been attempted, and none has been won so far (runs 151307 and 200750 were lost). Whole-round native acceptance remains open.
   `why:` repo:notes/Design/Build Ledger.md:104 ("No native win so far (runs 151307, 200750 lost) … Whole-round native acceptance remains open"); repo:notes/Reviews/Mining Native 151307 Final Review.md:3 (audit of `lab/runs/client-baseline-20261009T151307Z`).

3. `old:` `prototype/osfr-tools/tests/mining.rs` path-includes `../src/mining.rs`.
   `new:` `prototype/osfr-tools/tests/mining.rs` imports the library crate (`use osfr_tools::mining::{…}`), not a path include.
   `why:` repo:prototype/osfr-tools/tests/mining.rs:4-7 (`use osfr_tools::mining::{ … }`); no `#[path` or `include!` appears in that file.

4. `old:` 1. Register `pub mod mining;` in `lib.rs` and add mining state to the gameplay/gateway snapshot as a new optional field (serde default) so older saves still load.
   `new:` 1. (Done.) `pub mod mining;` is registered at `lib.rs:54`, and mining state is an optional snapshot field (`Option<Type8State>`) in `gameplay.rs:112`.
   `why:` repo:prototype/osfr-tools/src/lib.rs:54; repo:prototype/osfr-tools/src/gameplay.rs:112, 166, 647, 835-844. The "Tests (owned, no `lib.rs` edit)" heading is also outdated, since `lib.rs` now carries the registration.

**Unsure:**

- **Test count.** The note says `cargo test --test mining` gives "17 passed" (focused-green.log). I cannot run tests here. The tip has 20 `#[test]` attributes in `tests/mining.rs` (lines 208-1002). Later notes record 19 passing (repo:notes/Reviews/Mining Independent Review.md:40) and 21 passing (repo:notes/Reviews/Harvesting Independent Review.md:40; repo:notes/Research/Mining Wildcard Move Detection.md:51). The 17 is a dated log result, so I left it unchanged.
- **"Self-contained" / "std + serde only".** `src/mining.rs:44-46` includes `mining_lifecycle.rs` as `pub mod lifecycle`, and that file imports `osfr_tools::{minigame, mining, quest_engine, rewards}` (repo:prototype/osfr-tools/src/mining_lifecycle.rs:7-16). The engine core may still be std + serde only, but the module as a whole is not.
- **Harvesting `content_file = "harvesting"`.** `harvesting.rs:39` defines `CONTENT_FILE = "harvesting.json"`. I did not confirm which field the note's `content_file` refers to, so I left it alone.
- **Original-game claims** (script counts, byte-identical scripts, pack CRCs, the 129 preload names, the MiniGameData ids) live in `lab/`, outside the repo, so I could not check them.
