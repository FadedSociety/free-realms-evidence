<!-- fleet job=citem-infer id=cinvisibility-food-i-36365-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[5804, 11409, 6, 1633] model=claude-haiku-5-5 -->
# Invisibility Food I

{"item": {"name": "Invisibility Food I", "locale_id": 36365, "kind": "consumable"},
 "sources": [
  {"type": "other", "detail": "Unidentified coin store row (price only). The row names no vendor, shop or NPC; category_id 4 is shared by about 35 other food rows in the block, so it is not a vendor id. Vendor unknown.", "where": null, "price": "40 coins purchase (member price 36 coins, 10% member discount; sell-back 4 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11914 (item 36365)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Invisibility Food I' is locale 36365, type item, description 'Eating this food will temporarily turn the player invisible.', definition id 2998, class 9, slot 0, no models.", "source": "locale:36365"},
  {"claim": "stores.json has a coin purchase row for item 36365: category 4, purchase 40 coins, member 36, sell 4. The pack's claim that coin_store_prices was empty is wrong; this row exists.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11914"},
  {"claim": "Items 36366, 36367 and 36368 (Invisibility Food II, III, IV) have the same 40/36/4 category 4 rows. Item 36369 (Invisibility Food V) was outside the lines read, so its row is unverified.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11915-11917"},
  {"claim": "Grow Food I (36360) through Grow Food IV (36363) and 36364 share the same 40/36/4 row. The client types Grow Food II-V as quest_reward; Invisibility Food I-V are typed item. The shared tag set (L1, L2, L4, R2, T633, R1) is identical across the whole block, so it is not per-item sale evidence.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11909-11917; locale:36360-36369"},
  {"claim": "Lookup for 'Invisibility Food' returns only the five client name lines (36365-36369). No wiki page, article or video names the item.", "source": "lookup: client locale:36365-36369"}
 ],
 "confidence": 0.2,
 "open": [
  "Vendor unknown. The only sale evidence is one stores.json price row with no shop or NPC id, so the 'vendor' type from the earlier answer is not supported and is recorded here as 'other'.",
  "No wiki, article or video confirms that Invisibility Food I can be bought, won, or dropped. Live status is unsure and retirement is unknown, not confirmed.",
  "Whether the item is a quest reward (as Grow Food II-V are typed) or a store item is not established.",
  "Item 36369 (Invisibility Food V) was not checked in stores.json; its row is at or near line 11918 and was not in the read window (11880-11925 shows 36439 next).",
  "Effect duration and any link to the Chef food job were not checked."
 ]}
