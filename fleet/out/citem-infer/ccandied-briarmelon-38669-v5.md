<!-- fleet job=citem-infer id=ccandied-briarmelon-38669-v5 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6959, 9011, 6, 1842] model=claude-haiku-5-5 -->
# Candied Briarmelon

{"item": {"name": "Candied Briarmelon", "locale_id": 38669, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef recipe 'Candied Briarmelon Recipe' (client locale:1534; recipe key chef.candied_briarmelon, repo recipe_id 57; recipe pattern item definition 867). Ingredients: Briarmelon x3, Gummyfruit x3, Rainleaf x3, Sugar x8. Requires Chef level 20 (locale:1561). Output: item definition 21831.", "where": null, "price": null, "currency": null, "source": "wiki 'List of Recipes (Chef)' ([Candied] [Briarmelon] row: ingredients, 'Where to find' blank); wiki 'Chef' ('[Candied] [Briarmelon] - Increases Attack'); locale:1534; locale:1561; repo:prototype/osfr-tools/data/content/recipes.json:255-286 (output definition_id 21831 at line 284; pattern item 867 at line 327)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 38669 'Candied Briarmelon' is a food, description 'Eating this food temporarily increases your attack.', definition 21831, class 9, no coin store price.", "source": "client definition pack; locale:38669"},
  {"claim": "The recipe teaches creation of Candied Briarmelon and requires Chef level 20.", "source": "locale:1561"},
  {"claim": "Wiki Chef recipe list gives the ingredients and effect 'Increases Attack', with a blank 'Where to find' field.", "source": "wiki 'List of Recipes (Chef)'; wiki 'Chef'"},
  {"claim": "Repo maps recipe chef.candied_briarmelon (recipe_id 57) to output definition 21831; the recipe pattern item is definition 867 ('Candied Briarmelon Recipe').", "source": "repo:prototype/osfr-tools/data/content/recipes.json:255-286, 327"},
  {"claim": "Repo notes list Candied Briarmelon as a level-20 Chef recipe with no known source.", "source": "notes/Build Guides/Content/Jobs/Chef.md:236, 367"}
 ],
 "confidence": 0.5,
 "open": [
  "Acquisition of the recipe pattern (867) is unevidenced: no trainer, vendor, price, or quest teaching it appears in the client text, wiki, repo, or video. The crafting source has no price or where.",
  "The Briarwood Quarry Captain cook-and-deliver quest (locale:73410, 73382, 73266) is a related world link naming no item reward, so it is not listed as a source. Its live status is unconfirmed; the quest title locale:73265 is flagged not_live and is excluded as evidence.",
  "No coin store price, currency, or coin vendor stock found for item 21831.",
  "Retirement status unknown; no source says whether the recipe or food was removed later.",
  "Live status unsure: the item and recipe exist in the client and wiki, but no source confirms how players obtained them in live play.",
  "Earlier critique said recipe '867' contradicted recipe_id 57; both are correct: 57 is the repo recipe id and 867 is the recipe pattern item definition (repo recipes.json:327)."
 ]}
