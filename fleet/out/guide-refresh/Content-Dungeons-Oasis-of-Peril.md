<!-- fleet job=guide-refresh id=Content-Dungeons-Oasis-of-Peril status=done turns=14 usd=0.0146 tokens(read,write,in,out)=[369715, 46759, 30, 10030] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Oasis of Peril.md

**Verdict:** current. The note makes almost no claims about our code. Its checkable claims are client-text, wiki and vault-link claims, and nearly all of them hold at the tip. One link points at a page that does not exist.

**Corrections:**

- `old:` NPCs: [[Surfmonger Arthur]].
  `new:` NPCs: Surfmonger Arthur (row in [[NPCs - Seaside]]; there is no separate NPC page for him).
  `why:` repo:notes/Build Guides/Content/NPCs/ holds only zone NPC pages (NPCs - Seaside.md and the others), with no "Surfmonger Arthur.md". His row is at repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:160. The dangling link is the only defect found.

**Checked and holding:**
- Node-battle type and difficulty 4 / level 9 match the vault index at repo:notes/Build Guides/Content/Dungeons/Dungeons.md:138 ("Oasis of Peril!", 4, 9, Seaside, Special Spawn, written).
- The Surfmonger Arthur row at repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:160 agrees with the note's "south beach" placement.
- Locale text, by regex: "Oasis of Peril!", "Oasis of Peril", the Surfmonger panel and story lines, "Destroy all counterfeit surfboards.", "Defeat Surfmonger Arthur and stop his production…", "Counterfeit Quadfish/Tri Fin/Diamond Tail", "Requires a level 9 combat job", "Members Only Bonus!", "Bonus: 53 Coins!", "Luxurious Oceanfront Homes", "oasis of peril - boss ability", "Oasis of Peril Ninja Star".
- Prize-wheel items spot-checked by exact name, all present: Archer's Necklace of Vitality IV, Archer's Recurve Bow of Splintering, Bodkin Archer Boots, Stick and Move Brawler Boots, Pressure Wave Medic Boots, Medic's Megasaw of Immunization, Ninja's Jagged Scythe of Flame Wave, Sensei Ninja Tabi Boots, Threat Range Warrior Hightops, Warrior's Double Axe of Warcry, Disciple Wizard Shoes, Wizard's Jewel Wand of Tsunami, Battle Item Mystery Pack.
- Linked pages exist: [[Content]], [[Dungeons]], [[NPCs - Seaside]], [[Seaside Swoopers]], [[Stealthy Despoilers]].
- Nothing in the code or Autopilot reports (repo: `notes/Autopilot/`, `prototype/`) mentions Oasis of Peril, Surfmonger or the Counterfeit boards, so no code or status claim is contradicted.

**Unsure:**
- The note's `loc <id>` numbers (e.g. `loc 2373317666`, `loc 3960071289`) do not resolve with the `locale` tool, which looks up numeric row ids that differ from these. The same convention is used across the vault (e.g. `loc 1291047686` in Dungeons.md:46). I matched the text by regex instead, and every quoted string I searched exists. I did not check the ids themselves.
- The Snow Days toy and "85 Stars or less" come from the wiki, and I could not check them against our code.
