<!-- fleet job=item-critic id=imaxine-v1-world-r2 status=done turns=2 usd=0.0010 tokens(read,write,in,out)=[3124, 4176, 6, 846] model=claude-haiku-5-5 -->
# Maxine

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence", "issue": "The repo build guide cites Maxine's name as 1400430670, while the answer uses locale 45813. The pack does not show these are the same id system. The answer's claim that 45813 is the npc_name 'Maxine' is supported by the locale lookup, but the cross-reference to the repo id is unexplained.", "fix": "Keep locale:45813 as the Maxine npc_name (confirmed by lookup). Note that the repo's 1400430670 is a separate client name id for the same NPC, or state that the two ids were not reconciled."}]}
