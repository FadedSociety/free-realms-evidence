<!-- fleet job=note-refresh id=Pieces-014-Forging-recipes-content status=nothing_found turns=15 usd=0.0180 tokens(read,write,in,out)=[453395, 56474, 32, 12870] model=claude-haiku-5-5 -->
# notes/Research/Pieces/014 Forging recipes/content.md

**Verdict:** current. Every checkable code and status claim in `014 Forging recipes/content.md` holds at the tip. I found no false statement that needs a text change. One sentence is ambiguous enough to be worth a human look (see Unsure).

**Checked and holding:**
- Artifacts exist: `prototype/osfr-tools/src/restoration/piece_014.rs`, `prototype/osfr-tools/tests/piece_014.rs`, `scripts/pieces/piece_014.py`, `tests/pieces/test_piece_014.py` (all listed in `notes/WorkItems/014.md:8-12`).
- Not registered: no `piece_014` or `restoration` module line in `prototype/osfr-tools/src/lib.rs`. The owned test does `#[path = "../src/restoration/piece_014.rs"] mod piece_014;` (`tests/piece_014.rs:7-8`), as the note says.
- Test counts: `tests/piece_014.rs` has 7 `#[test]` functions (lines 16, 41, 67, 81, 105, 118, 134). `tests/pieces/test_piece_014.py` has 4 `def test_` methods (216, 230, 238, 250).
- Pattern catalogue: `PATTERN_COUNT = 28`, `patterns().len()` asserted 28 (`src/restoration/piece_014.rs:35`, `tests/piece_014.rs:18-19`). Record 2506 is `Param1 11`, `NameId 1565`, `DescriptionId 1587`, category 17, type 5 (`piece_014.rs:118-126`). 838 is the one non-category-17 record, and 869 is the Chef mousse (`piece_014.rs:91-108`, `tests/piece_014.rs:29-36`).
- Locale: 1587 reads "This recipe teaches you how to create a Spunky Scrapper Hammer." and 102173 reads "Spunky Scrapper Hammer" (locale tool).
- Equipment: `30280`-`30289` are class 71, slot 7, category 207, model `hammer_ar_ag_weapon_logjammer.adr` (`piece_014.rs:345-425`). `75030` is class 25 in this table (`piece_014.rs:427-431`). `6459` is class 34, category 107 (`piece_014.rs:435-440`).
- Class owners match the table in the note: 25→43 (wield 0), 34→16 (0), 58→16 (0), 71→43 (13) (`piece_014.rs:450-475`).
- Profiles: 16 (Blacksmith) allows 14, 34, 48, 49, 58, 60, 67, 69, …, and has slots `[1,2,3,4,5,7,13]`. 43 (Brawler) allows 5, 25, 42, 50, 52, 69, 71, …, and has slots `[1,2,3,4,5,7,8,12,6]` (`piece_014.rs:477-498`). 16 does not admit 71 and 43 does not admit 58, as stated.
- Slot 7 is `Weapon` with `is_weapon: true` (`piece_014.rs:444-448`). The client line `Resources/EquipmentSlotDefinitions.txt:8` reads `7^...^Weapon^...`.
- `check_equip` exists at `piece_014.rs:550` and applies the class allowlist plus slot spool check (`allows`, lines 534-546), as described.
- Consumption `10 Copper Bars, 5 Turquoise, 5 Wooden Planks, 5 Thorny Fasteners` appears at `src/gameplay/crafting.rs:145`, which matches the note's "reconstructed, unchanged here" line.
- Checker: `scripts/pieces/piece_014.py` emits a `warn` status for the 75030 class disagreement (`piece_014.py:462-466`) and writes to `lab/reports/piece-014-<UTC>` (`:590`).

**Corrections:** none that I could confirm as false.

**Unsure:**
- `notes/Research/Pieces/014 Forging recipes/content.md:33-34`: "the substitute the current opening campaign still compares against at slot 7." The prior opening generator `scripts/prepare-opening-content.py:138-139` still targets `75030` (the substitute goal). But the forging campaign generator `scripts/prepare-forging-campaign.py:75-79` replaces that goal's `definition_id` with `30280`, and `:93` sets `local_substitutions.hammer = 30280`. `notes/Research/Original Forging.md:19` says the forging campaign is only enabled through the migrator, so whether "current" means the live 75030 goal or the migrated 30280 goal is not settled by the code I read. If the migrated campaign is the intended current one, the sentence should say the prior opening targets 75030 and the forging campaign retargets to 30280.
- The lab-side evidence (`../lab/reports/piece-014-20261009T030806Z/…`, the pinned source hashes, the `lab/working/…` server customize file that gives 75030 class 71, and the "13 checks: 12 pass, 1 warn" run) lives outside the repo, so I could not verify it. The test-count and checker-warn logic above is consistent with it.
- The `ItemClasses.txt` / `Profiles.json` pinned values and the community Blacksmith page match are outside the tip and were not checked.
