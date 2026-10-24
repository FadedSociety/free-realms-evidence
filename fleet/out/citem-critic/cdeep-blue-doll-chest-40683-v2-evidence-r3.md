<!-- fleet job=citem-critic id=cdeep-blue-doll-chest-40683-v2-evidence-r3 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[4047, 5771, 6, 922] model=claude-haiku-5-5 -->
# Deep Blue Doll Chest

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "wireable", "issue": "The only source is set membership in the Deep Blue Sea Ninja Doll collection. It has no price, enemy, quest or event, so under the wireable rule it is not wireable. The answer does not state a wireable value.", "fix": "Set wireable to false. Source: repo collections.json wiki:4:109 (lines 6773-6845) lists the chest as a member entry with no per-item acquisition; the set-level Robgoblin/Wilds fields and the reward '21' are not per-chest evidence."}]}
