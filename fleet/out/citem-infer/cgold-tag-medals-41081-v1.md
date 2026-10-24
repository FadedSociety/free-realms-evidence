<!-- fleet job=citem-infer id=cgold-tag-medals-41081-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[40248, 15307, 12, 2959] model=claude-haiku-5-5 -->
# Gold Tag Medals

{"item": {"name": "Gold Tag Medals", "locale_id": 41081, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 41081 is 'Gold Tag Medals' with description 'This item can be added to the Gold Medals Collection' (locale 132369 gives the same 'Gold Medals Collection' wording).", "source": "locale:41081; locale:132369"},
  {"claim": "Item definition 3865 is entry index 3 (icon 457, tint 121, item_link 'sanctuary') of a collection whose entries run 795-799, the Gold medal set (Gold Racing 41079/3863, Gold Hide and Seek 41080/3864, Gold Tag 41081/3865, Gold Collection 41082/3866, Gold Swimming 41083, and so on).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9050-9077"},
  {"claim": "Item 3866 (Gold Collection Medal) is granted as a 10-coin + item reward on a collection-completion record, showing the Gold medals feed a collection reward chain.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9021-9036"},
  {"claim": "The Silver medal set (41076-41078, defs 3860-3862) sits in the same catalogue family with the same icon, so the medal items are collection fillers, not coin-store goods.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8975-9019"},
  {"claim": "No wiki page, article, video frame, vendor stock, quest reward or drop names this item.", "source": "lookup (client/wiki/articles/video): only locale:41081 matched"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is documented. The Gold Tag Medal appears only as a collection entry (collection id 110, name_id 7761, which has no locale text in our tables); how a player obtains the medal itself (drop, event, quest, or a collection-only item) is unknown.",
  "The client definition shows coin_store_prices: [] and no coin-vendor sale is proven. repo:prototype/osfr-tools/data/content/stores.json line 12559 has a row {item_id:41081, category_id:102, tint_group_id:2, purchase_price_coins:828, member_price_coins:745}. That is probably a collision: 41081 is the locale name id, not definition 3865, and the row's tint group 2 does not match the entry's tint 121. It is NOT used as a source. Confirm with the store owner before treating 828 coins as this medal's price (the member price 745 would be the discounted price, if it is real).",
  "Live status is unsure: the item exists in the client collection catalogue, but no source or wiki page confirms it is still obtainable.",
  "The wiki has no article for the Gold/Silver/Bronze medal sets; the collection's name (locale 7761) is unresolved in our tables."
 ]}
