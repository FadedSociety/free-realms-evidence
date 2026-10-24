<!-- fleet job=citem-infer id=cn-medic-s-bonesaw-of-vitamins-pl-medic-s-bonesaw-of-vitamins-131954-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[21581, 11034, 10, 3273] model=claude-haiku-5-5 -->
# {n}Medic's Bonesaw of Vitamins{pl="Medic's Bonesaw of Vitamins"}

{"item": {"name": "Medic's Bonesaw of Vitamins", "locale_id": 131954, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Kimble (Medic trainer set vendor, sells Medic's Bonesaw of Vitamins)", "where": "Stillwater Crossing", "price": "1055 coins (member price 949 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json (Kimble entry, item_id 75070, purchase_price_coins 1055, member_price_coins 949); wiki Kimble 'Sells' section https://freerealms.fandom.com/wiki/Kimble (lists 'Medic's Bonesaw of Vitamins'). Price is the stores.json reference price, not a captured NPC quote."},
  {"type": "coin_shop", "detail": "Coin Shop sale of the Bonesaw (store category 207)", "where": "Coin Shop", "price": "1055 coins (member price 949 coins; resell 105 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75070 (category_id 207, purchase_price_coins 1055); wiki page 'Medic's Bonesaw of Vitamins' says it is acquired from the Coin Shop (its price field is blank in the wiki text)"},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel (Battle Item Mystery Pack, Emergency Medic Boots and other Medic rewards)", "where": "Misty Mountain, Seaside Swoopers, Snatching Snappers!, The Mushroom Gigas! (dungeon prize wheels)", "price": null, "currency": null, "source": "wiki page 'Medic's Bonesaw of Vitamins' (acquired from prize wheels at Misty Mountain, Seaside Swoopers); wiki pages 'Seaside Swoopers', 'Snatching Snappers!', 'The Mushroom Gigas!' list 'Medic Prize Wheel' contents including Medic's Bonesaw of Vitamins"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 131954 is 'Medic's Bonesaw of Vitamins', a level 8 Medic weapon (slot 7, class 7, model sword_ar_ag_weapon_bonesaw.adr); one definition, no variant tints in the pack", "source": "locale:131954; client definition 75070"},
  {"claim": "Sold by Kimble at Stillwater Crossing for 1055 coins (949 with membership), resell 105", "source": "repo:prototype/osfr-tools/data/content/vendors.json Kimble entry item 75070; wiki Kimble Sells section"},
  {"claim": "Coin Shop item, category 207, purchase 1055 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75070"},
  {"claim": "Also a prize-wheel item at Misty Mountain and Seaside Swoopers; Medic wheel appears in Snatching Snappers and Mushroom Gigas pages", "source": "wiki page 'Medic's Bonesaw of Vitamins'; wiki 'Seaside Swoopers', 'Snatching Snappers!', 'The Mushroom Gigas!'"},
  {"claim": "Wiki tooltip image shows Required: Level 8, Medic; Power 3; Resell Value 105", "source": "wiki image 'Medic's Bonesaw of Vitamins item.jpg'"},
  {"claim": "Item is in the Medic set with Shock, Alarm, Triage, Vitals, Immunization bonesaws (adjacent locale ids 131949-131959), which sit together in the client text", "source": "locale:131949-131959"}
 ],
 "confidence": 0.7,
 "open": [
  "Wiki price for the Coin Shop sale is blank; the 1055 figure comes from the repo store data, not a wiki quote. Check the live Coin Shop price.",
  "Kimble's 1055 coin price is a stores.json reference price, not a captured NPC quote; the Kimble listing and the Coin Shop listing may be the same sale and should not be counted twice.",
  "Prize-wheel odds and the exact wheel tier were not captured; no price for the wheel.",
  "No evidence found of retirement or removal; retired left null. Live status 'yes' rests on the Kimble listing and the Coin Shop store row.",
  "No video frames, article facts, or quest/crafting/collection sources found for this item."
 ]}
