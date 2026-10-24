<!-- fleet job=citem-infer id=clace-sweetheart-dress-442695-v2 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[18610, 14090, 8, 2180] model=claude-haiku-5-5 -->
# Lace Sweetheart Dress

{"item": {"name": "Lace Sweetheart Dress", "locale_id": 442695, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. Only a store-data price record exists; no vendor, store or sale is named in it. Treat as unconfirmed.", "where": null, "price": "100 coins (member price 90 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16826 item 78401 (purchase_price_coins 100, member_price_coins 90, no_sale true); client coin_store_prices [100]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name text is 'Lace Sweetheart Dress', definition id 78401, description 'This dazzling dress is perfect for a night on the town!', slot 3 (chest), class 173", "source": "locale:442695; client definition in evidence pack"},
  {"claim": "stores.json record for item 78401 gives purchase_price_coins 100 and member_price_coins 90, with no_sale: true and no vendor or store named. Its source_tags (L1, L2, L4, R2, L3, L3) are unresolved.", "source": "repo:prototype/osfr-tools/data/content/stores.json:16826"},
  {"claim": "Client coin_store_prices [100] matches the store record's 100-coin price.", "source": "client definition in evidence pack"},
  {"claim": "Lookup of the client text and wiki found no page, article or video naming this dress. The only wiki hit for 'Party Dress' is an ad image ('Adventure With Style! Get a NEW [Party] [Dress]!!') that does not name this item.", "source": "lookup: image:art_or_promo Adventurestylerotator.jpg"},
  {"claim": "Sibling dress text (locale:442694 Rhinestone Halter Top Dress, locale:442696 Dotty One Sleeve Dress, locale:442700 'New Party Dresses and Earrings!') sits in the same block, which suggests a shared dress batch but does not name a source.", "source": "locale:442694, locale:442696, locale:442700"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor is unconfirmed. stores.json:16826 gives a price but names no vendor, store or zone, and its no_sale: true flag conflicts with a live coin sale. The price matches the client coin_store_prices [100], which is consistent with a coin store entry but is not a stock row. Keep the vendor source as unconfirmed until a stock row or wiki/video evidence is found.",
  "Live status is unsure, not yes. no_sale: true argues against a current sale, so the first-pass live: yes is not supported. Retired is null because nothing dates the removal.",
  "Store tags L1, L2, L4, R2, L3 are unresolved, so no vendor location can be set; where is null.",
  "Whether locale:442700 'New Party Dresses and Earrings!' is the sale that sold this dress is unverified. It may be a holiday or event promotion.",
  "Locale 442698 and 442699 duplicate the text of 442697 and are not separate items.",
  "No Station Cash marketplace, Coin Shop, quest, drop, prize-wheel, crafting or event source was found."
 ]}
