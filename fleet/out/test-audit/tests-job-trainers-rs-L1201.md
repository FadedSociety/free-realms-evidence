<!-- fleet job=test-audit id=tests-job-trainers-rs-L1201 status=done turns=11 usd=0.0100 tokens(read,write,in,out)=[218357, 33711, 24, 7181] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/job_trainers.rs lines 1201-1696 of 1696

Two findings in lines 1201-1696 of `prototype/osfr-tools/tests/job_trainers.rs`. The rest of the window checks out: the bundle-rollback, two-Talk, level-5 bar and two-session refusal assertions compare real state and fixture values, not the code's own output.

- **[medium] prototype/osfr-tools/tests/job_trainers.rs:1423-1428 all_six_combat_jobs_learn_activate_fight_and_gain_xp - a profile with no trainer row silently skips the learn step while the test name claims every job is learned.**
  Profile 43 (Brawler) has no row in `data/content/job_trainers.json` (it appears only as Warrior's `requires.profile`). The loop's `trainer` is therefore `None`, so it takes the `default_state` branch. The learn click, the "You learned the" check, and the unlock assertions at 1448-1463 are all skipped for 43. The job is then switched to and fought as if it were already available, so nothing proves the Brawler can be learned, and nothing proves it is locked before learning.
  **Why it cannot catch a regression:** removing the Brawler trainer row, or breaking its unlock, would still pass, because the `None` arm never reaches a learn assertion. The `Option` silently turns "no trainer" into "skip".
  **Fix:** replace `rows.iter().find(...)` with `.expect(...)` so a missing trainer row fails the test. If Brawler is meant to be taught by no NPC, assert that explicitly (for example, `assert!(!unlocked(&gateway).contains(&43))` before switching, and an explicit list of trainer-less profiles with a reason), rather than dropping the learn step.

- **[medium] prototype/osfr-tools/tests/job_trainers.rs:1478-1481 all_six_combat_jobs_learn_activate_fight_and_gain_xp - "profile is dressed" checks only that at least one equipment entry is non-zero.**
  `equipped(...) >= 1` is satisfied by the starter weapon alone. The client refuses a job outfit without Chest and Legs (the comment at 778 says so), so a job that grants only its weapon would pass this check.
  **Why it cannot catch a regression:** a `ensure_outfit` change that grants the weapon but drops the body pieces, or grants a partial set, still gives a count of 1 or more and the test stays green.
  **Fix:** assert the complete outfit for each profile. Compare `equipped(&gateway, profile)` against the job's expected starter slot count from `opening-abilities.json` or `starter_items` (at minimum, that slot 7 plus the Chest and Legs slots are non-zero for this profile).
