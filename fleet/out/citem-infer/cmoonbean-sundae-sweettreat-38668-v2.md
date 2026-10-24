<!-- fleet job=citem-infer id=cmoonbean-sundae-sweettreat-38668-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6686, 10424, 6, 2200] model=claude-haiku-5-5 -->
# Moonbean Sundae Sweettreat

{"item": {"name": "Moonbean Sundae Sweettreat", "locale_id": 38668, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef cooking recipe 'chef.moonbean_sundae_sweettreat' (recipe_id 56, Chef job profile 45, min rank 1, minigame type 9). Ingredients: Moonbean x3 (def 2878), Stainberry x3 (def 2887), Sugar x8 (def 2906), Snowhill Ice Cream: Chocolate x3 (def 2895). Output: 1x Moonbean Sundae Sweettreat (def 21830). Recipe pattern item 55828 ('Moonbean Sundae Sweettreat Recipe', locale:387775) is required; how a player obtains that pattern is not sourced.", "where": "Chef cooking station", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:1568-1600 (key chef.moonbean_sundae_sweettreat; output def 21830 at line 1598; pattern 55828 at line 1573); wiki 'List of Recipes (Chef)' (Ingredients line lists Moonbean x3, Stainberry x3, Sugar x8, Snowhill Ice Cream); wiki 'Chef' page ('[Moonbean] [Sundae] [Sweettreat] - Increases Energy')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 21830 is named Moonbean Sundae Sweettreat (locale 38668), description 'Eating this food temporarily increases your energy'; no coin store price.", "source": "locale:38668"},
  {"claim": "Repo Chef recipe produces def 21830 from the listed ingredients, gated by recipe pattern 55828.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:1568-1600"},
  {"claim": "Wiki Chef list gives the dish effect 'Increases Energy'.", "source": "wiki 'Chef'; wiki 'List of Recipes (Chef)'"},
  {"claim": "Live cooking quest text exists: quest title 'Cook Moonbean Sundae Sweettreat' and objective 'Primary: Cook up some Moonbean Sundae Sweettreat!'.", "source": "locale:140409; locale:77938"},
  {"claim": "A second cooking objective 'Mix up a Moonbean Sundae Sweettreat!' exists.", "source": "locale:102432"},
  {"claim": "Chef NPC dialog asks the player to bring one sample of this dish (a request, not a source).", "source": "locale:384674; locale:384675; locale:384450"},
  {"claim": "Recipe pattern client name 'Moonbean Sundae Sweettreat Recipe' (def 55828).", "source": "locale:387775; repo recipes.json:1573"},
  {"claim": "Placeholder quest title locale:47671 is rejected: flagged placeholder, not used as evidence.", "source": "locale:47671 (FLAG placeholder)"}
 ],
 "confidence": 0.6,
 "open": [
  "Recipe pattern 55828 (locale:387775): no wiki, vendor, quest or drop source found; the 'Where to find' field on the wiki is blank. The cooking source depends on an unverified unlock, so the acquisition path is incomplete.",
  "Fourth ingredient conflict: repo recipes.json (def 2895 x3) and the wiki 'List of Recipes (Chef)' Moonbean Mousse entry say 'Snowhill Ice Cream: Chocolate x3'. The critique reports the wiki Sundae entry reads 'Snowhill Ice Cream: Vanilla x3'; my lookup excerpt truncated that line ('Snowhill..') so I could not confirm the flavour. Left unresolved; the repo value is used.",
  "Output quantity 1 comes from the repo recipe, not a wiki statement.",
  "Live status 'unsure': sources date from the wiki and repo reconstruction; no current-game check. Retirement not stated by any source.",
  "No coin vendor, Station Cash, Coin Shop, drop or prize wheel source for the finished food was found."
 ]}
