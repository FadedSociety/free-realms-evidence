<!-- fleet job=note-refresh id=Native-Creator-Delivery-Proof status=nothing_found turns=11 usd=0.0157 tokens(read,write,in,out)=[307104, 56597, 24, 11061] model=claude-haiku-5-5 -->
# notes/Research/Native Creator Delivery Proof.md

**Verdict:** current. The code-checkable claims hold at the tip; the rest is dated run evidence or private `lab/` material that I cannot read from here.

**Corrections:** none.

Checked against the tip:
- **Journal writer and root layout** (note lines 5, 9, 44): `OpeningJournal::patch_self` replaces the inherited journal with accepted opening entries. It writes count, full records, rewarded count, first quest ID or `-1`, a selection flag of `0`, then the eight preserved root bytes. That matches "questcount0 / selected-1 / AutoSwitch false / tail" for the empty run (`repo:prototype/osfr-tools/src/opening_journal.rs:270-282`). `Gameplay::patch_self` calls it on the self packet (`repo:prototype/osfr-tools/src/gameplay.rs:1572-1574`).
- **Opcode 49 add vs. update** (line 46, "no 49/9 counter-update packet"): an accept of a not-yet-visible quest emits subtype 3 with a force-select byte. Subtype 9 is emitted only when a visible quest's objective count changes (`repo:prototype/osfr-tools/src/opening_journal.rs:344-366`; `repo:prototype/osfr-tools/src/quest_engine.rs:514-516`).
- **Opcode 35/subtype 37 definitions packet** (line 21): `startup_catalogues.rs:128` builds `header(35, 37)`.
- **Opcode 38/21 profile activation** (line 46): `restoration/piece_044.rs:98` and `profiles.rs:419` both cover it.
- **Class selection 26/13** (line 46): `gateway.rs:2102` routes it to `class_selection`.
- **Quest 910001 "Hero's Journal"** (line 46): `tests/fixtures/quests/opening.json:596-600`.
- **Opening stage count** (17 stages, "remaining 16" after one accepted): the opening content has 17 stages (`repo:notes/Current Progress.md:17`, `repo:prototype/osfr-tools/tests/quest_engine.rs:662`).
- **Cross-note links:** `Native Opening Quest Journal`, `Native Asset HTTP Delivery`, `Native NPC Motion and Animation`, and `Native Quest Journal UI` all exist under `notes/Research/`. The journal note's own "25 unrelated quests" matches this note's "25 inherited research quests" (`repo:notes/Research/Native Opening Quest Journal.md:3`).

**Unsure:**
- The gateway SHA256 values (`447161…`, `5063442e…`, `7e53bc…`) and the `1,632` definition count cannot be checked from the repo. `1,632` does not appear in any source file. The count is from a private run.
- The `lab/reports/*.py` helpers and `lab/runs/...` JSON are outside the readable roots, so the reconstruction and byte-match results (161,293 / 161,280 / 153,375 / 153,362 bytes) are unverified here.
- The 404 for `human_m_head_caucasian_08.dds` and the "not World Ready" result describe the first run only. I did not check whether that asset path is served correctly at the tip. The note's "Correct `.z` delivery is established separately" points to `Native Asset HTTP Delivery`, which I did not read.
- Ready6 / Loaded10 absence in the first run is a historical observation. I found Loaded10 referenced only in a comment (`repo:prototype/osfr-tools/src/gameplay.rs:1844`).
