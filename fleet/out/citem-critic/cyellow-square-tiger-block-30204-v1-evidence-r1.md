<!-- fleet job=citem-critic id=cyellow-square-tiger-block-30204-v1-evidence-r1 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[3839, 7789, 6, 1172] model=claude-haiku-5-5 -->
# Yellow Square Tiger Block

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where / open", "issue": "The store row's source_tags (L1, L2, L4, R2, T633, R1) are not mentioned. They are the only vendor-location hint in the repo data, and the answer leaves them out while saying the vendor NPC is unidentified. Repo row is stores.json line 16435.", "fix": "Cite the source_tags as unresolved vendor/location tags (stores.json:16435) so a builder knows where to look for the NPC. The price, currency and sell-price values themselves are correct."}]}
