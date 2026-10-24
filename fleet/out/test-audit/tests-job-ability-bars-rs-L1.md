<!-- fleet job=test-audit id=tests-job-ability-bars-rs-L1 status=done turns=5 usd=0.0050 tokens(read,write,in,out)=[34637, 16231, 12, 5181] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/job_ability_bars.rs lines 1-202 of 202

Window: `prototype/osfr-tools/tests/job_ability_bars.rs` lines 1-202. Read with `tests/common/job_playtest.rs` (bar_ids), `src/profiles.rs` 400-450 (select/activation) and 229, and `src/opening_abilities.rs` 315-345.

- **[high] prototype/osfr-tools/tests/job_ability_bars.rs:180-195 switching_jobs_keeps_each_jobs_level_and_unlocked_bar - the "bar after switching" check never reads the bar from the profile switch path, so switching cannot affect what it compares.**
  - Why it cannot catch a regression: `abilities.activation(id, level(..))` takes only the job id and a level, not `Profiles` or `active`. The bar is compared with `canonical`, which was computed from the same call before the loop. `profiles.select` returns only the 38/21 packet (profiles.rs:422-448), and the test checks just its first 4 bytes (line 182). A change where switching rewrites the toolbar, or where `select` leaves the previous job's bar in place, still passes because no toolbar bytes are read after `select`.
  - Fix: after each `profiles.select(id, ...)`, take the toolbar that the gameplay/session path sends for the newly active job and run `bar_ids` on it. Assert that it equals `bar_ids(&canonical[&id])`, and that Adventurer's result is all `None`.

- **[medium] prototype/osfr-tools/tests/job_ability_bars.rs:1-2, 143, 190-194 switching_jobs_keeps_each_jobs_level_and_unlocked_bar - the name and doc claim the unlocked bar and the unlocked skills are preserved, but nothing checks unlocks or skill state.**
  - Why it cannot catch a regression: the only state assertion in the loop is `profiles.state().experience == experience` (lines 190-194). A switch that drops a job from `unlocked`, or that consumes or grants a skill in inventory, still passes. `Profiles::activate` does check `unlocked` (profiles.rs:411-417), but the test never asserts it after switching.
  - Fix: inside the loop, assert `profiles.state().unlocked` equals the initial `JOBS` set. Also snapshot the inventory's owned items or equipment before the loop and assert it is unchanged after all switches.

- **[medium] prototype/osfr-tools/tests/job_ability_bars.rs:138-140 and 159, 184 - the expected level is computed by a copy of the production formula, so the level assertions compare the helper with itself.**
  - Why it cannot catch a regression: `level()` copies `(1 + xp / 100).min(20)` from `profiles.rs:229`. The expected `levels` map (line 159) and the check at line 184 both come from this helper. If production changes the curve or the cap, both sides change together and the test still passes. Line 184 is also only meaningful together with line 192, which is the one real check.
  - Fix: use the production level accessor from `profiles.rs:229` directly, or hard-code the expected levels from the comments (Adventurer 1, Medic 15, Warrior 10, Wizard 20, Ninja 10, Brawler 5, Archer 15) and compare with those literals.

- **[low] prototype/osfr-tools/tests/job_ability_bars.rs:171-172 switching_jobs_keeps_each_jobs_level_and_unlocked_bar - the Leg Sweep and Rock Toss slots are only checked with `is_some()`.**
  - Why it cannot catch a regression: the comment names Leg Sweep at slot 3 and Rock Toss at slot 4, but any non-empty id passes. Line 168 pins slot 0 to 4895 and shows the intended style. A change that swaps the two skills, or puts a different skill in those slots, still passes.
  - Fix: pin `brawler[3]` and `brawler[4]` to the authored ids of Leg Sweep and Rock Toss, as line 168 does for slot 0.

- **[low] prototype/osfr-tools/tests/job_ability_bars.rs:182 switching_jobs_keeps_each_jobs_level_and_unlocked_bar - only the 4-byte header of the 38/21 packet is checked.**
  - Why it cannot catch a regression: the payload's rank bytes (`rank_offset`), equipment, and attachments are not compared. A change that sends the wrong job's rank or equipment in the activation still passes, because only `[38,0,21,0]` is checked.
  - Fix: parse the payload length and rank bytes from the packet, and assert they match the target job's rank and level.
