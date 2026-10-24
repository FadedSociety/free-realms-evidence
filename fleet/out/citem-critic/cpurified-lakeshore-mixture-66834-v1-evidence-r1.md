<!-- fleet job=citem-critic id=cpurified-lakeshore-mixture-66834-v1-evidence-r1 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3922, 4746, 6, 1118] model=claude-haiku-5-5 -->
# Purified Lakeshore Mixture

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[0].claim", "issue": "Calls locale:132411 the 'collection-name line'. It is the item description text ('This item can be added to the Lakeshore Mixture Collection'), not a collection name. The name claim itself is fine: locale:66834 is the item name.", "fix": "Describe locale:132411 as the item's description line, which names the Lakeshore Mixture Collection. The wiki's List of Collections entry '[Lakeshore] [Mixture]' is confirmed by lookup, so the collection link stands."}]}
