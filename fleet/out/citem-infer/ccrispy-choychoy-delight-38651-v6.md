<!-- fleet job=citem-infer id=ccrispy-choychoy-delight-38651-v6 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[22165, 16148, 8, 2946] model=claude-haiku-5-5 -->
# Crispy Choychoy Delight

{"item": {"name": "Crispy Choychoy Delight", "locale_id": 38651, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked by a Chef at job rank 5 from Bundle of Choychoy x3, Bundle of Chugaroot x3, Bundle of Rainleaf x3, Sugar x4 (ingredient definition IDs 2879x3, 2888x3, 2884x3, 2906x4). Requires the recipe item 'Crispy Choychoy Delight Recipe' (item 849). Output definition 21813.", "where": "Cooking table (Chef job)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:390-417 (recipe_item_definition_id 849, required_job_rank 5, output 21813); locale:1543; wiki:List of Recipes (Chef) for ingredient names (names not re-checked against definition IDs)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item definition 21813 is named 'Crispy Choychoy Delight' (locale 38651), class 9, description 'This is a powerful food.'", "source": "client definition in pack; locale:38651"},
  {"claim": "Recipe item 849 teaches the dish at chef rank 5 and outputs definition 21813, with ingredients 2879x3, 2888x3, 2884x3, 2906x4", "source": "repo:prototype/osfr-tools/data/content/recipes.json:390-417"},
  {"claim": "Locale 1543 is the recipe's description: teaches the dish, requires chef level 5", "source": "locale:1543"},
  {"claim": "Zamzani's wiki Sells section lists '[Crispy] [Choychoy] [Delight] [Recipe]' with no price. This is the recipe item 849, not the dish 21813, so it is not a source for the dish.", "source": "wiki:Zamzani; repo:prototype/osfr-tools/data/content/vendors.json:46703-46743"},
  {"claim": "vendors.json row for item 849 carries purchase_price_coins 540 / member 486, but price_basis says it is a reconstructed Legacy reference with no captured NPC quote. Same for stores.json item 849 (no_sale: true, sell_price_coins null). Neither is a verified price, and neither row is for the dish.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:46707-46711; repo:prototype/osfr-tools/data/content/stores.json:17268"},
  {"claim": "No stores.json or client coin-store price exists for the dish 21813. No vendor sells the dish.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no row for 21813); client definition coin_store_prices empty"},
  {"claim": "Client NPC line says a player without the recipe can get it from the Coin Shop. This refers to the recipe, not the dish, and no listing or price was confirmed.", "source": "locale:428465"},
  {"claim": "Archery and Merry Vale lines (73260, 73359, 73406, 73407) describe the dish as a reward handed to an NPC-chosen archer or as something to cook. They are not player acquisition routes.", "source": "locale:73260; locale:73359; locale:73406; locale:73407"},
  {"claim": "Locales 47595 ('[Placeholder]') and 73259 ('NOT LIVE') are flagged and were not used as evidence.", "source": "locale:47595; locale:73259"}
 ],
 "confidence": 0.6,
 "open": [
  "Recipe acquisition (item 849, not the dish) is unresolved. Wiki Zamzani Sells lists the recipe with no price. locale:428465 says the Coin Shop sells it. repo stores.json marks 849 no_sale: true, which conflicts with both. The recipe's real source is not settled, so it is not listed as a source for the dish.",
  "Dish price: none known. Crafting costs ingredients only; no coin price is confirmed for the dish.",
  "The 540 / 486 figures on items 849 (vendors.json and stores.json) are reconstructed Legacy references, not captured prices. They are not used as prices here.",
  "Ingredient names (Bundle of Choychoy, Bundle of Chugaroot, Bundle of Rainleaf, Sugar) come from the wiki recipe list. The mapping from definition IDs 2879, 2888, 2884, 2906 to those names was not checked in the repo.",
  "Effect 'increases movement speed' is from the wiki recipe list only; not checked in client data.",
  "No wiki article exists for the dish itself. No live capture of the recipe or the dish was found.",
  "No retirement evidence found; retired is null."
 ]}
