<!-- fleet job=citem-critic id=cbraeburn-apple-66875-v3-evidence-r3 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3897, 9204, 6, 1058] model=claude-haiku-5-5 -->
# Braeburn Apple

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "open / evidence[2]", "issue": "The answer cites locale 132416 as 'Red Apples Collection', but the collection's own name_id in collection_catalogue.json is 67523 (line 12116), and the locale hits I found for 'Red Apples' are different ids. The 132416 reference is unverified and does not match the catalogue record.", "fix": "Cite the collection by its catalogue name_id 67523 (collection id 157, repo collection_catalogue.json:12114-12209) and drop the unverified locale 132416 reference."}]}
