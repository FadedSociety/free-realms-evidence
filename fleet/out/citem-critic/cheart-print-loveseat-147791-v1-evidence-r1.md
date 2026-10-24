<!-- fleet job=citem-critic id=cheart-print-loveseat-147791-v1-evidence-r1 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[3755, 7150, 6, 1025] model=claude-haiku-5-5 -->
# Heart Print Loveseat

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where / detail", "issue": "The store row's source_tags (L1, L2, L4, R2, T633, R1) are not mentioned. They may point to where the store is stocked, and the answer leaves that unexplained. The answer is otherwise honest that the vendor is unidentified.", "fix": "Keep the vendor as unknown, but record the raw source_tags from repo:prototype/osfr-tools/data/content/stores.json:12062 as unresolved location tags, so a builder can look them up. Do not present them as confirmed vendors."}]}
