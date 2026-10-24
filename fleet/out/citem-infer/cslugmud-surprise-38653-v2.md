<!-- fleet job=citem-infer id=cslugmud-surprise-38653-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6460, 8371, 6, 1916] model=claude-haiku-5-5 -->
# Slugmud Surprise

{"item": {"name": "Slugmud Surprise", "locale_id": 38653, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef recipe 'Slugmud Surprise' (recipe_id 41, chef job profile 45, Chef rank 5). Ingredients: Slugmud x3 (def 2893), Bundle of Chugaroot x3 (def 2888), Bundle of Choychoy x3 (def 2879), Broth x4 (def 2899). Output: definition 21815 x1. Recipe item: 'Slugmud Surprise Recipe' (def 851, locale 1518). The wiki row has an empty 'Where to find' field.", "where": "Chef cooking table", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:2600-2632 (chef.slugmud_surprise); wiki 'List of Recipes (Chef)' ([Slugmud] [Surprise] row); wiki 'Chef' ('[Slugmud] [Surprise] - Improves Maker's stats'); locale:1545 ('Requires chef level 5')"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 38653 is named 'Slugmud Surprise'; its description says it temporarily boosts Blacksmith, Chef, Miner and Postman talent; class 9; one definition (21815); no client coin store price.", "source": "locale:38653; client definition in the pack"},
  {"claim": "Chef recipe chef.slugmud_surprise makes definition 21815 from the four ingredients above at Chef rank 5.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2600-2632 (verified this pass)"},
  {"claim": "The wiki 'List of Recipes (Chef)' gives the same four ingredients and effect 'Improves Maker's stats'; the wiki 'Chef' page lists the same effect.", "source": "wiki 'List of Recipes (Chef)'; wiki 'Chef' (verified this pass)"},
  {"claim": "The recipe item text says it teaches Slugmud Surprise and requires chef level 5.", "source": "locale:1545"},
  {"claim": "Quest lines locale:24268 ('NOT LIVE - Making Slugmud Surprise') and 24243 (not_live flag) are NOT LIVE; 47603 ('Mimic: Cooking Slugmud Surprise [Placeholder]') is a placeholder. These are not used as evidence of live status. Unflagged lines 24245 and 24892 (recipe-reveal dialogue about a secret ingredient) do not by themselves prove the chain is live or not.", "source": "locale:24268, 24243, 47603, 24245, 24892"}
 ],
 "confidence": 0.6,
 "open": [
  "Recipe acquisition is unresolved: the wiki Gaston page lists 'Slugmud Surprise Recipe' with no price, while Chef.md records a Glurpie source (client line 68648192). I could not verify the Glurpie line in this pass, so neither is listed as a confirmed source for the recipe, and no price is attached.",
  "No coin store price is attached to the dish. stores.json item 38653 is a different definition (weapons.json: a power-4 weapon, rank 8, 1069 coins), so it is not evidence of a sale.",
  "Birthday Bash event (Chef) appears only in other answers' pack notes; no line or wiki page confirms it, so it is not listed.",
  "No enemy drop, prize wheel, collection, membership, Coin Shop or SC Marketplace source found.",
  "Retirement status unknown; no source says it was retired.",
  "Ingredient sources not checked. Slugmud (def 2893) may be the Slugmud Skipper fishing catch in Sacred Grove Shallows (fishing.json), but this link is unverified."
 ]}
