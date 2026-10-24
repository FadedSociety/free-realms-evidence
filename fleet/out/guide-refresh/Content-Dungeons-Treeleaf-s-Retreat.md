<!-- fleet job=guide-refresh id=Content-Dungeons-Treeleaf-s-Retreat status=done turns=10 usd=0.0111 tokens(read,write,in,out)=[188586, 36321, 22, 9301] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md

**Verdict:** minor drift. The note is almost entirely client-locale and wiki facts, which the repo cannot settle. Its one checkable claim about the wider vault is wrong: the ring-not-necklace accessory is not unique to this dungeon. The achievement names, the Briar Patch comparison and the wheel items I checked all hold.

**Corrections:**

1. `old:` Wheel gear carries "IV", matching difficulty 4. Unusually for a difficulty 4 dungeon, the accessory is the Ring of Energy IV, with no necklace.
   `new:` Wheel gear carries "IV", matching difficulty 4. The accessory is the Ring of Energy IV, with no necklace. Frostfang Caverns (also difficulty 4) has the same Ring of Energy IV on its wheel, so the ring is not unique to this dungeon.
   `why:` repo:notes/Build Guides/Content/Dungeons/Frostfang Caverns.md:17 (Type: "difficulty 4") and :77-82 (Archer, Brawler, Medic, Ninja, Warrior, Wizard rows all list "Ring of Energy IV", no necklace). The difficulty values come from repo:notes/Build Guides/Content/Dungeons/Dungeons.md:95-101 (Briar Patch and Treeleaf's Retreat both "4 | 9"; Frostfang Caverns "4 | 9" at :98).

2. `old:` Difficulty 4 pages Briar Patch and others use Necklaces of Bark Skin IV. This page's wheel has Rings of Energy IV instead.
   `new:` Difficulty 4 page Briar Patch uses Necklaces of Bark Skin IV. Frostfang Caverns (also difficulty 4) uses Rings of Energy IV, as this page does, so the ring is not the only difficulty 4 exception.
   `why:` repo:notes/Build Guides/Content/Dungeons/Briar Patch.md:71-76 (Necklace of Bark Skin IV on every wheel row); repo:notes/Build Guides/Content/Dungeons/Frostfang Caverns.md:77-82 (Ring of Energy IV on every wheel row). Note that Bandit Hideout (difficulty 4) also uses Necklaces, so "others" is correct for the necklace side only.

**Unsure:**

- `tests/pieces/test_piece_059.py:125` expects `document["gaps"]["entrance_text_absent"]` to include "Treeleaf's Retreat". This note now has a sourced Entrance row quoting the wiki ("Click **Treeleaf's Retreat** in the Thistlerow maze, in **Briarwood**. It has an Atlas icon."). The checker may not parse the bolded form, or the test may be stale. I did not change the note for this; whoever owns the checker should confirm.
- Locale ids: the `loc` numbers in the note (e.g. 1291047686, 3569063813, 3430278786, 1571001368) returned "(no such id)" through the `locale` tool. Its numeric lookup seems to use a different key, so I could not verify the id citations. The matching English text does exist: "Treeleaf's Retreat", "Treeleaf Hedge invaded the maze!...", "Knock out 50 Spikey Seedlings spawned by the Arboreants!", and "Complete the Treeleaf's Retreat encounter." / "Group: Treeleaf's Retreat" (group version) are present in the locale.
- Achievements: "Treeleaf's Retreat" (wiki:achievement:134) and "Group: Treeleaf's Retreat" (wiki:achievement:170) exist in `prototype/osfr-tools/data/content/achievements.json` (lines ~3711 and ~4575), which matches the Achievements row. The 2013 wiki figures (336 Stars, 202 and 304 Coins) and the video frame ids cannot be checked from the repo.
- No Autopilot report or Build Ledger entry mentions Treeleaf's Retreat, so I found no evidence that any dungeon code or routing changed the note's status claims.
