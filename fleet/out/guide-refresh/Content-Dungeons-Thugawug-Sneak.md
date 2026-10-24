<!-- fleet job=guide-refresh id=Content-Dungeons-Thugawug-Sneak status=nothing_found turns=11 usd=0.0143 tokens(read,write,in,out)=[306887, 55683, 24, 8457] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Thugawug Sneak.md

**Verdict:** current. None of the note's code-checkable claims is false at the tip. The note makes no build-status claim, so I have no correction to make.

**Checked and holding:**
- Client name id `3809365958` matches `data/content/dungeons/thugawug_sneak.json:7` and `:51`.
- Difficulty 2 and zone "Wilds (south of the Bumbleberry Patch)" match `thugawug_sneak.json:61` and `:72`.
- The "firepit" entrance matches the `target_name` at `thugawug_sneak.json:225` and `:1425`.
- The entry requirements are empty (`thugawug_sneak.json:9`), which matches "Combat job level: None".
- The locale strings I could resolve match the note: the Bumbleberry "southwest ... past the Bixie Farms" line, the panel text "Thugawug Sneaks kidnapped a semi-famous rock star!", and "Help the guest star!". The note's `loc` numbers are hashed ids, which the locale tool does not look up directly, so those I could only match by text.
- The Warrior quest "Knocking Some Sense In" is consistent with `data/content/npcs/wilds.json:1231`.
- The Thugawug Bumbler and Thugawug Fan strings exist in the client as the note describes.

**Not a correction, but relevant to a builder (the note's Gaps section does not say it):**
- `notes/Design/Battle Template.md:58` lists **Thugawug Sneak!** among the eight field battles that are *deferred*, with the blocker "Rescue script and original arena/roster/prizes". The same template (lines 43–47) says deferred battles are not in `dungeons_unresolved.json`.
- `data/content/field_battles.json` has 10 rows (ids 96, 12301, 12302, 12303, 12310, 12311, 12340, 12350, 12370, 12400). None is Thugawug Sneak, and no field_battles entry names it.
- So the battle is not runnable on our server, although `dungeons_unresolved.json` (around lines 26212–26423) does carry entries that cite this note. That contradicts the template's rule.
- If the lead wants the note to state this, a Gaps bullet would fit: "Not runnable at this tip: deferred in `notes/Design/Battle Template.md:58`; no `field_battles.json` row." I did not put it forward as a correction because the note does not claim otherwise.

**Unsure:**
- The wiki-sourced figures (62 Stars, 18 Coins, the Medic wheel contents, the Fan and Thugawug counts, the "red, 83 m" marker) and the scripted dialogue lines could not be checked against the repo or the client tables I could reach.
- Whether the Medic wheel items match the client, beyond the names already checked elsewhere in the repo.
