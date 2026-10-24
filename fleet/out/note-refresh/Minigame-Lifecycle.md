<!-- fleet job=note-refresh id=Minigame-Lifecycle status=done turns=11 usd=0.0134 tokens(read,write,in,out)=[223280, 43022, 24, 11585] model=claude-haiku-5-5 -->
# notes/Research/Minigame Lifecycle.md

**Verdict:** badly stale on integration status. The W15 ledger itself is as described (file paths, `RunSpec::empty`, the `minigame-run:<instance_id>` grant key, the 39/16, 39/45 and 39/17 packet claims all still hold), but the note says three times that the module is unregistered and has no adopter. At the tip it is registered and four activity modules implement the seam. The test count is also out of date.

**Corrections:**

1. `old:` It is not registered in `lib.rs`, adapted into an activity, save-integrated, or natively accepted.
   `new:` It is registered in `lib.rs` and consumed by activity adapters (chess, soccer, harvesting, mining, fishing, matchmaking); it is not natively accepted.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:53` (`pub mod minigame;`); `repo:prototype/osfr-tools/src/chess.rs:1743` (`impl Activity for ChessFinishActivity`), `repo:prototype/osfr-tools/src/soccer_service.rs:124`, `repo:prototype/osfr-tools/src/harvesting_lifecycle.rs:54`, `repo:prototype/osfr-tools/src/mining_lifecycle.rs:57`, `repo:prototype/osfr-tools/src/fishing_service.rs:103`.

2. `old:` an `Activity` seam for score and terminal outcome; no activity module implements it yet;
   `new:` an `Activity` seam for score and terminal outcome, implemented by `ChessFinishActivity`, `HarvestingActivity`, `MiningActivity` and `SoccerActivity`; Cooking, Smelting and Forging still own their own lifecycle;
   `why:` `repo:prototype/osfr-tools/src/chess.rs:1743`, `repo:prototype/osfr-tools/src/harvesting_lifecycle.rs:54`, `repo:prototype/osfr-tools/src/mining_lifecycle.rs:57`, `repo:prototype/osfr-tools/src/soccer_service.rs:124`. `repo:prototype/osfr-tools/src/cooking.rs`, `smelting.rs` and `forging.rs` have no `minigame::` import.

3. `old:` `prototype/osfr-tools/tests/minigame.rs` is standalone via `#[path]`, like `tests/rewards.rs`; no shared module registration changed.
   `new:` `prototype/osfr-tools/tests/minigame.rs` imports the library crate directly (`use osfr_tools::{inventory, minigame, profiles, rewards};`), not via `#[path]`; `minigame` is registered in `src/lib.rs:53`.
   `why:` `repo:prototype/osfr-tools/tests/minigame.rs:1` (no `#[path]` in the file); `repo:prototype/osfr-tools/src/lib.rs:53`.

4. `old:` **7 passed, 0 failed**
   `new:` **8 passed, 0 failed** at the later tip (the file now has eight `#[test]` functions; the 7-test run is the historical W15 result)
   `why:` `repo:prototype/osfr-tools/tests/minigame.rs:263,326,350,402,435,484,530,563`; `repo:notes/Autopilot/F140.md:80` records `cargo test --test minigame: 8 passed, 0 failed`.

5. `old:` **Mining** (`src/mining.rs`): adapt `Type8Engine::begin`, `cancel` and the lifecycle controls in `Type8Engine::handle`
   `new:` **Mining** (`src/mining.rs`, lifecycle in `src/mining_lifecycle.rs`): adapt `MiningLifecycle::begin`, `disconnect` and the lifecycle controls in `MiningLifecycle::handle`
   `why:` `repo:prototype/osfr-tools/src/mining_lifecycle.rs:153` (`begin`), `:180` (`handle`), `:228` (`disconnect`). `repo:prototype/osfr-tools/src/mining.rs` has no `begin`, `cancel` or `handle` function.

6. `old:` Registering the module, save-schema integration, save-failure rollback and real reward commit/send ordering are lead-owned integration work.
   `new:` Save-schema integration, save-failure rollback and real reward commit/send ordering remain lead-owned integration work; the module is already registered (`lib.rs:53`) and adapted by chess, soccer, harvesting and mining.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:53`; adapters as in correction 1.

**Unsure:**

- Line 73 ("No activity adapter or native client test is part of W15"). This is scoped to the W15 slice and is probably still accurate for that slice, but the tip now has adapters, so a reader may take it as current. I did not check whether any adapter has native client receipts.
- The Cooking, Smelting and Forging migration items (lines 64–66) still match the code: `info_packet`, `header`, `game_over`, `results` and `launch_packet` exist in those files, and `begin`, `cancel` and `handle` exist in `cooking.rs:258/338/355`, `smelting.rs:247/326/343` and `forging.rs:236/325/375`. I did not verify the cited native receipt notes.
- Encounter claim (line 74): `src/encounter.rs::on_zone_ready` still emits `41/2` (line 1500) and `39/17` (line 1504), so that claim holds. I did not check whether the native receipt has been reconciled.
- Protocol claims from the Flash handler, movie and nmq addresses (`009bd650`, `00c17470`, `0092f300`, and similar) were not checked; they cannot be verified from the repo alone.
