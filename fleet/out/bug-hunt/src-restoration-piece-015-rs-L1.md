<!-- fleet job=bug-hunt id=src-restoration-piece-015-rs-L1 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[25919, 18638, 10, 3412] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_015.rs lines 1-282 of 282

Window reviewed in full: `prototype/osfr-tools/src/restoration/piece_015.rs` lines 1-282. No high or medium defects. I found one low-severity logic issue, and it has no player-reachable path.

**[low] prototype/osfr-tools/src/restoration/piece_015.rs:155-156 - `optional_u32` turns any malformed non-empty numeric cell into 0, and `IS_FLASH` (line 209) turns a missing column into "not flash", so a schema or data error is swallowed instead of reported.**
- **Failure scenario:** a `MiniGameData.txt` row has `DIFFICULTY=x` or `LEADERBOARD_ID=12a`. `optional_u32` returns 0 and `parse` succeeds, so the bad value is silently accepted. Separately, if `MiniGameTypeData.txt` lost its `IS_FLASH` column, `Table::value` returns "" for every row, so `launch_mode` (line 252-259) reports `Native` for every type with no error. The `TYPE` and `ID` columns are checked by `required_u32`, but `IS_FLASH` is not.
- **Reach:** `LaunchCatalogue::parse` (line 171) is the only entry point. Its inputs are the four server-side resource text files, not packet fields, and no caller exists. The module is not registered in `lib.rs` or `restoration/mod.rs`, and `search` for `LaunchCatalogue`, `launch_mode`, and `games_in_group` finds no use outside this file. A remote player cannot reach it. The lenient parsing of optional cells is documented on line 154 for empty cells, so this is at most a design weakness and not a crash or gain.
- **Fix:** have `optional_u32` return an error when a non-empty cell fails to parse, and have the `IS_FLASH` lookup use `required`-style column checking (`column("IS_FLASH")` must exist).

Checked and ruled out:
- No panic path: `row.get(index)` is bounds-checked, `split('^')` cannot panic, and `from_utf8` is not used on any input here.
- No unbounded growth from client input: the tables are read from disk and there is no client-supplied count.
- No atomicity issue: `parse` builds locals and only returns `Self` on success.
- `games_in_group` filters links to unknown games, which matches its doc comment.
- Duplicate ids are rejected for games, types, and groups, as the doc on line 170 states.
