<!-- fleet job=citem-infer id=cmoonbean-mousse-38671-v2 status=done turns=4 usd=0.0027 tokens(read,write,in,out)=[23644, 8929, 10, 2737] model=claude-haiku-5-5 -->
# Moonbean Mousse

{"item": {"name": "Moonbean Mousse", "locale_id": 38671, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked at a Chef cooking station from 3 Moonbean (def 2878), 3 Stainberry (def 2887), 8 Sugar (def 2906), 3 Snowhill Ice Cream: Chocolate (def 2896); recipe_id 59, recipe item def 55827, Chef job profile 45, minimum Chef rank 1; output definition 21833", "where": "Chef cooking minigame", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:1438-1470 (verified); wiki page Chef (lookup: '[Moonbean] [Mousse] - Improves Maker's Stats')"},
  {"type": "other", "detail": "Quest step: Jack the Nibbler (Quarry) taught the recipe in the Jack quests ('Supply Jack With Moonbean Mousse', 'Cook Five Moonbean Mousse and Hand Them to Jack the Nibbler'). Teaching step, not a purchasable item and no reward item shown.", "where": "Quarry (Jack the Nibbler)", "price": null, "currency": null, "source": "locale:73264 ('He has taught you how to make some'); locale:73316; locale:73408; repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:23158"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client definition 21833 is named Moonbean Mousse (locale 38671), description: eating temporarily increases talent as Blacksmith, Chef, Miner, Postman", "source": "client definition in pack; locale:38671"},
  {"claim": "Chef recipe chef.moonbean_mousse exists: recipe_id 59, output definition 21833, four ingredients, Chef rank 1", "source": "repo:prototype/osfr-tools/data/content/recipes.json:1438-1470"},
  {"claim": "Wiki Chef page lists '[Moonbean] [Mousse] - Improves Maker's Stats' among dishes", "source": "wiki page Chef (lookup, wiki)"},
  {"claim": "Jack the Nibbler quest text says he taught the player to make Moonbean Mousse and asks for five to be cooked and handed to him", "source": "locale:73264; locale:73316; locale:73408"},
  {"claim": "Bordon Cloo Sanctuary objective 'Whip up a Moonbean Mousse for Bordon Cloo in Sanctuary' is a cooking use of the item, not an acquisition source", "source": "locale:140412"},
  {"claim": "Cooking minigame title 'Cooking: Moonbean Mousse' exists", "source": "locale:386065"},
  {"claim": "No coin store price for definition 21833 in the client definition", "source": "client definition coin_store_prices: []"},
  {"claim": "Mimic placeholder quest locale:47684 is flagged placeholder and excluded", "source": "locale:47684 (FLAG placeholder)"}
 ],
 "confidence": 0.65,
 "open": [
  "Store row repo:prototype/osfr-tools/data/content/stores.json:12396 has item_id 38671 (category 207, 1431 coins, member 1287). Store item ids should be definition ids, and definition 21833 has no store price, so this row is most likely a different item keyed on the locale number. Not used as a source; needs checking.",
  "Recipe acquisition price is unknown: no recipe purchase price or recipe-book source found. Whether Jack's teaching was a single quest step or a grant is not confirmed.",
  "Bordon Cloo quest 'Learning to Crave the Flave' (locale:24000 title) is dropped as an acquisition source: it only requires the item. Its link to the recipe is not shown.",
  "Retirement status not stated by any source; no wiki article for the item itself.",
  "The earlier pack's locale:1351507299 and 1107244138 do not exist; corrected to locale:73264 and locale:73408."
 ]}
