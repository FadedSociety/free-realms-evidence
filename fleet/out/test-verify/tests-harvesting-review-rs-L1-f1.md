<!-- fleet job=test-verify id=tests-harvesting-review-rs-L1-f1 status=done turns=9 usd=0.0104 tokens(read,write,in,out)=[169511, 33620, 20, 8934] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/harvesting_review.rs:157-178

**Verdict:** `confirmed` (goal-value side fully; bundle-id side only partly, see below)

**Evidence:** I could not find an assertion in `every_supported_region_spec_executes_and_requests_farming_assets` (tests/harvesting_review.rs:81-180), or in the helpers it calls, that fails under a change to `produce_value_for` or `produce`.

- **Goal values, lines 157-165:** the expected side is `region.produce.iter().map(|slug| harvesting::produce_value_for(slug).unwrap())`. `board_spec` (src/harvesting.rs:946-951, 952-960) builds `goals[slot].value` from the same `produce_value_for(slug)` call over the same `region.produce` order. A mutation such as `produce_value_for` returning `produce_value(index + 1)`, or a permuted or constant mapping, moves both sides together. The engine's checks do not reject it either: `mining.rs:1145` only requires 400..499, and `harvesting.rs:1174-1180` re-derives the value from the same function. The test then passes.
- **Bundle ids, lines 166-178:** the expected side is `harvesting::produce(slug).item_definition_id`, and `board_spec` writes `outputs[slot].definition_id` from the same `produce(slug)` (harvesting.rs:938, 963). A mutation to `produce()` also moves both sides together, so this test passes.
- **No literal anywhere in this test:** the only literal ids in the file are in `harvested_bundles_grant_once_from_a_serialized_completion_state` (lines 332-335, `vec![(2885, 5), (2887, 5), (2890, 5), (2877, 5)]`). No literal 401..416 appears in the file.
- **Repo-wide:** a grep of `prototype/osfr-tools` for `produce_value|PRODUCE|harvesting::produce`, `farmingValue`, and the literals 401..416 and 2875..2890 finds no test pinning recovered goal values. The only hits are `src/harvesting.rs` production code and unrelated tests.

**Partial counter-evidence on the bundle side:** the sibling test at line 334 does pin `(2885,5),(2887,5),(2890,5),(2877,5)` for region 111 (`harvesting.rs:320`, produce = stickfruit, stainberry, tumtumnip, spiralmint). So a `produce()` mutation that changes the item for any of those four slugs is caught, but by the reward test, not by this one. A mutation that only changes items for the other slugs (or only `produce_value_for`) is caught by nothing.

**Minimal fix:** in this test, pin the recovered literals per region rather than re-deriving them. For region 111, add `assert_eq!(spec.goals.iter().map(|g| g.value).collect::<Vec<_>>(), vec![411, 413, 416, 403])` and `assert_eq!(spec.outputs.iter().map(|o| o.definition_id).collect::<Vec<_>>(), vec![2885, 2887, 2890, 2877])`. Region 109 would be `[401, 410, 415, 407]`. Ideally cover all six regions with a literal table keyed by `game_id`.
