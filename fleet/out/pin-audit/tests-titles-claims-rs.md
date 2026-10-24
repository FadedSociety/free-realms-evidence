<!-- fleet job=pin-audit id=tests-titles-claims-rs status=nothing_found turns=2 usd=0.0006 tokens(read,write,in,out)=[1814, 2866, 6, 487] model=claude-haiku-5-5 -->
# tests/titles_claims.rs

No findings. Line 702 (`assert_eq!(before.gameplay.as_ref().unwrap().inventory.coins, 7)`, in `claim_payout_uses_live_coins_after_queueing`, around line 700 of the file as read) checks a value the test sets itself. Line 698 runs `chat::local_request("realm coins 7")` immediately before the snapshot, so the 7 is a fixture value, not a number from a data file. The claim price is not asserted here: the test only checks that coins are still 7 after the claim, which is a stale-wallet check. Retuning any data file would not affect this assertion.
