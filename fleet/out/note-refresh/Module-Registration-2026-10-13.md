<!-- fleet job=note-refresh id=Module-Registration-2026-10-13 status=done turns=7 usd=0.0088 tokens(read,write,in,out)=[102169, 32499, 16, 7459] model=claude-haiku-5-5 -->
# notes/Research/Module Registration 2026-10-13.md

**Verdict:** minor drift. The 13 registered modules and the crate-import conversions still hold. The "unregistered" claim, two failure explanations and two line cites are stale at the tip. The run table and totals are a dated record and were not re-run.

**Corrections:**

1. `old:` `startup_selfdata`, `housing_service`, `pets`, and `trade` remain unregistered as directed.
   `new:` `startup_selfdata`, `housing_service`, `pets`, and `trade` were left unregistered as directed at W30 time. At the current tip all four are declared in `src/lib.rs` (`pub mod housing_service;` line 32, `pub mod pets;` line 66, `pub mod startup_selfdata;` line 91, `pub mod trade;` line 98).
   `why:` repo:prototype/osfr-tools/src/lib.rs:32, :66, :91, :98

2. `old:` W22's assertion expects every job/quest NPC reference to remain in `npcs_unresolved.json`.
   `new:` W22's assertion now accepts a job/quest NPC reference that is either resolved or listed in `npcs_unresolved.json` (`tests/content_jobs.rs:117-122`). The assertion is at line 117, not 62, which is where the quest loop starts.
   `why:` repo:prototype/osfr-tools/tests/content_jobs.rs:117-122 (the `.all(|id| resolved_ids.contains(id) || unresolved_ids.contains(id))` check)

3. `old:` a save without pet state now writes schema 5 while this test expects 4; schema 6 is used when pet state exists.
   `new:` a save without pet state writes `BASE_SCHEMA_VERSION` (5), and the test now asserts that constant (`assert_eq!(upgraded["schema_version"], BASE_SCHEMA_VERSION)`) rather than 4; schema 6 (`PET_SCHEMA_VERSION`) is used when pet state exists.
   `why:` repo:prototype/osfr-tools/src/game_store.rs:15-16 (constants); repo:prototype/osfr-tools/tests/game_store.rs:41-42 (the assertion is at line 42, not 39)

**Unsure:**

- The "Test and type alignment" claims about the converted test files are current. Every converted file imports from `osfr_tools` and none contains a `#[path` include. Modules `world` and `quest_engine` use `crate::content`, as described.
- The verification totals (199 targets, 1,882 passed, 2 failed, 89 ignored), the per-target table, and the two failure rows (`content_jobs` and `game_store` at 0/1) are a dated run record. I did not re-run the suite. Items 2 and 3 suggest both failures may no longer reproduce, but I have not confirmed that by running the tests.
- The 13 registered modules (`abilities`, `content`, `minigame`, `players`, `social_chat`, `world`, `quest_engine`, `social_lists`, `mounts`, `derby`, `fishing_service`, `inventory_v2_fixes`, `soccer_service`) are all present as `pub mod` in `src/lib.rs`. I did not check whether the "no gateway or gameplay routing was added" claim still holds.
