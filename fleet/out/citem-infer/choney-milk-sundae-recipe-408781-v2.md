<!-- fleet job=citem-infer id=choney-milk-sundae-recipe-408781-v2 status=nothing_found turns=2 usd=0.0022 tokens(read,write,in,out)=[4940, 9832, 6, 1755] model=claude-haiku-5-5 -->
# Honey Milk Sundae Recipe

{"item": {"name": "Honey Milk Sundae Recipe", "locale_id": 408781, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Honey Milk Sundae Recipe' is locale 408781 (other). Pattern item definition 65832 (Comment 'Honey Milk Sundae Recipe') is the candidate in the Legacy-sourced definitions; the pack's second definition 65833 is not described anywhere in the repo.", "source": "locale:408781; prototype/osfr-tools/data/content/recipes_unresolved.json:266-316 (candidate_recipe_item_definition_id 65832; evidence cites lab/references/FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json)"},
  {"claim": "The recipe is the Chef cooking minigame 'Cooking: Honey Milk Sundae' (locale 403489). The recipe-to-item binding (candidate recipe index 71) is unconfirmed.", "source": "locale:403489; prototype/osfr-tools/data/content/recipes_unresolved.json:264-316; notes/Research/original-activity-coverage.json:12479"},
  {"claim": "Sanctuary quest 'Make Honey Milk Sundaes' (locale 403313) asks the player to make the dish for Bordon Cloo; its quest text (locale 403314) and dialog (locale 409002) do not say the recipe is granted as a reward.", "source": "locale:403313; locale:403314; locale:408996; locale:409002"},
  {"claim": "No coin store price: repo search for 65832/65833 finds no row in data/content/stores.json.", "source": "repo search (stores.json has no item 65832 or 65833)"},
  {"claim": "No wiki page, article, video frame, vendor stock line, drop or event row names this recipe.", "source": "lookup over client/wiki/articles/video for 'Honey Milk Sundae'; repo search"},
  {"claim": "Correction to prior answer: locale:191333005 does not exist and was removed. Locale 403312 could not be confirmed by lookup (locale query for 403312 returned no match), so the prior dialog citation is dropped. The Chef.md note (notes/Build Guides/Content/Jobs/Chef.md:215, Gummyfruit Gumbo 540 coins video vendor price) only shows Bordon Cloo sells some recipes; it does not name this one.", "source": "locale query 403312|403313 (no match for 403312); notes/Build Guides/Content/Jobs/Chef.md:215"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Bordon Cloo may sell it (coins) or the Chef quest 403313 may grant it, but no evidence either way.",
  "Price, currency, zone and retired status are unknown.",
  "Recipe index 71 to item 65832 binding is unconfirmed; the native recipe row is not captured.",
  "Definition 65833 is undescribed; may be a tint or variant.",
  "Chef.md notes Starnut Sundae's source is unresolved too, so Chef recipe sourcing is incomplete in the repo generally."
 ]}
