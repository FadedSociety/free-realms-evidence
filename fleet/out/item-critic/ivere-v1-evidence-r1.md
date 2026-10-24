<!-- fleet job=item-critic id=ivere-v1-evidence-r1 status=no_submit turns=4 usd=0.0013 tokens(read,write,in,out)=[12833, 5464, 10, 1012] model=claude-haiku-5-5 -->
# Vere

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item", "issue": "The target is an NPC merchant, not a purchasable item. The answer correctly reports no item sources, but it still files Vere under item-shaped fields (kind 'other', live 'unsure'), so this target should not enter the item acquisition pipeline.", "fix": "Reclassify as an NPC, not an item. Wiki 'Vere' (rev 46794) says she is a human female merchant near the Wugachug Cooking Table who sells Archer job items; the wiki stock list gives no prices."}]}
