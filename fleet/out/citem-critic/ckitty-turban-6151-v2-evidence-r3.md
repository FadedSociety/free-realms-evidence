<!-- fleet job=citem-critic id=ckitty-turban-6151-v2-evidence-r3 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[4029, 13779, 6, 1260] model=claude-haiku-5-5 -->
# Kitty Turban

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].detail", "issue": "The record is a coin store listing (purchase_price_coins 50, member 45, sell 5, no_sale false, stores.json line 630). Calling it a 'Coin store sale' blurs a standing purchase listing with a sale event. The price and currency themselves check out.", "fix": "Describe it as a coin store purchase listing: category 6, purchase 50 coins, member price 45 (10% discount), sell 5 (repo:prototype/osfr-tools/data/content/stores.json:630). Vendor still unidentified."}]}
