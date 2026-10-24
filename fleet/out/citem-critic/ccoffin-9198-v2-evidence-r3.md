<!-- fleet job=citem-critic id=ccoffin-9198-v2-evidence-r3 status=done turns=2 usd=0.0013 tokens(read,write,in,out)=[4117, 6533, 6, 905] model=claude-haiku-5-5 -->
# Coffin

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].detail", "issue": "The store row's source_tags (T633, R1, L1, L2, L4, R2) are not explained anywhere in the answer. They are not used as evidence, so the claim is not wrong, but the answer does not say what they mean.", "fix": "Either note that the tags in stores.json:3077 are unexplained and unused, or state the vendor they point to if a source defines them. The row itself is confirmed: item 10472, category 57, tint group 3, purchase 200, member 180, sell 20, no_sale false (stores.json:3077)."}]}
