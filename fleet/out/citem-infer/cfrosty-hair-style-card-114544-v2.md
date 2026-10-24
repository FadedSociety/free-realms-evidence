<!-- fleet job=citem-infer id=cfrosty-hair-style-card-114544-v2 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[21459, 19214, 8, 2528] model=claude-haiku-5-5 -->
# Frosty Hair Style Card

{"item": {"name": "Frosty Hair Style Card", "locale_id": 114544, "kind": "card"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop hair style card listing (Frosty Hair Style Card shown with Sassy, Marie, Asian/Aden?, Flame and Wavy cards)", "where": "Coin Shop", "price": "486 coins (member price); list price 540 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 6835 (category 141, purchase_price_coins 540, member_discount_percent 10, member_price_coins 486); video:1xtVveaQ3XI/00148.jpg and video:1xtVveaQ3XI/00150.jpg (OCR shows 'Frosty Hair Style Card 486 coins' under Coin Shop)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale:114544 'Frosty Hair Style Card', description 'You'll be cool as ice.', in the 'Hair Style Card' cluster locale:114539 to 114549", "source": "locale:114544"},
  {"claim": "Client definition ids 6835 and 35931 both carry the name; 6835 is a stores.json row with purchase 540 coins, member 486 coins, sell 54 coins, no_sale false. The 540 price is therefore matched, not unmatched as the prior answer said", "source": "repo:prototype/osfr-tools/data/content/stores.json:1850 (item 6835)"},
  {"claim": "Second definition 35931 is a stores.json row in category 141 with purchase 540, member 486, sell null, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:11687 (item 35931)"},
  {"claim": "The 486 figure is the stored member_price_coins for the row, not an inference from a discount; the store data itself records the 10% member discount", "source": "repo:prototype/osfr-tools/data/content/stores.json:1850"},
  {"claim": "Coin Shop frames list 'Frosty Hair Style Card 486 coins' alongside other hair style cards", "source": "video:1xtVveaQ3XI/00148.jpg; video:1xtVveaQ3XI/00150.jpg (lookup OCR)"},
  {"claim": "The wiki page 'Super Spooktacular' Week #1 (10/1/2013) says 'New Hair Color Style Cards were introduced: Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum...' The retrieved text is truncated and does not name Frosty, so it is not cited for the Frosty card", "source": "wiki:Super Spooktacular (Week #1 - 10/1/2013)"},
  {"claim": "Coin shop sale of the card in 2013 is the only dated evidence; no end date or retirement notice was found", "source": "video frames above; no retirement source in pack"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status unknown: the only dated sighting is 2013 Coin Shop video frames. Do not assert live or retired without a later source.",
  "The October 2013 wiki date is not confirmed for this card. The truncated wiki text does not list Frosty, so the Oct 2013 batch membership is unverified.",
  "Whether the card is also a prize, event or quest reward: no evidence in pack.",
  "Definition 35931 has no_sale true and sell price null, while 6835 is sellable. Their roles (tint or race variants versus a separate item) are not confirmed.",
  "The source_tags on the stores.json rows (L1, L2, L4, R2, T633, R1) are not decoded, so the store-list tags cannot be used as proof of a specific shop."
 ]}
