<!-- fleet job=citem-infer id=cjuicy-apricot-hair-color-card-414077-v4 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6294, 9100, 6, 2026] model=claude-haiku-5-5 -->
# Juicy Apricot Hair Color Card

{"item": {"name": "Juicy Apricot Hair Color Card", "locale_id": 414077, "kind": "card"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop hair color card listing (store category 142, item 35972). Store row carries no_sale=true, so this is an unconfirmed store-data listing, not a confirmed active sale. Link from store item 35972 to this card is inferred from matching definition id 35972 in the client definition.", "where": "Coin Shop (store category 142; shop section not decoded)", "price": "180 coins list (purchase_price_coins); 162 coins member price (10% member discount). The 162 figure is the member price, not the list price.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7905 (item 35972); sibling colour cards displayed at 162 coins in video:1xtVveaQ3XI/00112.jpg and video:1xtVveaQ3XI/00116.jpg (siblings only, this card not in frame)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 414077 is 'Juicy Apricot Hair Color Card'; description says it changes hair color; class 1, slot 3; definition ids 35972 and 68839.", "source": "locale:414077; client definition"},
  {"claim": "Store row item 35972: category 142, purchase_price_coins 180, member_discount_percent 10, member_price_coins 162, sell_price_coins null, no_sale true. Re-read and confirmed. Rows 35960-35981 in the same block carry identical values, all no_sale true.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7893-7914"},
  {"claim": "Video frames show sibling hair color cards (Gold Rush, Atomic Blast, Sun Kissed, Shock Wave) at 162 coins in the Coin Shop. This supports the member price for the family; it does not name Juicy Apricot.", "source": "video:1xtVveaQ3XI/00112.jpg; video:1xtVveaQ3XI/00116.jpg"},
  {"claim": "No wiki page, article, quest, drop, event, prize wheel, crafting, collection, membership or promotion source names this card (lookup on 'Juicy Apricot' over wiki, video and articles returned no matches).", "source": "lookup"}
 ],
 "confidence": 0.3,
 "open": [
  "The only source is a store row flagged no_sale=true. It shows a price, not a confirmed purchasable listing. Do not wire this card as an active coin-shop item from this row alone.",
  "Price is unresolved for this card: the row gives 180 list / 162 member. Sibling cards are displayed at 162 in frames, which fits the member price. No frame shows this card's own price, so the displayed price for this card is unknown.",
  "Live status is unsure and retirement is unknown. no_sale=true may mean it is no longer sold for coins; no dated source confirms either way. First-pass 'live: yes' is a hint only and is not supported by an active sale source.",
  "The 35972 to Juicy Apricot mapping is inferred from matching definition ids, not from a store row naming the colour.",
  "Definition 68839 has no store row; unclear whether it is a tint or a separate variant.",
  "Store category 142 and source tags (L1, L2, L3, L4, R2) are not decoded, so the exact shop section and location are unconfirmed.",
  "No quest, drop, event, prize wheel, crafting, collection, membership or promotion source was found."
 ]}
