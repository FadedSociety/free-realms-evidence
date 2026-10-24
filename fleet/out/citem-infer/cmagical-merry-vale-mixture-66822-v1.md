<!-- fleet job=citem-infer id=cmagical-merry-vale-mixture-66822-v1 status=done turns=10 usd=0.0088 tokens(read,write,in,out)=[149830, 36360, 22, 5488] model=claude-haiku-5-5 -->
# Magical Merry Vale Mixture

{"item": {"name": "Magical Merry Vale Mixture", "locale_id": 66822, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Merry Vale Mixture collection (rare aquatic collection, stage 7 of 8 in the Merry Vale Mixture entry list; the collection's final reward is 5x item definition 3082). The item is a collection entry, not a store item; the client description reads 'This item can be added to the Merry Vale Mixture Collection' (locale:132409).", "where": "Merry Vale", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11498-11506 (entry 1084, name_id 66822, item_definition_id 23209; collection id 150, name_id 67516, reward items 3082 x5); repo:prototype/osfr-tools/data/content/collections.json:11526 'Merry Vale Mixture'; wiki:List of Collections (Aquatic > Rare: 'Merry Vale Liquid Concoction', 'Merry Vale Mixture')"},
  {"type": "other", "detail": "Received as a loot/collection-progress message while playing in Merry Vale (chat line 'You receive 1 Magical Merry Vale Mixture' seen alongside Rich Tin Mining, Gold-Tipped Dragon and Fairy Cultist). The exact activity that yields the mixture is not confirmed by any source here; the Merry Vale Liquid Concoction and Merry Vale Water Samples collections sit in the same Aquatic chain.", "where": "Merry Vale", "price": null, "currency": null, "source": "video:9rPMuvwc728/00172.jpg; video:9rPMuvwc728/00174.jpg"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item 23209 is the 'Magical Merry Vale Mixture' (locale 66822) and is entry 7 of the Merry Vale Mixture collection (collection id 150, name 67516).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11498-11506 and 11421-11433"},
  {"claim": "The client sibling entries 66816-66823 are the eight Merry Vale Mixture variants (Toxic, Clean, Purified, Dirty, Boiling, Freezing, Magical, Mystical); the item's description ties it to the Merry Vale Mixture Collection.", "source": "locale:132409; locale:66816-66823 (client cluster)"},
  {"claim": "The Merry Vale Mixture is a Rare aquatic collection in the chain Merry Vale Water Samples (common) -> Merry Vale Liquid Concoction (rare) -> Merry Vale Mixture (rare).", "source": "wiki:List of Collections (Aquatic section, revid 27852, 2013-07-13)"},
  {"claim": "The client shows the player receiving 1 Magical Merry Vale Mixture in Merry Vale (Rich Tin Mining area, Fairy Cultist nameplate in view), so it was obtainable in-world, not retired at capture time.", "source": "video:9rPMuvwc728/00172.jpg, video:9rPMuvwc728/00174.jpg"},
  {"claim": "The collection's final reward is 5 of item definition 3082 (its name is not resolved here).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11517-11524"},
  {"claim": "No coin store price, vendor stock, or wiki page exists for this item; the client definition has coin_store_prices empty.", "source": "client definition in evidence pack; repo:data/content/stores.json not matched"}
 ],
 "confidence": 0.6,
 "open": [
  "The exact activity that yields the Magical Merry Vale Mixture (gather node, rare exploration, drop, or a mixing step) is not confirmed. The video shows only the loot message; the Rich Tin Mining, Gold-Tipped Dragon and Fairy Cultist text are on-screen context, not proven sources.",
  "Item 3082 (the collection reward) is not named in the evidence; it is unresolved.",
  "Retirement status of the Merry Vale Mixture collection is not stated by any source here; the wiki list is from 2013, and no later source confirms or retires it.",
  "No vendor, Coin Shop, Station Cash, or prize-wheel source exists for this item in the evidence."
 ]}
