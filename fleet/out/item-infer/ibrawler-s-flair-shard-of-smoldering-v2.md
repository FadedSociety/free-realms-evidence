<!-- fleet job=item-infer id=ibrawler-s-flair-shard-of-smoldering-v2 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[19604, 9272, 10, 2291] model=claude-haiku-5-5 -->
# Brawler's Flair Shard of Smoldering

{"item": {"name": "Brawler's Flair Shard of Smoldering", "locale_id": 131038, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Roosey (pixie NPC merchant, sells exclusively Brawler job items), Sells list", "where": "Cobblestone Village (near the Cooking Table)", "price": "750 coins (reference price from stores.json purchase_price_coins; member price 675; sell price 375; not a captured NPC quote)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Roosey (Sells section, rev 2022-03-22; item listed as Brawler's Flair Shard of Smoldering); repo:prototype/osfr-tools/data/content/vendors.json:14648-14661 and :14839-14879; repo:prototype/osfr-tools/data/content/stores.json:15239 (item_id 75294)"},
  {"type": "coin_shop", "detail": "Coin Shop listing per wiki category; no separate price beyond the 750 structured field", "where": "Coin Shop", "price": "750 coins (wiki structured field; page text price blank)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_Smoldering (rev 32678; categories Coin Shop, Marketplace Items)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item is a level 1 Brawler flair shard; description 'Casts a red glow over your weapons. Ominous!'", "source": "https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_Smoldering"},
  {"claim": "Client name for the item is locale 131038 'Brawler's Flair Shard of Smoldering'", "source": "locale:131038"},
  {"claim": "Roosey's wiki Sells list includes Brawler's Flair Shard of Smoldering, alongside Bell Brawler gear and Brawler's Flair Shard of Valentines; Roosey is found near the Cobblestone Village Cooking Table", "source": "https://freerealms.fandom.com/wiki/Roosey"},
  {"claim": "Repo vendor record maps Roosey (npc_id 9500000255, cobblestone_village.json) stock to item_id 75294 with name_id 131038", "source": "repo:prototype/osfr-tools/data/content/vendors.json:14648-14661, 14839-14879"},
  {"claim": "Repo reference prices for item 75294: purchase 750, member 675 (10% discount), sell 375; these are stores.json reference values, not captured NPC quotes", "source": "repo:prototype/osfr-tools/data/content/stores.json:15239"},
  {"claim": "Wiki Coin Shop category and structured coins field give 750", "source": "https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_Smoldering"}
 ],
 "confidence": 0.7,
 "open": [
  "The 750 price is not a captured Roosey quote; the Roosey page and repo record say prices are unknown. Treat 750 as reference only.",
  "Wiki lists the item both as a Coin Shop item and as a Roosey Sells item; the Coin Shop and Roosey sources may be the same offering, not two separate sales. Unverified which is current.",
  "The member price 675 and sell price 375 are repo reference values only, with no wiki or NPC quote evidence.",
  "No retirement or removal date was found; retired is null and live is unsure.",
  "No drop, quest, crafting, or station cash source is evidenced.",
  "Kind is 'other' because the schema has no flair category; a flair shard is not clearly clothing, weapon, or consumable."
 ]}
