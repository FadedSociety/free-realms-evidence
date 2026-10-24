<!-- fleet job=guide-refresh id=Content-Dungeons-Sheep-Watch status=done turns=13 usd=0.0180 tokens(read,write,in,out)=[344176, 52885, 28, 15975] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Sheep Watch.md

**Verdict:** minor drift. The note's status and gameplay claims hold up against the tip. What has drifted is the citation scheme: most of its `loc <id>` numbers do not resolve in the locale table, while the quoted text does. The code cites the Global.Text ids. Sheep Watch is built at the tip as battle 12350 (`tests/sheep_watch_dungeon.rs`, 9 tests), and the note never says otherwise.

**Corrections:**

1. `old:` `"Sheep Watch" (game data `loc 1279835357`, UI `loc 500606442`, `3880082132`)`
   `new:` `"Sheep Watch" (Global.Text `loc 30404`, `loc 71772`)`
   `why:` locale 30404 and 71772 both read "Sheep Watch". `loc 1279835357` returns no such id, and `prototype/osfr-tools/data/content/field_battles.json:1073` and `notes/Autopilot/T319.md:34` say that hash "is not a Global.Text id and is not used". The title id the code uses is 30404.

2. `old:` `"Wolves are attacking the sheep at this farm. Save the sheep by defeating the wolves!" (`loc 1190485307`)`
   `new:` `"Wolves are attacking the sheep at this farm. Save the sheep by defeating the wolves!" (`loc 92661`)`
   `why:` locale 92661 is that exact text. `1190485307` does not resolve.

3. `old:` `(`loc 238913308`, the wiki quote)`
   `new:` `(`loc 92659`, the wiki quote)`
   `why:` locale 92659 is "A pack of wolves is attacking the sheep at Farnum Farmstead…", the battle 12350 description (`tests/sheep_watch_dungeon.rs:68`, `notes/Autopilot/T319.md:34`). `238913308` does not resolve.

4. `old:` `"Defeat the Ravenous Wolves at Sheep Watch" (`loc 466525651`)`
   `new:` `"Defeat the Ravenous Wolves at Sheep Watch" (`loc 388319`, the battle 12350 goal)`
   `why:` locale 388319 is that text. `tests/sheep_watch_dungeon.rs:69` (`OBJECTIVE = 388319`). `466525651` does not resolve.

5. `old:` `"Win Combat Encounter Sheep Watch" (`loc 1125522988`). End line: "Thank you! Hopefully, the sheep can get some rest now." (`loc 1132992849`)`
   `new:` `"Win Combat Encounter Sheep Watch" (`loc 119145`). End line: "Thank you! Hopefully, the sheep can get some rest now." (`loc 101007`)`
   `why:` locale 119145 and 101007 are those texts. `tests/investigate_the_wolves.rs:1356` checks the end line against 101007.

6. `old:` `"Complete the Sheep Watch encounter." (`loc 1340339015`), full-group version (`338430328`)`
   `new:` `"Complete the Sheep Watch encounter." (`loc 30441`), full-group version (`loc 31092`)`
   `why:` locale 30441 and 31092 are those achievement strings. `prototype/osfr-tools/data/content/achievements.json:3108-3112` and `:3972-3976` carry the same two texts under keys `wiki:achievement:109:sheep-watch` and `wiki:achievement:145:group-sheep-watch`.

7. `old:` Candidate text: **"Gather the sheep within Sheep Watch!"** (`loc 1408024733`)
   `new:` Candidate text: **"Gather the sheep within Sheep Watch!"** (`loc 101010`)
   `why:` locale 101010 is that text. `1408024733` does not resolve.

8. `old:` The client has a "Sheep Watch Bonus Objective" group (`loc 1650289365`)
   `new:` The client has a "Sheep Watch Bonus Objective" group (`loc 140205`)
   `why:` locale 140205 is that string. `1650289365` does not resolve.

9. `old:` "Head to Sheep Watch in Farnum Farmstead and protect their flock of sheep from the wolves!" (`loc 1454689872`)
   `new:` "Head to Sheep Watch in Farnum Farmstead and protect their flock of sheep from the wolves!" (`loc 417270`)
   `why:` locale 417270 is that text. `1454689872` does not resolve.

10. `old:` "Investigate the Wolves" (`loc 894178537`) is probably the title.
    `new:` "Investigate the Wolves" (`loc 101015`) is the title. Its description is `101016`.
    `why:` locale 101015 reads "Investigate the Wolves", and 101016 is the Anne description with the `421718439` wording. `894178537` does not resolve. The quest-table row's `421718439` is also not a resolvable id.

11. `old:` `| `2217331453` |`
    `new:` `| `115464` |`
    `why:` locale 115464 is "As an archer, collect Vicki's lost arrows from inside the Sheep Watch in Farnum Farmstead.", the row's own text. `2217331453` does not resolve.

12. `old:` `1. **Panel description.** Two near-identical client strings exist (`loc 1190485307` "at this farm", `loc 238913308` "at Farnum Farmstead").`
    `new:` `1. **Panel description.** Two near-identical client strings exist (`loc 92661` "at this farm", `loc 92659` "at Farnum Farmstead").`
    `why:` locale 92661 and 92659 are those two texts. The ids `1190485307` and `238913308` do not resolve.

**Unsure:**

- **Id scheme.** I could not confirm whether the vault's `loc` numbers are a hash convention meant to resolve somewhere else. The locale tool and the code's own evidence use Global.Text ids. If the hash form is intended, keep it and add a line saying so, rather than applying corrections 1–12.
- **Rewards.** The note's wheel, 122 Stars and 51-coin figures are all wiki-attributed, so they are not false as written. The shipped battle 12350 is different: it pays 25 coins plus one random draw from four prizes copied from battle 12311, and no original wheel is recovered (`field_battles.json:1069`, `:1093`; `notes/Autopilot/T319.md:39`). The note does not claim otherwise, but a builder could mistake the wiki wheel for the shipped reward.
- **Entrance id.** `1012648018` (the "investigate those howls" line) and `3801319221` (the Ninja line) did not resolve in the locale tool, and I did not search their text. The Ninja text is close to locale 417260.
- **Herding controller line.** The note gives `loc 3116634121` for the controller wording. Locale 431157 reads "Herd the sheep … by Interact with them…", which may be that line, but I could not tie the id to it.
