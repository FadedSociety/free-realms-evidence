<!-- fleet job=citem-infer id=cslugmud-18617-v1 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[18633, 18614, 8, 3103] model=claude-haiku-5-5 -->
# Slugmud

{"item": {"name": "Slugmud", "locale_id": 18617, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Gathered by the player from rocks near Glerga's camp during the Chef quest 'Cooking: Slugmud Surprise' (quest asks for ten Slugmuds, then cook a Slugmud Surprise). Not an enemy drop, not a vendor sale.", "where": "Snowhill area Chef quest camp (Glerga's camp; exact zone not confirmed in the pack)", "price": null, "currency": null, "source": "locale:24246; repo: locale id 118949734 text 'look under the rocks near the camp for the Slugmud' (opening-native-lobby en_us_data.dat:3128)"},
  {"type": "other", "detail": "Ingredient for the Chef recipe Slugmud Surprise (recipe 41, needs 3 Slugmud). Crafting uses this item; it is not sold for it.", "where": "Chef cooking", "price": null, "currency": null, "source": "wiki: List of Recipes (Chef) [Slugmud] Surprise; repo:prototype/osfr-tools/data/content/recipes.json:2601-2628"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 18617 is 'Slugmud'; description says it is usable in recipes; it is a 'can be added to a collection' item.", "source": "locale:18617; locale:24229"},
  {"claim": "Client definition 2893 is named 'Slugmud' and is the ingredient for the Slugmud Surprise recipe.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2613 and :2681 (legacy ClientItemDefinitions comment 'Slugmud')"},
  {"claim": "Slugmud Surprise recipe uses Slugmud x3, Bundle of Chugaroot x3, Bundle of Choychoy x3, Broth x4; Chef job rank 5.", "source": "wiki: List of Recipes (Chef); wiki: Chef; repo:prototype/osfr-tools/data/content/recipes.json:2601-2632"},
  {"claim": "Cooking quest text tells the player to find ten Slugmuds by looking under rocks near the camp, then cook a Slugmud Surprise.", "source": "locale:24246; locale:102357 (quest objective 'Cook up some Slugmud Surprise!')"},
  {"claim": "Slugmud Skipper (a fish, locale 99924, definition separate) is a different item from Slugmud; fishing sources belong to the skipper, not to this item.", "source": "repo:prototype/osfr-tools/data/content/fishing.json:292; wiki: Sacred Grove Shallows"},
  {"claim": "Vendor 'Slugmud Surprise Recipe' (Gaston-area chef vendor stock, price unknown) is the recipe pattern, not Slugmud itself.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:17749; wiki: Gaston"},
  {"claim": "No coin store price, no wiki page for Slugmud itself, and no vendor stocks Slugmud.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no def 2893); lookup wiki returned no Slugmud article"}
 ],
 "confidence": 0.5,
 "open": [
  "Jev's first pass guessed 'drop'; the evidence says it is a rock-gathered quest ingredient, not an enemy drop. Treated as 'other'.",
  "Client also lists definition 10013 for this name; not checked. It may be a tinted or duplicate variant, and its sources were not verified.",
  "Exact zone of Glerga's camp and the rocks is not confirmed. Source pack places the quest in Snowhill; the locale text only says 'near the camp'.",
  "Whether rock-gathered Slugmud still spawns in the live game, and whether it can be bought or is a recurring quest pickup, is not confirmed by a wiki page. 'live: yes' rests on the wiki chef recipe list and the quest text, not a dated source.",
  "Quest-gathered count and respawn rules are unknown."
 ]}
