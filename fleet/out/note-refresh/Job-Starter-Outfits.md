<!-- fleet job=note-refresh id=Job-Starter-Outfits status=done turns=11 usd=0.0153 tokens(read,write,in,out)=[249010, 49854, 24, 13094] model=claude-haiku-5-5 -->
# notes/Research/Job Starter Outfits.md

**Verdict:** minor drift in the proof sections, badly stale in the W84 handoff and remaining-gates sections. The starter-list proofs hold: the six lists are still selected from `DefaultItems` at `scripts/prepare-opening-base.py:152`, and all 15 `DefaultItems` line numbers in the table match the pinned Legacy `Profiles.json`. The "seven missing definitions" and "not registered" gates were overtaken by W84/W88 and the round70 package.

**Corrections:**

1. old: `Seven of the 77 proposed starter definitions are absent:`
   new: `Seven of the 77 proposed starter definitions are absent from that captured file. They are no longer missing from the shipped package: W84's generated catalogue (`item-catalogue.json`) is loaded by W88, and round70 carries 4914, 29963 and the Kart Driver jersey 13419 (see the Build Plan 2026-10-16 entries).`
   why: `repo:notes/Design/Build Plan.md:154` (W88 loads W84's catalogue); `repo:notes/Design/Build Plan.md:156` ("Kart Driver's jersey 13419 is missing from the catalogue until W88 loads W84's definitions"); `repo:notes/Autopilot/T368.md:49-52` (round70 "already carries all of it", including 4914/29963); `repo:scripts/bundle/item_content.py:4` (the generated 58k-row catalogue).

2. old: `Warrior 29963 and Wizard 4914 require catalogue coverage.`
   new: `Warrior 29963 and Wizard 4914 were given catalogue coverage after W82: T010 and T368 install their captured client rows, and the round70 package now carries them.`
   why: `repo:notes/Autopilot/T010.md:5-7` (starter weapon definitions 4914 and 29963 wired); `repo:notes/Autopilot/T368.md:45-52`.

3. old: `**Lead/W84:** provide the seven missing definitions; review gender-specific equip behavior; register the chosen lists in a new private content package.`
   new: `**Done since W82:** the lists are registered in the round70 active play package (14 jobs), and W84's generated catalogue supplies the missing definitions. **Still open:** native acceptance of gender-specific equipping; W138 built equip eligibility including gender, but it has not been run natively.`
   why: `repo:notes/Design/Build Plan.md:156` ("job outfits integrated ... round70 = round69 + W82 starter lists (14 jobs)"); `repo:notes/Current Progress.md:5`; `repo:scripts/build_item_catalogue.py:316-318` (the generator reads `starter_items.json`); `repo:notes/Design/Build Ledger.md:91` (W138 gender eligibility, native not verified).

4. old: `This is a proposed field replacement, not a complete profiles package.`
   new: `This field was integrated into the round70 active play package (2026-10-16 "job outfits integrated"); it is not a standalone profiles package.`
   why: `repo:notes/Design/Build Plan.md:156`; `repo:notes/Current Progress.md:5`.

5. old: `The warnings include 16,551 unresolved runtime item references; W82 did not change those content files.`
   new: `At W82 time the warnings included 16,551 unresolved runtime item references. W84's generator covers all 16,551 missing references, so re-run the checker before quoting a current count.`
   why: `repo:notes/Design/Build Plan.md:162` (generator "covers all 16,551 missing references"); `repo:notes/Design/Build Ledger.md:93` (content_check applies the loader's rules to the merged set).

**Unsure:**
- The other five missing IDs (19431, 13317, 12416, 12252, 13419 is covered above) are not individually confirmed in the round70 `item-catalogue.json`. That file lives in `lab/`, which is not searchable from these roots, so the replacement in correction 1 only claims 4914, 29963 and 13419.
- The `lab/` evidence (native addresses such as `008fc960`, `0103e5e0`; `ClientPcData.cs` lines; `ItemFilterOptions.txt` lines; the 264 ADR and 77-definition counts; the 1,703/1,649 counts; the six-join equipment tables) could not be checked, because `lab/` is not among the roots. The helper functions the note cites do exist: `prepare-gameplay-inventory.py` (`item_state`, `item_bytes`, `unique_offset`), `prepare-opening-base.py::profile_bytes`, and `nmq.py`.
- Pet Trainer 121 is said to be absent from Legacy profiles. I did not check that against the full `Profiles.json`; I only confirmed the DefaultItems line numbers for the 15 listed entries.
