<!-- fleet job=citem-infer id=cdrill-hammer-98097-v3 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[18707, 11498, 8, 3299] model=claude-haiku-5-5 -->
# Drill Hammer

{"item": {"name": "Drill Hammer (Brawler's Drill Hammer family: of Chucking / Pummeling / Rumbling / Sweeps / Slammage / Cheapshot / Dirt Kick / Roundhouse)", "locale_id": 98097, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Evander, Brawler Job merchant (pixie at campfire near Donovan Shadeweaver's home). Sells list names Brawler's Drill Hammer of Chucking, of Pummeling, of Rumbling, of Sweeps. No NPC price captured.", "where": "Mire's Edge, Blackspore Swamp", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Evander (Sells list)"},
  {"type": "coin_shop", "detail": "Coin Shop sale of one unnamed Drill Hammer tint variant (item 37536, category 207, tint group 1). The variant-to-name mapping is not confirmed; do not attach to a named variant.", "where": "Coin Shop (category 207)", "price": "1431 coins (member price 1287 coins, 10% member discount; sell-back 143 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12273 (item 37536)"},
  {"type": "coin_shop", "detail": "Brawler's Drill Hammer of Pummeling is stated as sold at the Coin Shop. Wiki price field is blank; no price captured.", "where": "Coin Shop", "price": null, "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Drill_Hammer_of_Pummeling (text: 'acquired from the Coin Shop where it sells for')"},
  {"type": "prize_wheel", "detail": "Brawler's Drill Hammer of Pummeling is stated as obtainable from prize wheels at Brugo's Fishing. Wiki text only; not cross-checked.", "where": "Brugo's Fishing", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Drill_Hammer_of_Pummeling"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Drill Hammer' is locale 98097; 16 definitions share it (sample ids 37536-37565); slot 7, class 5, model hammer_ar_ag_weapon_drill.adr.", "source": "locale:98097; client definition pack"},
  {"claim": "Pummeling variant client name exists as locale 131928 'Brawler's Drill Hammer of Pummeling'.", "source": "locale:131928"},
  {"claim": "stores.json item 37536 (category 207, tint group 1) costs 1431 coins, member 1287, sell 143. The same 1431 price also appears on items 37510, 37528, 37538, 37539, 37547, 37562, so the price does not identify a variant.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12271-12280"},
  {"claim": "Pummeling tooltip: Level 12 Brawler, Power 4, Resell Value 150, skill 'Pound'.", "source": "image:item_tooltip (File:Brawler's Drill Hammer of Pummeling item.jpg)"},
  {"claim": "Slammage and Chucking tooltips: Level 12 Brawler, Power 4, Resell Value 150.", "source": "image:item_tooltip (wiki tooltips in pack)"},
  {"claim": "Evander's wiki Sells list includes Chucking, Pummeling, Rumbling and Sweeps Drill Hammers. Evander sells exclusively Brawler job items.", "source": "https://freerealms.fandom.com/wiki/Evander"},
  {"claim": "Brawler job wiki page lists Drill Hammer variants including Sweeps and Roundhouse at level 12 range.", "source": "https://freerealms.fandom.com/wiki/Brawler"},
  {"claim": "Items seen in reward displays: Brawler's Drill Hammer of Sweeps (Croaking Vale win screen; Daily Grab Bag); Brawler's Drill Hammer of Pummeling (Sampson Idlefist Daily Grab Bag). Display only, not confirmed as a drop or prize source.", "source": "video:H4v00arihLk/00294.jpg; video:H4v00arihLk/00060.jpg; video:vokALCeGZqY/00010.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "Variant-to-item-id mapping is unconfirmed. Item 37536 is one of 16 definitions; the 1431 price is verified for 37536 only and is not attributed to Pummeling or any named variant.",
  "Evander's Sells list is wiki-only. Repo reference prices of 1504 coins (member 1353, sell 150) for items 75042 (Sweeps) and 75043 (Rumbling) in vendors.json and stores.json lines 15058-15059 conflict with the 1431 Coin Shop figure. They are unverified stored values, not captured NPC quotes, so they are not listed as prices. No price is known for Chucking or Pummeling at Evander.",
  "Pummeling's Coin Shop price is blank on the wiki page. Brugo's Fishing prize-wheel source rests on that page's text alone; the wiki prize-wheel pages cited in the pack (Frostfang Caverns, Prince of Low Tide) were not re-checked.",
  "Stats: Level 12 / Power 4 / Resell 150 are tooltip-verified for Slammage, Chucking and Pummeling. Sweeps, Rumbling and the rest are wiki-text only.",
  "Minigame and Daily Grab Bag appearances are reward displays only and are not listed as sources.",
  "Retirement is not stated by any source. The Evander wiki page was revised 2023-05-28, so the variants were likely still sold then. live is 'yes' on the basis of that revision and the video frames, but no current-status check was done. The 'No longer in-game' category in the pack is on the Ned page, not Evander's, and does not apply here."
 ],
 "critique_fixes": "Coin price now tied to item 37536 only, unnamed variant. Evander vendor price left null with reference value disclosed in open. Pummeling coin-shop and Brugo's prize-wheel left unpriced and wiki-text-sourced. Pummeling tooltip added as third verified variant. Live status stated with its basis."}
