<!-- fleet job=citem-critic id=clarge-spotted-centipede-40859-v3-world-r4 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[25308, 11440, 10, 1454] model=claude-haiku-5-5 -->
# Large Spotted Centipede

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "sources[0].where", "issue": "Left null although the catalogue entry (collection_catalogue.json:6229-6230) carries item_link \"sanctuary\". That field is a link tag, not a verified acquisition location, so the answer is right not to treat it as a source, but it could be recorded as a note.", "fix": "Keep where null, or note 'catalogue item_link: sanctuary (not an acquisition location)' citing collection_catalogue.json:6230."}]}
