<!-- fleet job=pin-audit id=tests-two-player-dungeons-rs status=nothing_found turns=2 usd=0.0008 tokens(read,write,in,out)=[1809, 3610, 6, 606] model=claude-haiku-5-5 -->
# tests/two_player_dungeons.rs

Screened line 517 (`assert_eq!(a_with_delta.coins, a_paid.coins + 7);`, test `two_player_dungeons.rs` in the delta/Close section) is not a finding. The `7` is the amount the test itself types into the chat command `chat::local_request("realm coins 7")` at line 514, so it is a fixture-set value, not a number read from a data file. `a_paid.coins` comes from the test's own payout flow via `economy(...)`/`assert_payout`, and the test asserts only the delta on top of that. Nothing in this assertion pins a shipped data value, so no change is needed.
