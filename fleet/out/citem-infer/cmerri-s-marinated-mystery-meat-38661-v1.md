<!-- fleet job=citem-infer id=cmerri-s-marinated-mystery-meat-38661-v1 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[13636, 12686, 8, 2478] model=claude-haiku-5-5 -->
# Merri's Marinated Mystery Meat

{"item": {"name": "Merri's Marinated Mystery Meat", "locale_id": 38661, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Cooked at a cooking table with the Chef job, using the Merri's Marinated Mystery Meat Recipe (item 859, locale 1526). Recipe ingredients per Chef guide: Punkin x3, Spiralmint x3, Mystery Meat x3, Spice x7. Chef level 15 required (locale:1553).", "where": "Chef cooking table", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:1308 (output item definition 21823); notes/Build Guides/Content/Jobs/Chef.md:234; locale:1553"},
  {"type": "vendor", "detail": "Rachael (Chef job merchant, sells the recipe item 859 that unlocks the cooking, not the dish itself)", "where": "Blackspore Swamp, near the Blackspore Cooking Table", "price": "540 coins (reference price; member price 486 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:5875-5914 (item 859, stores.json reference price, not a captured NPC quote); wiki page Rachael (Sells section, revision 2013-10-09)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client definition: item 21823 named Merri's Marinated Mystery Meat (locale 38661), consumable, slot 0, class 9, one definition, no coin store price in stores.json.", "source": "client definition in pack; repo:prototype/osfr-tools/data/content/recipes.json:1336 and :1367"},
  {"claim": "Recipe text: 'This recipe teaches you how to create Merri's Marinated Mystery Meat. Requires chef level 15.'", "source": "locale:1553"},
  {"claim": "Rachael, Blackspore Swamp, sells the Merri's Marinated Mystery Meat Recipe (item 859) for 540 coins reference price (486 member).", "source": "repo:prototype/osfr-tools/data/content/vendors.json:5805-5914; wiki Rachael, https://freerealms.fandom.com/wiki/Rachael"},
  {"claim": "Dish is cooked in the Chef job; the Chef guide lists its ingredients and Chef level 15 gate.", "source": "notes/Build Guides/Content/Jobs/Chef.md:234"},
  {"claim": "Article names the dish as the example for Arts and Crafts Week (event context only; no drop or reward listed).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1624"},
  {"claim": "Client text: 'Cook up some of Merri's Marinated Mystery Meat!' (quest objective) and 'Cooking: Merri's Marinated Mystery Meat' (locale 386053) — a cooking quest/achievement references the dish.", "source": "locale:102397; locale:386053"}
 ],
 "confidence": 0.7,
 "open": [
  "Which quest uses locale 102397 ('Cook up some of...') is not identified; it may be a quest reward or chef-line task, not checked.",
  "Arts and Crafts Week article gives the dish as an example only; it is not confirmed as a holiday-only or event reward source.",
  "Rachael's 540-coin price is a stores.json reference price, not a captured NPC quote; the wiki page lists no price.",
  "Retirement status of the Rachael recipe sale and the cooking item is not stated in any source in the pack."
 ]}
