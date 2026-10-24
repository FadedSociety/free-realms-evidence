<!-- fleet job=citem-infer id=choney-milk-sundae-recipe-408781-v4 status=nothing_found turns=3 usd=0.0020 tokens(read,write,in,out)=[13853, 8106, 8, 1723] model=claude-haiku-5-5 -->
# Honey Milk Sundae Recipe

{"item": {"name": "Honey Milk Sundae Recipe", "locale_id": 408781, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Honey Milk Sundae Recipe' is locale 408781 (type other).", "source": "locale:408781"},
  {"claim": "Client definition 65832 (comment 'Honey Milk Sundae Recipe') is a candidate pattern item; definition 65833 is undescribed. Neither has a coin store row.", "source": "prototype/osfr-tools/data/content/recipes_unresolved.json:266-268, 313 (cites lab/references/FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json)"},
  {"claim": "The recipe links to Chef recipe index 71 as a candidate only (key chef.honey_milk_sundae, candidate_recipe_id 71); the binding is not confirmed.", "source": "prototype/osfr-tools/data/content/recipes_unresolved.json:264-268"},
  {"claim": "The output dish 'Cooking: Honey Milk Sundae' (locale 403489) is tagged quest_reward in the client, but the tag is not a source: no quest row grants this recipe.", "source": "locale:403489; notes/Research/original-activity-coverage.json:12479; quest-lines/quests.json (no link)"},
  {"claim": "Sanctuary quest 'Make Honey Milk Sundaes' (locale 403313) has quest text 403314 and dialog 409002 that do not say the recipe is granted or sold. The Bordon Cloo objective line is locale 403312 (quest-lines/lines.json:129102); the giver link is unconfirmed.", "source": "locale:403313; locale:403314; locale:409002; locale:403312"},
  {"claim": "Client lookup over client, wiki, articles and video returned only client-side lines. No wiki page, article, video frame, vendor stock line, drop or event names this recipe.", "source": "lookup over client, wiki, articles, video for 'Honey Milk Sundae'"},
  {"claim": "The wiki Chef recipe list does not include Honey Milk Sundae; the dish is among 11 minigame entries with no wiki recipe row.", "source": "notes/Build Guides/Content/Jobs/Chef.md:283"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found: no vendor, quest reward, drop, event, marketplace or coin shop evidence. Bordon Cloo may sell it or a Chef quest may grant it, but nothing shows either.",
  "Recipe index 71 to item 65832 binding is unconfirmed; the native recipe row is not captured.",
  "Definition 65833 is undescribed; may be a tint or variant.",
  "No coin store price in the client definition or stores.json; price, currency, zone and retired status unknown.",
  "Earlier answer's evidence citing locale:191333005 (does not exist) and the 403312 'no match' claim were removed; 403312 is a real string (Bordon Cloo objective)."
 ]}
