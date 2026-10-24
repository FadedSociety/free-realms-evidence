<!-- fleet job=citem-critic id=cn-amateur-blacksmith-goggles-pl-amateur-blacksmith-goggles-35198-v2-world-r2 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[11282, 9130, 8, 1371] model=claude-haiku-5-5 -->
# {n}Amateur Blacksmith Goggles{pl="Amateur Blacksmith Goggles"}

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "jev_first_pass / live", "issue": "The 'live: yes' status rests only on one store row (stores.json:4842, no_sale false). The store data has no dates, so this is an inference, not a verified live fact. The answer already says so in 'open', but the top-level field states it flatly.", "fix": "Record live as 'store row present, no_sale false (unverified currency)' or leave it unknown until a dated source confirms it."}]}
