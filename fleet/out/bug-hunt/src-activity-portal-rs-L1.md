<!-- fleet job=bug-hunt id=src-activity-portal-rs-L1 status=done turns=12 usd=0.0090 tokens(read,write,in,out)=[181453, 24746, 26, 8235] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/activity_portal.rs lines 1-396 of 396

One finding, reached through the reload path rather than inside the window. Everything else in `activity_portal.rs` 1-396 checked clean.

- **[medium] prototype/osfr-tools/src/gameplay/content_reload.rs:57-63 - `realm reload battles` (or `reload all`) rebuilds the portal catalogue from `field_battles.json` and chess rows only, so the soccer rows added at startup are silently dropped until restart.** The rebuild is `Catalogue::load` (activity_portal.rs:214-238) plus `with_chess_rows` (activity_portal.rs:251); neither adds soccer.
  - **Failure scenario:** The server starts with `soccer.json` present. Startup builds `activities` from battles, adds chess rows, then calls `add_soccer_rows(content.portal_rows())` (gameplay.rs:951-957). An admin runs `realm reload battles`. `reload_content_in_place` sets `self.activities = Catalogue::load(&path)?` (content_reload.rs:57), which holds only battle rows, and `with_chess_rows` re-adds chess (58-63). The soccer rows are never re-added. Afterwards:
    1. `list_packet` (activity_portal.rs:308) omits the soccer activity from 167/1/1, so the portal loses it.
    2. A Play for the soccer id reaches `admit` (activity_portal.rs:274) and returns `Refusal::Unknown`, even though `self.soccer_content` is still loaded and `begin_soccer` (gameplay.rs:3289-3295) would have served it.
    The reply still says "Reloaded: battles.", so the operator is not told.
  - **Reach:** Chat `realm reload battles` -> gameplay.rs:2891-2897 -> `reload_content` (content_reload.rs:20-35) -> `reload_content_in_place` (content_reload.rs:52-63). The command is developer-only (the account role gates developer commands, see `developer_teleport.rs`), so this is an operator-triggered logic error, not a remote player one. The staging and atomic commit are fine; only the content set is wrong.
  - **Fix:** In content_reload.rs, after line 63 and inside the staged block, re-add soccer rows when `staged.soccer_content` is set: `if let Some(content) = &staged.soccer_content { self.activities = self.activities.clone().add...` (or, more simply, `staged.activities.add_soccer_rows(content.portal_rows())?;` before the `done.push`). Alternatively, move the startup catalogue build (gameplay.rs:939-957) into one function and call it from both places.

No other defects were found in the window. Checked and cleared:
- `parse` (activity_portal.rs:361-374): the slice and length checks are safe (`inner[..2]`, `inner[4..8]` guarded by `len() == PLAY_LEN`).
- `list_packet` row count: capped at 64 by `validate_rows` and `with_chess_rows`, so `as i32` is safe; `position as u32 + 1` is at most 65.
- `icon_id`: `u32::try_from(...).unwrap_or(0)` (line 231).
- `add_soccer_rows` validates before it mutates.
- `with_chess_rows` consumes `self` on error, so no partial state is visible.
- Admission and list `can_join` agree for all three kinds: battle via `level_refusal` (encounter/field.rs:33), chess open, soccer `level < required`.</result>
