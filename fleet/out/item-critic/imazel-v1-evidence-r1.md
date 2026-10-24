<!-- fleet job=item-critic id=imazel-v1-evidence-r1 status=done turns=3 usd=0.0011 tokens(read,write,in,out)=[6996, 4288, 8, 983] model=claude-haiku-5-5 -->
# Mazel

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[2].source", "issue": "The seaside.json:5454 citation is a single comma-joined name string (\"Betsy , Connie , Marie , Mazel , ...\"), not a standalone Mazel entry. The claim is still true, but the citation overstates how it is listed.", "fix": "Cite prototype/osfr-tools/data/content/npcs/seaside.json:5454 as a combined name list containing Mazel, and npc_spawns_extra.json:7647 as the separate per-NPC entry. Nothing about the answer changes."}]}
