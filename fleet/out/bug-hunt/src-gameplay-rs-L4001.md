<!-- fleet job=bug-hunt id=src-gameplay-rs-L4001 status=nothing_found turns=31 usd=0.0407 tokens(read,write,in,out)=[1563186, 77599, 64, 30624] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 4001-4800 of 5475

No reportable defect in `gameplay.rs` lines 4001-4800. I read the whole window and followed the client-reachable paths out of it. Every candidate I checked is guarded upstream or cannot be reached from a client packet.

Checked and cleared:

- **Length and index guards (4372-4483, 4634-4668, 4699-4721, 4755+).** `26/13` requires `len == 8` (4373) before `inner[4..8]`. `26/8` requires `len == 13` (4472) before `inner[12]` and `inner[4..12]`. `26/10` requires `len == 16` (4477) before `inner[12..16]`. The `36/10` path is gated by `unsupported_cast` (`abilities.rs:821-837`), which returns a malformed error for a wrong length and a failure reply for every unserved shape. `job_slot` (`opening_abilities.rs:279-286`) uses `try_from` and `checked_sub`, so a huge or negative client `slot` cannot panic.
- **Chat `realm ` path (4306-4330).** `&text.trim()["realm ".len()..]` is safe because the lowercased prefix matched ASCII, so the byte offset is a char boundary. Dev commands are gated by `tool` (`may_run`, 3661-3671).
- **Unwraps on `encounter`, `profiles` and `opening` (4488, 4619, 4335, 4365, and others).** These are only reachable from `handle_opening_inner`, which runs only when `self.opening.is_some()` (`gameplay.rs:2332-2351`). Load (`gameplay.rs:681-697`) sets opening, encounter, profiles and abilities together, so the unwraps hold.
- **Class switch (4376-4385, `jobs.rs:145-187`).** The requested id must be in `unlocked` before anything changes, and `activate` re-checks it. Staging through `self.clone()` makes a refusal leave no state behind.
- **Atomicity.** `handle_opening_inner` runs on `staged = self.clone()` (`gameplay.rs:2335`), so a `?` error discards every mutation in the window, including the `forging_tick_ms` stamp at 4432.
- **Interaction gate (4484-4618).** The actor is looked up in server content (`opening.actors()`), excluding enemies, and checked for zone and `interaction_radius`. `selection` is checked to be exactly 1. The gather drop (4542-4577) fires only on a count increase from `on_event`, which caps counts at `required` (`opening.rs:841-843`) and skips completed objectives (`opening.rs:779`). It cannot be repeated for items.
- **Tutorial craft (4529-4541)** goes through `start_tutorial_craft`, which checks active job, pending stage, and material shortage before starting.
- **Darkthorne door (4522, `opening_dungeon_destination` 4948-4990)** checks the giver, accepted stage, and cleared cave before zoning.
- **Position/NaN.** `CharacterState::validate` rejects non-finite coordinates on save load (`character_store.rs:33-45`), and movement is validated in `gateway.rs`, so the distance checks in this window are not bypassable by NaN.
- **Developer paths (4001-4300).** `realm offer` and `developer_gather` are reachable only with dev tools or a role via `may_run`. Their `?` calls precede the `dev_mark_offered` mutation (4149), and the staged clone covers the rest.
- **Indexing into `state.stages[&id]` (4590, opening.rs:424, 556).** These use ids from server content whose state is initialised for every stage, so they are not client-controlled.
