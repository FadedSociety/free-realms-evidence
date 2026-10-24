<!-- fleet job=item-infer id=imedic-s-flair-shard-of-ice-v2 status=done turns=5 usd=0.0030 tokens(read,write,in,out)=[31373, 11433, 12, 2540] model=claude-haiku-5-5 -->
# Medic's Flair Shard of Ice

{"item": {"name": "Medic's Flair Shard of Ice", "locale_id": 131104, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the Medic's Flair Shard of Ice (level 1 Medic flair shard; Coin Flair / Flair Shard category)", "where": "Coin Shop", "price": "750 coins (wiki coin field, rev 32684; undated; rendered page body reads 'sells for .')", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Medic's_Flair_Shard_of_Ice (rev 32684, categories Coin Shop / Coin Flair / Flair Shard / Marketplace Items); corroborated by wiki Category:Coin Flair, 'list of flair shards currently sold in the Coin Shop'"},
  {"type": "vendor", "detail": "Shephard, Medic merchant (sells exclusively Medic job items), listed in Sells section as Medic's Flair Shard of Ice", "where": "Medic Job Center, Sanctuary", "price": "750 coins (repo reference price, stores.json; not a captured NPC quote); member price 675 coins; sell price 375 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Shephard (Sells section, wiki revision 2025-06-08); repo:prototype/osfr-tools/data/content/vendors.json:24774-24815 (item_id 75360, npc_id 9500000533 per vendors.json:24406 and npcs/sanctuary.json:53790)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client English name is \"Medic's Flair Shard of Ice\"", "source": "locale:131104"},
  {"claim": "Wiki page describes a level 1 Medic flair shard acquired from the Coin Shop; coin field 750", "source": "https://freerealms.fandom.com/wiki/Medic's_Flair_Shard_of_Ice (rev 32684)"},
  {"claim": "Wiki Category:Coin Flair lists flair shards currently sold in the Coin Shop, and sibling Coin Shop flair shard pages use the same 'acquired from the Coin Shop' wording", "source": "wiki Category:Coin Flair; wiki Warrior's Flair Shard of Valentines, Ninja's Flair Shard of Discipline"},
  {"claim": "Shephard is a Medic Job Center merchant in Sanctuary who sells only Medic job items; the repo vendor record lists Medic's Flair Shard of Ice in his stock with 750 coin purchase, 675 member, 375 sell reference prices", "source": "https://freerealms.fandom.com/wiki/Shephard; repo:prototype/osfr-tools/data/content/vendors.json:24774-24815"},
  {"claim": "No Station Cash price exists in the pack; the 'Marketplace Items' category is not a price source", "source": "wiki rev 32684 (station_cash empty)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 750 Coin Shop price is single-source (wiki coin field / {{Coin|750}} in rev 32684) and the rendered body is blank ('sells for .'); undated. Verify against a dated Coin Shop listing.",
  "The Shephard vendor price of 750 is a repo stores.json reference price marked '(R)', not a captured NPC quote; the wiki Shephard snippet retrieved in the lookup was truncated before the Ice line, so the stock row rests on the repo record citing the wiki Sells section (rev 2025-06-08). Re-check the live Shephard sell list.",
  "The earlier answer's claim that no repo vendor stocks this item was wrong; vendors.json item 75360 lists it under Shephard.",
  "Retirement status not found in the pack; live is unsure. The Coin Shop sale is undated, so it may be historic.",
  "Pages with broken file links category on the item page was not checked for rendering; irrelevant to sources but unverified."
 ]}
