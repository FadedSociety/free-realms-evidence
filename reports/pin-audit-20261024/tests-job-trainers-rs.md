<!-- fleet job=pin-audit id=tests-job-trainers-rs status=done turns=11 usd=0.0052 tokens(read,write,in,out)=[98894, 17689, 24, 3966] model=claude-haiku-5-5 -->
# tests/job_trainers.rs

Two of the three screened lines are findings. Both pin 400, which is the Archer prerequisite XP that the test fixture computes from the Ninja trainer's `requires.rank` in data. Line 1696 is not a finding.

- **prototype/osfr-tools/tests/job_trainers.rs:1541 trainer_xp_survives_reconnect (the test that contains this line; the name is not confirmed) - pins `400` from `data/content/job_trainers.json` `trainers[Ninja].requires.rank` (5) x the 100-XP curve.** The chain is: `profile_state` (line 247-254) sets `experience[need.profile] = 100 * (need.rank - 1)`, and `need` is `trainer.requires` for Ninja, which is `{profile 35, rank 5}` in `job_trainers.json` lines 65-69. So the fixture value is 400 only because rank is 5. Retuning the gate, as the data note allows ("restoring 20 needs no code"), would make the fixture write 1900 while the literal still expects 400, so the test breaks while the code is right.
  **Fix:** read it through the trainer row: compute `let expected = 100 * (trainer.requires.rank - 1)` (or whatever `profile_state` uses), with `trainer` taken from `trainers(&content)` for profile 2, and assert `before.get(&35) == Some(&expected)`. Better still, have `profile_state` return the XP it wrote so the assertion reads that value instead of recomputing it.

- **prototype/osfr-tools/tests/job_trainers.rs:1695 two_sessions - pins `400` from the same source (`job_trainers.json` Ninja `requires.rank` 5 via `profile_state` 100 * (rank - 1)).** A's Archer XP comes from `state_for(content, &ninja, true)`, so the same breakage applies if the gate changes.
  **Fix:** read it through the same expression as line 1541, e.g. `100 * (ninja.requires.as_ref().unwrap().rank - 1)`, or the value from a shared helper, instead of the literal 400.

Not a finding:
- **job_trainers.rs:1696 two_sessions - `300`.** B's 300 is written by the test itself (`b_state.profiles.experience.insert(35, 300)` at line 1635, the "rank 4" fixture). It is not read from any data file, so it is a fixture value.
