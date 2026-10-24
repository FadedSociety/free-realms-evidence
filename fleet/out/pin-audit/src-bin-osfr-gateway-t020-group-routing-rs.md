<!-- fleet job=pin-audit id=src-bin-osfr-gateway-t020-group-routing-rs status=nothing_found turns=4 usd=0.0016 tokens(read,write,in,out)=[10889, 6551, 10, 1293] model=claude-haiku-5-5 -->
# src/bin/osfr_gateway/t020_group_routing.rs

No finding for `prototype/osfr-tools/src/bin/osfr_gateway/t020_group_routing.rs:1065` (test `group_routing` case around the "picker with no committed place" check).

The `100` is not read from a data file. The member's health is injected by the test's own fixture: line 1063 calls `hurt_member(&mut server, keys[1], &hurt)`, and `hurt` was built at line 1026 by `damaged_gateway(&server, keys[1], 100)`. That helper (lines 1151-1159) overwrites `encounter.player_health` with the `health` argument. So the asserted 100 is the wounded value the test itself sets, and it does not depend on `member/npc` base health or any other shipped data field. Retuning the data would not change it.

The adjacent `100` literals at lines 1057, 1069, 1114 and 1127 come from the same fixture and are not findings either. No change is needed.
