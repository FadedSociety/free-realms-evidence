<!-- fleet job=citem-infer id=cspiralmint-steak-recipe-1510-v5 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[6624, 12909, 6, 1544] model=claude-haiku-5-5 -->
# Spiralmint Steak Recipe

{"item": {"name": "Spiralmint Steak Recipe", "locale_id": 1510, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item locale:1510 'Spiralmint Steak Recipe' is definition 843, class 59, slot 0. It is a recipe-teaching item: description locale:1537 'This recipe teaches you how to create Spiralmint Steak.' No coin store price in the client definition, so no coin vendor sale is evidenced.", "source": "locale:1510; locale:1537; client definition 843"},
  {"claim": "recipes.json links chef.spiralmint_steak (recipe_id 33) to recipe_item_definition_id 843. This proves the definition-to-recipe link only, not how a player obtains the item or whether it is live.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2863-2867"},
  {"claim": "Chef quest text refers to Simone's Spiralmint Steak and to mastering her recipe (context only, no grant or reward record for definition 843 found).", "source": "locale:419226; locale:419224; locale:436580"},
  {"claim": "Quest objective 'Complete the recipe and you'll earn stars and some coin!' describes cooking the dish, not how the recipe is obtained.", "source": "locale:77905"},
  {"claim": "Repo-wide search for definition id 843 in content JSON found no store, vendor, drop, event, or collection row naming it (only unrelated ids that contain the digits).", "source": "repo search of prototype/osfr-tools/data/content/*.json"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. No coin vendor, marketplace, prize wheel, drop, event, collection, or quest reward record names definition 843.",
  "Unconfirmed lead: C1 'Chef: Cobblestone Village Cafe' (quest 3050006, Simone). Its objective text mentions the steak (locale:94534), but no grant or reward record for definition 843 exists. Chef.md lists C1 rewards as unknown. Not a sourced quest_reward.",
  "Removed from the lead list: the not_live Cooking/Bundle ids (locale:21835, 21837, 24079, 24080) and the duplicate locale:431167, per the id check. Unverified chef-job intro lines (locale:431102, 431139, 115069) did not resolve and are not used.",
  "Dead ids from the previous pack (locale:2362971086, locale:1379080248) are discarded.",
  "Kind: the client category is class 59 (recipe). The schema has no recipe kind, so 'other' is used here.",
  "Live status unverified: the definition exists in the client, but no live sale or grant source was found. Retirement status unknown."
 ]}
