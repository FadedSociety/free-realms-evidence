<!-- fleet job=citem-infer id=cmedic-s-power-shard-of-the-vampire-131096-v3 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[14662, 8961, 8, 1678] model=claude-haiku-5-5 -->
# Medic's Power Shard of the Vampire

{"item": {"name": "Medic's Power Shard of the Vampire", "locale_id": 131096, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing (store item 75352, category 121). Selling NPC not identified in repo data; no vendor stock row evidenced", "where": "coin store (category 121; category name not confirmed)", "price": "2435 coins (member price 2191 coins, 10% member discount; sell price 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15269 (item_id 75352, category_id 121, purchase_price_coins 2435, member_price_coins 2191, sell_price_coins 243); matches client coin_store_prices 2435 for definition 75352"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for definition 75352 is locale:131096 \"Medic's Power Shard of the Vampire\"", "source": "locale:131096"},
  {"claim": "Store row for item 75352 is category 121, purchase 2435 coins, member 2191 (10% off), sell 243, no_sale false, no dates", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15269"},
  {"claim": "Rows 75348-75353 all carry 2435 coins with the same tag set, so price alone does not identify the item; the definition id mapping 75352 -> locale:131096 does", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 15265-15270"},
  {"claim": "Wiki page 'Mushroom Mania!' Archer Prize Wheel lists Archer's Power Shard of the Vampire. This is a sibling only; no Medic wheel entry appears in the lookup excerpt", "source": "wiki page 'Mushroom Mania!' (Archer Prize Wheel)"},
  {"claim": "Client has sibling class versions of the Power Shard of the Vampire: Archer (locale:130966), Brawler (131031), Medic (131096), Ninja (131161), Warrior (131226), Wizard (131291)", "source": "locale:130966, locale:131031, locale:131096, locale:131161, locale:131226, locale:131291"},
  {"claim": "Earlier 'vendor' label was dropped: no selling NPC is evidenced; the source is a coin-store catalogue row", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15269"}
 ],
 "confidence": 0.35,
 "open": [
  "Selling NPC or specific coin store page for store item 75352 is not identified; the coin-store type is based only on the catalogue row.",
  "No Medic Prize Wheel entry is evidenced. The Archer wheel entry on 'Mushroom Mania!' is a sibling cross-reference only and is not a Medic source. A full read of that page's wheel section is still needed.",
  "Live status and retirement are unknown: the store row has no dates and category 121 rows share one tag set and price tier, so the row does not confirm current sale.",
  "No wiki page of its own, article facts, video frames, or drop/crafting evidence found for this item. The client description is empty, so the shard's effect is not documented here."
 ]}
