<!-- fleet job=note-refresh id=Pieces-042-Soccer-and-postman-progression status=done turns=23 usd=0.0260 tokens(read,write,in,out)=[911166, 70044, 48, 16157] model=claude-haiku-5-5 -->
# notes/Research/Pieces/042 Soccer and postman progression.md

**Verdict:** minor drift. The module, tests, locale and client citations check out at the tip. Two statements need correcting: one overstates the tutorial helper, and one misses a reconstructed crosswalk that now exists in the repo.

**Corrections:**

1. `old:` - `soccer_tutorial_advance(page, action_column)` reproduces the client tutorial advance rule.
   `new:` - `soccer_tutorial_advance(page, action_column)` reproduces the client's page/column transitions only. It takes no value argument, so the client's non-zero value check and its `SoccerIsActive` guard are not modelled.
   `why:` The client's `OnDataChanged` returns early unless `SoccerIsActive`, maps `value == 0` to false, and advances only when `value == true` (`repo:ui/ScriptsBase.lua:25753-25774`). The Rust helper matches on `(page, columns)` alone (`repo:prototype/osfr-tools/src/restoration/piece_042.rs:658-663`, table at `:521-552`). Its doc comment at `:520` calls the table "column/value pairs", but the table has no values.

2. `old:` community breadcrumb id has no matching row in any recovered quest corpus.
   `new:` community breadcrumb id has no row in the recovered quest records. The repo's reconstructed crosswalk maps it to regional quest 3140001 `Become a Soccer Star` (`prototype/osfr-tools/data/content/breadcrumb_quests.json:345-362`, `original_quest_id` 1881, `poi_ids` [117]). That quest is a reconstructed record (`prototype/osfr-tools/data/content/quests/soccer_star.json:5-18`), and the crosswalk notes it is "Hollow and disabled today". It is not a recovered unlock quest id, so `unlock_quest_ids_recovered = false` still holds.
   `why:` `repo:prototype/osfr-tools/data/content/breadcrumb_quests.json:345-362`; `repo:prototype/osfr-tools/data/content/quests/soccer_star.json:5-18`.

**Checked and holding:**
- Module path, helper names and `XP_CURVE_RECOVERED`, `UNLOCK_QUEST_IDS_RECOVERED` and `SOCCER_TUTORIAL_SOURCE_COLUMN_MEANING_RECOVERED` all set to `false` (`piece_042.rs:568-574`). `#[path]` include and the unregistered module are correct (`tests/piece_042.rs:30-34`; no `mod piece_042` in `src`).
- Test counts: 8 `#[test]` in `tests/piece_042.rs`; 9 `def test_` in `tests/pieces/test_piece_042.py`.
- Locale rows for 3237/3238/4650, 34115-34124, 34195-34204, 387931-387945 and 93381 match the locale tool.
- Client Lua: `DS_SOCCER_TUTORIAL = 25` (`ScriptsBase.lua:4819`), `pageCount = 7` (`:26108`), the transition pairs, images 20999/20998/20248 (`:25777-25781`) and pickups 11542/17353/18855 (`:25829`, `:26163-26171`).
- `CodeStringMappings.txt`: `SoccerTut0001-0007` = 406669-406674 and 416748; `SoccerTutIcon0001/0002/0004` = 406675/406676/406678; `MailSortingTutorialOneTop/Bottom` = 19323/19302 (`client:Resources/CodeStringMappings.txt:1915-1916, 2942-2952`).
- POI 117 `Snowhill Soccer Field`: name 407110, location 207771, position, heading and breadcrumb 1881 (`refs:Sanctuary/src/Resources/PointOfInterests.json:1472-1486`).
- Profile 4 and 52 rows and class 3 / 134 names (`refs:Sanctuary/src/Resources/Profiles.json:251-269, 1457-1470`; `ItemClasses.txt:4, 135`).
- `Profile_DS` columns 5/11/12 (`ScriptsBase.lua:2851-2858`).
- `soccer_tutorial_advance` is referenced only by `piece_042.rs` and its test, so "wired into no client or gateway path" holds.
- No `notes/Autopilot/` report changes piece 042 since it was written.

**Unsure:**
- The SHA-256 values in the Artifacts table could not be recomputed with the tools available.
- The activity row numbers (42/43/44 and the Postman rows) come from `lab/reports/minigame-content-inventory.json`, which is not in the repo. I could not check them. `notes/Research/original-activity-coverage.json` lists the same names, but I did not compare the row numbers.
- The wiki claims (30 quest entries, the Goal Time update date, the stat lists) are external and were not checked.
