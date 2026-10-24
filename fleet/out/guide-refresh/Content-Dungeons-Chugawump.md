<!-- fleet job=guide-refresh id=Content-Dungeons-Chugawump status=done turns=7 usd=0.0083 tokens(read,write,in,out)=[79059, 26984, 16, 8186] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Chugawump.md

**Verdict:** minor drift. The note makes no claims about our Rust code (no file, path:line, routing or build-status claims; `repo` search finds Chugawump only in notes and the Autopilot logs, never in code). Its checkable claims are about client text and the wiki, and most hold. The client strings for the Chugawump goals, the Test Your Mettle description, the shield messages, the dev notes, the level-13 requirement and every listed prize-wheel item name check out. Two lines do not.

**Corrections:**

1. `old:` Stand tall, soldier! This is no time to be dozin' off. I'm always on the lookout for someone to fight, so test my skills in combat and maybe teach them a thing or two.
   `new:` Stand tall, soldier! This is no time to be slackin' off. I'm always on the lookout for someone to fight, to test my skills in combat and maybe teach them a thing or two. Do you want to give it a go?
   `why:` locale 72863 reads "...no time to be slackin' off... to test my skills in combat and maybe teach them a thing or two.<BR><BR>Do you want to give it a go?". The note's quote is a misquote ("dozin'", "so test") and drops the closing question.

2. `old:` The wheel items match those of [[Mudshell]] for most jobs.
   `new:` The wheel items match those of [[Mudshell]] for most jobs, except that every Mudshell wheel also carries a Power Shard of Entangling, which the Chugawump wheels do not list.
   `why:` repo:notes/Build Guides/Content/Dungeons/Mudshell.md:63-68 (each job row lists "Power Shard of Entangling"); the Chugawump table at lines 64-69 has none.

**Unsure:**

- **Battle Item Mystery Pack on every wheel** (line 60, "Every wheel also holds Battle Item Mystery Pack and 33 Coins. [wiki]"). The Mudshell note says the wiki list shows **no** Battle Item Mystery Pack for Archer (repo:notes/Build Guides/Content/Dungeons/Mudshell.md:63). Both cite the same wiki, so one of the two readings is wrong. I could not check the wiki page itself.
- **"Return to Mugred" as the second Test Your Mettle objective** (line 75). The exact phrase is not in the client locale. The closest strings are "Return Neelix to Mugred." (loc 73011) and "Return to Chugawump" (72932). The note cites video `Huk5snVvXMI/00006, 00054`, which I could not check. The NPC note (repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:247, 302) repeats the same claim, so it rests on the video alone.
- **Members bonus "68 Coins"** (line 55). The client has only "Members Only Bonus!" (loc 427736), with no amount. The 68 figure is wiki-only and I could not confirm it.
- **"Goals (1)"** (line 36). No locale string matched. It may be UI-generated, so I left it alone.
- **Client `loc` IDs.** The note's hashed IDs (e.g. `loc 3991503382`) do not match the locale tool's numbering, so I checked each string by its text, not its ID.
