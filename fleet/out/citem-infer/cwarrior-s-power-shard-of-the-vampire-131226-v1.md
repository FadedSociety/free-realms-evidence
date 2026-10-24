<!-- fleet job=citem-infer id=cwarrior-s-power-shard-of-the-vampire-131226-v1 status=done turns=6 usd=0.0056 tokens(read,write,in,out)=[59901, 22925, 14, 4178] model=claude-haiku-5-5 -->
# Warrior's Power Shard of the Vampire

{"item": {"name": "Warrior's Power Shard of the Vampire", "locale_id": 131226, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (coin vendor stock; purchase price 270 coins, member price 243 coins, sell-back 27 coins; store category 103, tint group 2)", "where": "coin store data (stores.json); vendor/shop not named in the repo row", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 5876 (item_id 2435); client definition coin_store_prices [2435]. Caveat: see open."},
  {"type": "prize_wheel", "detail": "Warrior prize wheel, Mushroom Mania (dungeon) reward wheel; one of six items on the Warrior wheel", "where": "Mushroom Mania (dungeon)", "price": "Wheel spin cost 77 coins (the wheel's price, not this item's)", "currency": "coins", "source": "wiki page 'Mushroom Mania!' (Warrior [Prize] [Wheel] lists \"[Warrior]'s [Power] [Shard] of the Vampire\"); repo:notes/Build Guides/Content/Dungeons/Mushroom Mania.md line 68"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is \"Warrior's Power Shard of the Vampire\" at locale 131226, in the same Power Shard cluster (131221-131231) as other Warrior shards.", "source": "locale:131226; client cluster locale:131221-131231"},
  {"claim": "Our coin store data carries a sale row for item 2435: 270 coins purchase, 243 coins member price (10% member discount), 27 coins sell price.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 5876"},
  {"claim": "The Warrior prize wheel of Mushroom Mania lists Warrior's Power Shard of the Vampire, alongside Warrior's Power Shard of Vitality V, Warrior's Necklace of Vitality V and a Battle Item Mystery Pack; the wheel costs 77 coins.", "source": "wiki page 'Mushroom Mania!'; repo:notes/Build Guides/Content/Dungeons/Mushroom Mania.md lines 55, 62-68"},
  {"claim": "Each combat job has its own wheel in Mushroom Mania; the Vampire shard is on the Archer, Brawler, Medic, Ninja, Warrior and Wizard wheels, so it is a six-job wheel item.", "source": "repo:notes/Build Guides/Content/Dungeons/Mushroom Mania.md lines 64-69"},
  {"claim": "Client has the name as a dungeon target in the Mushroom Mania data.", "source": "repo:prototype/osfr-tools/data/content/dungeons_unresolved.json line 17107 (target_name \"Warrior's Power Shard of the Vampire\")"}
 ],
 "confidence": 0.55,
 "open": [
  "Store id mismatch: the client definition id is 75482 but the coin price row is keyed item_id 2435 in stores.json. The pack maps 2435 to this item; I could not confirm 2435 is the same item id rather than another item. Verify before trusting the 270-coin price.",
  "Coin shop vendor name, zone and sale dates are not in the evidence. The store row has no vendor name, and no wiki page names the shop.",
  "Retirement and current availability are unknown. Neither the store row nor the wiki gives an end date, so live is 'unsure'.",
  "The wiki Mushroom Mania wheel entry does not say if the wheel is a repeatable or event-only reward; the dungeon's own schedule is not confirmed.",
  "Wiki spin cost 77 coins is the wheel's cost per spin, not this item's value."
 ]}
