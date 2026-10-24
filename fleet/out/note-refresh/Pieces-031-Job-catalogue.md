<!-- fleet job=note-refresh id=Pieces-031-Job-catalogue status=done turns=23 usd=0.0315 tokens(read,write,in,out)=[1056120, 86503, 48, 20304] model=claude-haiku-5-5 -->
# notes/Research/Pieces/031 Job catalogue.md

**Verdict:** Current apart from one false clause about the client's use of the trial flags. The artifact paths, test counts, the `src/profiles.rs` claims, the Lua line numbers, the locale ids and the captured-payload set all check out at the tip.

**Corrections:**

- `old:` The client only reads `Trial`/`TrialExpired` in `ValidateJobForStartScreen`,
  `new:` The client reads `Trial`/`TrialExpired` in the job-list builder and forwards both to the job-browser SWF; only `TrialExpired` feeds `ValidateJobForStartScreen`,
  `why:` `ui:ScriptsBase.lua:8199-8206` (reads `trial` and `trialExpired`, passes both to `swf:Invoke("AddClass", ...)`, gates on `trialExpired` only); `ui:ScriptsBase.lua:8240-8247` (the function body tests `trialExpired` and `Ui.IsMember()`, never `Trial`); `ui:ScriptsBase.lua:58474` and `58484` (`populateJobsList` receives `Trial` and `TrialExpired` from both datasources). The conclusion that the exact policy is unrecovered still holds.

**Checked and holding (no change):**

- Artifacts exist: `src/restoration/piece_031.rs` (18-row `JOBS`, `validate_locale`, `LocalizedNameDiffers`), `tests/piece_031.rs` (8 `#[test]`s, `#[path]` include), `scripts/pieces/piece_031.py` (`LocalizedNameDiffers`, "piece 031 evidence ok" line), `tests/pieces/test_piece_031.py` (7 test methods), and `notes/WorkItems/031.md`.
- `piece_031` is still not registered in `src/` (no `mod piece_031`), so the `#[path]` wording is current.
- `src/profiles.rs:2` says unlock timing and the XP curve are reconstructed local rules. `src/profiles.rs:331` names the readers FUN_008d86e0 (38/14) and FUN_008d8910 (38/18). `src/profiles.rs:441` builds the 38/21 activation.
- `ScriptsBase.lua` lines 2844 and 2862 (`Profile_DS`, `Profile_Filtered_DS`) declare the same 16 columns. `StartJobQuest` is at line 8303 and uses column 0 and column 4. `SelectJob` is gated on `Ui.GetActiveProfileId() ~= tonumber(b)` (line 8283). `GroupMemberData_DS.PlayerJobId`, `QuestData_DS.JobLevel` and `PlayerInspectDS.JobsUnlocked` exist.
- Captured ids in the note's table match `CAPTURED_PAYLOAD_IDS` (16 entries). The profile-1 row matches the captured file: `refs:rust-opening/profiles.json`, length 579, sha256 `43de6f62810276c0…`.
- Classification counts (Combat 6, Crafting 3, Freestyle 7, Staff 2) match the `JOBS` rows. Nine `Trial` rows and all-false `MembersOnly` match. Pet Trainer is 17419 with a 2009-12-14 removal, matching `REMOVED_JOBS`.
- Locale: 4419970 and 4420004 are the two roster headers. 17419 is "Pet Trainer". 2919 is "Demo Derby Driver". 4419983 is "Demo Driver". 140763 and 4419987 are "Kart Racer". The short forms are achievement strings, as the note says.

**Unsure:**

- "`starter_items` covers six kits" (Limits section): I could not count it. `scripts/fixtures/starter_items.json` says the bundled `data/content` has no `profiles.json`, and no `profiles.json` with `starter_items` is in the repo. Needs a check against the runtime content directory.
- The wiki membership list (Chef, Kart Driver, Pet Trainer, Postman, Warrior, Wizard), the wiki classification roster, and the trainer lines (Ashley Lightwings, Carlos Brazenfist, Harold, Caitlyn Gravefog) were not checked. The checker has a `trainer_lines` function, but the lab report JSON is outside the readable roots.
- The lab report paths (`lab/reports/job-catalogue-20261009T022023Z/`, `piece-031-20261009T035045Z/`) and the 85,932-row count are not readable from here. The test comment cites the same count.
- Hashes for ids 16 and 137 were not matched in `refs`. Only id 1 was confirmed.
