<!-- fleet job=note-refresh id=Harvesting-Job-Binding status=done turns=8 usd=0.0081 tokens(read,write,in,out)=[105791, 32098, 18, 5991] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Job Binding.md

**Verdict:** Minor drift. The research conclusion (Chef45, not Farmer; do not use game111) still holds. One code-status claim is false: the harvesting job gate is no longer a placeholder. The citation also moved from `src/` to `prototype/osfr-tools/src/`.

**Corrections:**

1. old: `` `src/harvesting.rs::content` currently uses `profile_id: game_id` and explicitly labels it as a placeholder. That is not a usable production job gate. ``
   new: `` `prototype/osfr-tools/src/harvesting.rs::content` (line 1016) now binds `profile_id: CHEF_PROFILE_ID` (45, line 1026), documented as "(R) Local Chef binding" (`CHEF_PROFILE_ID` at line 64, comment at line 62). The Chef binding is implemented and reviewed; see [[Reviews/Harvesting Chef Binding]]. ``
   why: repo:prototype/osfr-tools/src/harvesting.rs:1016-1026 and :62-64; no `profile_id: game_id` remains in `content()`. The "placeholder" wording at harvesting.rs:85-87 refers to the 600-block code-string goals, not the job gate. Review: repo:notes/Reviews/Harvesting Chef Binding.md:28-32 (fix "adds `CHEF_PROFILE_ID: i32 = 45`, binds it in `content()`, and refuses every other profile").

2. old: `Chef45 is therefore the supported job candidate for a later local Harvesting111 launch.`
   new: `Chef45 is therefore the supported job candidate for a local Harvesting111 launch, now wired as an opt-in candidate (`harvesting.json`) bound to Chef45 at the gateway; world entry is still unverified natively.`
   why: repo:prototype/osfr-tools/src/gameplay.rs:977-992 (Harvesting111 "opt-in candidate bound to Chef45"; refuses any other profile); repo:notes/Reviews/Harvesting Chef Binding.md:99-102 (world entry for Harvesting 111 still open; not registered in `lib.rs`). Treat this as a status update, not a reversal of the research claim.

**Checked and holding:**
- `Miner14` as the supported Mining18 job: repo:prototype/osfr-tools/src/mining.rs:54 (`MINER_PROFILE_ID = 14`).
- "Do not replace the current quest gather path": the quest grant is unchanged at repo:prototype/osfr-tools/src/gameplay.rs:1219 (cited in the Chef Binding review, :89-90).
- `[[Reviews/Type8 Gateway Integration Handoff]]` exists at repo:notes/Reviews/Type8 Gateway Integration Handoff.md.

**Unsure:**
- `lab/reports/harvesting-job-binding-lead-20261009.json` and the wiki revision/hash claims (Chef rev 46136, `870b47c6…`): the `lab/` directory is not reachable from these roots, so I could not check the file. The Chef Binding review (repo:notes/Reviews/Harvesting Chef Binding.md:29) repeats the rev 46136 and hash, which is consistent.
- "The preserved rotation profiles include Chef45" and the Farmer/housing-farm claims depend on wiki and client data I did not check. MODLOG (repo:MODLOG.md:270) records a native run that unlocked and selected Chef45, which supports it.
