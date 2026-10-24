<!-- fleet job=bug-hunt id=src-quest-engine-rs-L1 status=nothing_found turns=11 usd=0.0136 tokens(read,write,in,out)=[261070, 38943, 24, 12303] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/quest_engine.rs lines 1-800 of 3000

No reportable defects in `prototype/osfr-tools/src/quest_engine.rs` lines 1-800. The window is mostly type definitions, serde shapes, packet encoders and the split-content loader. I read the whole window and the call sites that matter for reachability.

Checked and dropped:

- **Split-content loader (`read_split_file` 240-256, `from_split_content` 776-881):** size and total byte caps are enforced before reading. Objective count is capped per quest (817), quest count across files is capped (875), and duplicate ids are rejected (883). Errors abort the whole load before the engine exists, so the partial `poi_locations`/`runtime_goals` mutations at 830-835 are not observable.
- **`runtime_objective` (94-197):** `ReachPoi` geometry is validated before `location` is returned (174-180). `source` is required (185). Location is only returned on `Ok`.
- **`take_optional_locale_id` (207-221):** rejects zero and out-of-range values, and the error aborts the load.
- **Encoders (528-582, 2986-3000):** `progress` is checked for finite and `0..=1` before the f32 is written. Every u32 to i32 conversion uses `try_into().ok()?`. `47/15` (579) matches the `[47, 0, subtype]` layout used by `quest_journal.rs:65-68` and `:252`.
- **`From<OpeningTrigger>` (672-730):** the `ObjectiveKind::from` match is exhaustive, so the `unreachable!` at 727 cannot fire. `Defeat` maps `definition_id as u32` (688-690), which would wrap a negative i32. I dropped it because `OpeningEvent::Defeat` takes server-side encounter definitions, and the NPC path at `gameplay.rs:4905` uses `try_from` rather than `as`. No client packet reaches this.
- **Pending turn-in state (426-444, 2525/2533):** the actor is set and cleared together through `open_pending_turnin`/`clear_pending_turnin`. Every other write I found also clears both fields.
- **`dev_offer` (1594, 1627, 1731, 1779):** each path that ends a `pending_offer` clears it, matching the doc at 748-751.
- **Radius dropped in the `QuestEvent` adapter (714-716):** the match at 2768-2777 uses the objective's own radius, so nothing is lost.
- **`valid_objective_kind` (2601-2651) and `validate_event` (2653-2692):** both bound client-facing values (client ids, UI event length, angle, offset, position, radius).

I found no panic on client input, no unbounded growth from client counts, no atomicity break, no client-trusted authority, and no doc/logic contradiction inside the window.
