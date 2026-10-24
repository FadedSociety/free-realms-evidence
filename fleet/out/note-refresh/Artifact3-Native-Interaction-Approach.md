<!-- fleet job=note-refresh id=Artifact3-Native-Interaction-Approach status=nothing_found turns=12 usd=0.0124 tokens(read,write,in,out)=[275506, 46707, 26, 7691] model=claude-haiku-5-5 -->
# notes/Research/Artifact3 Native Interaction Approach.md

**Verdict:** current. Every checkable claim about our code and status holds at the tip. I found no false statement and no moved citation to correct.

**Checked and holding:**
- **Server 12 m radius.** The Artifact3 actor (GUID 5715144128442925079, `Gloam Artifact`, position `[-1838, -46.92, 370]`) carries `interaction_radius: 12.0` in `repo:prototype/osfr-tools/tests/fixtures/quests/opening.json:489-511`. The range check is `repo:prototype/osfr-tools/src/gameplay.rs:4498-4509`, which compares squared distance against `actor.interaction_radius`. The note's "server's 12 m radius" is correct.
- **Ordered objective and actor binding.** Objectives 91001001–91001003 bind to actors 5715144128442925077–079 (`repo:prototype/osfr-tools/src/restoration/piece_068.rs:64-66`, `opening.json:2164-2182`). The note's "objective 91001003" and GUID "…5079" match.
- **Frame and state numbers.** Menu 7729, choice 7769, removal 7772, objective frames 7773–7774, coins 194, HP 895 and "allows only the ordered objective counts to change" all match `repo:notes/Reviews/Native Bartle and Artifacts 193318.md:28-30`.
- **Native 7 m fallback.** The "observed native default X range of 7 m" matches `repo:notes/Research/Native Interaction Acquisition Range.md:11`, which records the effective fallback prompt radius as 7 m.
- **Status.** Nothing in `notes/Autopilot/` or `notes/Design/Build Ledger.md` changes the artifact path. `repo:notes/Current Progress.md:128` says ordinary native walking and interaction completed all three ordered artifacts, which agrees with the note's "reachable and interactable".
- **Arithmetic.** The 0.08796 m, 6.36145 m, 6.27955 m and 0.13855 m margins follow from the coordinates the note gives. The close-path length is about 5.26 m, consistent with the stated 5.26128 m.

**Unsure (not checkable from the repo; they cite lab artifacts outside it):**
- Navigation log IDs 200854, 200907 and 200918, the "arrived with radius 0.5 m" result and "A/D/W only" input.
- "The retained input interval contains no Space" and the single X press plus `click 640 506`.
- The proof SHA256 values and the 438-source count in `lab/reports/artifact3-native-193318-v1/proof.json`.
- All slope, grade, normal-Y and triangle-clearance figures, which come from the lab geometry reports.
- Original screenshot filenames under `lab/runs/`.
