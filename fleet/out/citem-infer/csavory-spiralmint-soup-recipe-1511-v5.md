<!-- fleet job=citem-infer id=csavory-spiralmint-soup-recipe-1511-v5 status=done turns=3 usd=0.0040 tokens(read,write,in,out)=[20586, 19992, 8, 2571] model=claude-haiku-5-5 -->
# Savory Spiralmint Soup Recipe

{"item": {"name": "Savory Spiralmint Soup Recipe", "locale_id": 1511, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Bordon Cloo (Chef recipe seller, Royal Chef, Cloo's Cooking Academy); sells the Savory Spiralmint Soup recipe (client definition 844)", "where": "Sanctuary", "price": null, "currency": null, "source": "locale:414272 ('Bordon Cloo has them for sale if you don't have them yet... You'll want to buy the Savory Spiralmint Soup recipe'); locale:414285 ('purchase these recipes from him'); repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:8217 (Recipes: Gummyfruit Gumbo, Savory Spiralmint Soup, Burnetta's Curious Creation, 'can be purchased from Bordon Cloo'); repo:prototype/osfr-tools/data/content/recipes.json:2212-2216 (chef.savory_spiralmint_soup, recipe_item_definition_id 844)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 844 is 'Savory Spiralmint Soup Recipe' (locale 1511), in the client cluster with the other Chef recipes (locale 1510-1516). Its description is 'This recipe teaches you how to create Savory Spiralmint Soup.' (locale 1538).", "source": "locale:1511; locale:1538; repo:prototype/osfr-tools/data/content/recipes.json:2212-2216"},
  {"claim": "Quest text tells the player that Bordon Cloo has the recipe for sale and that they should buy it. No price is given in the text.", "source": "locale:414272; locale:414285; locale:414274"},
  {"claim": "The Chef quest-line text tells the player to cook the soup for Bordon Cloo or Oxalis/Simone. These errands consume the recipe; they do not grant it.", "source": "locale:140109, 140112, 140118, 414297, 414304, 419228, 419325"},
  {"claim": "Wiki Sanctuary page lists Chef: Bordon Cloo as the job unlock and Merry Vale page places the Chef questline start with Bordon Cloo; the wiki has no item-specific recipe page.", "source": "wiki: Sanctuary; wiki: Merry Vale; wiki: Chef"},
  {"claim": "Generic article text: Cloo sells cooking ingredients and recipes for many dishes at his stove on the Sanctuary main street. Not item-specific.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=654 (fact:economy)"},
  {"claim": "The client definition for item 844 has no coin store price (coin_store_prices is empty), so there is no store-data price row. vendors.json stock for Bordon Cloo does not include recipe 844.", "source": "client definition for item 844; repo vendor data"},
  {"claim": "Flagged or placeholder lines (not_live Simone quest, placeholder Mimic/Temp Recipe lines) were excluded and are not cited.", "source": "locale flags (not_live, placeholder)"}
 ],
 "confidence": 0.5,
 "open": [
  "No coin or Station Cash price is verified. The 540-coin figure from video ukTXIyG6EKI frames 00006 and 00320 is not attributed: the vendor badge is unreadable, and Chef.md gives the same 540 for Gummyfruit Gumbo and Burnetta's Curious Creation. It is not used as a price. Re-check the frames for row-to-item mapping before wiring any price.",
  "Currency of the Bordon Cloo sale is unknown. It is set to null, not coins.",
  "Retired status is unknown. No dated wiki page or current in-game vendor check was found.",
  "live is 'unsure': the client definition exists and the sale text is unflagged, but no current in-game check was made.",
  "The Chef.md note citing client vendor id 3190984693 and the locale ids 2579573797 and 2645354306 could not be verified as locale ids and are not cited. The string-id questions in wilds.json:31095 were not checked.",
  "The cooked Savory Spiralmint Soup (definition 21834, locale 1538) has its own sources and is not researched here."
 ]
}
