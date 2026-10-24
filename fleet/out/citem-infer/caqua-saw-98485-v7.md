<!-- fleet job=citem-infer id=caqua-saw-98485-v7 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[5970, 10103, 6, 1907] model=claude-haiku-5-5 -->
# Aqua Saw

{"item": {"name": "Aqua Saw", "locale_id": 98485, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. Candidate only: the coin store row for definition 37924 in store category 207 is the sole price evidence, but no NPC or vendor is named for that category, and category 207 holds about 60 rows that share the same generic source_tags. Not confirmed as a live sale.", "where": null, "price": "1431 coins (member price 1287, 10% member discount; sell 143)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12316 (item_id 37924, category_id 207); client coin_store_prices 1431"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. No trader, trade price or date recorded.", "where": null, "price": null, "currency": null, "source": "wiki page Aqua Saw"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Aqua Saw is a level 12 Medic Blue Text weapon, Power 5, with Incision (2609 damage) and Triage effects", "source": "wiki page Aqua Saw; image:item_tooltip Aqua Saw item.jpg; locale:98485"},
  {"claim": "Wiki says Aqua Saw 'can only be acquired through trade' and lists it in Category:Retired Weapons. The retirement is undated.", "source": "wiki page Aqua Saw"},
  {"claim": "Wiki Blue Text weapon table lists [Aqua] [Saw] as the level 12 Medic entry", "source": "wiki page Blue Text weapon"},
  {"claim": "stores.json row for item 37924 in category 207: purchase 1431, member 1287, sell 143; matches client coin_store_prices 1431 and tooltip Resell Value 143", "source": "repo:prototype/osfr-tools/data/content/stores.json:12316"},
  {"claim": "Definition 37924 appears in the reference weapon data", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:1581"}
 ],
 "confidence": 0.3,
 "open": [
  "Conflict: the coin-store row (1431 coins, category 207) and the wiki's trade-only statement disagree. No vendor or NPC is named for category 207, so whether any live vendor sells Aqua Saw is unresolved. Treat the vendor entry as an unconfirmed candidate.",
  "Retirement date is unknown. Retired status rests only on the wiki's Category:Retired Weapons, which is undated.",
  "Resell value conflict: tooltip and stores.json say 143, but a critique reports reference/weapons.json:1581-1585 with resell_value 0. The file contains id 37924 at line 1581, but I did not check the resell field, so the figure stays unresolved.",
  "No drop, quest, crafting, collection, event, prize-wheel or membership source was found. No article or video evidence names the item.",
  "The wiki's Triage values ('Heals 2372 damage', 'Deals 8302 damage') are not verified."
 ]}
