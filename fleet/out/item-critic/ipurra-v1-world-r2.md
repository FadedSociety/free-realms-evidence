<!-- fleet job=item-critic id=ipurra-v1-world-r2 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3085, 5626, 6, 946] model=claude-haiku-5-5 -->
# Purra

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Purra is an NPC (a lost pixie quest target), not an item. The answer correctly records no sources, but the entry should not sit in the item inventory at all. Its only real content is the NPC and quest-target role, which belongs in the NPC catalogue.", "fix": "Mark as not an item and leave it out of the acquisition set. Evidence: wiki Purra (rev 45503) categories NPC/Pixie/Briarwood; client locale:38617 npc_name 'Purra'; locale:38456 quest objective 'Find the lost Pixie, Purra, in Nettleseed'."}]}
