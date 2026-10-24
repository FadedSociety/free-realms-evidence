<!-- fleet job=bug-hunt id=src-gameplay-rs-L3201 status=done turns=35 usd=0.0424 tokens(read,write,in,out)=[1714155, 81529, 72, 30207] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 3201-4000 of 5475

Window `gameplay.rs` 3201-4000 read in full. One defect found; the rest of the window checked clean (details below).

**[low] prototype/osfr-tools/src/gameplay.rs:3934-3940 - `load_marks` turns any read or parse failure of `marks.json` into an empty list, and the `mark` command then saves that list back, so one unreadable file silently erases every developer mark.**

- **Failure scenario:** `marks.json` holds valid marks but is malformed or unreadable (a hand edit with a stray comma, a permission error, a truncated write from an older tool). A developer runs `realm mark hunt start`. At 2766-2778, `load_marks()` returns `[]`, the handler pushes the new mark, and `save_marks(marks)` (3942-3949) atomically replaces the file with that single entry. Every other mark is gone, and nothing reports the failure.
- **Reach:** `developer_cheat` (gameplay.rs:2766-2785) is reached only from `handle_opening_inner`'s developer block, which requires `tool = self.may_run(command)` (4308-4330). So it is a developer-only path. It is not reachable by an ordinary player, and it does not touch player saves. The contrast with `place_npc`/`unplace_npc` (3847-3854, 3895-3902) is the point: those paths return "Nothing changed" on a read error, and the doc comment at 3754-3755 states that design goal ("so no command overwrites rows it could not read"). `load_marks` does not follow it.
- **Fix:** Make `load_marks` return `io::Result<Vec<Mark>>`, treating only `NotFound` as empty (as `load_placements` does at 3756-3762). In the `mark` branch, print "Could not read the marks: … Nothing changed." on error and skip the save. `goto mark` and `unmark` can keep treating a read error as "no mark".

**Checked and dropped (not defects):**
- Atomicity in `handle_chess`, `begin_chess`, `handle_warp`, `begin_field_battle`: every in-world packet runs on `staged_game = game.clone()` (gateway.rs:1656, 1676, committed at 1725 only on Ok), so a mid-handler `?` discards the partial state.
- `handle_soccer` `unwrap()`s (3327, 3341): guarded by the `is_none()` check at 3322 with no intervening mutation.
- `exit_soccer` `unwrap`/`encounter` (`exit`/`retry` at 4335/4343): reached only from `handle_opening_inner`, which runs only when `opening` is Some (2332-2335). `opening.json` implies `encounter` is loaded (gameplay.rs:681-688), so no panic.
- Portal busy gating (3435, `warp_blocker`): Soccer, Chess, Kart, Derby and Fishing all carry the warp gate (occupation.rs:65-74), so a second activity cannot overwrite an active soccer session.
- Chat `place` argument alignment: `raw` has the "realm " prefix removed (4325), so `raw_words.get(2..)` in `developer_cheat` (2803) lines up with `rest` from `place_npc`. Names keep their case.
- `goto_place`, `place_npc` and `unplace_npc` float and index handling: non-finite values are filtered (3626, 3815), `atan2` and `flat_distance` are total, and all parsing is `.ok()`-guarded.
- `handle_warp`'s `Err` on `MalformedRequest` (3580): decode runs before any state change in `piece_077.rs` (1155, 1170, 1199, 1272), and the gateway treats it as a per-packet rejection.
- `developer_command_denied` / `may_run` ordinary list (3684-3698): the developer branches are all gated by `tool`, and no ordinary-listed word reaches a dev-only effect.
