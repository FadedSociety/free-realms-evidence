<!-- fleet job=pin-audit id=tests-power-up-drops-rs status=done turns=4 usd=0.0047 tokens(read,write,in,out)=[28998, 18965, 10, 4065] model=claude-haiku-5-5 -->
# tests/power_up_drops.rs

Findings in `tests/power_up_drops.rs`. The heal percentages come from `data/content/power_ups.json` `kinds.<kind>.heal_pct_max` (`health_big` = 50, `health_small` = 15). The 500 maximum health comes from `data/content/combat_scale.json` `player_base_health` (500). The fixture's own 100 starting health, and the `max_alive_per_instance` value the test sets itself at line 370, are not findings.

- **tests/power_up_drops.rs:277 walking_onto_the_big_heart_heals_from_the_server_position_and_asks_for_the_group - pins `350` (= 100 + 50% of 500) from `data/content/power_ups.json` `kinds.health_big.heal_pct_max` (50) and `data/content/combat_scale.json` `player_base_health` (500).**
  **Fix:** read the percent with `PowerUps::load(f.path()).unwrap()` and the kind's `heal_pct_max`, and the max from the `player_base_health` row in combat_scale.json. Compute the expected value as `start + max * pct / 100`, or bound it.

- **tests/power_up_drops.rs:278 walking_onto_the_big_heart_heals_from_the_server_position_and_asks_for_the_group - pins `[250]` (50% of 500) from `data/content/power_ups.json` `kinds.health_big.heal_pct_max` (50).**
  **Fix:** compute 250 as `player_base_health * heal_pct_max / 100`, reading both values from their data rows.

- **tests/power_up_drops.rs:279 walking_onto_the_big_heart_heals_from_the_server_position_and_asks_for_the_group - pins `Some(50)` from `data/content/power_ups.json` `kinds.health_big.heal_pct_max` (group heal percent for the big heart).**
  **Fix:** compare against `heal_pct_max` read from the `health_big` row through `PowerUps::load(f.path())`.

- **tests/power_up_drops.rs:281 walking_onto_the_big_heart_heals_from_the_server_position_and_asks_for_the_group - pins `350` from `data/content/power_ups.json` `kinds.health_big.heal_pct_max` (50) and `data/content/combat_scale.json` `player_base_health` (500).**
  **Fix:** same as line 277: derive the expected health from the two data rows.

- **tests/power_up_drops.rs:292 the_small_heart_heals_only_the_player - pins `175` (= 100 + 15% of 500) from `data/content/power_ups.json` `kinds.health_small.heal_pct_max` (15) and `data/content/combat_scale.json` `player_base_health` (500).**
  **Fix:** read `heal_pct_max` from the `health_small` row through `PowerUps::load(f.path())`, take the max from `player_base_health`, and compute `100 + max * pct / 100`.

- **tests/power_up_drops.rs:334 only_one_stored_kind_is_held_and_a_refused_pickup_stays_on_the_ground - pins `175` (same small-heart math) from `data/content/power_ups.json` `kinds.health_small.heal_pct_max` (15) and `data/content/combat_scale.json` `player_base_health` (500).**
  **Fix:** same as line 292.

- **tests/power_up_drops.rs:744 big_hearts_from_one_kill_share_a_kill_key_so_the_group_heals_once - pins `50` from `data/content/power_ups.json` `kinds.health_big.heal_pct_max`.**
  **Fix:** compare `a.percent` against `heal_pct_max` read from the `health_big` row through `PowerUps::load(f.path())`. The kind-key comparison with `b.kill` is fine as is.

- **tests/power_up_drops.rs:762 a_group_heal_restores_a_hurt_member_and_is_silent_at_full_health - pins `Some((500, 500))` (the maximum) from `data/content/combat_scale.json` `player_base_health` (500).**
  **Fix:** read the maximum from the `player_base_health` row of combat_scale.json, or bound the check to "health reaches the maximum" by comparing the returned max with the current health.

Not findings: line 372 (the count 2 is set by the test's own `max_alive_per_instance` edit), line 723 (count of 1 removed pickup), line 758 and line 759 (the 50 is passed by the test to `receive_group_heal`, and the 250 is derived from that argument, so the test sets it, although the 500 max still comes from the data), and line 281 is listed above.
