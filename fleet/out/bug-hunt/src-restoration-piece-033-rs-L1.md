<!-- fleet job=bug-hunt id=src-restoration-piece-033-rs-L1 status=nothing_found turns=4 usd=0.0037 tokens(read,write,in,out)=[27077, 18147, 10, 2232] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_033.rs lines 1-467 of 467

Reviewed `prototype/osfr-tools/src/restoration/piece_033.rs` lines 1-467 in full. No defects I can tie to a client-reachable path.

What I checked:

- **Lines 1-410 (constant tables, `pub const` slices and structs):** data only. No indexing, slicing, parsing or allocation runs on input here.
- **Lines 417-443 (`warrior_class`, `warrior_slot`, `warrior_skill`, `skill_unlocked`, `unlocked_skill_name_ids`):** linear `find`/`filter` over constant slices. No panic path, no unwrap, and no client-sized growth (the output is bounded by the 4-row skill table).
- **Lines 447-467 (`check_warrior_equip`):** the level gate is `max(item_min_profile_rank, slot_rule.min_profile_rank)`, which matches the doc comment ("both the item and slot level gates are at or below the job level"). The class and slot checks match the doc too. `max` and the `<` comparison cannot overflow or panic for any `i32`.

Reach: nothing in the server calls these functions. `search` finds no `restoration::piece_033` or `#[path = "restoration/piece_033.rs"]` include outside `prototype/osfr-tools/tests/piece_033.rs`, which is test-only. No packet handler reaches this module, so no client-supplied value can reach it.

Possible concern, not reported: `check_warrior_equip` does not verify that the class matches the slot (for example, a class 15 gear item in slot 7 Weapon passes). The doc comment does not claim that check, and the module is not wired into the server, so I did not raise it as a defect.
