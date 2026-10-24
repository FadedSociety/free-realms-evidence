<!-- fleet job=note-refresh id=Opening-Historical-Coverage-Ledger status=done turns=23 usd=0.0295 tokens(read,write,in,out)=[953055, 83226, 48, 19211] model=claude-haiku-5-5 -->
# notes/Research/Opening Historical Coverage Ledger.md

**Verdict:** Minor drift in the code and path claims, badly stale in the native-status cells. The local code and citations I could check still hold. The stage 7 to 17 acceptance language predates the October 9 native runs that Current Progress records as accepted.

**Corrections:**

1. Stages 8-12 row, status cell.
   - `old:` Implemented and packet/restart simulation passes; root's continuing native playthrough is a separate gate.
   - `new:` Native accepted: Gloam combat, Bartle and the three artifacts, Mac, and Queen (Reviews/Native Gloam Combat 183551, Reviews/Native Bartle and Artifacts 193318, Reviews/Native Queen and Prompt 203139). Packet and restart checks also pass.
   - `why:` repo:notes/Reviews/Native Bartle and Artifacts 193318.md:3 and :7 (Bartle, artifacts, Mac accepted); repo:notes/Current Progress.md:138 (lists the native Gloam, Bartle and Queen reviews as evidence).

2. Stages 16-17 row, status cell.
   - `old:` Native acceptance remains separate.
   - `new:` Native run `client-baseline-20261009T103605Z` completed the ordered job-center tour, the Adventurer/Medic/Archer/Chef switches and the Student Chef Hat equip. Restart `client-baseline-20261009T111125Z` reloaded them (Reviews/Native Opening 17 103605).
   - `why:` repo:notes/Current Progress.md:92 and :94; repo:notes/Reviews/Native Opening 17 103605.md:3 and :9.

3. Stages 13-15 row, status cell.
   - `old:` Native repeat-contract acceptance remains separate.
   - `new:` Stage 15 Smelting/Forging is natively accepted (run 103605). Cleetus and Sunspark repeats left the save byte-identical in that run. Mae and eleventh-ore repeats left the save unchanged in run 054421. Stage 13 repeat acceptance is therefore partial, not absent.
   - `why:` repo:notes/Current Progress.md:92 and :106; repo:notes/Reviews/Native Opening 17 103605.md:3.

4. Stage 7 row, status cell.
   - `old:` Cleetus turn-in was still pending at the reviewed checkpoint.
   - `new:` Cleetus turn-in was still pending at the reviewed checkpoint. It was accepted at the next checkpoint: 146 to 164 coins and Brawler XP 125 to 150 (Reviews/Native Outdoor Wolf Controls 183551).
   - `why:` repo:notes/Reviews/Native Wolves and Anvil 183551.md:11; repo:notes/Reviews/Native Outdoor Wolf Controls 183551.md:21. The original sentence is accurate for the cited checkpoint, so this is a pointer update only.

Checked and holding:
- `StartingZone.cs` lines 867/879/891 are the region-1 records for quests 2572, 2573 and 2587 (repo:refs `FreeRealms-Legacy/src/Sanctuary.Game/Zones/StartingZone.cs:867-900`).
- Quests 2572, 2573 and 2587 do not appear in the Rust source, so they are absent from the 17-stage chain.
- Every stage in the fixture uses a 910xxx ID with `original_quest_id: null` (repo:prototype/osfr-tools/tests/fixtures/quests/opening.json:597 onward).
- The job-center unlock profiles 45, 14, 16, 11 and 35, plus initial profiles 1 and 43, total seven (same fixture).
- Hammer 30280 is the authentic forging output (repo:prototype/osfr-tools/src/restoration/piece_014.rs:347). The 14794 hat is a stage 6 item reward in the fixture (line 840).
- Human/Pixie creator rows are documented (repo:prototype/osfr-tools/src/restoration/piece_049.rs:16-17).
- Sheep Watch and Highroad Hijinx exist only as gate rows in repo:prototype/osfr-tools/src/restoration/piece_059.rs:144,149. Neither is implemented as a dungeon.
- The Starting Area Content Audit exists and reports the same 17 stages, 51 objectives, 27 actors and 4 discovery markers (repo:notes/Research/Starting Area Content Audit.md:38).

**Unsure:**
- `lab/references/opening-anvil-placement-v1/content/opening.json` (SHA256 `4e6ac15c…`), `lab/reports/opening-historical-coverage-ledger.json`, and `profiles.json` ("16 profile records") are not in the repo snapshot. The 17/51/27/4 counts, the 13 hub records and the 16 profiles cannot be checked from here.
- "Palace entry is a zone0 proximity marker" and "Mac is a local outdoor fight" are not located in `src/opening.rs`. A broader search found no match for "proximity" tied to the palace.
- The wiki revision numbers (27815, 28955, 49122, 49129, 49729, 46065, 43870) are outside the repo and were not checked.
