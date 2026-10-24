<!-- fleet job=test-audit id=tests-type8-native-repairs-rs-L1 status=done turns=13 usd=0.0110 tokens(read,write,in,out)=[240945, 29507, 28, 9699] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/type8_native_repairs.rs lines 1-498 of 498

Window: `prototype/osfr-tools/tests/type8_native_repairs.rs` lines 1–498. Six findings, ordered by severity.

- **[medium] prototype/osfr-tools/tests/type8_native_repairs.rs:482 engine_accepts_a_registered_selectable_goal_value - the name says the engine accepts a registered selectable goal, but the body only checks that an unregistered goal (412, not in `selectable` 411/413/416/403) is refused; no load of a registered goal is asserted.**
  - Why it cannot catch a regression: a change that made `Type8Engine::load` refuse every selectable goal would still pass, because the test only expects an error. The `contains("goal")` check is also satisfied by any goal-related refusal. The positive case (value 411) is only covered indirectly by `farming_chain_feeds_the_produce_goal_and_stops_the_level`.
  - Fix: rename it to `engine_refuses_an_unregistered_selectable_goal_value`, or add `fixture.load().expect(...)` on the 411 spec before mutating the goal to 412, and assert the error text names the goal value (e.g. contains "invalid mining goals" plus a value check).

- **[medium] prototype/osfr-tools/tests/type8_native_repairs.rs:232 recovered_produce_table_matches_the_client_code_strings_and_movie_frames - the `locale_id` column of `RECOVERED_PRODUCE` (117115, 69328, …) is never asserted against anything; it only appears in a failure message, and `Resources/CodeStringMappings.txt` is never read.**
  - Why it cannot catch a regression: the test checks the hand-typed slug names and `PRODUCE` locale ids 23285+index, which are the bundle locale ids, not the `farmingValue` code-string ids. Editing or drifting a code-string id in `RECOVERED_PRODUCE` (or the mapping file) changes nothing the test sees. The name claims a match with the client code strings, which is not checked. The real code-string mapping (`client/Resources/CodeStringMappings.txt` 4784–4799) is correct today, but nothing enforces it.
  - Fix: read the client `CodeStringMappings.txt` (or a copied fixture under the repo) in the test and assert that each `farmingValue{value}` line maps to the `locale_id` in `RECOVERED_PRODUCE`, or rename the test to drop "client code strings".

- **[medium] prototype/osfr-tools/tests/type8_native_repairs.rs:321 harvesting_content_round_trips_through_the_repaired_writer - the name promises a round trip, but the body only validates the content and checks two JSON fields (`collectable` empty, `collectable_percent` 0).**
  - Why it cannot catch a regression: a writer that emits a different goal, tile, or output set (or drops fields) still passes, because `content_json` is never parsed back into `HarvestContent` and compared with `content(...)`. The JSON is only probed for two keys.
  - Fix: deserialise `json` into the content type and assert equality with `harvesting::content(r.game_id)` (or compare `spec.goals`, `spec.tiles`, `spec.outputs` values against the in-memory content), or rename the test to say it checks the mirror's 600-block fields.

- **[medium] prototype/osfr-tools/tests/type8_native_repairs.rs:433 mining_chain_still_does_not_feed_a_collectable_goal - the test asserts only negatives (no `OnQuotaUpdateMsg`, `collected == [0]`) and has no positive control that the chain was processed at all.**
  - Why it cannot catch a regression: if the `OnChainMsg` with three `-401` tiles were silently dropped (e.g. a parse or chain-detection regression), the goal would still show no quota update and `collected == [0]`, so the test passes. It can therefore pass without exercising the chain path it is meant to guard.
  - Fix: first assert the same chain on a selectable goal (value 401 with quota 3) produces `OnQuotaUpdateMsg` (or that the chained tiles were removed from the board), then assert the 601 collectable goal stays at zero on the identical chain.

- **[low] prototype/osfr-tools/tests/type8_native_repairs.rs:294-300 harvesting_goals_use_the_recovered_produce_values_and_frames - `assert_eq!(kind.value - kind.category, (kind.value - 400) as u16)` restates the computation: `category` was just asserted equal to 400, so both sides are `value - 400`.**
  - Why it cannot catch a regression: the equality is a tautology and cannot fail for any tile that has category 400. Only the following `(1..=16).contains(&frame)` check constrains the frame.
  - Fix: delete the tautological equality and assert against the constant directly, e.g. `assert_eq!(kind.value - SELECTABLE, expected_frame)` where `expected_frame` comes from the recovered table (`index + 1`), or assert `kind.value == produce_value(slot)`.

- **[low] prototype/osfr-tools/tests/type8_native_repairs.rs:493-496 engine_accepts_a_registered_selectable_goal_value (refusal branch) - `error.to_string().contains("goal")` is a substring match on a generic message.**
  - Why it cannot catch a regression: the source error is `invalid("invalid mining goals")` (`src/mining.rs:1166`). Any error whose text contains "goal" passes, including one raised for an unrelated reason that happens to mention a goal.
  - Fix: assert the exact message, e.g. `assert_eq!(error.kind(), io::ErrorKind::InvalidData)` plus `error.to_string() == "invalid mining goals"`, or check the error with the goal value included.
