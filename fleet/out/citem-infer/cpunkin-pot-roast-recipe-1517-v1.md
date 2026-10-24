<!-- fleet job=citem-infer id=cpunkin-pot-roast-recipe-1517-v1 status=done turns=8 usd=0.0065 tokens(read,write,in,out)=[114327, 28197, 18, 3612] model=claude-haiku-5-5 -->
# Punkin Pot Roast Recipe

{"item": {"name": "Punkin Pot Roast Recipe", "locale_id": 1517, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 850 is named 'Punkin Pot Roast Recipe' (locale 1517), description 'This recipe teaches you how to create Punkin Pot Roast.' (locale 1544), one definition, slot 0, class 0, no models, no coin store price.", "source": "locale:1517; locale:1544; repo:prototype/osfr-tools/data/content/recipes_unresolved.json (key chef.punkin_pot_roast, candidate_recipe_item_definition_id 850, candidate_recipe_id 40)"},
  {"claim": "The recipe is a Chef cooking recipe (minigame type 9). The dish is the cook-off dish 'Punkin Potroast', with the Glerga cook-off challenge 'Cook a Punkin Potroast in under a minute!' and the quest objective 'Cook up some Punkin Pot Roast!'.", "source": "locale:20881; locale:20884; locale:20886; locale:77923; locale:116857; repo:prototype/osfr-tools/data/content/recipes_unresolved.json"},
  {"claim": "The recipe row is unresolved: the native recipe payload, ingredient counts, required Chef rank and the output definition were not captured; the recipe-to-minigame binding is missing.", "source": "repo:prototype/osfr-tools/data/content/recipes_unresolved.json chef.punkin_pot_roast missing_fields"},
  {"claim": "The Chef job guide has no row for Punkin Pot Roast, so no recipe giver, vendor, or quest reward is documented for it. Its nearest documented dish, Mystery Pot Roast, is taught by Chef Jarvie (217741357) and is a cook-off dish, which does not confirm the same path for this recipe.", "source": "repo:notes/Build Guides/Content/Jobs/Chef.md:221 (Mystery Pot Roast row); repo:notes/Build Guides/Content/Jobs/Chef.md:183 (Cook-off Contest)"},
  {"claim": "No wiki page, article fact, video frame, coin vendor stock, or other answer names this recipe as sold, granted, dropped or crafted.", "source": "lookup over client, wiki, articles and video for 'Punkin Pot Roast' (wiki hits were only the Chef recipe list row 'Mystery [Pot] [Roast]')"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Each candidate needs evidence: a Chef trainer or merchant line that hands out this recipe, a quest reward, a cook-off win reward, or a vendor row.",
  "Pack's first-pass source_guess 'unknown' is not confirmed by any evidence.",
  "Live status is unconfirmed: the client defines the recipe and a cook-off quest uses the dish, but no retirement or availability source was found. The first-pass 'live: yes' is a hint only.",
  "The recipe-to-minigame binding and the required Chef rank are unresolved (recipes_unresolved.json missing_fields), so the item's rank gate is unknown.",
  "No coin store price in client or repo:data/content/stores.json for item 850; no coin vendor stock found.",
  "The wiki list of Chef recipes has no 'Punkin Pot Roast' row; the list shows 'Mystery [Pot] [Roast]' instead, which may be a different name.",
  "Pack's critiques: none carried."
 ]}
