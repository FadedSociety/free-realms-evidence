<!-- fleet job=citem-infer id=ccracked-ancient-statue-67001-v1 status=done turns=6 usd=0.0049 tokens(read,write,in,out)=[59912, 19141, 14, 3760] model=claude-haiku-5-5 -->
# Cracked Ancient Statue

{"item": {"name": "Cracked Ancient Statue", "locale_id": 67001, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Ancient Artifact Statues collection (collection id 173, name locale:67539), entry 2 of 8 (item definition 23388, icon tint 126). The item is a collection entry, not a standalone purchasable or droppable item. Completing the set pays 3 coins and 50 XP (profile 49).", "where": null, "price": "3 coins (set completion reward)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 13650-13745 (collection id 173: entries 1262-1269, reward.coins 3, xp 50)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Cracked Ancient Statue' is client locale 67001 (item), with description 'This item can be added to the Ancient Artifact Statues Collection' (locale:132432 for the collection line).", "source": "locale:67001; locale:132432"},
  {"claim": "Item definition 23388 is entry 2 of collection 173 'Ancient Artifact Statues' (name locale:67539, description locale:67651).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json line 13674 (item_definition_id 23388, name_id 67001) and line 13650 onward; locale:67539; locale:67651"},
  {"claim": "The Ancient Artifact Statues collection is listed on the wiki's List of Collections under the Rare group ('[Ancient] [Artifact] [Statues]'), with the 2013-07-13 revision.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); repo:prototype/osfr-tools/data/content/collections.json line 10950-10961 area"},
  {"claim": "A video frame lists '[Ancient] [Artifact] [Statues] (5/8)' in the collection progress list, so the set was a live in-game collection with 8 entries.", "source": "video:p5sDafXSQtQ/00114.jpg"},
  {"claim": "Sibling set Ancient Chalice Artifacts (collection 172) pays 8 coins; Ancient Arrowhead Artifacts pays 20 coins per wiki. These are sibling sets, not this item's price.", "source": "repo:collection_catalogue.json lines 13636-13638; wiki page Ancient Arrowhead Artifacts"}
 ],
 "confidence": 0.5,
 "open": [
  "No store price: client definition has no coin_store_prices entry, so no vendor sale is evidenced.",
  "How a player obtains the individual statue piece is not evidenced in any source (no wiki page for the item, no vendor stock, no quest, no drop, no video frame naming it). The source of the piece itself is unknown.",
  "The 3 coins set reward comes from our own catalogue (repo), not from a wiki or in-game source. Verify against the wiki's List of Collections or a live reward before treating it as a confirmed price. Sibling sets pay 8 coins (chalice) and 20 coins (arrowhead, wiki), so 3 is unusual.",
  "Live status and retirement date are not evidenced beyond the 2013 wiki list and one video frame; treat live as unsure.",
  "Pack's client definition says 'slots [0]' and 'class_ids [0]' and no models, consistent with a collection-only item with no equip slot."
 ]}
