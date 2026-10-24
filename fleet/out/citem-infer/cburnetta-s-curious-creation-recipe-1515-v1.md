<!-- fleet job=citem-infer id=cburnetta-s-curious-creation-recipe-1515-v1 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[18787, 18782, 8, 2760] model=claude-haiku-5-5 -->
# Burnetta's Curious Creation Recipe

{"item": {"name": "Burnetta's Curious Creation Recipe", "locale_id": 1515, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Mae Farnum (cook and merchant), sells the recipe; client line 'you can buy the recipe from Mae Farnum in Farnum Farmstead'", "where": "Farnum Farmstead", "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 848 (purchase_price_coins 540); repo:prototype/osfr-tools/data/content/vendors.json:305-358 (npc 9000000396, stock_source string ids 2373329029, 30334094); repo:notes/Build Guides/Content/Jobs/Chef.md:216 (video vendor list shows 540 coins)"},
  {"type": "vendor", "detail": "Bordon Cloo (master chef); client line 'If you don't have the recipe, you can buy it from Bordon Cloo in Sanctuary'", "where": "Sanctuary", "price": "540 coins (price not captured from this NPC; reference price from stores.json)", "currency": "coins", "source": "locale:829103903; repo:notes/Build Guides/Content/Jobs/Chef.md:216 and :350 (cites 829103903)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item 848 is the recipe for Burnetta's Curious Creation (recipe_id 38, Chef job, required job rank 1, output item 21812)", "source": "repo:prototype/osfr-tools/data/content/recipes.json:124-131 and :184-200"},
  {"claim": "Coin store price 540 coins, member price 486 coins (10% off), marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:17267 (item_id 848, purchase_price_coins 540)"},
  {"claim": "Client text says the recipe is bought from Mae Farnum in Farnum Farmstead", "source": "repo:prototype/osfr-tools/data/content/vendors.json:309 (string ids 2373329029, 30334094)"},
  {"claim": "Client text says the recipe is bought from Bordon Cloo in Sanctuary", "source": "locale:829103903"},
  {"claim": "Recipe item name and id", "source": "locale:1515; repo:prototype/osfr-tools/data/content/vendors.json:314-316"},
  {"claim": "Recipe is a Chef job recipe; ingredients Mystery Meat x3, Stickfruit x3, Tumtumnip x3, Butter x3", "source": "repo:notes/Build Guides/Content/Jobs/Chef.md:216"},
  {"claim": "Holiday gift-basket context: Downey asks for the dish for gift baskets", "source": "locale:1275934548"}
 ],
 "confidence": 0.6,
 "open": [
  "Two different vendors are named for the recipe (Mae Farnum at Farnum Farmstead per vendors.json; Bordon Cloo in Sanctuary per client string 829103903). Not resolved; both are listed. Verify in-game or with the wiki Mae Farnum / Bordon Cloo pages.",
  "The 540-coin price is a stores.json reference price, not a captured NPC quote (price_basis: '(R) stores.json reference price; no captured retail NPC quote'). Treat as the coin store price, not confirmed by a vendor screen.",
  "No wiki article for the recipe itself was found; no wiki price or sale data to compare.",
  "Retired status unknown: no source states it was removed or made unobtainable. Stores.json marks no_sale: true, which may mean it is not resold; check the stores source for that flag's meaning.",
  "Not a Coin Shop, SC Marketplace, prize wheel, drop or quest-reward item in any source provided.",
  "Member price 486 coins is from stores.json, not a captured quote."
 ]}
