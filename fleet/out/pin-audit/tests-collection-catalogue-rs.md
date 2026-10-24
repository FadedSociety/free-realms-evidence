<!-- fleet job=pin-audit id=tests-collection-catalogue-rs status=done turns=3 usd=0.0013 tokens(read,write,in,out)=[4602, 4922, 8, 1368] model=claude-haiku-5-5 -->
# tests/collection_catalogue.rs

**prototype/osfr-tools/tests/collection_catalogue.rs:237 reward_catalogue (test containing this assert) - pins `12` from `prototype/osfr-tools/data/content/collection_catalogue.json` `reward.coins` on the collection row with `"id": 313` (the row starts at line 23646, `"coins": 12` at line 23686).**
- **Fix:** read it through the row, not a literal: `assert_eq!(reward(313).coins, content.collection(313).unwrap().reward.coins);`. Or bound it, e.g. `assert!(reward(313).coins > 0)`. The `reward` closure already loads the row from `content`, so no new helper is needed.

Not a finding: line 236 `reward(313).items == [item(Some(79446), 12410)]`. Both numbers are item definition ids (79446 granted, 12410 captured), which are identifiers and not tunable values. The file's own comments explain them, and they match `collection_catalogue.json` lines 23689-23691. The test checks ids, so retuning gameplay data would not change them.
