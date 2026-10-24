<!-- fleet job=note-refresh id=DeepSeek-Worker-Setup status=done turns=11 usd=0.0086 tokens(read,write,in,out)=[160135, 23887, 24, 8098] model=claude-haiku-5-5 -->
# notes/Research/DeepSeek Worker Setup.md

**Verdict:** minor drift. The note is a dated October 8 tooling milestone, and its setup and first-work claims still match the tip (MODLOG.md:386–398, notes/Current Progress.md:143–149). One standing claim about the lead is now false.

**Corrections:**

1. `old:` The lead remains `gpt-6-astra`; its reasoning setting is preserved.
   `new:` At setup the lead was `gpt-6-astra`, with its reasoning setting preserved. From October 10 Claude Code is the lead, after Bryce's Codex weekly limit was reached. From October 16 workers run as Claude subagents (Sonnet or Haiku), not DeepSeek. See the "Lead and worker change" sections.
   `why:` repo:AGENTS.md:38–44 ("Claude Code is now the lead"; "Workers now run as Claude subagents"); repo:notes/Design/MMO Worker Contract.md:5 ("Claude Code is the lead").

**Unsure:**

- "Restart Codex before assigning the first real worker task" (line 39) and the matching "After fully quitting and reopening Codex…" sentence (line 16) read as pending. The restart did happen: repo:notes/Current Progress.md:122 says "After Bryce relaunched Codex, actual dispatch succeeded." The note's own "First real work" section already records this, so I left the wording alone.
- The crafting Quit39/6 claim (179-pass suite, RED/GREEN) matches repo:MODLOG.md:396 and repo:notes/Current Progress.md:149. The pre-win cancel is in repo:prototype/osfr-tools/src/cooking.rs:389, forging.rs:404 and smelting.rs:376. I did not find a dedicated crafting Quit module, so the "crafting builder" wording is only partly traced.
- Router doctor (88 checks), crack doctor `static-ready`, the scheduled task, LiteLLM repair, the `src/doctor.mjs` and `src/control.mjs` commands, and the private receipt paths live outside the repo. They are consistent with repo:MODLOG.md:386–390 but I could not verify them. The "separate worker reproduced the old failures" claim is also unverified here.
- "Game acceptance remains at the existing Queen checkpoint" was true on October 8 (repo:MODLOG.md:398 reverifies the Queen checkpoint). Later notes add accepted stages and the kart work, so the line is a dated statement, not a live one.
