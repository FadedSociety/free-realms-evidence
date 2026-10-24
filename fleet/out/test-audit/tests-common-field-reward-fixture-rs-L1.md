<!-- fleet job=test-audit id=tests-common-field-reward-fixture-rs-L1 status=nothing_found turns=10 usd=0.0070 tokens(read,write,in,out)=[126935, 23646, 22, 5551] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/field_reward_fixture.rs lines 1-282 of 282

Reviewed `prototype/osfr-tools/tests/common/field_reward_fixture.rs` lines 1-282 in full. This is a shared helper module with no `#[test]` functions and no assertions of its own, so the five report categories mostly do not apply. I found no finding that meets the bar.

Checked and OK:
- `CREDIT_TTL_MS` (line 27) is linked to `osfr_tools::encounter::field_rewards::CREDIT_TTL_MS` (`src/encounter/field_rewards.rs:31`), so it cannot drift from the engine.
- `shipped_field_actor` (173-199) takes its expected values from the shipped `data/content/field_enemies.json` rows and spawn groups, not from the code under test.
- `kill` / `kill_one` (243-277) stop on `field.health(target) == Some(0)` and panic after 40 attempts. They do not compare a value with itself, and they fail loudly when the target never dies.
- `RewardFixture::new` and `minimal` write the field file the test exercises. `Drop` removes the scratch directory.
- The `kill` doc's "2569 HP" figure is consistent with `level_health(20) * 180` (about 2569, using `src/encounter.rs:45-48` and a 180-HP shipped baseline). The "26 hits of 100 damage" figure and the 30 s window (`field_rewards.rs:253`, default 30_000) are only doc comments. The loop does not depend on the hit count, so I did not treat them as a finding. I did not confirm the 100-damage player hit in the Select path.

Not reported, for the record:
- `opening_content()` points at `lab/references/opening-anvil-placement-v1/content`, which does not exist in this repository (`list` on that path returned "not a directory"). `copy_missing` would then panic on `read_dir`. That is a loud failure, not a silent pass, and it depends on the environment variable `OSFR_OPENING_REFERENCE`, so I could not confirm the behaviour from here.
- The module doc says the shipped `field_kill_rewards.json` fills the rest. But `root()` copies the opening reference first, and `copy_missing` keeps existing files, so a `field_kill_rewards.json` in the opening reference would win over the shipped one. I could not check whether the reference has that file, so I left it out.
