<!-- fleet job=citem-infer id=cn-big-bang-coveralls-pl-big-bang-coveralls-144411-v1 status=done turns=6 usd=0.0048 tokens(read,write,in,out)=[51486, 18577, 14, 3938] model=claude-haiku-5-5 -->
# {n}Big Bang Coveralls{pl="Big Bang Coveralls"}

{"item": {"name": "Big Bang Coveralls", "locale_id": 144411, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store row for definition 52529 (tint group 1), listed at 9453 coins (member price 8507)", "where": "repo:data/content/stores.json category 103 (no_sale: true)", "price": "9453 coins (member 8507)", "currency": "coins", "source": "repo:data/content/stores.json:8322 item_id 52529"},
  {"type": "vendor", "detail": "Coin store rows for definitions 52544 (tint group 2) and 76760 (tint group 2), listed at 1761 coins each (member 1584)", "where": "repo:data/content/stores.json category 103 (no_sale: true)", "price": "1761 coins (member 1584)", "currency": "coins", "source": "repo:data/content/stores.json:8323 item_id 52544 and :16312 item_id 76760"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name and item text: locale:144411 is the name 'Big Bang Coveralls'; locale:150498 is the generic item line 'This is a Big Bang Coveralls item.'", "source": "locale:144411; locale:150498"},
  {"claim": "Three client definitions (52529, 52544, 76760) share the name, slot 3 (chest), class 12, model worker_<race>_<gender>_chest_tuckedcoverallswkerchief.adr; they look like tint/race variants", "source": "client definition in pack; repo:data/content/stores.json:8322-8323, :16312"},
  {"claim": "Coin store rows exist for these three definition IDs at 9453 coins (52529) and 1761 coins (52544, 76760). The pack's coin_store_prices values are these prices, not item IDs; the same 1761 and 9453 values appear on many other store rows, so they do not identify this item alone", "source": "repo:data/content/stores.json:8322, :8323, :16312"},
  {"claim": "All three store rows are flagged no_sale: true with sell_price null, which suggests they are not currently sold for coins; their source_tags (L1, L2, L4, R2, L3) are legacy-era tags", "source": "repo:data/content/stores.json:8322-8323, :16312"},
  {"claim": "Wiki search for 'Big Bang Coveralls' and 'Big Bang' returned no article, image, video or article fact", "source": "lookup wiki/articles/video, no matches"},
  {"claim": "'Big Bang' appears in client credits only as Big Bang Entertainment LLC, the minigame developer; this does not name the item", "source": "locale:432569; locale:408320"}],
 "confidence": 0.3,
 "open": ["No wiki page, article, video frame, quest, enemy drop or event names this item, so no non-store source can be cited.",
  "No vendor in repo vendors.json stocks it (vendor_stock empty); the store category 103 rows do not name a vendor, so the coin-store vendor that sold it is unidentified.",
  "The three store rows are no_sale: true, so the 9453 and 1761 coin prices may be historical or may be placeholder store data; whether it was ever sold for coins at those prices is unconfirmed.",
  "Which tint/race each of the three definitions covers is not stated; the pack counts them as variants of one item, not separate items.",
  "The name 'Big Bang' with the 'Don't stand too close to open flames' description suggests a worker or mining outfit, possibly a set item, but no set or promotion is confirmed.",
  "Retirement status and live status are unknown; the store rows' no_sale flag is the only hint that it is not current."]}
