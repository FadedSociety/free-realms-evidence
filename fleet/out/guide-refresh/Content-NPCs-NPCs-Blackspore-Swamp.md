<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Blackspore-Swamp status=done turns=23 usd=0.0304 tokens(read,write,in,out)=[1048945, 77660, 48, 20341] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md

**Verdict:** minor drift. The note's counts, job-page links, trainer level gates, the Brawler and Miner band facts and the Adventurer E19 to E21 links all match the vault and client. One pair of boss assignments is reversed, and the Dance Practice pages are right on this point.

**Corrections:**

1. Ed Sullenfangs row (Part F, row for Ed Sullenfangs)
   - `old:` boss of [[Werewolf Dance Practice]] ("Defeat the head vampire Ed Sullenfangs!", 3523083160)
   - `new:` boss of [[Vampire Dance Practice]] ("Defeat the head vampire Ed Sullenfangs!", 3523083160)
   - `why:` The client text says the werewolves sabotage the vampires' practice and the target is "Defeat the head vampire Ed Sullenfangs!" (locale 432025). The vault's own Vampire page names Ed as its boss (repo:notes/Build Guides/Content/Dungeons/Vampire Dance Practice.md:44). Repo:notes/Build Guides/Content/Dungeons/Werewolf Dance Practice.md:45 names Jake, not Ed.

2. Jake Blackforest row (Part F, row for Jake Blackforest)
   - `old:` boss of [[Vampire Dance Practice]] (1919166048)
   - `new:` boss of [[Werewolf Dance Practice]] (1919166048)
   - `why:` Locale 432023 is "The vampires have given you their powers to help them sabotage the werewolves' dance practice. Defeat the werewolf leader Jake Blackforest!" The Werewolf page cites that same id 1919166048 as its panel description (repo:notes/Build Guides/Content/Dungeons/Werewolf Dance Practice.md:18) and lists Jake as its boss (line 45).

**Unsure:**
- Client name and row ids (for example 3719150561, 3152923960) are hash ids. The locale tool only resolves its own numeric string ids, so I could not look them up. I checked the quoted text instead, and it matched.
- The Overview's Briarwood-north claim (30189753) matches locale 78179 ("The entrance to Briarwood is just north of Blackspore."). The id itself did not resolve.
- The repo has no code-level claims about Blackspore NPCs beyond `data/content/npcs/blackspore_swamp.json`. Chloe, Hannibal and Petra in that file agree with the note's level gates, vendor stock and quest-giver rows.
