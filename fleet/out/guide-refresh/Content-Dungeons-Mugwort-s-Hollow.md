<!-- fleet job=guide-refresh id=Content-Dungeons-Mugwort-s-Hollow status=done turns=14 usd=0.0205 tokens(read,write,in,out)=[458652, 59300, 30, 16983] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Mugwort's Hollow.md

**Verdict:** minor drift. The note makes almost no claims about our code. Its client-locale IDs and strings check out against the locale data. The one substantive error is the ghost-enemy claim, which the client's own locale data contradicts. The `mugwort_s_hollow.json` record agrees with the note on difficulty 4, combat level 9, members-only false, and the 97 and 264 coin grants.

**Corrections:**

1. Enemies (client) row, Notes cell.
   - `old:` The client has no "Ghost Warthog" or "Ghost Snake" string by those words.
   - `new:` The client has a key `snake_ghost` whose text is "ghost snake" (`loc 582630628`), the same form as "ghost toad" (`loc 4168755251`) and "ghost raven" (`loc 3186883069`). Its warthog key `warthog_ghost` (`loc 3542288624`) has no display text. "Ghost Snake Form" (`loc 3968311690`) is a separate form name.
   - `why:` refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:15453 (`582630628 ucdt snake_ghost ghost snake`), :84190 (`birds_raven_ghost ghost raven`), :110136 (`toad_ghost ghost toad`), :93783 (`3542288624 ucdt warthog_ghost`, no text), :104926 (`Ghost Snake Form`).

2. Conflicts item 4.
   - `old:` The wiki's Ghost Snakes and Ghost Warthogs have no client string by those names. Ghost Toad and a ghost raven exist.
   - `new:` The wiki's Ghost Snakes and Ghost Warthogs have no display string by those names. "ghost snake" exists (`loc 582630628`, key `snake_ghost`). The Ghost Warthog key `warthog_ghost` (`loc 3542288624`) has no text. Ghost Toad and a ghost raven exist.
   - `why:` refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:15453 and :93783, as in item 1.

3. Conflicts item 2.
   - `old:` Client "Shard" (`loc 567538116`). Client used.
   - `new:` Client "Wizard's Power Shard of Vitality IV" (`loc 567538116`), capital S. Client used.
   - `why:` refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:15050 gives the full string. The note cites only the word "Shard", so the conflict is effectively a non-issue.

**Checked and holding:** `loc 1339804009` ("Mugwort's Hollow"), `2474280079`, `2793325066`, `2216126723`, `3500909485`, `1339572619`, `2950930613`, `118381270`, `939677309`, `863942879`, `733152254`, `1623844062`, `1677061632`, `1920299577`, `1801107415`, `1347689903`, `2646277932`, `2692431127`, `1057237145`, `1852018411` (Pressure Wave Medic Fatigues; no Pants), Warrior Breeches and the other Conflicts-1 names, and `2431923117` (Chaz's three-boss line). All are in en_us_data.dat or the locale table. Quest descriptions `1377414031` (Troy's dare) and `2867760776` also match. The `mugwort_s_hollow.json` record (difficulty 4, level 9, members_only false, coin grants 97 and 264) agrees with the note.

**Unsure:**
- "Level 9 combat job (difficulty 4 rule, `loc 1291047686`)". The string is "Requires a level 9 combat job" (en_us_data.dat:34198), which other notes call a generic tier string not tied to a single dungeon (e.g. Stealthy Despoilers.md). The "difficulty 4 rule" label is an interpretation, so I did not correct it.
- Prize-wheel item names beyond the Pants and Breeches spot-checks were not verified one by one. `dungeons_unresolved.json` lists the wheel items as having no item IDs, which is consistent with the note's "unconfirmed" framing.
- Wiki-only claims (entrance wording, 370 Stars, members bonus, bonus-goal clothing) cannot be checked against our code or the client. Ghost Toad `loc 4168755251` is confirmed as `toad_ghost ghost toad`, so the ID is right.
