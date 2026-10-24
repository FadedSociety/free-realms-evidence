<!-- fleet job=pin-audit id=tests-kart-pickups-rs status=nothing_found turns=2 usd=0.0012 tokens(read,write,in,out)=[1901, 5963, 6, 799] model=claude-haiku-5-5 -->
# tests/kart_pickups.rs

No findings in `prototype/osfr-tools/tests/kart_pickups.rs`. Both screened lines are safe:

- **119 `item_expired_frame_matches_the_recovered_shape`**: `(21, 4)` is not from a data file. `EXPIRE_SUBTYPE = 21` and `SHIELD_EXPIRE_VALUE = 4` are protocol constants defined in code (`src/kart_pickups.rs:57` and `:61`), and the test comment ties them to the recovered native PE comparison. Retuning data would not change them, so this is not a tunable value.
- **217 `claim_consumes_once_and_replies_grant_then_destroy`**: `.len(), 2` is a count of the lifecycle replies (grant 33/18, then destroy 33/16), which the test states as a protocol shape ("a claim produces no economy frames"). The `1_000, 600_000` arguments are inputs the test passes itself, not values read from data. Not a finding.
