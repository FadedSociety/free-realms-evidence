<!-- fleet job=guide-refresh id=Client-Engine-Audio status=done turns=14 usd=0.0133 tokens(read,write,in,out)=[263163, 35907, 30, 12374] model=claude-haiku-5-5 -->
# notes/Build Guides/Client Engine/Audio.md

**Verdict:** minor drift. The per-function rows I spot-checked (about 60 addresses, names, confidence tags, and the `wire` claim) match the client label table and decompiled code. The generated header counts and the shard list are stale against the current label table. The "How it works" placeholder is still accurate: the server (`prototype/osfr-tools/src`) has no audio module, and the only sound references in our code are locale/sound-id comments in `restoration/piece_043.rs:10-22` and `piece_061.rs:22`.

**Corrections:**

1. old: `421 accepted functions: 121 confirmed, 148 likely, 84 speculative, 68 unknown.`
   new: `518 accepted functions: 160 confirmed, 159 likely, 130 speculative, 69 unknown.`
   why: client label table, `label` rows whose subsystem is `audio` or `audio.*`, all `status = accepted` (518 rows). Confidence split from the `confidence` field: 160 / 159 / 130 / 69. The `wire` count of 0 still holds (no audio label has a non-empty `wire` list).

2. old: `` `audio.sound` (171), `audio.service` (100), `audio.definition` (60), `audio` (32), `audio.music` (21) ``
   new: `` `audio.sound` (195), `audio.service` (105), `audio.definition` (81), `audio` (66), `audio.music` (34) ``
   why: client label table, per-subsystem counts for the same query. The other subsystem counts (ambient 16, fishing 7, listener 4, minigame 3, vehicle 3, soccer 3, derby 1) are unchanged.

3. old: `[[S0184|S0184]] (7)`
   new: `[[S0180|S0180]] (46), [[S0181|S0181]] (17), [[S0184|S0184]] (7)`
   why: client label table. Rows with audio subsystems exist for S0180 (18 definition, 13 music, 5 service, 10 sound = 46) and S0181 (3 definition, 14 sound = 17). Neither shard appears in the note's "Source shards" line. The other listed shards match the label table.

4. old: `The callee is unlabeled.`
   new: `The callee is labelled \`007c7700\` NotifyUnflaggedNodesOnRefSet (speculative, subsystem \`anim.controller\`) in the client label table.`
   why: client `label` row for `007c7700` (name NotifyUnflaggedNodesOnRefSet, confidence speculative, subsystem anim.controller). The note's row for `0078e3d0` (ActorSoundEmitterDefinition::ClearFlagAndCallHelper) calls it.

**Unsure:**
- Whether the 421 figure in the header was a deliberate filter (for example, only the shards in the list) or simply a snapshot from before the S0180/S0181 relabeling. The label table now gives 518 across all shards. Correction 1 and 2 assume the current table is the right basis.
- Several rows I did not check against the label table (the `audio.definition` and `audio.service` tables, roughly 170 rows). The sample I did check showed no confidence or name mismatches.
