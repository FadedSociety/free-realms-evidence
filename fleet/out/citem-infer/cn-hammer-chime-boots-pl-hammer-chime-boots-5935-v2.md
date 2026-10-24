<!-- fleet job=citem-infer id=cn-hammer-chime-boots-pl-hammer-chime-boots-5935-v2 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[5633, 13939, 6, 2322] model=claude-haiku-5-5 -->
# {n}Hammer Chime Boots{pl="Hammer Chime Boots"}

{"item": {"name": "Hammer Chime Boots", "locale_id": 5935, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin-store vendor. Price row only: stores.json item_id 5935, category 6, tint group 2, 270 coins regular, 243 coins member price (10% discount), sell-back 27 coins. The row names no NPC. Seppa (Dartmoor Quarry, Blacksmith merchant) is a candidate only, not confirmed: the Seppa stock list is not reconstructed (notes/Build Guides/Content/NPCs/NPCs - Wilds.md:58 says so), and the Blacksmith notes list Seppa's sales as Lunar Enchanted Wand and shards/tongs, not boots (notes/Build Guides/Content/Jobs/Blacksmith.md:190).", "where": "unidentified coin store (stores.json category 6)", "price": "270 coins (member 243 coins; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 5935 (line 13450)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 5935 is '{n}Hammer Chime Boots{pl=\"Hammer Chime Boots\"}', an item; the same set has Hammer Chime Gloves (5977), Goggles (35181), Shirt (5918) and Apron (5938) in client text.", "source": "locale:5935; locale:5977; locale:35181; locale:5918; locale:5938 (lookup client results)"},
  {"claim": "Client definition: slot 5 (feet), class 14, model worker_<race>_<gender>_feet_strappedboots.adr, 17 definitions over 12 definition ids. The pack's coin store price (270) is attached to this name.", "source": "client_definition in evidence pack"},
  {"claim": "Coin store row for item_id 5935: category 6, tint group 2, 270 purchase, 243 member, 27 sell-back, not no_sale. The same price and tag set (L1,L2,L4,R2,T633,R1) repeat on many category-6 rows (for example item_id 25935 and 75935 are in the same file, with different values for 75935), so it looks like a category template; the tags are undecoded.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 8830, 13450, 15682"},
  {"claim": "No wiki page, article fact, video frame, quest, drop, recipe or event names Hammer Chime Boots. No repo note names it either (repo search for 'Hammer Chime' returns nothing).", "source": "lookup (wiki, articles, video) and repo search, no matches"},
  {"claim": "Seppa's sold recipes per the notes are Lunar Enchanted Wand; the Blacksmith page lists Seppa's gear as sets and shards, but no boots list.", "source": "notes/Build Guides/Content/Jobs/Blacksmith.md:190, :250; notes/Build Guides/Content/NPCs/NPCs - Wilds.md:58"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor is unidentified. The only price evidence is an unattributed category-6 coin-store row (stores.json line 13450) whose values repeat across many items, so it is weak proof the item is sold at all. Do not name Seppa or any NPC until a stock list or wiki line ties item 5935 to them.",
  "Confirm stores.json item_id 5935 is an item id and not a definition id (the 12 definition ids 1358 to 21140 do not match it).",
  "Live status is unsure: the only source is the store row. No wiki, article or video confirms current sale. Retired status unknown.",
  "The source_tags (L1, L2, L4, R2, T633, R1) are not decoded, so they cannot confirm a sale point.",
  "No quest reward, enemy drop, crafting recipe, collection, event, prize wheel, or membership source found."
 ]}
