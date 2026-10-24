<!-- fleet job=citem-infer id=cstainberry-chocolate-gumdrop-38659-v2 status=no_submit turns=3 usd=0.0038 tokens(read,write,in,out)=[22686, 16968, 8, 2812] model=claude-haiku-5-5 -->
# Stainberry Chocolate Gumdrop

```json
{"item": {"name": "Stainberry Chocolate Gumdrop", "locale_id": 38659, "kind": "consumable"},
 "sources": [
  {"type": "vendor", "detail": "Recipe 'Stainberry Chocolate Gumdrop Recipe' (item 857, locale 1524), sold by Lorraine (NPC 9500000354). The dish itself is not sold, only the recipe.", "where": "Lakeshore, near the Lakeshore Cooking Table", "price": "540 coins (member price 486 coins), stores.json reference price, not a captured NPC quote", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:20158-20199; repo:prototype/osfr-tools/data/content/stores.json:17272 (item_id 857); notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:79 (Lorraine, near the Lakeshore Cooking Table, stock added 1 Oct 2013)"},
  {"type": "crafting", "detail": "Cooked at a cooking table from recipe 857. Ingredients per wiki list: Gummyfruit x3, Stainberry x3, Sugar x6, Chocolate Bar x3. Effect: raises Blacksmith, Chef, Miner and Postman talent (temporary). Requires Chef level 10.", "where": "Cooking table, Lakeshore (per Lorraine's location)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:2995-3066 (output definition 21821); locale:1551 ('Requires chef level 10'); notes/Build Guides/Content/Jobs/Chef.md:229 (ingredient list)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item name and description: 'Eating this food temporarily increases your talent as a Blacksmith, Chef, Miner, and Postman.' (definition 21821, class 9, consumable)", "source": "locale:38659; client definition"},
  {"claim": "Recipe 857 is named 'Stainberry Chocolate Gumdrop Recipe' and its text says it teaches the dish and requires Chef level 10", "source": "locale:1524; locale:1551"},
  {"claim": "Dish is cooked by the player; quest objectives 'Cook up a Stainberry Chocolate Gumdrop!'", "source": "locale:102387; locale:77928"},
  {"claim": "Lorraine sells the recipe (Stainberry Chocolate Gumdrop Recipe, item 857) and the vendor stock note dates it 1 Oct 2013", "source": "repo:prototype/osfr-tools/data/content/vendors.json:20107, 20158-20199"},
  {"claim": "Recipe price 540 coins, member 486 coins, is a stores.json reference price", "source": "repo:prototype/osfr-tools/data/content/stores.json:17272"},
  {"claim": "Recipe pattern and output definition 21821 linked in recipes.json", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2995-3066"}
 ],
 "confidence": 0.6,
 "open": [
  "Assistant Chef Edward (NPC 3884809748, Snowhill) is dropped as a vendor source. Chef.md:229/:255 are the author's own notes, the video line 918625045 is a learn message, and locale:414515 does not name Edward. No price or shop evidence exists.",
  "Snowhill kitchen is dropped as a location for this dish; no cited source places it there.",
  "stores.json line 12393 does exist: item_id 38659, category 207, tint_group 1, purchase 1069 coins, member 962, sell 106. It is keyed by the locale id, not definition 21821, and the cited sources do not identify it. Not used as a source. It could be a separate item or a mis-keyed row, so verify it before wiring any price.",
  "Quest 'Mimic: Cooking Stainberry Chocolate Gumdrop' (locale:47631) is flagged Placeholder, so it is not used. locale:414579 is not used either.",
  "The recipe text (locale:1551) names 'Stainberry Stickfruit Gumdrop', while the item name is 'Stainberry Chocolate Gumdrop'. The variant name is unverified.",
  "Lorraine's current availability rests on the wiki page revision (2025) per the earlier answer. Not independently confirmed here, so the live status is only moderately supported.",
  "No enemy drop, collection, prize wheel, membership, promotion, or event source found."
 ]}
```
