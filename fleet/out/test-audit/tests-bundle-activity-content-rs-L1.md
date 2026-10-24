<!-- fleet job=test-audit id=tests-bundle-activity-content-rs-L1 status=done turns=5 usd=0.0063 tokens(read,write,in,out)=[46299, 24255, 12, 5632] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bundle_activity_content.rs lines 1-301 of 301

Window reviewed: `prototype/osfr-tools/tests/bundle_activity_content.rs` lines 1-300 (file is 301 lines). The mining check at 194 is not tautological: `mining_spec()` (src/mining.rs:951) is a hand-written constant, and `Type8Engine::load` reads the spec from the JSON, so that comparison does test the file. The Python gate at 291-300 exists (`tests/test_bundle_activity_content.py`), and a missing file or interpreter fails the test rather than skipping it.

- **[medium] tests/bundle_activity_content.rs:146 bundled_activity_content_loads_without_lab - the only "not lab" check compares the temp directory against the lab path, so it cannot fail.**
  - Why it cannot catch a regression: `Scratch::new()` always creates the directory under `std::env::temp_dir()`, so `starts_with(<repo>/../../../lab)` is always false. A loader that quietly fell back to a lab package would still load, and this test would pass. The real protection is only that the scratch copy contains just `FILES`, and nothing checks that loaders never read outside `directory`.
  - Fix: Make the scratch directory contain only `FILES`, then assert that each loader's returned source paths (or a read-trace) stay under `directory`. Alternatively, delete the tautological `assert!` and rely on the fixture alone, with a comment saying so.

- **[medium] tests/bundle_activity_content.rs:135 frozen_activity_bytes_are_the_reviewed_snapshot - the name and module doc claim the whole activity bundle is frozen, but only 9 of the 12 files in `FILES` are pinned.**
  - Why it cannot catch a regression: `fishing_spots.json`, `mining_nodes.json` and `harvest_nodes.json` are loaded by the test at 220-229 but have no hash. Any change to them passes this test, and `FROZEN_SHA256` is not checked against `FILES`.
  - Fix: Add a test asserting that every entry in `FILES` appears in `FROZEN_SHA256` (or explicitly list the unpinned files with a reason). Pin the three node/spot files, or rename the test and narrow its doc.

- **[medium] tests/bundle_activity_content.rs:176 bundled_activity_content_loads_without_lab - "ships the recovered vehicle definition, not the synthetic fixture" is checked only by `definition.len() > 4`.**
  - Why it cannot catch a regression: any definition array with five or more entries passes, including a synthetic or truncated one. The assertion does not identify the recovered definition.
  - Fix: Assert the exact recovered definition content (for example its first element or a hash of the vehicle block), or assert that it equals the value in the pinned `derby_entry.json` hash entry.

- **[low] tests/bundle_activity_content.rs:217-223 bundled_activity_content_loads_without_lab - exact counts (`dungeons[0].id == 411`, `world_enemies.len() == 7`, `gate_npcs().len() == 6`) pin incidental data sizes.**
  - Why it cannot catch a regression: these counts are unrelated to what the test is about (loading without lab). Adding or removing one enemy or gate fails the test without any loader bug, which causes churn.
  - Fix: Keep the load-success and identity checks, and drop the count pins, or move them into the content-specific tests.

- **[low] tests/bundle_activity_content.rs:224 and :229 bundled_activity_content_loads_without_lab - `menu_string_id() > 0` and `actors().count() >= 2` are near-vacuous.**
  - Why it cannot catch a regression: a loader that returns any positive string id, or any two actors (including wrong ones), still passes. Neither checks the content that was loaded.
  - Fix: Assert the exact menu string id (as is done for derby at line 172) and the exact actor GUIDs or the count derived from the pinned `harvest_nodes.json`.
