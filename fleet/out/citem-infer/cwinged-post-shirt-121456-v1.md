<!-- fleet job=citem-infer id=cwinged-post-shirt-121456-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[40836, 15215, 12, 2979] model=claude-haiku-5-5 -->
# Winged Post Shirt

{"item": {"name": "Winged Post Shirt", "locale_id": 121456, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store vendor sale, tint group 1 (base colour), 618 coins (member price 556 coins, 10% member discount)", "where": "coin vendor category 103 (vendor name not present in stores.json)", "price": "618 coins", "currency": "coins", "source": "repo:data/content/stores.json item 41457 (category_id 103, tint_group_id 1, purchase_price_coins 618)"},
  {"type": "vendor", "detail": "Coin store vendor sale, alternate tint groups 2 and 3, 9453 coins each (member price 8507 coins)", "where": "coin vendor category 103 (vendor name not present in stores.json)", "price": "9453 coins", "currency": "coins", "source": "repo:data/content/stores.json item 41464 and item 41471 (category_id 103, tint_group_id 2 and 3, purchase_price_coins 9453)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 121456 is 'Winged Post Shirt'; the cluster of sibling names is Winged Post Shoes (121457), Gloves (121459), Hat (121460), Skirt (121461), Shorts (121462), all one courier set.", "source": "locale:121456; locale:121457; locale:121459; locale:121460; locale:121461; locale:121462"},
  {"claim": "Client definition lists the item in store-data at coin prices 618 and 9453, consistent with a coin vendor sale; the store rows use category 103 with tint groups 1, 2 and 3.", "source": "repo:data/content/stores.json item 41457, 41464, 41471"},
  {"claim": "Store rows carry source tags L1, L2, L4, R2, T633, R1 and no_sale false, so the item was listed for sale in the source store data.", "source": "repo:data/content/stores.json item 41457 (source_tags)"},
  {"claim": "Model is courier_<race>_<gender>_chest_shortslvsmallbag.adr: a courier (postman) chest piece, matching the Postman job theme.", "source": "client definition model file"},
  {"claim": "No wiki page, article fact, video frame or vendor/quest answer names this item in the pack; the search for 'Winged Post' in wiki, articles and client text found only the locale line.", "source": "lookup: wiki, articles, client (no matches beyond locale:121456)"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor name for coin store category 103 is not in stores.json; the coin vendor that sells it is unidentified. Need the NPC/vendor for category 103 to finish the source.",
  "Client definition shows 16 definitions but only 12 definition ids; store rows found in stores.json are 41457, 41464 and 41471 only, so the other tint/race variants have no store price in repo data.",
  "No wiki page, article or video names the item, so the postman/courier event context and the release window are unconfirmed; retired status unknown.",
  "The 9453-coin tint price is high relative to the 618-coin base tint; treated as the price for alternate tints per store data, not verified in-game.",
  "No quest reward, drop, event, prize wheel, crafting or membership source found; these are not evidenced and are left out.",
  "Live status: the store data lists the item as sellable (no_sale false) but the source is a legacy repository, so live 'yes' in the rebuild is unverified."
 ]}
