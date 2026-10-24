<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-quest-reward-save-failure-rs-L801 status=nothing_found turns=6 usd=0.0033 tokens(read,write,in,out)=[46589, 14476, 14, 1993] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/quest_reward_save_failure.rs lines 801-1142 of 1142

No defects in `prototype/osfr-tools/src/bin/osfr_gateway/quest_reward_save_failure.rs` lines 801-1142.

Why nothing qualifies:

- **The whole window is test-only code.** `tests.rs:1758-1762` includes this file as `#[cfg(test)] #[path = "quest_reward_save_failure.rs"] mod quest_reward_save_failure;`. Every function in the window is a `#[test]` or a test helper (`function_body`, lines 1091-1108, and the source-inspection test at 1113-1142). Per the review rules, code in `#[cfg(test)]` is not a defect, so the panics, `unwrap`/`expect` calls, and `now += 10` arithmetic here do not count.
- **`function_body` (1091-1108) does not underflow.** `depth -= 1` on a `usize` only runs after `open` has been found, and the scan starts at that `{`. A `}` cannot be seen before the first `{` increments `depth`. It is also test-only.
- **The window's assertions are self-consistent.** The bystander turn-in (820-866), the reconnect replay checks (883-964), the same-session replay checks (966-1029), and the full-bag refusal checks (1031-1086) all match the production path described in the file's module doc (lines 4-12). I found no mutation-before-error or wrong-comparison problem in the production code they drive, and none of that production code lies in my window.

No production code is in this window, so there is nothing to attribute to a client packet, save, or real `Session` path.
