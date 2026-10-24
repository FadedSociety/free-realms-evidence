<!-- fleet job=citem-critic id=cstandard-outdoor-bench-132577-v1-evidence-r1 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[4001, 10685, 6, 1380] model=claude-haiku-5-5 -->
# Standard Outdoor Bench

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "live", "issue": "The top-level 'live: yes' is stronger than the evidence. The only support is that the store rows are not flagged no_sale, which the answer's own open list says is unconfirmed. The retired field is null and no wiki, article or video source backs current sale.", "fix": "Set live to 'unknown (store row present, not no_sale; no current-sale source)', or keep 'yes' only with that qualifier. Source: repo stores.json rows 15601 (line 3994) and 36164 (line 11837), no_sale false."}]}
