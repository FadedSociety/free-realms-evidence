<!-- fleet job=citem-critic id=cpatchwork-padded-dining-chair-147728-v2-world-r4 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[4031, 9069, 6, 806] model=claude-haiku-5-5 -->
# Patchwork Padded Dining Chair

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "live", "issue": "\"live: yes\" is stated more firmly than the evidence allows. The only source is a shipped store row (stores.json:12000, no_sale false, enabled). Nothing shows the listing is currently sold. The answer's own open list already says this, so the field should match it.", "fix": "Set live to \"unknown (present in shipped store data, no_sale false)\" or keep \"yes\" only with that qualifier. Source: repo:prototype/osfr-tools/data/content/stores.json:12000."}]}
