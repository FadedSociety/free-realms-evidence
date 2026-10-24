<!-- fleet job=citem-critic id=cphysician-infernal-ring-86361-v1-world-r2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[3945, 8718, 6, 1364] model=claude-haiku-5-5 -->
# Physician Infernal Ring

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1]", "issue": "The family count is loose. Locale ids 86350-86366 hold 17 entries, and the claim calls the family '11-ring' while listing both the Hoodlum and Physician blocks. The Physician block (86359-86366) is 8 ids, which matches the listed ranks. The '11' figure is not backed by a clean list.", "fix": "Describe the family as the Hoodlum block (86350-86358) and the Physician block (86359-86366), citing locale:86350-86366. Drop the '11-ring' count unless each member is listed."}]}
