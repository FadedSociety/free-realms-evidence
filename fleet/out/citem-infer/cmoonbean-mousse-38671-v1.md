<!-- fleet job=citem-infer id=cmoonbean-mousse-38671-v1 status=done turns=6 usd=0.0060 tokens(read,write,in,out)=[80084, 25006, 14, 4219] model=claude-haiku-5-5 -->
# Moonbean Mousse

{"item": {"name": "Moonbean Mousse", "locale_id": 38671, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked at a Chef cooking station from 3 Moonbean, 3 Stainberry, 8 Sugar, 3 Snowhill Ice Cream: Chocolate (recipe_id 59, recipe item def 55827, Chef job profile 45, minimum Chef rank 1); output definition 21833", "where": "Chef cooking minigame", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:1438-1470; wiki Chef page ('[Moonbean] [Mousse] - Improves Maker's Stats') via lookup; notes Build Guides Content Jobs Chef.md row 'Moonbean Mousse'"},
  {"type": "quest_reward", "detail": "Recipe taught by Jack the Nibbler (Quarry) in the Jack quests: 'Supply Jack With Moonbean Mousse' (locale:73316), 'Cook Five Moonbean Mousse and Hand Them to Jack the Nibbler' (locale text 1107244138); Jack 'has taught you how to make some' (locale 1351507299). This is a teaching/quest step, not a purchasable item, so listed as quest-linked rather than a reward item.", "where": "Quarry (Jack the Nibbler)", "price": null, "currency": null, "source": "locale:73316; locale:1351507299 (string id as listed in en_us_data.dat); repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:23158 (Jack the Nibbler)"},
  {"type": "quest_reward", "detail": "Chef M3 quest 'Learning to Crave the Flave' (Bordon Cloo): 'Whip up a Moonbean Mousse for Bordon Cloo in Sanctuary' (locale:140412 Sanctuary objective)", "where": "Sanctuary (Bordon Cloo)", "price": null, "currency": null, "source": "locale:140412; repo:notes Build Guides Content Jobs Chef.md M3 row"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client definition 21833 is named Moonbean Mousse (locale 38671) with description 'Eating this food temporarily increases your talent as a Blacksmith, Chef, Miner, and Postman' (matches the wiki's 'Improves Maker's Stats' category)", "source": "client definition in pack; wiki page Chef (lookup, wiki)"},
  {"claim": "Chef recipe exists: recipe_id 59, output definition 21833, four ingredients, job Chef, rank 1", "source": "repo:prototype/osfr-tools/data/content/recipes.json:1438-1470"},
  {"claim": "Wiki Chef page lists Moonbean Mousse as a dish with a stat effect", "source": "lookup wiki page 'Chef' (Moonbean Mousse - Improves Maker's Stats)"},
  {"claim": "Quest objectives and quest titles tie the item to Jack the Nibbler (Supply Jack With Moonbean Mousse; Cook Five Moonbean Mousse and Hand Them to Jack) and to Bordon Cloo (Whip up a Moonbean Mousse for Bordon Cloo in Sanctuary)", "source": "locale:73316, locale:140412, locale text 1107244138"},
  {"claim": "Quest 'Mimic: Cooking Moonbean Mousse [Placeholder]' (locale:47684) is flagged placeholder and is not counted as a source", "source": "locale:47684 (FLAG placeholder)"},
  {"claim": "Cooking minigame title 'Cooking: Moonbean Mousse' and recipe item 'Moonbean Mousse Recipe' exist in client text", "source": "locale:386065; locale:387776"},
  {"claim": "No coin store price for definition 21833 in the client definition", "source": "client definition coin_store_prices: []"}
 ],
 "confidence": 0.6,
 "open": [
  "Conflict: repo:prototype/osfr-tools/data/content/stores.json:12396 has item_id 38671 (category 207, purchase 1431 coins, member 1287) with the same number as this item's locale id, but the client definition is 21833 and lists no coin store price. The store row is most likely a different item keyed on the locale number (repo weapons.json:45413 also uses 38671 for another item). Not used as a source; needs checking against definition ids.",
  "Jack the Nibbler's and Bordon Cloo's quest step numbers and exact quest names for the teaching step are not confirmed; the dialog string 73375 is tagged to the item name, not to a speaker.",
  "Whether the recipe is bought, taught by a single quest, or unlocked by Chef level is not confirmed: the source notes say the Chef rank is 1 but no recipe-book purchase price was found. Recipe price is unknown.",
  "Retirement status not stated by any source in the pack; no wiki page for the item itself.",
  "No critiques were included in the evidence pack."
 ]}
