<!-- fleet job=pin-audit id=tests-piece-037-rs status=nothing_found turns=3 usd=0.0025 tokens(read,write,in,out)=[10844, 13615, 8, 1413] model=claude-haiku-5-5 -->
# tests/piece_037.rs

No findings in `prototype/osfr-tools/tests/piece_037.rs` for the screened lines.

- **Lines 70-75 `first_aid_ladder_is_the_recovered_five_rank_text`:** the ladder `[250, 281, 313, 344, 375]` is the `FIRST_AID_HEAL_LADDER` constant in `src/restoration/piece_037.rs:70`. Its doc comment says it comes from the client locale texts (3813, 47279-47282). No file under `data/content` holds these First Aid heal values; a search for "first aid" there returned nothing relevant. This is a recovered historical text value, not a tunable data value, so the test is not pinning a data-file number.
- **Lines 233-235 `paid_revive_is_disabled_below_the_server_supplied_cost`:** the 1000 comes from the test's own `ReviveOffer` fixture (`revive_cost_coins: 1000`, line 231). The 999/1000/1001 values are boundary checks around that fixture value. No data file supplies this number to the test, so it is not a finding.
