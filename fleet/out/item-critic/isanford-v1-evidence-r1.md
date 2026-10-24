<!-- fleet job=item-critic id=isanford-v1-evidence-r1 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[3403, 7005, 6, 1144] model=claude-haiku-5-5 -->
# Sanford

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[2]", "issue": "Locale 94574 is a quest_dialog line spoken by Banani ('You want a smoothie for Sanford?...'), not a quest objective. The other IDs (94565, 94566, 94567, 94572) are objectives. The claim is otherwise accurate.", "fix": "Label 94574 as Banani's quest_dialog line (lookup: quest_dialog - Banani). Keep 94565, 94566, 94567, 94572 as quest_objective rows. 94570 is Sanford's own quest_dialog offering the smoothie errand."}]}
