<!-- fleet job=guide-refresh id=Content-Dungeons-Mushroom-Mania status=done turns=16 usd=0.0162 tokens(read,write,in,out)=[398746, 47312, 34, 12567] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Mushroom Mania.md

**Verdict:** minor drift. Almost every checkable claim holds. The one false claim is the Members-only flag in the Requirements table, and the note's own Rewards and Conflicts sections already imply the battle is members-only.

**Corrections:**

1. `old:` No. The wiki gives "Members Only Bonus: 108 Coins". No client string "Bonus: 108 Coins!" was found.
   `new:` Yes. The reference server's copy of the client activity table flags it `MembersOnly` (Id 135, NameId 73989, Difficulty 5). The wiki gives "Members Only Bonus: 108 Coins". No client string "Bonus: 108 Coins!" was found.
   `why:` refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientActivityDefinitions.json:6411-6429 (Comment "Mushroom Mania!", `"MembersOnly": true`, `"NameId": 73989`). Same file marks the sibling Nettleseed Nibblers! (Id 130) members-only at lines 6313-6327. The Members-only figure is a table value from a community server, not a string from the client itself. I could not read the client's binary table directly, so treat this as strong but second-hand. Note that the locale search found no "108 Coins" string, which is consistent with the rest of the cell.

**Checked and holding:**
- Name and description ids: `Mushroom Mania!` (`ucdt 3176844611`, `ugdt 660030603`) appear in client `locale/en_us_data.dat:83877` and `:17470`. Locale row 73989 is "Mushroom Mania!", and 74047 is "Monstrous mushrooms are multiplying…".
- Goal "Defeat all the pests!" (locale 74039). "Knock out all the Nettleseed Pests in this area." (74040). "Stop them from Multiplying!" (74058). The long "Prevent the Nettleseed Pests from multiplying…" text (74062). "The Nettleseed Pest begins to split!" (74051). "Nettleseed Pest Spawn" (74001). "Nettleseed Pest" (73988). No "Win Combat Encounter Mushroom Mania" string; "Win Combat Encounter Mushroom Cavern" exists (119151), so the absence claim holds.
- Level 13 tier strings exist: "Requires a level 13 combat job" (4201), "You must have a combat job of at least level 13 to play this battle" (4191), invitee form (4205). Our server agrees on difficulty 5 → level 13: `repo:prototype/osfr-tools/src/restoration/piece_062.rs:59-60` (`BATTLE_MIN_COMBAT_LEVEL: u8 = 13`) and `piece_060.rs:98`.
- Prize-wheel item names: all 40+ names in the table exist in the locale (for example "Archer's Raptor Bow of Volleys" 131904, "Chunin Ninja Wristguards" 133260, "Warrior's Warlord Axe of Spinning" 132024, "Wizard's Ornate Wand of Shock" 132054). Each job lists six items, with two Power Shards, as the note says.
- Dungeons index row for Mushroom Mania (difficulty 5, level 13, Nettleseed/Briarwood): `repo:notes/Build Guides/Content/Dungeons/Dungeons.md:145`, consistent with this note.
- Our repo has no Mushroom Mania data file and no code path for this battle (search for "mushroom"/"nettleseed" finds only harvest nodes and notes). The note makes no claim about our server, so nothing there needs correcting.
- Neighbour links exist: Moldy Shamblers, Nettleseed Nibblers, Dark Spore Depths, Tanglewood Fort, NPCs - Briarwood.

**Unsure:**
- "Stars: 40 Stars" and the "59 to 156" comparison for other pages come only from the wiki. I did not check them.
- The `loc <hash>` ids (for example 3176844611 and 316039202) are not accepted by the locale tool, which indexes by row id. I confirmed the name ids through the file lines above, not the hash ids for every row.
- The wiki's "Shady Smugglers!" infobox title slip and the 77 Coins wheel slot were not checked.
- Video claims (frame keys, red-marker nameplates) cannot be checked from the repo.
