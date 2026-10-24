<!-- fleet job=pin-audit id=tests-bandit-hideout-dungeon-rs status=nothing_found turns=2 usd=0.0008 tokens(read,write,in,out)=[1865, 3751, 6, 548] model=claude-haiku-5-5 -->
# tests/bandit_hideout_dungeon.rs

No findings. Both screened lines (1171 and 1205, plus the matching 1184 in the same test) assert `filler_before + 2`. The `2` is the quantity the test itself sends in its own chat command, `realm give {filler} 2` (line 1163), so it is a fixture-set value, not a number read from `reward` or any data file. The `filler_before` baseline is read live from the gateway. The `reward_coins` value that the payout line uses (line 1179) is already read from the battle row, so it is not pinned. Nothing to change.
