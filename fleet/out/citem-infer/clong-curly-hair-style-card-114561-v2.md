<!-- fleet job=citem-infer id=clong-curly-hair-style-card-114561-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5402, 7046, 6, 1576] model=claude-haiku-5-5 -->
# Long Curly Hair Style Card

{"item": {"name": "Long Curly Hair Style Card", "locale_id": 114561, "kind": "card"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop hair style card (sold alongside Wolfy Hair Style Card and the facial hair cards)", "where": "Coin Shop", "price": "540 coins (purchase price, non-member); 486 coins (member price, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 6852 (line 1866: category 141, purchase_price_coins 540, member_discount_percent 10, member_price_coins 486, no_sale false); video:1xtVveaQ3XI/00128.jpg (Coin Shop frame lists Long Curly Hair Style Card at 486 coins)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Long Curly Hair Style Card' with description 'This natural wave will have all the girls jealous.'", "source": "locale:114561"},
  {"claim": "Store row for item 6852 is sellable: purchase 540 coins, member 486 coins, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:1866"},
  {"claim": "Coin Shop frame lists Long Curly Hair Style Card at 486 coins, alongside Wolfy Hair Style Card (486) and the facial hair cards (243). The frame does not show whether the viewing account was a member, so it confirms the 486 price only", "source": "video:1xtVveaQ3XI/00128.jpg; lookup confirmed the same OCR text"},
  {"claim": "Second definition 35948 has the same category and prices but no_sale true and sell_price_coins null, so it has no evidenced sale path and is not counted as a source", "source": "repo:prototype/osfr-tools/data/content/stores.json:11704"},
  {"claim": "Sibling hair cards share the client block 114556-114562 with flavour lines 114563-114566", "source": "locale:114556, locale:114557, locale:114559, locale:114560, locale:114562, locale:114563-114566"},
  {"claim": "No wiki page, article fact, quest, drop or vendor stock entry names this card", "source": "lookup wiki/articles/video returned only the video frame; vendor_stock empty"}
 ],
 "confidence": 0.6,
 "open": [
  "Price discrepancy: 540 is the non-member purchase price in stores.json; 486 is the member price and is what the video frame shows. Confirm the wiki price and whether the frame came from a member account.",
  "Definition 35948 (no_sale true) may be a tint or non-sale variant. Confirm whether it is obtainable at all; it is left out of sources.",
  "The video frame is undated, so the listing cannot be dated and retirement status is unknown. No wiki article or retirement source was found.",
  "No wiki article covers this card, so the Coin Shop source rests on repo store data and one undated video frame, not a wiki category."
 ]}
