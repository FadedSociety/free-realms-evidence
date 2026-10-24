<!-- fleet job=citem-infer id=cgummyfruit-gumbo-38647-v3 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7781, 11155, 6, 2273] model=claude-haiku-5-5 -->
# Gummyfruit Gumbo

{"item": {"name": "Gummyfruit Gumbo", "locale_id": 38647, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked by a Chef at a cooking table from the Gummyfruit Gumbo Recipe (pattern item 845, recipe 35, Chef profile 45). Yields 1 Gummyfruit Gumbo (item 21809), effect: temporarily increases Energy. Ingredient list unresolved: recipes.json says 3 Gummyfruit, 3 Honeytwig, 3 Tumtumnip, 3 Broth; the wiki 'List of Recipes (Chef)' snippet is ambiguous.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:914 (key chef.gummyfruit_gumbo); wiki page 'Chef' (line '[Gummyfruit] [Gumbo] - Increases Energy'); wiki 'List of Recipes (Chef)' ([Gummyfruit] [Gumbo] entry, ingredients: Bundle of [Gummyfruit] x3, Bundle of Honeytwig x3, Bundle of Tumtumnip); locale:38647; locale:1539"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 38647 is named 'Gummyfruit Gumbo' with description 'Eating this food temporarily increases your energy.' (food definition 21809, class 9, no coin store row)", "source": "locale:38647; client definition in pack"},
  {"claim": "The recipe item 'Gummyfruit Gumbo Recipe' is taught by 'This recipe teaches you how to create Gummyfruit Gumbo.'", "source": "locale:1512; locale:1539"},
  {"claim": "Recipe pattern 845 is a Chef recipe (profile 45) that outputs food item 21809.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:914-1043"},
  {"claim": "Wiki Chef page lists Gummyfruit Gumbo as a Chef food with Increases Energy.", "source": "wiki page 'Chef' (lookup)"},
  {"claim": "A store-screen frame shows 'Gummyfruit Gumbo Recipe' at 540 coins, vendor and zone not visible. This is the recipe item, not the food. Single OCR'd frame.", "source": "video:ukTXIyG6EKI/00006.jpg"},
  {"claim": "repo stores.json has no row for item 21809 (food) or 845 (recipe); the coin price in the pack is not confirmed by store data.", "source": "search of repo:prototype/osfr-tools/data/content/stores.json"}
 ],
 "confidence": 0.5,
 "open": [
  "Recipe sale: 'Gummyfruit Gumbo Recipe' (item 845) shown at 540 coins in one OCR'd frame (video:ukTXIyG6EKI/00006.jpg). Vendor and zone unidentified, so it is not listed as a source for the food. Repo Chef notes attribute it to Bordon Cloo (Sanctuary) and client lines 1412043698 and 704534977 (Coin Shop) name sellers, but neither was confirmed against a store row or second frame. Needs a second frame or store data row.",
  "No coin store price for the food (21809 / 38647) in repo stores data or client definition, so no vendor sale of the food is evidenced.",
  "Ingredient list conflict between recipes.json:914 (3 Gummyfruit, 3 Honeytwig, 3 Tumtumnip, 3 Broth) and the wiki 'List of Recipes (Chef)' snippet, which is ambiguous. Not resolved.",
  "Quest step, not reward: Shrouded Glade lines (locale 389999, 390009, 390011) ask the player to cook and feed Gumbo to Aedon. No reward row found. Placeholder quest locale 47575 is excluded as evidence (flagged placeholder). No quest source recorded.",
  "Live and retirement status not established: no dated source states whether the recipe or food is still obtainable. Left as unsure with retired null.",
  "Locale 102287 'cooking_GummyfruitGumbo' is an internal key, not player-facing."
 ],
 "critique_fixes": "Evidence pack critique 1: removed placeholder quest 47575 as evidence; re-scoped 540-coin row to the recipe item 845 and out of the food's sources; live changed from 'yes' to 'unsure'. Critique 2: removed the vendor row for the food; vendor attribution to Bordon Cloo/Coin Shop moved to open; crafting row kept with ingredient conflict noted; no quest source added."
}
