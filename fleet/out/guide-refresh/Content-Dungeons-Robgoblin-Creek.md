<!-- fleet job=guide-refresh id=Content-Dungeons-Robgoblin-Creek status=done turns=11 usd=0.0148 tokens(read,write,in,out)=[285188, 48032, 24, 11851] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Robgoblin Creek.md

**Verdict:** minor drift. The note is almost entirely client-locale and wiki facts, and the locale claims I could check mostly hold. Two absolute "no such string" statements are false as written. The note makes no claim about our Rust code or build status, so there is nothing code-side to correct.

**Corrections:**

1. Requirements table, "Combat job level" row.
   - `old:` No level-3 string exists in the client.
   - `new:` No battle-entry level-3 string exists in the client. The level-3 strings that do exist are item wear requirements, e.g. "Wearable by a level 3 or higher Archer." (locale 42431) and "Sorry, you need to be at least a level 3 Miner to mine Iron." (locale 71461).
   - `why:` Locale search for "level 3" returns many hits (locale 42431–42584, 48423, 71461, 71974–71976). None is tied to a battle entry. The Dungeons index row (`notes/Build Guides/Content/Dungeons/Dungeons.md:126`, "none (3+ recommended)") and `prototype/osfr-tools/data/content/dungeons/robgoblin_creek.json` (`recommended_player_level: 3`) agree with the wiki figure.

2. Goals table, "Main (only goal)" row.
   - `old:` No bonus goal on the wiki; no "Bonus" string in the client.
   - `new:` No bonus goal on the wiki; no battle-specific "Bonus" goal string in the client (only generic UI labels such as the bare "Bonus" at locale 9078 and "Bonus Goals Complete:" at locale 4463).
   - `why:` locale 9078 is exactly "Bonus", and locale 4463 is "Bonus Goals Complete:". Neither is tied to this battle, so the note's conclusion survives, but the literal claim is false.

**Checked and current:**
- The quoted client strings match the locale text: "Defeat all the Robgoblins!" (73164), "Defeat all the robgoblins." (95068), "The player needs to defeat all the robgoblins to complete the encounter." (42069), "Robgoblin Creek!" (71695, 73169), "robgoblin pondblasters AND robgoblin creek - fish toss" (73504), "Retrieve four jars of fish oil from the Robgoblin Fishmongers in Robgoblin Creek." (389646), "Robgoblin Fisherman" (73039, 5102929), and the Shelby and Pixie Nursery lines (389645, 390461, 388531, 388530).
- The singular "Robgoblin Fishmonger" has no stand-alone locale string, as the note says.
- No "Win Combat Encounter Robgoblin Creek" string exists. Other dungeons have one (locale 119140–119169).
- All 12 prize-wheel item names in the per-job table exist in the locale (for example 131888, 131918, 132038, 133402, and the Vitality II necklace/shard range 130935–131295).

**Unsure:**
- The `loc <id>` numbers in the note (e.g. 615695389, 1673059531, 801423612) return "no such id" from the `locale` tool, which uses line-number ids. They appear to be hash keys, and the robgoblin_creek.json record uses the same numbers, so I did not treat them as false. I could not verify them independently.
- The link targets [[Sera Bella]] and [[Emil Jadefish]] have no standalone note file. Sera Bella and Emil Jadefish are covered in `NPCs - Shrouded Glade.md` and `NPCs - Wilds.md`. This is a link-convention question, not a factual claim, so I did not propose a change.
- The "8 Coins" wheel slot and the 113 stars / 21 coins payouts are wiki figures. I could not check them against the client or the code.
