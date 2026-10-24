<!-- fleet job=citem-critic id=crectangle-briarwood-hedge-147958-v1-evidence-r1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[3593, 11759, 6, 1065] model=claude-haiku-5-5 -->
# Rectangle Briarwood Hedge

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "Null vendor is honest, but the source is a store-table row with no vendor or NPC, so 'coin_shop' records a price listing rather than a located sale point. The first-pass 'vendor' guess is correctly left unconfirmed.", "fix": "No change needed for pass. Keep 'where' null and state in open that the vendor is unknown (stores.json:4475 gives category 57, tint group 3, no NPC)."}]}
