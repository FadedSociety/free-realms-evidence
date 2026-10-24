<!-- fleet job=citem-infer id=cpathfinder-s-backpack-29102-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[19487, 12490, 10, 2811] model=claude-haiku-5-5 -->
# Pathfinder's Backpack

{"item": {"name": "Pathfinder's Backpack", "locale_id": 29102, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, store category 104, tint group 2 (one of the 8 definitions); the vendor/NPC name is not in the store data", "where": "coin store (category 104)", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:10463 (item_id 29102, purchase_price_coins 270, member_price_coins 243); client definition coin_store_prices 270"},
  {"type": "collection", "detail": "Rare Exploration collection reward, Wilds Northwest Rare Exploration (wiki reward line: 'Pathfinder's Hat' and 'Pathfinder's Backpack'); rare collections are paid with Rare Exploration Coins", "where": "Wilds (Northwest)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:1979-1983 (wiki_lines); repo:notes/Build Guides/Content/Jobs/Adventurer.md:199; wiki page Adventurer (Pathfinder's [Backpack] (Both Genders))"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 29102 is \"Pathfinder's Backpack\"; sibling locale 29103 is \"Explorer's Backpack\"", "source": "locale:29102; locale:29103"},
  {"claim": "Store data lists item 29102 in category 104 at 270 coins, member price 243, sell 27, not no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:10463"},
  {"claim": "Wiki Adventurer page lists Pathfinder's Backpack as part of the Pathfinder's clothing set, both genders", "source": "wiki page: Adventurer"},
  {"claim": "Wilds Northwest Rare Exploration collection rewards Pathfinder's Hat and Pathfinder's Backpack", "source": "repo:prototype/osfr-tools/data/content/collections.json:1981-1982; repo:notes/Build Guides/Content/Jobs/Adventurer.md:199"},
  {"claim": "Video frames list Pathfinder's Backpack among Explorer-backpack items seen in gameplay, and a Wilds rare-exploration quest frame", "source": "video:JNEzUHfmocc/00026; video:22IH8XFo6R4/00024; video:45PgwOt0gMI/00024"},
  {"claim": "Client has 8 definitions for the name (tints/races) sharing one model freestyle_<race>_<gender>_shoulders_backpack.adr", "source": "client definition pack"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store price of 270 comes from our store data (category 104), but no wiki page or article names the vendor or NPC that sells it; the Coin Shop vs. vendor label is unconfirmed.",
  "The collection source rests on the wiki's reward line, which is a secondary source: it is not confirmed that the reward is the same item at the same locale id 29102 and not another tint.",
  "The wiki mentions Pathfinder's Backpack only in the Adventurer page; no dedicated wiki article exists, so the wiki price for the coin store sale is not independently cross-checked.",
  "Retirement status is unknown: the store row has no_sale false, but no source gives a retirement or end-of-sale date.",
  "The first-pass tag 'source_guess: vendor' is only a hint; the coin store row is the evidence used here, and the collection reward is listed as a second source.",
  "Critiques were not carried in the pack, so none needed fixing."
 ]}
