<!-- fleet job=citem-infer id=cgummyfruit-topped-sundae-recipe-387778-v1 status=done turns=7 usd=0.0071 tokens(read,write,in,out)=[111599, 30543, 16, 4343] model=claude-haiku-5-5 -->
# Gummyfruit Topped Sundae Recipe

{"item": {"name": "Gummyfruit Topped Sundae Recipe", "locale_id": 387778, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 55825 is the recipe pattern for the Chef dish Gummyfruit Topped Sundae (recipe_id 43, job profile 45 Chef, MinProfileRank 1, crafting minigame type 9); output is dish definition 21817 with 4 Bundle of Gummyfruit (2875), 3 Snowhill Ice Cream: Vanilla (2895), 3 Starnut (2886), 4 Sugar (2906).", "source": "repo:prototype/osfr-tools/data/content/recipes.json:1044-1120 (chef.gummyfruit_topped_sundae); the 55825 comment is from lab/references/FreeRealms-Legacy ClientItemDefinitions.json as cited in that row"},
  {"claim": "The dish is on the wiki Chef recipe list with ingredients Gummyfruit x4, Snowhill Ice Cream: Vanilla x3, Bundle of Starnut x3, Sugar x4, effect Increases Maker's Reach. The wiki 'Where to find' line is blank.", "source": "wiki: List of Recipes (Chef) (oldid 45318); wiki: Chef (Maker's Stats)"},
  {"claim": "Client quest text names the dish in the Chef series 'Chef: Learning to Crave the Flave' (Bordon Cloo, after level 5): 'How are those recipes coming along? I'm looking for one Gummyfruit Topped Sundae...' and 'Whip up some Gummyfruit Topped Sundae for Bordon Cloo.'", "source": "locale:384674; locale:102367; locale:140400; repo:notes/Build Guides/Content/Jobs/Chef.md:112"},
  {"claim": "Client text for the dish (locale 38655) and the recipe item (387778) are in the same name cluster as Starnut Sundae, Moonbean Sundae Sweettreat and Moonbean Mousse recipes.", "source": "locale:38655; locale:387778; locale:387775-387780"},
  {"claim": "Bordon Cloo's recipe sales are recorded for Gummyfruit Gumbo, Savory Spiralmint Soup and Burnetta's Curious Creation, not for the Sundae recipe.", "source": "repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:8217; repo:notes/Build Guides/Content/Jobs/Chef.md:214-216"},
  {"claim": "No coin store price exists for definition 55825 in the store data (search of stores and content JSON found no 55825 row).", "source": "repo search for 55825 across *.json; repo:data/content/stores.json has no entry"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is confirmed. The pack has no vendor stock, store price, quest reward, drop or wiki 'Where to find' entry for this recipe, so sources is empty rather than guessed.",
  "Bordon Cloo is the likely seller by analogy with Gummyfruit Gumbo, but no repo or wiki line says he sells the Sundae recipe. Check the Sanctuary Bordon Cloo vendor list in-client before adding him.",
  "The M3 quest asks for the dish, not the recipe. It is not evidence the recipe is a quest reward.",
  "Wiki Chef list says 'Named in Learning to Crave the Flave (M3)'. Whether the recipe is a level-gated purchase, a cook-off reward, or a starter is unknown.",
  "Price and currency unknown. The 540-coin video vendor price applies to other recipes (Gumbo, Burnetta's), not verified for this one.",
  "Live status: the client defines it and wiki lists the dish, but no current-sale evidence was found. Retirement unknown.",
  "Starnut Sundae recipe source is unresolved in Chef.md (item 10), so the same gap applies to this sibling recipe."
 ]}
