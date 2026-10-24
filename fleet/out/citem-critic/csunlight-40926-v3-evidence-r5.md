<!-- fleet job=citem-critic id=csunlight-40926-v3-evidence-r5 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3836, 7881, 6, 1290] model=claude-haiku-5-5 -->
# Sunlight

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "kind", "issue": "Kind is set to 'collection' even though the item is a member of the Sunburst Lanterns collection (id 90), not the collection itself. The answer's own open note says so. A member collectible should not carry the collection kind; the label is a classification guess and is not evidenced.", "fix": "Use a member/collectible kind (or leave kind unset) and record the collection membership separately as collection id 90, entry index 5, definition 3710. Source: repo collection_catalogue.json lines 7029-7082."}]}
