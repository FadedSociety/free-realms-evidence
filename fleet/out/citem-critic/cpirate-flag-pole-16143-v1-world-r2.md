<!-- fleet job=citem-critic id=cpirate-flag-pole-16143-v1-world-r2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[4119, 12372, 6, 1103] model=claude-haiku-5-5 -->
# Pirate Flag Pole

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "live", "issue": "The 'live: yes' status is asserted, but the only support is the store row's no_sale=false flag and the first-pass tag. The answer's own open list says no source confirms the sale is still running. The status should be labelled as inferred from the store row, not as confirmed.", "fix": "Keep live as 'inferred yes (repo stores.json:2688, no_sale false)'. Confirmation would need a client or wiki source showing the coin store still sells item 9045."}]}
