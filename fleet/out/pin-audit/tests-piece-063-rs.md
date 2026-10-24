<!-- fleet job=pin-audit id=tests-piece-063-rs status=nothing_found turns=5 usd=0.0015 tokens(read,write,in,out)=[16068, 6321, 12, 996] model=claude-haiku-5-5 -->
# tests/piece_063.rs

No findings. `tests/piece_063.rs:301` (`snapshot["runs"][0]["coins"] == 50`) is not pinned to a data file. The 50 is the test's own fixture: `bundle()` at lines 81-86 builds `RewardBundle { coins: 50, items: vec![(14794, 1)] }`, and `opened_ledger()` opens the run with that bundle. The ledger passes the bundle's coins straight through to the snapshot, so the assertion checks the fixture value, not a shipped data value. A search of `data/content` found no minigame coin payout that equals 50 and feeds this path. No change is needed.
