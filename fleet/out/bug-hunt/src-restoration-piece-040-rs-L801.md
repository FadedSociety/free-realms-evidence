<!-- fleet job=bug-hunt id=src-restoration-piece-040-rs-L801 status=nothing_found turns=7 usd=0.0059 tokens(read,write,in,out)=[64648, 21055, 16, 5189] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_040.rs lines 801-834 of 834

Window `prototype/osfr-tools/src/restoration/piece_040.rs` lines 801-834 (`level_title`, `level_gate_quest`, `wiki_gates`, `wiki_gate`, `wiki_gate_access`) reviewed. No defect I can tie to a line and show reachable from client input.

What was checked:
- `level_title` (800-806): `level.min(MAX_JOB_RANK)` clamps a u8, so no panic. Filter and `max_by_key` are correct for the unique (profile, level) rows in `LEVEL_TITLES` (lines 547-628). It matches the doc comment and `tests/piece_040.rs:329-361`, including the clamp to 20 and `None` below 4.
- `level_gate_quest` (808-812): exact-match `find` on a u8 with no indexing, so it cannot panic. It has no production callers.
- `wiki_gate` / `wiki_gates` (814-820): plain lookups over the static `WIKI_GATES` table, no indexing.
- `wiki_gate_access` (824-834): `required_rank.unwrap_or(0)` feeds `rank_access`, which applies `.max(1)`, so the "rank 1 floor" in the doc comment holds. The owner check uses `gate.profile_id`, which yields `WrongJob` for the other job. Expected values match `tests/piece_040.rs:300-325`, e.g. `(CHEF, 0, 1232)` gives `BelowRequiredRank{1,0}`, and `(CHEF, 9, 38658)` gives `BelowRequiredRank{10,9}`.

Reach: a grep of `prototype/osfr-tools` found no caller of `level_title`, `level_gate_quest`, `wiki_gate_access`, or `wiki_gates` outside this file and its own test file (`tests/piece_040.rs`, which `#[path]`-includes the module). None of these functions is wired to a client packet handler, and no client-supplied value reaches them in production. Even a defect here would not be remotely triggerable.

Nothing else in the window is a panic, unbounded growth, atomicity, trust, or logic defect.
