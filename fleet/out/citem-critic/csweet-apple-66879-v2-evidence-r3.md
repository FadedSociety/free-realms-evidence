<!-- fleet job=citem-critic id=csweet-apple-66879-v2-evidence-r3 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3851, 5702, 6, 962] model=claude-haiku-5-5 -->
# Sweet Apple

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "kind", "issue": "Kind is 'collection', but the evidence only shows Sweet Apple as a member of the Red Apples collection (catalogue entry index 8, item_definition_id 23266). The item itself is a collectible apple, not a collection. The kind label is a classification choice, not a sourced fact.", "fix": "Set kind to a collectible/flora item, or leave it open. Source: repo collection_catalogue.json:12186-12194 (entry 8 of Red Apples) and locale:132416 ('This item can be added to the Red Apples Collection')."}]}
