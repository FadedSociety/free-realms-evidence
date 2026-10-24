<!-- fleet job=citem-infer id=cburnetta-s-curious-creation-38650-v3 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[21263, 15940, 8, 3047] model=claude-haiku-5-5 -->
# Burnetta's Curious Creation

{"item": {"name": "Burnetta's Curious Creation", "locale_id": 38650, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked by a Chef at a cooking table from recipe 'Burnetta's Curious Creation Recipe' (recipe item 848, locale:1515; recipe_id 38, job chef, required rank 1). Ingredients: definition 2859 x3, 2885 x3, 2890 x3, 2902 x3 (the pack names these as Mystery Meat, Bundle of Stickfruit, Bundle of Tumtumnip, Butter). Output: definition 21812 x1.", "where": "Cooking table (Chef job)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:124-155 (key chef.burnetta_s_curious_creation, output 21812); locale:38650; repo:notes/Build Guides/Content/Jobs/Chef.md:216"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 38650 is the dish, definition 21812, class 9, with a description giving Blacksmith, Chef, Miner and Postman talent buffs.", "source": "locale:38650; client definition in evidence pack"},
  {"claim": "The recipe item 848 (name locale:1515) teaches the dish: 'This recipe teaches you how to create Burnetta's Curious Creation.'", "source": "locale:1542; locale:1515; repo:prototype/osfr-tools/data/content/recipes.json:125-155"},
  {"claim": "Mae Farnum sells the recipe at Farnum Farmstead, per client text.", "source": "locale:421052; repo:prototype/osfr-tools/data/content/vendors.json:305-358 (Mae Farnum, item 848)"},
  {"claim": "Client text also says the recipe can be bought from Bordon Cloo in Sanctuary.", "source": "locale:421061; repo:notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md:140"},
  {"claim": "Holiday quest 'Curious Gift Baskets' (Downey, Snowhill) asks the player to cook the dish and consumes it; it does not award it.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:196; locale:421000"},
  {"claim": "Client quest text 'Get the Burnetta's Curious Creation recipe' exists, but its reward was not verified, so it is not used as a dish source.", "source": "locale:414286"},
  {"claim": "Burnetta's Greenwood Camp quests ask the player to cook the dish for her (objective text), and the dish is not shown as an award.", "source": "locale:73402; locale:73403; locale:77921; locale:421050; repo:notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md:180"},
  {"claim": "Titles 47591 ([Placeholder]) and 73257 (NOT LIVE) are flagged and were excluded from the evidence; they say nothing about retirement.", "source": "id_check flags on locale:47591 and locale:73257"}
 ],
 "confidence": 0.6,
 "open": [
  "No dish-level price: the dish has no coin store entry (coin_store_prices empty for definition 21812), and no captured price exists.",
  "The 540-coin price (member 486) belongs to recipe item 848 at Mae Farnum, and it is a stores.json reference price, not a captured NPC quote (vendors.json:317-321). It is a prerequisite for the dish, recorded on item 848 and not as a dish price. The Chef.md 'video vendor' claim for this price was not verified.",
  "Recipe vendors conflict: Mae Farnum (Farnum Farmstead, locale:421052) and Bordon Cloo (Sanctuary, locale:421061). Neither vendor's stock list or current price is confirmed.",
  "Stat effect conflicts: the wiki list page gives +12 Maker's Sense / +12 Maker's Speed; the wiki Chef page says 'Improves Maker's Stats'; the client description (locale:38650) gives Blacksmith, Chef, Miner and Postman talent buffs. The current effect is unresolved.",
  "Quest locale:414286 ('Get the Burnetta's Curious Creation recipe') was checked only as text. Its reward was not verified, so it is not listed as a source of the recipe or the dish.",
  "No wiki page, article or video was found for the dish. The wiki lookup failed on the apostrophe in the query and was not retried with a safe form.",
  "No retirement source was found. Retired is null, not false."
 ]}
