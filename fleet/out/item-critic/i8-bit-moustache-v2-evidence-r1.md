<!-- fleet job=item-critic id=i8-bit-moustache-v2-evidence-r1 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[4317, 9556, 6, 1223] model=claude-haiku-5-5 -->
# 8-Bit Moustache

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "evidence[4].source", "issue": "Cites locale:5102426, which the automatic id check flags as a fragment/flavour line with no quest meaning (flags.tsv line 17726). It is not live evidence and should not support the item's identity or acquisition.", "fix": "Drop locale:5102426. The name match is already covered by locale:5102425 ('8-Bit Moustache'), which is unflagged in npc-packs and item-packs. Keep the flavour line out of the evidence list."}]}
