<!-- fleet job=pin-audit id=tests-blacksmith-first-order-rs status=done turns=12 usd=0.0087 tokens(read,write,in,out)=[197441, 26016, 26, 7008] model=claude-haiku-5-5 -->
# tests/blacksmith_first_order.rs

Source of the numbers: `data/content/quests/blacksmith.json` quest 3020003 (Smithy Merchandise) and quest 3020005 (Curious Cancelation) each carry `rewards[0].coins = 5` and `rewards[0].job_xp = {"16": 20}`. `data/content/stores.json` rows for items 55, 56 and 879 carry `purchase_price_coins = 12`, which is the `UNIT_PRICE` const at test line 64. The test's own fixture-set values (the 100 starting coins, the buy counts 8 and 2) are not findings.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:345 the_supply_visit_and_the_vendor_purchase_pay_once - pins `5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020003).**
  Fix: read it through the row. The coin amount reaches the test as the literal `5` passed to `finish_merchandise` (line 237, `finish_quest(..., 5, 20, ...)`), so fix the helper too. Load `rewards[0]` of record id 3020003 from `content_dir().join("quests/blacksmith.json")` with the existing `read_json` (already imported; `read_json` is also used at lines 660 and 676) and use its `coins`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:346 the_supply_visit_and_the_vendor_purchase_pay_once - pins `20` from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]` (quest 3020003).**
  Fix: read it through the row. Same as 345: take `job_xp["16"]` from record 3020003 in `quests/blacksmith.json` and use it in the `finish_merchandise` call (line 237) and here, rather than the literal `20`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:424 the_cancelation_talk_chain_pays_once - pins `5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020005).**
  Fix: read it through the row. Load `rewards[0].coins` from record 3020005 in `quests/blacksmith.json` and use it in place of the literal `5` in the `finish_quest(..., CANCELATION, BLACKSMITH, 5, 20, now)` call (line 423) and in this assert.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:425 the_cancelation_talk_chain_pays_once - pins `40` (20 + 20) from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]`, on quests 3020003 and 3020005.**
  Fix: read it through the rows. Sum `job_xp["16"]` from records 3020003 and 3020005 in `quests/blacksmith.json`, so the expected total is the sum of the two rewards rather than the literal `40`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:652 refusals_and_reconnect_change_nothing - pins `5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020003).**
  Fix: read it through the row. Use `rewards[0].coins` of record 3020003 in `quests/blacksmith.json`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:653 refusals_and_reconnect_change_nothing - pins `20` from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]` (quest 3020003).**
  Fix: read it through the row. Use `job_xp["16"]` of record 3020003 in `quests/blacksmith.json`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:827 bruno_sells_exactly_the_three_recovered_components - pins `20` from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]` (quest 3020003).**
  Fix: read it through the row. Use `job_xp["16"]` of record 3020003 in `quests/blacksmith.json`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:828 bruno_sells_exactly_the_three_recovered_components - pins `20` from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]` (quest 3020003).**
  Fix: read it through the row. Use `job_xp["16"]` of record 3020003 in `quests/blacksmith.json`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:829 bruno_sells_exactly_the_three_recovered_components - pins `+ 5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020003), plus `UNIT_PRICE` 12 from `data/content/stores.json` `purchase_price_coins` (items 55/56/879).**
  Fix: read the reward through the row (`rewards[0].coins` of record 3020003) and read the unit price from the stores row for item 55 (`purchase_price_coins`, which the file already loads at line 692), replacing `UNIT_PRICE`. Alternatively, bound the result rather than pin it.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:830 bruno_sells_exactly_the_three_recovered_components - pins `+ 5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020003), plus `UNIT_PRICE` 12 from `data/content/stores.json` `purchase_price_coins`.**
  Fix: same as 829: read `rewards[0].coins` of record 3020003 and the stores row's `purchase_price_coins` for the purchased item.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:883 bruno_sells_exactly_the_three_recovered_components - pins `20` from `data/content/quests/blacksmith.json` `rewards[0].job_xp["16"]` (quest 3020003).**
  Fix: read it through the row. Use `job_xp["16"]` of record 3020003 in `quests/blacksmith.json`.

- **prototype/osfr-tools/tests/blacksmith_first_order.rs:884 bruno_sells_exactly_the_three_recovered_components - pins `+ 5` from `data/content/quests/blacksmith.json` `rewards[0].coins` (quest 3020003), plus `UNIT_PRICE` 12 from `data/content/stores.json` `purchase_price_coins`.**
  Fix: same as 829: read `rewards[0].coins` of record 3020003 and the stores row's `purchase_price_coins`.

Notes: the file's `UNIT_PRICE` const (line 64) is itself a copy of `stores.json` `purchase_price_coins` for items 55, 56 and 879. Reading it from the stores row once removes the pin for 829, 830 and 884. No existing helper under `tests/common/` loads quest rewards; the test already uses `read_json` on the content directory, so reading the rows there is the fix. The `finish_quest` calls with `5, 20` (lines 237 and 423) are the source of the expected values in the helper and should take them from the row too.
