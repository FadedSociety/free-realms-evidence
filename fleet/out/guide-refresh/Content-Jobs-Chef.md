<!-- fleet job=guide-refresh id=Content-Jobs-Chef status=done turns=22 usd=0.0245 tokens(read,write,in,out)=[926562, 67420, 46, 13522] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Chef.md

**Verdict:** minor drift. Most of the note is client, wiki and video data, which I could not check against code. Its code-facing claims (max level 20, non-member cap of 4, six cooking phases, the Chef profile and the quest-line gate numbers) still hold. One status claim in the Gaps section is now answered by our quest data.

**Corrections:**

1. `old:` Which of the Sacred Glade or opening cooking quests are live (Chef Express, Stewing to Success, Party Payback, Cooking 101, Farming 101).
   `new:` Only Cooking 101 is live in our data. `chef.json` 3050004 is `enabled: true`, with giver 9000000019 (the Highroad Junction Chef trainer, Auguste Frydaze). Chef Express (3050001), Stewing to Success (3050002), Party Payback (3050003) and Farming 101 (3050005) are `enabled: false`.
   `why:` `repo:prototype/osfr-tools/data/content/quests/chef.json:156-266` (3050004, `enabled: true` at line 266); `chef.json:5-51` (3050001, false), `:54-102` (3050002, false), `:105-153` (3050003, false), `:269-314` (3050005, false). The only `"enabled": true` in the file is line 266. `repo:notes/Autopilot/F124.md:41` and `repo:notes/Autopilot/T202.md:10` also say Cooking 101 is the enabled one. Giver 9000000019 is the Highroad Junction trainer: `repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:789`.

**Unsure:**

- The E4 row (Cooking 101) gives the giver as "unknown". Our `chef.json` 3050004 sets `giver_npc_id` 9000000019, which is Auguste Frydaze's trainer. That is a reconstruction (its evidence tags say "(R)"), not a client fact, so I left the row alone. The note's author may want to add it as a dagger-marked "our data assigns Auguste (reconstructed)".
- The quest-count and title-matching claims (33 Chef titles, the gate quests M2, M5, M10, M13) are client-data claims. I checked the gate rows against the note's own table (lines 111, 119, 129, 137), and they agree with the note. I did not check the locale ids.
- The movie-default tuning in the "Original movie phases" paragraph (8 hits, speed 15 to 50, 160 of 200 units) is marked [analysis]. `cooking.rs` says its phase tuning is "reconstructed" (`repo:prototype/osfr-tools/src/cooking.rs:1-6`), and I found no phase values in the data to compare against. Left unchecked.
- `recipes.json` gives the Strong Arm Stew recipe `job_profile_id` 45 and `minigame_id` 46 (`repo:prototype/osfr-tools/data/content/recipes.json:3256-3265`). The note does not state these numbers, so no change is needed.
