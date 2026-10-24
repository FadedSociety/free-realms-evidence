<!-- fleet job=item-critic id=ivaal-v1-world-r2 status=done turns=1 usd=0.0009 tokens(read,write,in,out)=[0, 3513, 4, 901] model=claude-haiku-5-5 -->
# Vaal

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "sources", "issue": "The answer records no sources, but the wiki's Sells list (rev 48966) is a vendor relationship for 10 named goods. The answer mentions these only in open, so the vendor link is not captured in any structured field. This is a minor omission, since no prices or currencies are evidenced.", "fix": "If a per-item vendor entry is wanted, record each Sells-list good as a vendor source of Vaal with price and currency marked unknown, citing https://freerealms.fandom.com/wiki/Vaal (rev 48966). Do not invent prices."}]}
