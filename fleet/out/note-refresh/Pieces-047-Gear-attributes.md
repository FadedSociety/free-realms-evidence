<!-- fleet job=note-refresh id=Pieces-047-Gear-attributes status=nothing_found turns=19 usd=0.0258 tokens(read,write,in,out)=[725130, 71269, 40, 19196] model=claude-haiku-5-5 -->
# notes/Research/Pieces/047 Gear attributes.md

**Verdict:** current. Every checkable claim I could reach matches the tip. No corrections.

**Checked against the code and data:**
- `src/restoration/piece_047.rs` exists (634 lines). `CHARACTER_STAT_ID_COUNT` = 69, `NATIVE_ITEM_STAT_CONTAINER_CAPACITY` = 71, `INT_WIRE_TYPE` = 0 / `FLOAT_WIRE_TYPE` = 1, and `equip_gate` (line 609) and `decode_item_stat` (line 444) match the note's description.
- Stat kinds: the table holds 24 Float rows (ids 2, 3, 10, 12, 17, 20, 22, 24, 25, 27, 28, 31, 32, 34, 53, 56, 57, 59-63, 67, 68) and 45 Int rows. That is 44 Int defaults plus `InvalidStat`, which has no default, so the note's "44 int / 24 float" holds.
- `tests/piece_047.rs` exists and includes the module by `#[path]` (line 31). It has 8 `#[test]` functions, matching "8 passed".
- `tests/pieces/test_piece_047.py` has 4 `FixtureTests` and 3 `RealSourceTests`, so "7 tests" holds. It pins 58,800 item rows, 184 class rows, 911 absent `MinProfileRank`, 926 `MembersOnly`, and 10 and 3 for the override and equip-set rows.
- `scripts/pieces/piece_047.py` exists. `main` returns 2 on failure (lines 815, 818, 824), matching "fails closed (exit 2)".
- Not registered: `src/lib.rs` has no reference to `piece_047` or `restoration`, and there is no `restoration/mod.rs`. The note's "not registered in `lib.rs`" is correct.
- Item facts: the `piece_047.rs` `GEAR_STAT_ITEMS` table (lines 546-584) holds 18092 with 7 stats and 78397 with 8. The raw IEEE-754 bit patterns decode to the note's values (for example 1090519040 = 8.0, 1094713344 = 12.0, 1086324736 = 6.0). Slot 6, `CategoryId` 106, and `Param1` 13459 also match the community item rows. `Mounts.json` mount 13459 carries the same eight glide values plus `MaxMovementSpeed` 12.5.
- Class rows (lines 475-526): class 2 = `Ninja Gear`, profile name id 3100, owner profile 2. Classes 50, 69, 158, and 172 have no owner. `ItemClasses.txt` rows match.
- Equip policy (lines 609-634): a missing class returns `UnknownClass`, a class owner mismatch returns `WrongProfile`, rank below the floor returns `RankTooLow`, and `MembersOnly` without membership returns `MembersOnly`. This matches "Reconstructed policy".
- No Autopilot report or Build Ledger entry touches piece 047 since the note was written.

**Unsure:**
- The `lab/reports/piece-047-20261009T041533Z/` artifacts, `locale-id-to-text.json`, the native `pseudocode.c`, and the Sanctuary pinned tree are outside the repo, so I could not verify them or their sha256s.
- The restriction counts other than the three the Python test pins (`PowerRating` 20,338, `NoTrade` 10,575, `NoSale` 7,409, `SingleUse` 1,207, `GenderUsage` 3,836/4,163, 5,005 rows with no `Class`) are not pinned by any test I could read. I did not count the full 58,800-row table.
- The "only two of 58,800 rows carry a stat vector" claim is not verifiable from search. I checked the two rows and found no others in the community copy I read, but I did not scan the whole file.
- The gap line "StatId column for gear classes (recovered values 16, 19, 0)": the five classes in `GEAR_CLASSES` carry only 16 and 0. `ItemClasses.txt` does carry StatId 19 on other rows (for example `6^2926^40^9^19^3100`, which is also profile 3100 Ninja), so the note's wording holds if those rows count as gear. I left it unchanged.
- The `Ride` class (172) profile name id 5101171 resolving to a scope string with no profile row was not checked against `Profiles.json`.
