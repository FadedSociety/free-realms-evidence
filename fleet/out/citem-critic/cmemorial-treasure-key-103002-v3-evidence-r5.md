<!-- fleet job=citem-critic id=cmemorial-treasure-key-103002-v3-evidence-r5 status=done turns=2 usd=0.0013 tokens(read,write,in,out)=[3765, 5939, 6, 1006] model=claude-haiku-5-5 -->
# Memorial Treasure Key

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "open[3]", "issue": "Cites locale:103283 ('NOT LIVE: hidden collection key') as a reference. The id check flags that line as not_live, and the answer itself says it is not used as evidence. Citing it at all in the open list adds a flagged line to the record without a need for it.", "fix": "Drop the locale:103283 reference from open[3] and keep only the statement that no retirement or live-status source was found."}]}
