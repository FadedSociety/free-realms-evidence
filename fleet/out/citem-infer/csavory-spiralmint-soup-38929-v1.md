<!-- fleet job=citem-infer id=csavory-spiralmint-soup-38929-v1 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[19619, 19768, 8, 3117] model=claude-haiku-5-5 -->
# Savory Spiralmint Soup

{"item": {"name": "Savory Spiralmint Soup", "locale_id": 38929, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef cooking recipe (recipe id 34, chef job profile 45, min rank 1, cooking minigame type 9). Ingredients: 3 Bundle of Spiralmint (def 2877), 3 Bundle of Bumbleberry (def 2889), 3 Bundle of Gummyfruit (def 2875), 3 Broth (def 2899); output 1 Savory Spiralmint Soup (def 21834). Learned from recipe pattern item 'Savory Spiralmint Soup Recipe' (def 844; locale 1511, locale 1538 'This recipe teaches you how to create Savory Spiralmint Soup.').", "where": "Chef cooking table (any Chef trainer's cooking table; trainer not confirmed)", "price": null, "currency": null, "source": "wiki Chef (list entry '[Savory] [Spiralmint] [Soup] - Makes player smaller'); wiki List of Recipes (Chef) (ingredient row, oldid=45318); repo:prototype/osfr-tools/data/content/recipes.json:2212-2243 (key chef.savory_spiralmint_soup); locale:1538; locale:1511"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item definition 21834 is named 'Savory Spiralmint Soup' with description 'Eating this food will make you smaller.' (consumable-type class 9).", "source": "locale:38929; client definition in pack"},
  {"claim": "Chef recipe list on the wiki includes Savory Spiralmint Soup with effect 'Makes player smaller'.", "source": "wiki Chef"},
  {"claim": "Chef recipe needs 3 each of Spiralmint, Bumbleberry, Gummyfruit and 1 Broth-type set; recipe pattern def 844 min rank 1, output def 21834.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:2212-2243; wiki List of Recipes (Chef)"},
  {"claim": "Recipe pattern item 'Savory Spiralmint Soup Recipe' exists in client (def 844).", "source": "locale:1511; repo:prototype/osfr-tools/data/content/recipes.json:2284 (legacy ClientItemDefinitions)"},
  {"claim": "Cooking minigame quest text 'Cook up some Savory Spiralmint Soup!' with time limits (finish in 40s/32s, add ingredients in 5s, smash bumbleberry in 4s) exists in client, showing the cooking minigame's objectives for this dish.", "source": "locale:102322, locale:102323, locale:102324, locale:102325, locale:102326"},
  {"claim": "An NPC line asks how the player's Savory Spiralmint Soup is coming and offers Broth from the NPC's cooking ingredients; a quest 'Cook 3 servings of Spiralmint Soup' exists.", "source": "locale:67606015; locale:157276871 (both in client en_us_data)"}
 ],
 "confidence": 0.6,
 "open": [
  "Source of the recipe pattern item 'Savory Spiralmint Soup Recipe' (def 844) is not evidenced: which Chef trainer or vendor sells/teaches it, and its price, are unknown. Only the cooking table crafting path is confirmed; no coin-store price exists in stores.json for def 21834 or 844.",
  "The 'Mimic: Cooking Savory Spiralmint Soup [Placeholder] [Temp Recipe]' quest (locale 47537, 78363) is flagged placeholder/temp; not counted as a live quest reward.",
  "Ingredient counts (3 each, Broth x3) come from the wiki's List of Recipes (Chef) oldid=45318; the wiki ingredient row for Broth may be a different quantity; not re-verified against a live page.",
  "NPC who sells Broth and asks about the soup (locale:67606015) is not identified; the NPC is not confirmed as a vendor of the soup itself.",
  "Retirement status and any later removal are unknown; no source says the soup was retired.",
  "Output quantity 1 is a default, not a wiki statement.",
  "Lab cooking quest 'Cook 3 servings of Spiralmint Soup' (locale:157276871) is a quest objective, not confirmed as a reward source.",
  "No video frames, article facts, or Coin Shop/SC Marketplace entries found for this item."
 ]}
