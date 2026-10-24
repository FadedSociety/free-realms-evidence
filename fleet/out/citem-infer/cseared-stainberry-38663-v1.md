<!-- fleet job=citem-infer id=cseared-stainberry-38663-v1 status=done turns=6 usd=0.0055 tokens(read,write,in,out)=[56475, 22527, 14, 4156] model=claude-haiku-5-5 -->
# Seared Stainberry

{"item": {"name": "Seared Stainberry", "locale_id": 38663, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef cooking recipe 'Seared Stainberry' (recipe_id 51, cooking minigame type 9, Chef job profile 45, min rank 1). Ingredients: Bundle of Sunleaf x3 (def 2880), Bundle of Rainleaf x3 (def 2884), Bundle of Stainberry x3 (def 2887), Sugar x7 (def 2906). Output: definition 21825, count 1. Buff: temporarily raises Blacksmith, Chef, Miner and Postman talent.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:2343-2468; locale:38663; wiki page 'Chef' (list of Chef recipes, 'Seared Stainberry - Improves Maker's Stats')"},
  {"type": "other", "detail": "Recipe scroll 'Seared Stainberry Recipe' (pattern item 861) is the item that teaches the recipe. Seen as a reward in a Cooking minigame ('Mystery Pot Roast' -> 'Royal Stew Du Jour' recipe learned, with Seared Stainberry recipe shown in the same reward screen). Exact recipe-granting source (minigame reward vs. vendor/quest) is not confirmed.", "where": null, "price": null, "currency": null, "source": "locale:1528; locale:1555; video:w-9vtebjou4/00100.jpg"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item is client definition 21825 with name locale 38663 'Seared Stainberry', class 9, food buff text", "source": "client definition in pack; locale:38663"},
  {"claim": "Chef recipe exists in the recipe store with four ingredient stacks and output 21825", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2343-2468"},
  {"claim": "Wiki Chef recipe list includes Seared Stainberry (Improves Maker's Stats)", "source": "wiki page Chef (ns0), lookup result"},
  {"claim": "Recipe item 'Seared Stainberry Recipe' exists in client", "source": "locale:1528; locale:1555"},
  {"claim": "Sanctuary quest 'Cook Seared Stainberry' / objective 'Make some Seared Stainberry for Bordon Cloo in Sanctuary' (quest title 140407, objective 140408, and Sanctuary placeholder mimic quest 47651) shows the item was a quest craft objective in the Sanctuary/refs content", "source": "locale:140407; locale:140408; locale:47651 (placeholder flag)"},
  {"claim": "A Sanctuary NPC dialog lists Seared Stainberry among recipes being collected", "source": "locale:384674"},
  {"claim": "Video shows Cooking minigame reward screen with 'Seared Stainberry (recipe)' alongside Royal Stew Du Jour recipe", "source": "video:w-9vtebjou4/00100.jpg"}
 ],
 "confidence": 0.6,
 "open": [
  "stores.json has an entry with item_id 38663, category 207, tint_group 2, 1069 coins (member 962). The id equals the NAME locale id, not definition 21825, and category 207 is clothing-style data (tint groups), so this is most likely a different item keyed by name id. It is NOT attributed as a coin store sale of Seared Stainberry; verify before using it as a price.",
  "How the Seared Stainberry recipe scroll (def 861 / locale 1528) is obtained is unconfirmed: video shows it as a cooking minigame reward, but no vendor, quest or drop source is verified in the pack.",
  "Sanctuary quest 'Cook Seared Stainberry' is a Sanctuary-server quest objective (Bordon Cloo), not a verified live reward. Treat as a possible quest-consumption use, not a source.",
  "Retired status and any later availability are not stated by any source in the pack.",
  "Price of the cooked item itself: no store or vendor price found."
 ]}
