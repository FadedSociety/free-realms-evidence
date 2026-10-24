<!-- fleet job=note-refresh id=Pieces-029-Housing-decoration-discovery status=done turns=17 usd=0.0284 tokens(read,write,in,out)=[791011, 83046, 36, 20273] model=claude-haiku-5-5 -->
# notes/Research/Pieces/029 Housing decoration discovery.md

**Verdict:** minor drift. The note's status, owned paths, test counts, gate policy and refusal order all match the tip. One Lua line citation no longer points at the Exterior group.

**Corrections:**

- `old:` (`ScriptsBase.lua:33244`, `:33265`)
  `new:` (`ScriptsBase.lua:33265`; the `Wall` / `Floor` / `Roof` names behind `GetFixtureGroupByType` are the `CatStrs` rows at `:33244`–`:33246`)
  `why:` ui `ScriptsBase.lua:33244` is `CatStrs[59] = "Wall"`, not the Exterior group. `GROUPID_EXT = "Exterior"` is at `:33265`. `CatStrs[51] = "Floor"` and `CatStrs[55] = "Roof"` are at `:33245`–`:33246`.

**Checked and holding (no change needed):**

- Owned paths exist: `repo:prototype/osfr-tools/src/restoration/piece_029.rs` (456 lines), `tests/piece_029.rs` (974 lines, `#[path]` include at line 33), `scripts/pieces/piece_029.py`, `tests/pieces/test_piece_029.py`.
- Not registered: `repo:prototype/osfr-tools/src/lib.rs` has no restoration or piece_029 registration, so the "lead integration" gap is still open. Work Queue row 029 agrees ("lead review/integration/native pending").
- Test counts: `tests/piece_029.rs` has 16 `#[test]` functions plus one `#[ignore]` private gate (line 550–551), matching "16 passed, 1 ignored". `tests/pieces/test_piece_029.py` has 16 `def test_` functions.
- `Resources/StringHashToValue.txt:78–80` has exactly the three `*FixtureActionName` rows, and `:81` `Housing.StaticSeatingDisabled^1` and `:133` `RatingSystem.HousingId^Housing` are present.
- `ScriptsBase.lua:33248–33252` (five interaction ids), `:33358` and `:33389` (SelectedFixture), `:33801` (RemoveFixture), `:33822` (MoveFixture), `:33925` (`-1` closes menu), `:33805` (members-only guest menu) and `:33731–33741` (House.* calls) all match.
- `IsActionPermitted` appears only with `"RemoveFixture"` and `"MoveFixture"`, and `Elevate` has no call site. The note's gap 3 is accurate.
- `Resources/Requirements.txt`: 43 rows (IDs 1–43) over exactly the six factories listed. `RequirementGroups.txt` has 39 rows and `RequirementSets.txt` has 34. `HousingPlacementData.txt` has rows `1^1^test.adr` and `2^1^test2.adr`. `HousingPlacementAssociations.txt` has one row. `HousingNames.txt` has two string ids.
- The gate matches the note: `src/restoration/piece_029.rs:308–309` gives the refusal order (edit, selection, interaction, definition, members-only, declared action, requirement). `:325` is the members-only rule, `:261–273` the named gates, `:340–347` the requirement-0 and unknown-id rules, and `:240–249` the interaction ids.
- Wire claims: `piece_025.rs` decodes PlaceFixtureRequest, PickupFixture, SaveFixture and PreviewByItemDefinitionIdRequest (opcode 20).
- `refs:FreeRealms-Legacy/.../Housing/FixtureDefinition.cs` has `Actions`, `FixtureAction.RequirementId` and `CompositeEffectId`.

**Unsure:**

- The `pseudocode.c:` line numbers (1402661, 1397564, 1191058, 1840204, 1702798, 1795360, 1409677, and others) cannot be checked here. The client DB confirms the strings and functions exist: `Adding HousingFixtureMove objective` is in `fn 00c43940`, `Failed to find ModelDefinition for modelId` in `fn 00ac7f40`, and the `HashListMap<int,FixtureDefinition::FixtureAction,16,-1>` constructors in `00abc420`, `0105ab30` and others. The DB has no line numbers.
- "carries exactly this shape" (`FixtureDefinition`): the file also has `Id`, `Unknown*` fields and `Category`/`LuaCall` as nullable strings. The listed fields are all present, so the claim holds in substance, but "exactly" is loose.
- The "22 vectors / 22 agreements" and the regression counts (26 + 8 + 12, `--lib` 24) cannot be verified without running the suites. The exported-vector loop is at `tests/piece_029.rs:875`, and `scripts/pieces/piece_029.py:315–329` compares them.
- The sha256 hashes cited for `StringHashToValue.txt`, `Requirements.txt`, `ScriptsBase.lua` and the packet model were not recomputed.
