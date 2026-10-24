<!-- fleet job=guide-refresh id=Content-Dungeons-Floren-Forest status=done turns=16 usd=0.0199 tokens(read,write,in,out)=[513922, 58323, 34, 14868] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Floren Forest.md

**Verdict:** Minor drift. The note makes almost no claims about our code or build status, and nearly all of its `loc` ids and quoted strings match the shipped locale. Three client citations are overstated or misattributed. The note's status-type statements are consistent with the tip: `Build Ledger.md:78` says none of the dungeons beyond the cave are playable, and `data/content/dungeons/floren_forest.json` has an empty goal and reward list for its main encounter. Nothing in the note contradicts that.

**Corrections:**

1. Overview, "Entrance" row.
   - `old:` `**Location conflict:** the client places the forest "east of Seaside, near the flower nursery" (`loc 329719655`, `3060616761`)`
   - `new:` `**Location conflict:** an NPC guesses the forest is "east of Seaside, near the flower nursery" ("I think", `loc 329719655`); another line says "Head east of Seaside and collect vegetables in the Floren Forest." (`loc 3060616761`, no nursery mentioned)`
   - `why:` locale `en_us_data.dat:8742` reads "I think the Floren Forest is east of Seaside, near the flower nursery." (a hedged guess); `en_us_data.dat:80843` (`3060616761`) reads "Head east of Seaside and collect vegetables in the Floren Forest." and does not mention a nursery.

2. Conflicts, item 1.
   - `old:` `The client says the forest is east of Seaside next to the Pixie Nursery.`
   - `new:` `An NPC's hedged guess ("I think ... east of Seaside, near the flower nursery", `loc 329719655`) puts the forest east of Seaside. A separate line says the wand is "right next to Pixie Nursery" (`loc 2963706801`).`
   - `why:` `locale/en_us_data.dat:8742` (hedged "I think"); `locale/en_us_data.dat:78239` (`2963706801`: "Morgulg dropped his wand in Floren Forest, right next to Pixie Nursery.").

3. Goals, "Bonus" row. The "related line" belongs to the Mushroom Caverns dungeon, not this one.
   - `old:` `A related line is "Collect all of the Sprouting Budlings!" (`loc 75020374`)`
   - `new:` `The line "Collect all of the Sprouting Budlings!" (`loc 75020374`) is Mushroom Caverns text (its detail line names the Mushroom Caverns, `loc 1914220773`), so it is not evidence for this forest. See [[Mushroom Cavern]]. The Sprouting Budling object (`loc 896101975`) is shared with that dungeon.`
   - `why:` `locale/en_us_data.dat:50409` (`1914220773`: "Search for the Sprouting Budlings within the Mushroom Caverns..."); `notes/Build Guides/Content/Dungeons/Mushroom Cavern.md:37`. The "Sprouting Budling" object strings are at `en_us_data.dat:23734` and `:4706`.

**Unsure:**

- The "Atlas icon exists" claim in the Overview table cannot be checked from the repo or the locale.
- The wiki-only figures (192 stars, 54 and 125 coins, the bonus-clothing sets, the "(4)" budling count) and the video-only marker distances cannot be checked here.
- The note's links to `[[Ozymandias]]`, `[[Sakka]]`, `[[Lief]]`, `[[Dahlia]]` and `[[Morgulg]]` could not be confirmed as files. The repo's `notes/Build Guides/Content/NPCs/` folder has no per-person pages. Those names may be dangling links, but I did not check every link.
- Quest ids and quoted strings were spot-checked (about 60 ids) and all matched the locale. Ids not found in the locale file were `1287859559`-style cases I did not resolve. The `loc 3212486024` entry for "Defeat Ozymandias!" is present in the file (`en_us_data.dat:84881`), but the `locale` tool did not return it by id.
