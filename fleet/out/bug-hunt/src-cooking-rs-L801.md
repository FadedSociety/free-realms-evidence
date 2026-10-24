<!-- fleet job=bug-hunt id=src-cooking-rs-L801 status=nothing_found turns=13 usd=0.0106 tokens(read,write,in,out)=[234965, 34377, 28, 7862] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/cooking.rs lines 801-1152 of 1152

Window `repo:prototype/osfr-tools/src/cooking.rs` 801-1152 read in full. No defect I can tie to a line and show reachable from client input or a save.

What I checked:

- **`load_recipes` (803-853):** Runs at load time from server-owned `recipes.json`, not client input. Its `i32::try_from` on `minigame_id` is fallible and returns an error, not a panic. `recipes.insert` cannot silently overwrite a key, because `RecipeCatalog::load` (recipes.rs:216-241) rejects duplicate keys. `validate_recipe` (recipes.rs:432-500) rejects zero/negative ingredient ids and counts, and repeated ingredient definitions, so `has_ingredients` never sees duplicate requirements.
- **`has_ingredients` (855-864):** Sums `u32` counts into a `u64` before comparing, so no overflow. Its callers `begin_recipe` (cooking.rs:292-299) and `gameplay/crafting.rs:186-193` pass aggregated, non-rental inventory (`gameplay.rs:1468-1477`, saturating add). Requirements are the server's recipe data, not packet fields.
- **`header_with_game` / `invalid` (866-876):** Fixed-width little-endian writes, no indexing, no panics.
- **Test modules (878-1152):** Excluded by the rules. I checked the behaviour they name against `handle` (cooking.rs:355-420), `cancel` (338-353) and `validate_state` (191-254). They match: sub 6 quit cancels only Offered/Playing runs, terminal runs are kept, sub 7 ACK is a no-op, and the length checks reject malformed packets. `handle` guards `inner[..2]` and `read_i32` behind the `len < 15` check.
- **`Cooking::begin` (258-272):** Bypasses the inventory and rank checks by passing `available = consumes`. I found only dev/test callers (`gameplay/developer_teleport.rs:44`, `gameplay/ordinary_quit_routing.rs:44,81`, `restoration/piece_012.rs:182`, tests). The gateway path uses `begin_recipe` with real inventory, so this is not client-reachable as far as I can see.

Nothing in the window meets the defect criteria at high, medium or low severity.
