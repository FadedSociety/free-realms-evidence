<!-- fleet job=pin-audit id=tests-free-revive-rs status=done turns=5 usd=0.0042 tokens(read,write,in,out)=[40976, 20208, 12, 2455] model=claude-haiku-5-5 -->
# tests/free_revive.rs

Two findings. The rest of the screened lines are not findings: the 15 s timer (208, 331) comes from the code constant `AUTO_REVIVE_MS` in `src/encounter/revive.rs:27`, not a data file; lines 358-360 use the price of 250 that the test's own `field` closure writes into `tuned_field_enemies.json`, so it is a fixture value.

- **prototype/osfr-tools/tests/free_revive.rs:285 the_window_carries_the_retail_paid_price... no: paid_revive_is_refused_and_the_window_comes_back - pins `1000` from `data/content/field_enemies.json` `paid_revive.cost`.**
  The feedback line is `format!("You need {cost} coins to revive here.")` (`src/encounter/revive.rs:122`), so the literal "1000 coins" only matches while the data price is 1000.
  **Fix:** read it through `format!("{} coins", REVIVE_COST)`, or better, load `paid_revive.cost` from `data/content/field_enemies.json` in the test and build the text from that value.

- **prototype/osfr-tools/tests/free_revive.rs:326 paid_revive_below_the_price_changes_nothing - pins `1000` from `data/content/field_enemies.json` `paid_revive.cost`.**
  Same literal "1000 coins" as line 285, checked against the refusal feedback.
  **Fix:** read it through `format!("{} coins", REVIVE_COST)`, or read `paid_revive.cost` from `data/content/field_enemies.json`.

Not listed, but the same rule applies: `const REVIVE_COST: i32 = 1_000;` (line 98) hard-codes the shipped price. Its uses at lines 103-104, 194, 296-297 and 324 would follow a retune only if the constant is replaced by a value read from `field_enemies.json` `paid_revive.cost`.
