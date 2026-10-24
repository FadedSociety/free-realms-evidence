<!-- fleet job=test-audit id=tests-mounts-rs-L1 status=done turns=7 usd=0.0055 tokens(read,write,in,out)=[68102, 17927, 16, 5108] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mounts.rs lines 1-427 of 427

Reviewed `tests/mounts.rs` lines 1-427 against `src/mounts.rs` (spawn 349-423, spawn_by_item_definition 425-449, mount 451+, dismount_request 507-541, on_minigame_start/on_ability_use 543-559, RideRestrictions::allows at 238). I found no test that cannot fail, no silent skip, and no name that overclaims. The debounce boundary (5999 blocked, 6000 allowed) matches `now_ms - last < 1000`. The restriction and unowned-mount tests fail if their guards are removed. The `dismount_request` idempotence check (line 226) and the state checks on the unowned path (line 298) are real. The findings below are churn risks only.

- **[low] tests/mounts.rs:133 client_table_and_mount_data_load_with_provenance - the exact type count (30, and 29 non-empty) pins the shipped data file rather than the loader's behaviour.**
  - Why it cannot catch a regression: it does not catch a loader regression. Adding or removing one mount type in `data/content/mounts.json` fails the test even though the loader still works.
  - Fix: assert the loader's invariants instead (every non-zero id is unique, every `mount_type_id` on a mount resolves to a loaded type, and the count is greater than zero). Keep a single canary on a known id such as `mount(7)`.

- **[low] tests/mounts.rs:135 client_table_and_mount_data_load_with_provenance - the exact mount count (54) is data-pinned, so an unrelated content update breaks this test.**
  - Why it cannot catch a regression: the number says nothing about provenance or candidate resolution. The two `all(...)` checks on lines 136-141 already cover those.
  - Fix: drop the exact count or replace it with `> 0`, and keep the `all(...)` provenance checks.
