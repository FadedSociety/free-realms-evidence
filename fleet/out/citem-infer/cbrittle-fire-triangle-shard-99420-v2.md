<!-- fleet job=citem-infer id=cbrittle-fire-triangle-shard-99420-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[12623, 9933, 8, 1796] model=claude-haiku-5-5 -->
# Brittle Fire Triangle Shard

{"item": {"name": "Brittle Fire Triangle Shard", "locale_id": 99420, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale in store category 121 (item 32301). Vendor NPC and category name not identified in repo data", "where": "store category 121 (name unverified)", "price": "811 coins (member price 729 coins, derived at 10%)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:8247 (item_id 32301, category_id 121, purchase_price_coins 811); client coin_store_prices 811 for definition 32301"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item as locale 99420 'Brittle Fire Triangle Shard', definition id 32301, slot 12, class 68", "source": "locale:99420"},
  {"claim": "Store data lists item 32301 in category 121 at purchase price 811 coins; the client's coin_store_prices also gives 811", "source": "repo:prototype/osfr-tools/data/content/stores.json:8247"},
  {"claim": "The 10% member price (729) and sell price (81) are generic derivations applied to every row, not independent sourced prices", "source": "repo:prototype/osfr-tools/data/content/stores.json:8247 (same pattern on every row)"},
  {"claim": "Category 121 holds many other items at 540, 866, 1149, 1656, 2363 and 811 coins, so the category alone does not identify a coin vendor", "source": "repo:prototype/osfr-tools/data/content/stores.json:596-613, 8240-8255"},
  {"claim": "The eleven 'Brittle <element> Triangle Shard' items (locale 99415 to 99425 family) share a name pattern; no source states they are crafting materials", "source": "locale:99415 to locale:99425"},
  {"claim": "No wiki page, article, video, or other answer names this item; lookup returns only the client locale line", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.35,
 "open": [
  "Category 121 name and the NPC vendor are not in the repo data; the sale is recorded as a coin store price, not as a named vendor.",
  "Member price 729 and sell price 81 are derived 10% figures, not sourced prices.",
  "Retired status unknown: no retirement flag in store data and no source states an end date.",
  "The client description is empty and there are no models, so use (crafting material, collection, or other) is unconfirmed; no crafting, drop, quest, or collection source found.",
  "Live status is unsure: the only evidence is the store row and the client definition; no wiki or article source confirms current availability.",
  "The row's source tags (L1, L2, L4, R2, T633, R1) are unexplained in the repo data and were not decoded."
 ]}
