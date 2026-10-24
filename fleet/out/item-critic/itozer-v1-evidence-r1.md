<!-- fleet job=item-critic id=itozer-v1-evidence-r1 status=done turns=2 usd=0.0011 tokens(read,write,in,out)=[3054, 4699, 6, 942] model=claude-haiku-5-5 -->
# Tozer

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[2]", "issue": "Locale 73749 is tagged quest_objective ('Speak with Tozer'), not quest dialog as the answer says. The other cited ids (73755, 103040, 103046) check out as described: 103040 is the Half a Dozen picture objective and 103046 is the picture delivery dialog to Tozer's family in Merry Vale.", "fix": "Relabel locale:73749 as a quest_objective (Seaside, 'Speak with Tozer'). Source: client lookup, locale:73749 quest_objective Seaside Tozer."}]}
