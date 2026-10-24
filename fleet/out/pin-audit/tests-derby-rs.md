<!-- fleet job=pin-audit id=tests-derby-rs status=nothing_found turns=5 usd=0.0055 tokens(read,write,in,out)=[67110, 30118, 12, 2124] model=claude-haiku-5-5 -->
# tests/derby.rs

No findings in `prototype/osfr-tools/tests/derby.rs`. All eight screened lines take their numbers from the test's own fixture or from a code constant, not from a shipped data value that retuning would change:

- **140 (`activate`, offer[35..39] == 11):** the bytes are the trailing `DEMO_DERBY_TYPE_ID` from `src/derby.rs:23`, written by `offer_packet` (`src/derby.rs:1005`). That is a code constant, not `derby_entry.json`.
- **378 (`contacts_apply_server_damage...`, score == 2):** `rules().knockout_points = 2` (fixture, lines 24-54).
- **385, 438, 470, 548 (health == 20):** `rules().start_health = 20` (fixture). The `start_health: 100` in `data/content/derby_entry.json` is not read by this test; it builds `DerbyRules` directly through `service()`.
- **413, 550 (health == 15):** 20 minus an impact of 5.0 from the test's own `hit`/`damage` fixture, with `contact_damage_per_unit: 1.0` from `rules()`.
- **379 and 548 context:** same fixture reasoning; no data file value is pinned.

The `derby_entry.json` values that differ (`start_health` 100, `health_pickup` 25, `score_target` 22) are not used by these assertions, so retuning them does not affect this file.
