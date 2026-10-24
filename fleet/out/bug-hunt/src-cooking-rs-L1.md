<!-- fleet job=bug-hunt id=src-cooking-rs-L1 status=nothing_found turns=11 usd=0.0231 tokens(read,write,in,out)=[307066, 55709, 24, 26139] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/cooking.rs lines 1-800 of 1152

No defects found in `prototype/osfr-tools/src/cooking.rs` lines 1-800 that a remote client or a save can reach.

I read the whole window and traced the callers (`gameplay/crafting.rs:54-83, 337-400`, `gameplay.rs:4276-4286`). Candidates I checked and dropped:

- **`handle` `message.unwrap()` (cooking.rs:434).** Safe. Subs 5, 6 and 7 all return before line 434, so only sub 14 reaches it, and that is the only case where `message` is `Some`.
- **`active.as_mut().unwrap()` (cooking.rs:422, 432).** Safe. `a` was taken from `Some` at line 378, and `next` is a clone of that state.
- **`validate_totals` unwraps (cooking.rs:696, 702).** Safe. Every caller first checks that all round and game stats are `Some`: line 514-515 in the GameWon path, and lines 226-229 and 245 in `validate_state`. `unfinished` is sticky, so a Won run has no `None` slots.
- **`decode_payload` (cooking.rs:722-737).** Safe. `length` is checked for `< 1` and `> MAX_PAYLOAD` before `19 + length` is computed. `inner.len() == 19 + length` then guarantees `len >= 20`, so `last().unwrap()` and the slice `[19..len-1]` are in range.
- **`read_i32` offsets (cooking.rs:366-368, 726).** Safe. Length is checked to be `>= 15`, and `>= 20` before offset 15.
- **`validate_state` subtraction (cooking.rs:194).** Safe. `next_instance_id < FIRST_INSTANCE` short-circuits first.
- **`selected_recipe` HashMap index (cooking.rs:328).** Safe. Both the saved key (cooking.rs:161-167) and the begin key (cooking.rs:291) are checked against `recipes`, and the content default is validated in `validate_content`.
- **`validate_content` phase indexing (cooking.rs:619-679).** Safe. `phases.len() == 6` is checked first. The `(1..=d[1])` range is only evaluated when `d[1]` is already in 5..=50.
- **Numeric casts (cooking.rs:754, 762, 768).** No overflow is reachable. Stat values are bounded to <= 1e9 or <= 21600 and `score` is <= 1e9 at every entry point.
- **Reward trust.** The transaction's consumes and grants come from the local catalog (cooking.rs:527-531). The client's score and quantity are only validated, and `quantity` must be 0. Ingredients are re-checked at completion in `gameplay/crafting.rs:356-365`.
- **Atomicity.** Every fallible step in `handle` runs before `self.state = next` (cooking.rs:573-574). The one direct mutation is the sub-5 launch at cooking.rs:422, which has no fallible step after it. `results_presented` is set only after the last `?` in the GameWon arm (cooking.rs:533 vs 535).
- **`begin()` compat entry (cooking.rs:258-272).** Skips the ingredient check, but its only callers are tests and a dev-test in `gameplay/developer_teleport.rs:44`. It is not reachable from a client packet.
- **Handle/validate consistency.** The stat bounds, round and game ordering, and `validate_totals` rules agree between `handle` and `validate_state`.
