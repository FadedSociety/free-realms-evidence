<!-- fleet job=guide-refresh id=Content-Jobs-Postman status=done turns=26 usd=0.0379 tokens(read,write,in,out)=[1462712, 92507, 54, 23326] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Postman.md

**Verdict:** current, with minor drift. The note is almost entirely client-locale and wiki content, and it makes no claims about our Rust code, so there was little to falsify. Every locale string, achievement, level gate, title and count I spot-checked matches the client or our data. The one defect is a dead wiki link.

**Corrections:**

1. `old:` `[[Mailbit]], [[Minigame Framework]]`
   `new:` `Mailbit (in [[NPCs - Wilds]]), [[Minigame Framework]]`
   `why:` No `Mailbit.md` exists under `repo:notes/Build Guides/Content/` (the NPCs and Dungeons folders were listed). Mailbit is covered as a row in `repo:notes/Build Guides/Content/NPCs/NPCs - Wilds.md:107`, and the boss sits on `repo:notes/Build Guides/Content/Dungeons/Return to Sender.md:44`.

**Checked and holding (no change needed):**
- Frontmatter and job facts match `repo:prototype/osfr-tools/data/content/jobs.json:1233-1238` (Postman, profile 4, freestyle, max_level 20, members_only true).
- Level achievements at 4, 8, 12, 16 and 20 match `repo:prototype/osfr-tools/data/content/achievements.json:2112-2225`. Trophy tiers match too: Bronze for 4, 8 and 12, Silver for 16, Gold for 20. The "Reach Level 8" copy error on Level 12 is also present in our data (`achievements.json:2164`).
- The Postmaster achievement (Gold, 15 points, title "Postmaster") matches `achievements.json:5958-5972`.
- The "Delivers On Time" title matches `repo:prototype/osfr-tools/data/content/titles.json:2706`.
- The quest-line row count (33 series and entry rows) matches the 33 `quest_ids` in `jobs.json:1251-1285`.
- Locale spot-checks confirm the quoted text: the level-gate lines (Felipe level 5, Enve level 10), the "Oh, no! Want to keep playing as a Postman?" prompt, "Speak with Felipe at Pixiewood", "Postchug Runalug is in the Thoroughfare", the Matcher's stat lines, the PCA Camp directions, "Postman Membership Upgrade Bundle", and the gear sets (Snail, Flat Rate, Telegram, Parcel, Priority, Certified, Special, Express and others).
- The Return to Sender description (node battle, difficulty 3, Evil Postman entrance) matches `repo:notes/Build Guides/Content/Dungeons/Return to Sender.md:11` and `Dungeons.md:133`.

**Unsure:**
- The note's "How to unlock" and Trainers rows say Felipe unlocks the job and gives the Sanctuary starter quests. Our `repo:prototype/osfr-tools/data/content/job_trainers.json:96-102` says Felipe is only a `poi_anchor` in our content and that Flitter is the reachable menu trainer. The note makes no claim about our implementation, so I did not correct it. It is a real gap between the note and our data that a builder should know about.
- `jobs.json:1239-1250` lists `9000000079` (Enaine) among the Postman trainer ids. Conflicts 1 calls Enaine a probable wiki error, so this may be a stale entry on our side, but I did not settle it.
- The note's numeric locale ids (for example 2051750787, 1328272967) use a different id scheme from the `locale` tool and from `achievements.json` `name_id` values (for example 34115). I verified the text, not the ids.
- Video-based claims (job-bar levels, frame references) and the Mail Sorting daily-activity claim could not be checked with these tools.
