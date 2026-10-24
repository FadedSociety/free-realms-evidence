<!-- fleet job=citem-infer id=cforgotten-ancient-bone-66991-v2 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[24424, 10673, 10, 2548] model=claude-haiku-5-5 -->
# Forgotten Ancient Bone

{"item": {"name": "Forgotten Ancient Bone", "locale_id": 66991, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Piece 8 of 8 in the 'Ancient Bone Artifacts' collection (collection id 171, name locale 67537). Its description says the item 'can be added to the Ancient Bone Artifacts Collection'. How a player obtains the loose piece itself is not evidenced.", "where": null, "price": null, "currency": null, "source": "locale:132430; locale:67537; repo:prototype/osfr-tools/data/content/collection_catalogue.json:13459-13538 (collection 171, entry index 8, name_id 66991, item_definition_id 23378); video:p5sDafXSQtQ/00116.jpg (shows '[Ancient] [Bone] [Artifacts] (1/8)'); wiki 'List of Collections' (lists [Ancient] [Bone] [Artifacts] under Common)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 66991 'Forgotten Ancient Bone', definition_id 23378, has the description 'This item can be added to the Ancient Bone Artifacts Collection'.", "source": "locale:66991; locale:132430"},
  {"claim": "The collection 'Ancient Bone Artifacts' (id 171) has eight entries, and entry index 8 is name_id 66991 / item_definition_id 23378, so the item is a member piece. The set is 66984-66991 and matches the (1/8) progress shown in video.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13459-13538; video:p5sDafXSQtQ/00114.jpg; video:p5sDafXSQtQ/00116.jpg"},
  {"claim": "Completing the collection gives 2 coins and 50 XP (reward block of collection 171). The catalogue's reward block for the collection is coins 2, XP 50 for profile 120; no item reward.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13540-13552"},
  {"claim": "The collection exists in the wiki 'List of Collections' under Common, alongside other [Ancient] artifact collections.", "source": "wiki 'List of Collections' (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "The client defines no coin store price for this item, and no store entry exists.", "source": "client definition coin_store_prices empty; repo:data/content/stores.json has no entry for 23378"},
  {"claim": "Collection flavor text: 'Ancient bone artifacts in various conditions. Don't let dogs get these, you might never see them again.'", "source": "locale:67649"}
 ],
 "confidence": 0.45,
 "open": [
  "The acquisition path for the loose piece is unknown: no vendor, quest, drop, dig, crafting, prize-wheel or event source was found. The locale 67649 flavor text hints that pieces are found in the world but this is not a verified source.",
  "The catalogue entry item_link is 'sanctuary' for each piece; its meaning is not explained in the pack and was not checked.",
  "Live status is unsure: the collection is visible in video, but no source confirms this piece is currently obtainable.",
  "Retired is null, not false: no source states retirement either way.",
  "No prices: no coin store price, Station Cash, Coin Shop or prize-wheel entry was found.",
  "Locale 140834 'Ancient Bone' (definition 48262) is a different quest item and is not this item.",
  "Critique fix applied: the earlier claim that the piece is 'not bought or dropped' was removed as unsupported."
 ]}
