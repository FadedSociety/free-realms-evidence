<!-- fleet job=item-critic id=imaya-v1-world-r2 status=done turns=2 usd=0.0010 tokens(read,write,in,out)=[3620, 4455, 6, 742] model=claude-haiku-5-5 -->
# Maya

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "live", "issue": "The answer sets live to \"unsure\" for an entity that is an NPC, not an item. The brief is about item acquisition, so the field is not meaningful here. It is an honest unknown, not a wrong claim.", "fix": "Set live to null or 'not applicable (NPC, not an item)'. Locale 403386 is typed npc_name, and the wiki calls Maya a pixie NPC in Briarwood (wiki page Maya, rev 49953)."}]}
