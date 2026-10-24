<!-- fleet job=citem-infer id=cleaf-wing-pattern-card-415213-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[10119, 13036, 8, 2153] model=claude-haiku-5-5 -->
# Leaf Wing Pattern Card

{"item": {"name": "Leaf Wing Pattern Card", "locale_id": 415213, "kind": "card"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale, store category 146 (wing pattern cards), item 36038 (no_sale=true, so not resaleable); vendor NPC not named in our data", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36038 (line 11769)"},
  {"type": "coin_shop", "detail": "Second definition of the same card, item 68985 (sellable, sell price 27 coins), same coin store category 146", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 68985 (line 14729)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name 'Leaf Wing Pattern Card' is locale 415213 (item), description 'This style card allows you to change your wing pattern.' (locale 415217 text, shared by the set)", "source": "locale:415213; locale:415217"},
  {"claim": "Two item definitions (36038, 68985) share the name; both are listed in coin store category 146 at 270 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36038; item 68985"},
  {"claim": "Sibling wing pattern cards (Winter, Mayfly, Phoenix, Creepy, Fan, Magma, Petal, Striped, 415208-415216) sit in the same client block, consistent with a single wing-card set sold in the coin store", "source": "locale:415208 through locale:415216"},
  {"claim": "No wiki page, article, or video frame names this card; the wiki-side coin price is not confirmed", "source": "lookup wiki/articles/video for 'Leaf Wing Pattern Card' returned only client rows"}],
 "confidence": 0.5,
 "open": ["The coin vendor NPC and zone that sell item 36038/68985 are not named in our data (vendor_stock empty; stores.json only gives category 146 and source_tags L1/L2/L4/R2/L3/T633/R1, which are not vendor names). Need the wing-card vendor identity.",
  "Item 36038 is no_sale=true while 68985 is sellable (sell 27 coins); the two definitions may be different tint/variant records and need a check before the rebuild treats them as one item.",
  "No wiki or article source gives a live date or a retirement date, so 'retired' is unknown; the store entry alone does not prove current availability.",
  "The first-pass 'source_guess: vendor' is consistent with the store data but is not independent evidence.",
  "No wiki price was found to compare against the 270-coin store price, so no sale-price comparison is possible."]}
