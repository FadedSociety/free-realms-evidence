<!-- fleet job=test-verify id=tests-battle-prize-bag-preflight-rs-L1-f1 status=done turns=5 usd=0.0039 tokens(read,write,in,out)=[32280, 15240, 12, 3408] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/battle_prize_bag_preflight.rs:809

**Verdict:** `refuted`

**Evidence:** The claim is right that the loop at lines 814-831 only asserts `accepted == paid`. It is wrong that nothing else in the file pins a truth value. The same file has hard-coded expectations for the exact cases the claim says would drift, and they fail under the regressions it names.

- **`grant_bundle` starts refusing a valid row `vec![(item, 1)]`:** `the_preflight_answers_like_the_payout_path` still passes, but `an_invalid_bundle_is_refused_without_a_panic` fails at line 702: `assert!(inventory.accepts_reward_bundle(&[(item, 1)]));`. The positive control in test 4 (line 701 `accepts_reward_bundle(&[])`, line 702 `(item, 1)`) is an absolute `assert!`, not an equality. `duplicate_prizes_are_counted_together` also pins it at line 623: `assert!(live.accepts_reward_bundle(&[(item, 1)]), ...)`.
- **`grant_bundle` starts accepting an invalid row `(0, 1)`:** test 4 fails at lines 718-720, `assert!(!inventory.accepts_reward_bundle(&bundle), "{case} must be refused")`, for the case `("zero definition", vec![(0, 1)])`. The same test also refuses `(item, 0)`, `(i32::MAX, 1)`, `(-1, 1)`, `(i32::MIN, u32::MAX)` and `(item, u32::MAX)`, and a valid row after two invalid ones.
- **Full-bag and two-stack boundaries:** lines 570-571 (`accepts_reward_bundle(&[(item, max_stack)])` true, two max-stack rows false) and 627 (`!live.accepts_reward_bundle(&[(item, 1), (item, 1)])`) are absolute assertions on the full-bag fixtures.
- **Row bound:** line 836 `assert!(!inventory.accepts_reward_bundle(&long))` and test 4's `more than 16 rows` case pin the 17-row refusal independently of `grant_bundle`.

Both proposed mutations therefore fail a test. The tests in `battle_prize_bag_preflight.rs` are not `#[ignore]`d, and `runtime_inventory()` (line 292) is a plain `Inventory::load` with no fixture-gated early return.

The equality in test 6 is intentional: its doc comment says it exists so that a rule added to `grant_bundle` reaches the start gate and the payout together. The concrete-value pins live in tests 1-4 of the same file. The claim's suggested fix (`assert!(accepts_reward_bundle(&[(item, 1)]))`, `assert!(!accepts_reward_bundle(&[(0, 1)]))`) is already present at lines 702, 706 and 623.

**Minimal fix:** None needed. Optionally add the `(item, 0)` / `(0, 1)` absolute checks to the loop in test 6 as `assert_eq!(accepted, expected)` with an explicit `expected` column, but the current suite already catches the regressions the claim names.
