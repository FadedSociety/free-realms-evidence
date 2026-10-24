<!-- fleet job=citem-infer id=cn-flat-rate-postman-short-shorts-pl-flat-rate-postman-short--132976-v3 status=done turns=5 usd=0.0025 tokens(read,write,in,out)=[28904, 8992, 12, 2170] model=claude-haiku-5-5 -->
# {n}Flat Rate Postman Short Shorts{pl="Flat Rate Postman Short Shorts"}

{"item": {"name": "Flat Rate Postman Short Shorts", "locale_id": 132976, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Ferd (Postman job vendor), 'Sells' section; listed as 'Flat Rate Postman Short Shorts'", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ferd (section Sells, revision 2013-10-20); repo:prototype/osfr-tools/data/content/vendors.json lines 15686-15727 (item_id 75968, stock_source wiki Ferd Sells)"},
  {"type": "coin_shop", "detail": "Coin store reference row for item 75968, category 104, tint group 1 (reference price only; a live Coin Shop listing is not confirmed)", "where": "Coin Shop", "price": "378 coins purchase; 340 coins member price (10% member discount); sell-back 37 coins", "currency": "coins", "source": "repo:data/content/stores.json item 75968 (prototype/osfr-tools/data/content/stores.json line 15708); client definition coin_store_prices [378]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 75968 is named Flat Rate Postman Short Shorts, locale 132976, slot 4, one definition", "source": "locale:132976; client definition pack"},
  {"claim": "Wiki Ferd 'Sells' lists Flat Rate Postman Short Shorts among Postman job-related items, introduced in game with the October 1, 2013 update", "source": "https://freerealms.fandom.com/wiki/Ferd"},
  {"claim": "Coin store reference row: purchase 378, member 340, sell 37 coins, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15708"},
  {"claim": "The 378 figure in vendors.json (lines 15691-15695) is copied from stores.json and is labelled '(R) reference price; no captured retail NPC quote'. It is not a Ferd quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 15691-15695 and 15721-15725"}
 ],
 "confidence": 0.5,
 "open": [
  "Ferd's own price for this item is unverified. No captured NPC quote exists; the 378/340 figures are store reference prices.",
  "Whether the item is still sold in the Coin Shop today is unconfirmed. The stores row has no retirement flag, but no source confirms a current listing or a retirement date.",
  "Ferd's zone is unverified. The earlier pack's Greenwood Forest claim has no source in this pack.",
  "Ferd's stock restrictions (Postman job/level) were not checked.",
  "No separate wiki page for the Short Shorts item was found; the only wiki evidence is the Ferd 'Sells' listing.",
  "No drop, quest reward, event, marketplace, or prize-wheel source was found.",
  "Sibling Telegram Postman items (locale 132977-132981) and the Flat Rate set siblings were not analysed for source consistency."
 ]}
