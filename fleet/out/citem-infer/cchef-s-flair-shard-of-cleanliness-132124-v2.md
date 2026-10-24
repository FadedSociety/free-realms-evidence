<!-- fleet job=citem-infer id=cchef-s-flair-shard-of-cleanliness-132124-v2 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[29674, 12813, 10, 2605] model=claude-haiku-5-5 -->
# Chef's Flair Shard of Cleanliness

{"item": {"name": "Chef's Flair Shard of Cleanliness", "locale_id": 132124, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Zamzani (pixie Chef gear and recipe merchant, NPC id 9500001006)", "where": "Wugachug (near the Wugachug Cooking Table)", "price": "806 coins purchase (stores.json reference price, not a captured NPC quote); 725 coins member price; 80 coins sell-back", "currency": "coins", "source": "wiki page Zamzani, Sells section, listed as \"Chef's Flair Shard of Cleanliness\" (https://freerealms.fandom.com/wiki/Zamzani, CC BY-SA, revision 2025-07-04); repo:prototype/osfr-tools/data/content/vendors.json:46871-46910 (price_basis: reference price, no captured retail NPC quote); repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:79"},
  {"type": "coin_shop", "detail": "Coin store listing, category 124 (category name not established in the pack)", "where": "Coin Shop", "price": "806 coins (client definition coin_store_prices)", "currency": "coins", "source": "locale:132124 / ClientItemDefinitions Id 75678 coin_store_prices [806] (refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1218549); refs FreeRealms-Legacy/src/Resources/CoinStoreItems.json:69718-69719 (Id 75678, CategoryId 124)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Chef's Flair Shard of Cleanliness', locale 132124, description 'Sparkle, sparkle.', definition id 75678, slot 13, class 21", "source": "locale:132124"},
  {"claim": "Wiki Zamzani Sells section lists Chef's Flair Shard of Cleanliness; Zamzani is a pixie Chef gear merchant introduced 1 Oct 2013", "source": "wiki page Zamzani (Sells); repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:79"},
  {"claim": "Zamzani's shops are 2013 update additions, outside a launch-era rebuild", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:187"},
  {"claim": "Item 75678 has a coin-store row (CategoryId 124) in the Legacy server's coin store data; the date of that row is not established", "source": "refs FreeRealms-Legacy/src/Resources/CoinStoreItems.json:69718-69719"},
  {"claim": "The 806/725/80 figures are stores.json reference prices, explicitly not captured NPC quotes", "source": "repo:prototype/osfr-tools/data/content/vendors.json:46879, 46908"},
  {"claim": "Sibling Chef flair shards share one locale cluster (132119-132129)", "source": "client cluster locale:132119-132129"}
 ],
 "confidence": 0.6,
 "open": [
  "Zamzani's 806 coin price is a stores.json reference, not a captured NPC quote; the wiki Sells list carries no price.",
  "The coin-store row (category 124) is evidenced as present, but the category name and whether it is the live Coin Shop channel, and its date, are not established by the pack.",
  "Retirement status unknown: no source says whether Zamzani or the coin store still sells this shard. Live status is 'unsure'.",
  "Whether the shard is sold singly or only as part of a set is not stated.",
  "No quest, drop, crafting, prize-wheel or event source found in the pack.",
  "Zamzani's 2013 vendor may be outside a launch-era rebuild scope; the rebuild must decide whether to include it."
 ]}
