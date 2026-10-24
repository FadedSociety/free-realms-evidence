<!-- fleet job=guide-refresh id=Content-Dungeons-Precursor-Ruins status=nothing_found turns=17 usd=0.0185 tokens(read,write,in,out)=[547611, 54703, 36, 12316] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Precursor Ruins.md

**Verdict:** current. The note makes almost no claims about our code (no path:line, no routed packet, no built/not-built status), and the client-facing claims I checked hold at the tip.

**Corrections:** none. Nothing in the note is false against the tip, and I found no citation that moved.

What I checked and found to hold:
- **Dungeon data agrees with the note.** `prototype/osfr-tools/data/content/dungeons/precursor_ruins.json` has `difficulty: 5` and `minimum_combat_job_level: 13`, both sourced to this note's Requirements and Overview rows. Its `goals` and `rewards` are empty, and `zone_id` is null. That is consistent with the note's "Unknown" and "unproven" wording. `dungeons/Dungeons.md` line 108 also gives 5 | 13.
- **String IDs resolve.** `client/locale/en_us_data.dat` has `1437391086` "Precursor Ruins", `1323029355` "Requires a level 13 combat job", `540067880` the queen-spider goal, `2767276185` the panel blurb, `1551834791` "Venoxa", `595687844`, `413478426` "Buckled Skull Jacket", and the rest of the Enemies, Goals and Quests IDs I sampled (e.g. `3155082900`, `2569427213`, `2641088394`, `3021968095`, `4206829172`, `3484067677`, `4029078262`).
- **Negative claims hold.** No "Complete the Precursor Ruins encounter with a full group" string exists, while every other dungeon has one. Only the Precursor Ruins name strings (`1437391086`, `2108272728`, `3169130279`) and the "Precursor Ruins - 313 - ..." dev strings name this place.

**Unsure:**
- `Rocklar Guardian (loc 281206154, 2691726200)`: `2691726200` does not appear anywhere in `client/locale/en_us_data.dat` or `.dir`. `281206154` does ("Rocklar Guardian", en_us_data.dat:7458). The second ID may come from a source I could not reach. If it does not resolve, drop it from that row.
- `Tarantula Tunnel spawner exists (loc 512923587)`: the string is only the name "Tarantula Tunnel". Nothing in the locale says it is a spawner, so "spawner" is an inference.
- `Garros ... crystal "Heal Aura"`: the locale supports "Garros Crystal Heal Aura" (`88623805`, `2888801228`) and "Attack the power source to stop Garros from healing!" (`769209083`). The Gaps line that the client does not tie Garros to this dungeon still stands. A TCG locale string calls Garros "the most powerful of all the Rocklar guardians" (`tcg/locale/en_us_data.dat`, id `2651736789`). That is a card text and does not place him here.
- `Click on the artifact to add your power to it!` (`loc 152515907`): the full string is "I'm going to need your help. Click on the artifact to add your power to it!" (en_us_data.dat:3990). The quote is a fragment, not a false claim.
- `Dungeons` locale tool: the `locale` tool does not accept the note's `loc` IDs directly. I confirmed them through `client/locale/en_us_data.dat` instead.
