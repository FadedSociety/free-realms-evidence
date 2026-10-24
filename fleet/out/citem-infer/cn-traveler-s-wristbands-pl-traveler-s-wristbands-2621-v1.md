<!-- fleet job=citem-infer id=cn-traveler-s-wristbands-pl-traveler-s-wristbands-2621-v1 status=done turns=11 usd=0.0078 tokens(read,write,in,out)=[177922, 28153, 24, 4988] model=claude-haiku-5-5 -->
# {n}Traveler's Wristbands{pl="Traveler's Wristbands"}

{"item": {"name": "Traveler's Wristbands", "locale_id": 2621, "kind": "clothing"},
 "sources": [
  {"type": "collection", "detail": "Yo-yos collection (wiki 'Toys (Collections)'; the reward line reads \"Traveller's Wristband\", the wiki's spelling; the 'Yo-yos' collection lists 8 yo-yo entries, Common quality, spawn type Robgoblin, area Central Wilds, with a second reward value '21' that is unexplained)", "where": "Central Wilds (collection spot per Toys (Collections))", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:8386 (wiki_lines), :8380-8392 (quality/spawn/area); wiki page Toys (Collections), revision 31048 (2013-08-21)"},
  {"type": "collection", "detail": "Meta collections (Plates, Mission Complete, Yo-yos) per the Adventurer job note, which says the Gloves and Wristband pieces come from these, not from an exploration level", "where": null, "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Jobs/Adventurer.md:202 (cites wiki clothing sets; only the Yo-yos entry is confirmed by a data row)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 2621 is named Traveler's Wristbands and sits in a 33-definition family (ids 253, 1425-1429, 16264-16268, 16270) with slot 2 and one hand-model file.", "source": "locale:2621; client definition pack"},
  {"claim": "Wiki reward for the Yo-yos collection lists \"Traveller's Wristband\" (Traveler's Wristbands, spelling differs).", "source": "repo:prototype/osfr-tools/data/content/collections.json:8386; wiki page Toys (Collections)"},
  {"claim": "The wiki file page 'File:Traveler's Wristbands.png' exists, so the wiki has an article/image for this item name.", "source": "wiki ns6 File:Traveler's Wristbands.png (lookup)"},
  {"claim": "The Traveler's set (Cap, Shirt, Wristband, Shorts, Boots, Backpack) is a wiki clothing set; Shorts and Boots come from Rare Exploration coin chests (Briarwood, Seaside, Wilds), but no Rare Exploration row lists the Wristbands.", "source": "repo:notes/Build Guides/Content/Jobs/Adventurer.md:193,196,199,202"},
  {"claim": "Rumbledome reward 'Stitched Wristbands' (client 794123706) is a different item, not this one.", "source": "repo:prototype/osfr-tools/data/content/dungeons/the_rumbledome.json:817"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin store price 270 is NOT confirmed. The pack says coin_store_prices [270], but none of the 33 family definition ids is 270. stores.json line 166 has item_id 270 (category 101, purchase 270 coins, member 243) and the client's Models.txt/Images.txt name id 270 as other things (Butterfly Particle Effect, Seafarer Face Type). The price is attached to the wrong or an unrelated id, so no vendor source is claimed from it.",
  "No vendor, coin shop, marketplace, prize wheel, or event source was found for the Wristbands. No vendor_stock or video frame names it.",
  "The Yo-yos collection reward row carries an extra value '21' (coins: 21). Unclear whether this is a coin payout alongside the wristband or a count; it was not used as a price.",
  "The wiki spelling 'Traveller's Wristband' vs client 'Traveler's Wristbands' should be confirmed against the Toys (Collections) page, which was not opened directly; only the repo data row was read.",
  "Which of the 33 family variants (races/tints) are the Yo-yos rewards is unknown.",
  "Retired status and whether the Yo-yos collection is still live are not established, so live is 'unsure'."
 ]}
