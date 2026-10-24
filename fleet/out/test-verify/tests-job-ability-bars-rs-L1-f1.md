<!-- fleet job=test-verify id=tests-job-ability-bars-rs-L1-f1 status=done turns=5 usd=0.0055 tokens(read,write,in,out)=[36247, 17688, 12, 5916] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/job_ability_bars.rs:180-195

**Verdict:** `confirmed`

**Evidence:**

I tried to refute the claim by finding an assertion that would fail under a switch-path toolbar regression. I found none.

- The bar assertion at `tests/job_ability_bars.rs:185-189` calls `abilities.activation(id, level(&profiles, id))`. `OpeningAbilities::activation(profile_id, level)` (`src/opening_abilities.rs:317`) takes no `Profiles`, no `active`, and no previous-bar state. Its output depends only on `(id, level)`. The comparison target `canonical[&id]` (line 160-163) is the same function at the same levels, so the check is close to tautological. Its only real input is `level`, which is already pinned by line 184.
- `Profiles::select` (`src/profiles.rs:422-425`) is `activate` plus `activation`. It returns only the 38/21 packet, and the test checks only its first four bytes (line 182). Nothing in `Profiles` holds a bar, so "select leaves the previous bar in place" cannot be represented in the state this test inspects.
- The real switch toolbar is built in the gameplay layer: `src/gameplay/jobs.rs:127` calls `ability_activation_for(job)` inside the job-switch path, and `stage_job_selection` (lines 145-187) does its own staging. The test never calls the gameplay path, so a regression there (dropping that call, or emitting the old bar) passes.
- The Adventurer assertions at lines 197-201 check `bar_ids(&canonical[&1])`, which is `activation(1, _)` computed before the loop. They do not read anything produced by a switch.
- The assertions that do run (`active()` at 183, `level` at 184, and `experience` at 190-194) catch experience resets and level drift. They say nothing about toolbar bytes.

Conclusion: the claimed regressions (switching rewrites the toolbar, or select leaves the old bar) pass this test. The "bar after switching" check cannot observe the switch path, as the claim states.

**Minimal fix:** route each switch through the gameplay path (`gameplay/jobs.rs` job-switch or `stage_job_selection`) and take the last 36/5 reply, then assert `bar_ids(&reply) == bar_ids(&canonical[&id])` and that Adventurer's result is all `None`. Keep the hardcoded Brawler slot checks (lines 167-173), since they are the only assertions here that pin bar contents independently of `activation`.
