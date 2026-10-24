<!-- fleet job=bug-hunt id=src-restoration-piece-040-rs-L1 status=nothing_found turns=4 usd=0.0059 tokens(read,write,in,out)=[38507, 25856, 10, 4591] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_040.rs lines 1-800 of 834

Reviewed `prototype/osfr-tools/src/restoration/piece_040.rs` lines 1-800 (and the 800-834 tail of `level_title`, `level_gate_quest`, `wiki_gate_access` that the window's last function starts). No finding meets the defect bar.

What I checked:

- **Panics on client input:** every function here takes only scalars (`i32` ids, `u8` rank/level). The only arithmetic is `min`/`max` clamps (`rank.min(MAX_JOB_RANK)`, `required_rank.max(1)`, `level.min(MAX_JOB_RANK)`). No indexing, slicing, `unwrap`, or division on client values. Lookups are `iter().find`/`filter`, which cannot panic.
- **Unbounded resources:** all collections are `&'static` tables of fixed size (49 recipes, 8 level titles, 8 quests, 2 wiki gates). Nothing is allocated from client input.
- **Trusting the client:** `recipe_access` and `wiki_gate_access` look up the item/name id in server-side tables and take the shard-class owner from those tables, not from the request. A wrong job returns `WrongJob`. Rank 0 is refused (floor 1). Ranks above 20 clamp to 20, as documented and tested (tests/piece_040.rs:207-211). Unknown ids return `UnknownRecipe`.
- **Logic against its own docs/tests:** I checked the recipe ladder ordering (class, then rank, then id) against the header; the 49-record count; the cross-class pair 869/2518 (documented and asserted in the test at tests/piece_040.rs:130-141); the `rank_gated_recipes` filter (`> 1`); `level_title` (highest row at or below the clamped level); and the `wiki_gate_access` rank mapping (`None` maps to 0, then the floor of 1). All match their doc comments and the test expectations I read (tests/piece_040.rs:120-232).
- **Atomicity:** these are pure read-only functions. There are no saves or state mutations.
- **Reach:** `piece_040` is not registered in `src/lib.rs` or `src/restoration/mod.rs`. The only includer is the `#[path]` test harness (tests/piece_040.rs:29-31). No server code path calls `recipe_access`, `wiki_gate_access`, or `level_title` from a client packet, so even the policy weaknesses I considered would not be reachable.

Observations I did not report, because they are not defects against the criteria: the duplicated doc sentence at lines 18-19; the stray backtick in the name string "Snowberry Top`ped Sundae Recipe" (line 409); and the recovered data that places Chef recipe 869 under the Blacksmith shard class. The last one is pinned source data that the test asserts on purpose, and the policy applies it consistently.
