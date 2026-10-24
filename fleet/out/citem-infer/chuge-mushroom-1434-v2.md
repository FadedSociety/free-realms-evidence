<!-- fleet job=citem-infer id=chuge-mushroom-1434-v2 status=nothing_found turns=3 usd=0.0034 tokens(read,write,in,out)=[21172, 17176, 8, 2063] model=claude-haiku-5-5 -->
# Huge Mushroom

{"item": {"name": "Huge Mushroom", "locale_id": 1434, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text locale:1434 is 'Huge Mushroom', an item-name string. It sits in the 1422-1437 run of mushroom item names (Spotted, Frosty, Enchanted, Thorny, Tiny, Rotten, Stinky, Crystal).", "source": "locale:1434; locale lookup 1422-1437"},
  {"claim": "The description 'This item can be added to the Unique Mushrooms Collection' is locale:132305 (ui, 'Unique Mushrooms Collection'). The previous answer's citation locale:1997116615 does not exist and is withdrawn.", "source": "locale:132305"},
  {"claim": "The collection name 'Unique Mushrooms' is locale:38900, and its collection description 'These mushrooms are all one-of-a-kind.' is locale:38901.", "source": "locale:38900; locale:38901"},
  {"claim": "The wiki's 'List of Collections' page lists '[Unique] [Mushrooms]' as a collection, under the Rare group. It does not list the items inside it.", "source": "wiki page 'List of Collections' (lookup hit, wiki ns0)"},
  {"claim": "Mushroom-related quest text exists: 'Collect the mushroom specimens!' (locale:4539). It does not name Huge Mushroom and gives no source for it.", "source": "locale:4539"},
  {"claim": "No coin store price, no vendor stock and no wiki, article or video line names Huge Mushroom as a drop, reward, vendor or crafting input.", "source": "lookup over client, wiki, articles and video for 'Huge Mushroom', 'Unique Mushrooms'; repo search for 1434 and 3286 (no hits in data)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. The item belongs to the Unique Mushrooms collection (wiki List of Collections), but the collection's member list and each mushroom's source (gathering, drop, or other) are not in the refs. Check the wiki 'Unique Mushrooms' collection page or the Briarwood collection page for the list.",
  "The Spotted Mushroom sibling set (locale 1422-1428, 5461) and the Mushroom Gigas or Mushroom Caverns content are the likely neighbours, but no line ties Huge Mushroom to any of them.",
  "Live status and retirement are unconfirmed. No wiki or article line says the item was obtainable or retired.",
  "The Sanctuary and FreeRealms-Legacy 'Huge Mushroom' comments (ClientItemDefinitions.json:61102) carry no source, price or drop, so they add nothing."
 ]}
