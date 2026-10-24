<!-- fleet job=citem-infer id=cdust-devil-hair-color-card-414074-v1 status=done turns=5 usd=0.0041 tokens(read,write,in,out)=[33955, 15869, 12, 3539] model=claude-haiku-5-5 -->
# Dust Devil Hair Color Card

{"item": {"name": "Dust Devil Hair Color Card", "locale_id": 414074, "kind": "card"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, vendor not identified in the pack (stores.json lists the item at purchase_price_coins 180, member_price_coins 162, no_sale true, category 142, source_tags L1/L2/L4/R2/L3)", "where": null, "price": "180 coins (member price 162 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7902 (item 35969)"},
  {"type": "marketplace", "detail": "Sibling hair color style cards (Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum, Grape Frosting) were sold in the Station Cash Marketplace in the October 2013 Super Spooktacular update. No wiki source ties Dust Devil itself to the marketplace.", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "wiki page Super Spooktacular; wiki Template:News (hair color style cards)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 414074 is 'Dust Devil Hair Color Card'; description 'This style card allows you to change your hair color.'", "source": "locale:414074"},
  {"claim": "Item 35969 is in the coin store data at 180 coins (member 162), no_sale true, in the same 35950-35977 block of 180-coin entries.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7883-7910"},
  {"claim": "Item definition 68836 does not appear in stores.json or vendors.json, so only one of the two definitions has a coin price.", "source": "repo search for 35969|68836"},
  {"claim": "Dust Devil Hair Color Card sits in a 11-item cluster of hair color cards (Sugarplum through Cotton Candy, locale 414069-414079).", "source": "locale:414069..414079"},
  {"claim": "Sibling hair color style cards were added to the Station Cash Marketplace in October 2013 (Super Spooktacular).", "source": "Super Spooktacular wiki page; Template:News"},
  {"claim": "'Dust Devil' in the client is also the name of a Sunstone Valley quest ('A Deal with a Dust Devil') and the Dust Storm Flair Shard item, which is a different item and is not the card.", "source": "locale:438848, locale:429635, locale:33967"}
 ],
 "confidence": 0.35,
 "open": [
  "Which coin vendor sells item 35969 is not in the pack; vendors.json has no row for it. The vendor name and zone are unknown.",
  "The 180-coin price comes from our store data only; no wiki page or article confirms a Dust Devil sale price.",
  "The wiki places the sibling hair cards in the Station Cash Marketplace, while the store data shows a coin price. Check whether Dust Devil was a coin vendor item, a marketplace item, or both.",
  "Retirement status is unknown. The no_sale flag in the store data does not show whether the item is still sold.",
  "Definition 68836 has no store row. Confirm whether it is a tint or race variant of the same card.",
  "The first-pass 'live: yes' is not confirmed by any current source; it is left as unsure.",
  "No drop, quest, event or crafting source was found for this card in the pack."
 ]}
