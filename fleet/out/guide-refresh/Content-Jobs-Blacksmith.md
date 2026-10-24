<!-- fleet job=guide-refresh id=Content-Jobs-Blacksmith status=done turns=20 usd=0.0250 tokens(read,write,in,out)=[886607, 79126, 42, 12402] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Blacksmith.md

**Verdict:** minor drift. Most of the note is client-locale and wiki evidence, which I did not check against code. The code-checkable claims mostly hold. One is now stale: the server grants rewards on two Blacksmith quests that the note says have none.

**Corrections:**

1. Gaps, "Rewards" bullet (line 380)
   - `old:` `- **Rewards.** No coin, XP, star or item reward is known for any quest. Recipe teaching is known for rows 6, 7, 13 and 18 only.`
   - `new:` `- **Rewards.** No coin, XP, star or item reward is known from any source for any quest. The server's content grants a reconstructed 5 coins and 20 Blacksmith job XP on rows 3 and 5 (Smithy Merchandise, Curious Cancelation), a local fallback with no source behind it. Recipe teaching is known for rows 6, 7, 13 and 18 only.`
   - `why:` `repo:prototype/osfr-tools/data/content/quests/blacksmith.json:98` and `:145-158` (quest 3020003 "Smithy Merchandise": `coins: 5`, `job_xp {"16": 20}`, source kind "reconstructed"); `:264` and `:307-320` (quest 3020005 "Curious Cancelation", same values). The test `repo:prototype/osfr-tools/tests/blacksmith_first_order.rs:235-238` asserts the 5 coins and 20 XP.

2. Row 3 "Smithy Merchandise", Rewards cell (line 83)
   - `old:` `unknown. A "You receive 100 coins" line is on screen while the quest is still open (2fhn8kePbKQ/00648), so it is not attributed to the quest.`
   - `new:` `unknown from any source. The server content grants a reconstructed 5 coins and 20 Blacksmith job XP (no source; see Gaps). A "You receive 100 coins" line is on screen while the quest is still open (2fhn8kePbKQ/00648), so it is not attributed to the quest.`
   - `why:` `repo:prototype/osfr-tools/data/content/quests/blacksmith.json:145-158`; `repo:prototype/osfr-tools/data/content/quests/blacksmith.json:98`

**Checked and current (no change):**
- `Forging139` board geometry: the 14x14 `SIDE` and an 8x8 playable area, 180-second duration and 10% collectable chance match the test fixtures (`repo:prototype/osfr-tools/src/forging.rs:20`, `:1224-1243`).
- Rust server note (line 344): `repo:prototype/osfr-tools/src/forging.rs:1` is the server-owned board service, so the claim holds.
- Only one Forging item is tied to a native run (line 386). The Current Progress note agrees (`repo:notes/Current Progress.md:92`).

**Unsure:**
- Line 343, "three selectable colours, 10% hammer spawn, a quota of five hammers". The shipped Forging content file is not in the repo. The code accepts 1 to 5 `selectable_types` (`repo:prototype/osfr-tools/src/forging.rs:1022-1030`), and the synthetic fixture uses all five (`:1243`, `tests/forging.rs:27`) with quota 1. I could not confirm the "three colours" or "five hammers" values from any repo file, so I did not correct them.
- Line 238, "65" Forging titles, and line 342, "61 type-8 rows". These two counts disagree within the note. The client query I tried returned nothing, and the locale tool cannot count, so I could not settle either number.
