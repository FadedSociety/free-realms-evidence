<!-- fleet job=citem-infer id=cpathfinder-s-shirt-2639-v1 status=done turns=5 usd=0.0041 tokens(read,write,in,out)=[40595, 16891, 12, 3091] model=claude-haiku-5-5 -->
# Pathfinder's Shirt

{"item": {"name": "Pathfinder's Shirt", "locale_id": 2639, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store vendor sale (exact vendor not identified; the store row is category 104, tint group 3)", "where": null, "price": "464 coins (member price 417 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 694 (item_id 2639, purchase_price_coins 464, member_price_coins 417, sell_price_coins 46)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client item name locale 2639 is \"Pathfinder's Shirt\"; a clothing item in slot 3 and class 1 with 15 definitions (variants) and the model freestyle_<race>_m_chest_vestoverrolledslv.adr", "source": "locale:2639"},
  {"claim": "Store data has a coin store row for item 2639 at 464 coins (member 417), not sell-restricted (no_sale false), so it was sold for coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 694"},
  {"claim": "The Adventurer wiki page lists Pathfinder's Shirt as a member of the Pathfinder set (alongside Hat, Gloves, Midriff Shirt, Pants, Capris, Boots), with no acquisition method given for the shirt", "source": "wiki page: Adventurer"},
  {"claim": "Wiki file pages exist for Pathfinder's Shirt (Guys), confirming the item was player-visible", "source": "wiki file: File:Pathfinder's Shirt (Guys).png"},
  {"claim": "Video frame shows Pathfinder's Shirt among items seen in the chest slot", "source": "video:22IH8XFo6R4/00014.jpg"},
  {"claim": "Pathfinder's Gloves are the set piece acquired through the Plates collection (a Meta collection); the shirt is not stated to be", "source": "wiki page: Adventurer"}],
 "confidence": 0.4,
 "open": ["Pack conflict: the pack lists coin_store_prices [270], but store row 2639 says 464 coins. 270 is the price of item_id 271 (a different definition id in the same set), so the 464 price was used. Confirm which row the live store sold.",
  "Which coin vendor or store category (104) sold it is not confirmed; the pack's vendor_stock is empty and no NPC was found.",
  "No wiki or article source gives the shirt's acquisition method, its era, or a retirement date. Retired status is unknown.",
  "Shirt's Adventurer set membership does not say whether the shirt came from the Plates collection, a quest, or a store; treat the set's other pieces as unverified for this item.",
  "The 15 definition variants (tints/races) were not each checked for separate prices; only the 2639 row was read."]}
