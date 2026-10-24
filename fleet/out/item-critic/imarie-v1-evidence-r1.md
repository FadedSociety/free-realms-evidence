<!-- fleet job=item-critic id=imarie-v1-evidence-r1 status=done turns=2 usd=0.0008 tokens(read,write,in,out)=[3017, 3464, 6, 657] model=claude-haiku-5-5 -->
# Marie

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The value \"other\" is not evidenced by anything. The only match for the name is an NPC, so no item kind can be supported. The answer should say the kind is unknown rather than assign one.", "fix": "Leave kind null or 'unknown'. Only locale:93121 (npc_name, 'Marie') and the wiki page 'Marie' (a human NPC at Seaside, rev 45840) match. My own lookup found no item-type client row or wiki item page for Marie."}]}
