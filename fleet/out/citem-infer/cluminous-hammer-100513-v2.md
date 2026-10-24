<!-- fleet job=citem-infer id=cluminous-hammer-100513-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5660, 11248, 6, 1991] model=claude-haiku-5-5 -->
# Luminous Hammer

{"item": {"name": "Luminous Hammer", "locale_id": 100513, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin store listing, stores.json category 207 (vendor/NPC and store name not recorded in our data). Unconfirmed: the same 2204-coin tier is shared by many category-207 item ids (48113-48134 block and others), so this row may be a generic price tier rather than a sale of this hammer.", "where": null, "price": "2204 coins (member price 1983 coins; sell price 220 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48120 (line 13176); client definition coin_store_prices 2204"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 100513 'Luminous Hammer', item type; part of the Luminous set with Shadowblade, Wand, Axe, Bow, Shockrod (locale 100510-100515).", "source": "locale:100513; locale:100510-100515"},
  {"claim": "Wiki: [Luminous] [Hammer] is a level 16 Brawler Blue Text weapon that 'can only be acquired through trade'; Glancing Blow 2372 damage, Leg Sweep 8302 damage; page is in Category:Retired Weapons.", "source": "wiki page 'Luminous Hammer'"},
  {"claim": "Wiki 'Blue Text weapon' page lists [Luminous] [Hammer] with the rest of the Luminous set.", "source": "wiki page 'Blue Text weapon'"},
  {"claim": "Store data lists item 48120 at 2204 coins (member 1983, sell 220), but the identical row is shared by many other category-207 items, so it is weak evidence of a real sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 13176 and lines 13169-13186"},
  {"claim": "Client has two definition ids (29934, 48120) for the hammer; only 48120 has a store price.", "source": "client definition (definition_ids 29934, 48120)"}
 ],
 "confidence": 0.35,
 "open": [
  "Conflict: the wiki says the hammer can only be obtained through player trade and is in Retired Weapons, while the store row prices item 48120 at 2204 coins. The store row names no vendor, store name, or date, and is one of many identical 2204 rows, so the coin-store source is listed only as an unconfirmed price. Needs confirmation of what category 207 is and whether item 48120 was ever stocked.",
  "'Can only be acquired through trade' (player-to-player) is not a listed source type and is not recorded as a source. It is the wiki's only acquisition statement.",
  "No vendor, quest reward, enemy drop, event, prize wheel, crafting, collection, membership, or promotion source was found in the pack, the wiki, or the articles. No Coin Shop or SC Marketplace category is listed for this item on the wiki.",
  "Definition id 29934 has no store price and no known source.",
  "Wiki images (File:Luminous Hammer held.jpg, File:Luminous Hammer item.jpg) carry no transcribed acquisition text. No article facts or video frames mention the item.",
  "Locale 100508 (Graawwrrrr!), 100516 (bogwart) and 100518 (toads) are unrelated gag/quest lines and were not used as evidence.",
  "Critique fixes applied: source typed as an unidentified coin store listing with no vendor name; wiki trade-only statement stated alongside it; store row described as a generic price tier; live kept 'unsure' and retired true."
 ]}
