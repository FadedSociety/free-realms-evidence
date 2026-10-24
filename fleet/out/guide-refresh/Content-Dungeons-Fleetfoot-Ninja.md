<!-- fleet job=guide-refresh id=Content-Dungeons-Fleetfoot-Ninja status=done turns=12 usd=0.0147 tokens(read,write,in,out)=[303848, 49848, 26, 10787] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Fleetfoot Ninja.md

**Verdict:** Current, with minor drift. Almost every locale id and string the note cites checks out against the client locale data. Two sentences overstate what the client lacks. The note's own repo-side data agrees with it: `prototype/osfr-tools/data/content/dungeons/fleetfoot_ninja.json` has `minimum_combat_job_level` null, `recommended_player_level` 3, `members_only` false, and zone "Greenwood Forest". The note makes no build-status claim about the battle, and nothing in `prototype/osfr-tools/src` mentions Fleetfoot.

**Corrections:**

1. Goals table, Main row.
   - `old:` no "Bonus" string in the client.
   - `new:` no Fleetfoot-specific bonus-goal string; the client only has the generic "Bonus Goals" UI strings (`loc 2348967742`, `1253579955`).
   - `why:` refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat lines 61759 (`2348967742 Bonus Goals`) and 33191 (`1253579955 Bonus Goals Complete:`). The note itself cites `343739712` "Bonus: 22 Coins!" in its Rewards section, so "no Bonus string" is false as written.

2. Requirements table, Combat job level row.
   - `old:` No level-3 string exists in the client.
   - `new:` No battle-specific level-3 string exists in the client. The "level 3" strings that do exist are item wearability text (e.g. "Wearable by a level 3 or higher Ninja", locale tool id 42521).
   - `why:` refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat has many "level 3 or higher" item strings. None mention the battle, and the wiki wording "recommended levels 3 and higher" is not in the client. Only the item strings contradict the note's flat claim.

**Unsure:**

- Overview, Entrance row: the client objective "Defeat Fleetfoot Ninjas in Sacred Grove." (`2350636737`) is real. The client's "Sacred Grove" is a place name that also appears in many other strings, and nothing I checked relates it to Greenwood Forest. I left the note's "not stated" wording alone.
- Rewards, Achievement row: "None on the wiki list" is a wiki claim I could not check. The client has "Win Combat Encounter …" strings for many dungeons (`93383990`, `127061170`, and others), but none for Fleetfoot or Greenwood. So "no 'Win Combat Encounter' string" holds for this battle.
- Prize wheel by job: the item names match `repo:prototype/osfr-tools/data/content/dungeons_unresolved.json` lines 8705–8840 (these entries are marked "no item definition ID"). I did not check every item in the table line by line.
- Scroll of the Jade Tiger speaker ("probably Rokuro") and the "wiki item pages for the six weapons" claim could not be settled from the local sources.
