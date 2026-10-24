<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Stillwater-Crossing status=done turns=20 usd=0.0251 tokens(read,write,in,out)=[834320, 72331, 42, 15374] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Stillwater Crossing.md

**Verdict:** minor drift. The note is largely current: the Part counts (27 NPC rows), the 48-row Quest index and its per-page split (Adventurer 1, Pet Trainer 5, Brawler 8, Chef 4, Fisherman 21, Demo Derby 5, plus 3 with no job page and 1 repeat) and the Part G count (10 rows) all check out. Spot-checked quotes and names in the locale (Valerie, Francis, Caitlyn, Helena, Gavin, Zachery, Vince, Muggup, Kanan, Fernando, the merchant item names, "Stillwater Party", "Stillwater Crossing Newbie", "Stillwater Start") match. One claim is false: Gravedigger Dustin is in the client.

**Corrections:**

1. `old:` `**Gravedigger Dustin** (wiki-only; no client name entry)`
   `new:` `**Gravedigger Dustin** (name `ucdt` 3108444472; `ugdt` 1475257861)`
   `why:` `client:locale/en_us_data.dat:82049` (`ucdt 3108444472 Gravedigger Dustin`) and `:39054` (`ugdt 1475257861 Gravedigger Dustin`); locale id 116668 holds the same string among the Stillwater strings (116660s to 116690s).

2. `old:` `One weak source; the client has no "Dustin" string.`
   `new:` `The client holds the name (locale 116668) but no sentence that places him; the place is still wiki-only.`
   `why:` `client:locale/en_us_data.dat:82049`; locale 116668. The only "Dustin" string nearby is the unrelated "Dustin Downshift" (locale 19345), which is a different name.

3. `old:` `None known. | None known. | [wiki Exploration (Collections)]`
   `new:` `None known. | None known. | [client 116668] [wiki Exploration (Collections)]`
   `why:` `client:locale/en_us_data.dat:82049`; the Part C row's source cell should now cite the client.

4. `old:` `- **Gravedigger Dustin** appears only in one wiki route description. His role and whether he is an interactive NPC are unknown.`
   `new:` `- **Gravedigger Dustin** has a client name (locale 116668) and one wiki route description. His role and whether he is an interactive NPC are unknown.`
   `why:` `client:locale/en_us_data.dat:82049`; locale 116668. The client also has a wraith thanks line (116487, "I may be a gravedigger, but that thing was just scary!"), which may be his, but no speaker is named.

**Unsure:**

- **Ashley Lightwings "(no longer in game)"** (Sacred Glade tutorial row, Part G). I found no code or Autopilot record either way; the Highroad Junction note makes the same claim. Left as is.
- **Gravedigger Dustin's role.** The wraith thanks line (locale 116487) reads like his, but nothing in the client names its speaker. I did not change the "None known" quest and service cells.
- **Quest and string IDs** (for example 570656378, 2565999761, 1114196202) are hash-style IDs. The locale lookup returns line numbers, so I checked each quote by text, not by ID.
- **Repo code.** No code or Autopilot report changes the note's Stillwater claims. Only `prototype/osfr-tools/data/content/npcs/stillwater_crossing.json` and the Autopilot T316 and T378 reports cover this zone, and they concern greeting bindings and spawns, which the note does not claim.
