<!-- fleet job=item-critic id=imichelle-oceanflutter-v1-world-r2 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3346, 5001, 6, 1007] model=claude-haiku-5-5 -->
# Michelle Oceanflutter

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.locale_id", "issue": "The answer gives 382924 as her name string. The repo notes (NPCs - Merry Vale.md:47 and NPCs - Seaside.md:134) record the name as ucdt 276115508, and the locale lookup returns 382924 as npc_name. The two ids differ, and the answer does not reconcile them. This is a minor sourcing gap, not a change to the verdict.", "fix": "Record both ids and say which is the npc_name entry, citing locale:382924 and the repo note's ucdt 276115508, or drop the claim that 382924 is the name id."}]}
