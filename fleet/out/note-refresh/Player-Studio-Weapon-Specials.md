<!-- fleet job=note-refresh id=Player-Studio-Weapon-Specials status=nothing_found turns=10 usd=0.0074 tokens(read,write,in,out)=[120298, 24770, 22, 6246] model=claude-haiku-5-5 -->
# notes/Research/Player Studio Weapon Specials.md

**Verdict:** current. Every checkable claim in `Research/Player Studio Weapon Specials.md` matches the tip. No corrections.

**What I checked**

- **Text ids and pairing.** `prototype/osfr-tools/data/reference/item_abilities.json:4-170` maps 11 items to front and area ability ids. Batch 1 (items 78711–78718) uses text ids 5103184–5103215, and batch 2 (79020–79022) uses 5102642–5102652. The `source` block at `:171-176` says the pairing is "by order and theme, not a data link". This matches the note's "How they were matched" section and its id ranges.
- **Ability names by id (locale lookups).** 5103184 Freezing Strike, 5103186 Snowstorm, 5103190 Gleam Explosion, 5103194 Gloam Fire, 5103198 Lightning Blast, 5103202 Celestial Spin, 5103206 Feather Spin, 5103208 Ringing Smash, 5103210 Tolling Bell, 5103212 Magic Snowball, 5103214 Ice Storm, 5102642 Strong Layup, 5102644 Power Drive, 5102647 Royal Power, 5102651 Energy Storm. Each matches the note's table and sits in the slot the JSON gives it.
- **Descriptions.** 5103197 "Punch opponents in front of you with electrical power!", 5103199 "Blast out lightning and damage all opponents in front of you.", 5103209 "Deliver a ringing smash to oppponents in front of you." (sic), 5102648 "Destroy all nearby opponents with your Royal Power.". These match the table.
- **Power Drive has no description.** The JSON gives `"description_id": null` for item 79020's area ability (`item_abilities.json:133-137`), and the locale has only the name 5102644. This matches the note.
- **Count.** Eleven weapons, each with a front and an area ability (8 + 3 entries in the JSON). This matches the note's table and `notes/Research/Player Studio Weapons.md`.
- **"Server assigned weapon abilities."** `item_abilities.json:3` says "weapon abilities were assigned server-side". This is consistent with the note.
- **Other repo references.** `notes/Design/Studio Toolkit.md:46` mentions the Ice Axe's Freezing Strike and Snowstorm specials, which also agrees with the note. I found no code in the repo that defines Player Studio ability damage, so the note's "damage unknown" stance still holds.

**Unsure**

- The note's claim that the old server held the ability definitions cannot be checked from the tip. It is consistent with the JSON's "server-side" wording, so I left it alone.
- The note's description of the Lightning Blade's special as "in front of you" was confirmed from the text (5103199). I did not check the Lightning Blade's front-attack text (5103196/5103197) against the in-game effect, because that needs video.
