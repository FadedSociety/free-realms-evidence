<!-- fleet job=citem-infer id=cn-stopping-power-medic-fatigues-pl-stopping-power-medic-fati-133144-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5860, 6677, 6, 1605] model=claude-haiku-5-5 -->
# {n}Stopping Power Medic Fatigues{pl="Stopping Power Medic Fatigues"}

{"item": {"name": "Stopping Power Medic Fatigues", "locale_id": 133144, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "Medic Prize Wheel reward (wheel list on the Dark Spore Depths page, alongside Wound Ballistic [Medic] [Fatigues] and the Medic shards/rings)", "where": "Dark Spore Depths (Medic Prize Wheel)", "price": null, "currency": null, "source": "wiki: Dark Spore Depths (Medic Prize Wheel list naming [Stopping] [Power] [Medic] [Fatigues])"},
  {"type": "vendor", "detail": "Coin store sale, store category 104; listed for item 76136 (tint group 1) and item 900011 (tint group 2). Vendor NPC/shop name not identified in repo data.", "where": null, "price": "1500 coins (member price 1350 coins, 10% member discount; sell price 150 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76136 (line 15840) and item 900011 (line 17213)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale 133144 'Stopping Power Medic Fatigues', part of the Stopping Power Medic set (Helmet 133143, Jacket 133140, Boots 133141, Gloves 133142, Backpack 133145) and Wound Ballistic Medic Backpack 133139.", "source": "locale:133144; locale:133139-133145"},
  {"claim": "The wiki Medic Prize Wheel list on the Dark Spore Depths page names '[Stopping] [Power] [Medic] [Fatigues]' as a prize wheel item.", "source": "wiki: Dark Spore Depths (Medic Prize Wheel)"},
  {"claim": "Store data lists item 76136 and item 900011 (two tint variants) in category 104 at 1500 coins purchase, 1350 member price, 150 sell price, not no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76136 (line 15840); item 900011 (line 17213)"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin store vendor/shop for category 104 is not identified in the repo; the sale is evidenced by store data only, so the NPC and location are open.",
  "Forest Troll Fort was removed as a source: its reward list names the Stopping Power Medic Helmet and Energy Transfer Medic Jacket, not the Fatigues.",
  "Live status and retirement date are not confirmed by any wiki or article source; the store entry suggests it was on sale at export time.",
  "The Prize Wheel source is a wiki list entry without a stated price or drop rate; the pack's Thugawug Sneak! and Treasure of the Bone Shaman! citations do not name the Fatigues and were dropped.",
  "The 'coin_shop' first-pass tag is only a hint; the store price is the hard source for the coin sale."
 ]}
