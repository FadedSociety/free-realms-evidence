<!-- fleet job=citem-critic id=cbronze-button-40993-v3-world-r4 status=done turns=2 usd=0.0013 tokens(read,write,in,out)=[3827, 6016, 6, 1024] model=claude-haiku-5-5 -->
# Bronze Button

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[3] / open[3]", "issue": "The answer calls the 'sanctuary' item_link on entry 709 unexplained, but the same item_link and icon_id 228 appear on all eight entries of collection 99 (707-714), so it is a collection-wide field, not something specific to Bronze Button.", "fix": "State that item_link 'sanctuary' is shared by every entry in collection 99 (repo:prototype/osfr-tools/data/content/collection_catalogue.json:7907-7978). Only icon_tint_id varies per entry."}]}
