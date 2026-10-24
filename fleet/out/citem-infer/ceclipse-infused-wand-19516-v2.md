<!-- fleet job=citem-infer id=ceclipse-infused-wand-19516-v2 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[22886, 13465, 10, 3015] model=claude-haiku-5-5 -->
# Eclipse Infused Wand

{"item": {"name": "Eclipse Infused Wand", "locale_id": 19516, "kind": "weapon"},
 "sources": [
  {"type": "crafting", "detail": "Blacksmith recipe 'Eclipse Infused Wand Recipe' (locale 384393); the recipe text says it teaches the wand and requires Blacksmith level 10 (locale 384392). Ingredients not in repo (recipes_unresolved.json, candidate pattern item 49385, unconfirmed).", "where": null, "price": null, "currency": null, "source": "locale:384393; locale:384392; wiki page Eclipse Infused Wand (Blacksmith recipe); wiki page Blacksmith (Recipes list)"},
  {"type": "vendor", "detail": "Masa (Blacksmith NPC) sells the 'Eclipse Infused Wand Recipe' (the recipe, not the wand). Price not recorded.", "where": "Lakeshore", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/vendors.json line 20480 (item_name 'Eclipse Infused Wand Recipe'); repo:prototype/osfr-tools/data/content/npcs/lakeshore.json line 8773; wiki page Masa"},
  {"type": "coin_shop", "detail": "Coin store sale of the wand, item 38659 (tint group 1; siblings 38663, 38665 share the price). Store category 207; the row names no NPC, so the selling vendor is unidentified.", "where": null, "price": "1069 coins (member price 962 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12393 (item_id 38659); client definition coin_store_prices 1069"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item name is locale 19516 'Eclipse Infused Wand'; locale 4419903 carries the same text (duplicate name entry)", "source": "locale:19516; locale:4419903"},
  {"claim": "Wand is a level 8 Wizard weapon, Green Text, acquirable via the Blacksmith recipe; Zap 1492 and Lightning Blast 6107 damage", "source": "wiki page Eclipse Infused Wand"},
  {"claim": "Recipe teaches creation of the wand and requires Blacksmith level 10", "source": "locale:384392"},
  {"claim": "Quest title 'Forging: Eclipse Infused Wand' exists, but nothing in the pack shows it grants the recipe or wand; not listed as a source", "source": "locale:386113"},
  {"claim": "Masa's stock includes the Eclipse Infused Wand Recipe; added 6 Aug 2013 per the repo's stock note; wiki Masa trivia gives the Aug 6, 2013 introduction date", "source": "repo:prototype/osfr-tools/data/content/vendors.json line 20469 and 20480; wiki page Masa (Trivia)"},
  {"claim": "Coin store row: item 38659 category 207, tint group 1, purchase 1069 coins, member 962 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12393"},
  {"claim": "Wiki lists the wand under Green Text weapons and the Blacksmith recipe list; wiki says it 'can still' be acquired", "source": "wiki page Green Text weapon; wiki page Blacksmith"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor for item 38659 at 1069 coins is unidentified: stores.json category 207 has no NPC name, and no vendor record (vendors.json, lakeshore.json) lists item 38659 or the wand itself. Verify the NPC before publishing a placed vendor.",
  "Recipe ingredients and counts are not in the repo; crafting is confirmed only as the recipe's existence and rank 10 requirement.",
  "Quest 'Forging: Eclipse Infused Wand' (locale 386113) is not a confirmed source; its reward is unverified.",
  "Masa's recipe price is unknown.",
  "Retired status unknown: no source gives a withdrawal date for the coin sale or the recipe. Wiki wording 'can still acquired' is undated.",
  "Previous answer's 'added 6 Aug 2013' came from repo stock notes plus the wiki Masa trivia; this is consistent across sources."
 ]}
