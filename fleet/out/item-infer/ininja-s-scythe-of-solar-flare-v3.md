<!-- fleet job=item-infer id=ininja-s-scythe-of-solar-flare-v3 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[48070, 16326, 12, 4031] model=claude-haiku-5-5 -->
# Ninja's Scythe of Solar Flare

{"item": {"name": "Ninja's Scythe of Solar Flare", "locale_id": 131985, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 8 Ninja weapon (Power 3). Single-sourced from the wiki coins field; page text price is blank.", "where": "Coin Shop", "price": "1055 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (rev 32887; coins field; categories 'Coin Shop', 'Coin Shop Weapons'); not confirmed against a client vendor table"},
  {"type": "vendor", "detail": "Dizzy Toad (Pixie NPC merchant), Nusumi Ninja job set, stock 'Scythes of Solar Flare'; wiki 'Sells' list dated 2013-10-03 with stock note 'Added 27 Aug 2013'", "where": "Perry's Pastures, south of Snowhill", "price": "1055 coins (reference price from stores.json, not a captured NPC quote; member price 949, sell-back 527)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:33063 and :33173 (item_id 75101, name_id 131985, purchase_price_coins 1055); repo:prototype/osfr-tools/data/content/npcs/snowhill.json:11678; https://freerealms.fandom.com/wiki/Dizzy_Toad (Sells)"},
  {"type": "prize_wheel", "detail": "Prize wheel, Ninja job slot", "where": "Bone Bog Cemetery", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (category 'Prize Wheel Weapons'); repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:82 ('Prize wheel by job', Ninja row); repo:prototype/osfr-tools/data/content/dungeons/bone_bog_cemetery.json:1697 (same entry, under Rewards > Prize wheel by job > Ninja). Wheel cost and odds not stated."},
  {"type": "prize_wheel", "detail": "Prize wheel at Thugawug Bandits!", "where": "Thugawug Bandits!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text; category 'Prize Wheel Weapons'). Wheel cost and odds not stated."},
  {"type": "prize_wheel", "detail": "Prize wheel at Venemous Frogs!", "where": "Venemous Frogs!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text; category 'Prize Wheel Weapons'). Wheel cost and odds not stated."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client string id 131985", "source": "locale:131985"},
  {"claim": "Level 8 Ninja weapon, Power 3; abilities Ashen Strike (853 dmg) and Flaming Uppercut (2716 dmg)", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text and tooltip image)"},
  {"claim": "Sold in the Coin Shop, 1055 coins (wiki coins field only)", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (rev 32887)"},
  {"claim": "Dizzy Toad stocks 'Scythes of Solar Flare' in the Nusumi Ninja set; the stock row maps to item_id 75101 / name_id 131985 and lists purchase 1055 coins as a stores.json reference, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:33063, :33173-:33178; repo:prototype/osfr-tools/data/content/npcs/snowhill.json:11678; https://freerealms.fandom.com/wiki/Dizzy_Toad"},
  {"claim": "Bone Bog Cemetery Ninja prize wheel includes this scythe", "source": "repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:82; repo:prototype/osfr-tools/data/content/dungeons/bone_bog_cemetery.json:1697"},
  {"claim": "Resell value 105 (tooltip)", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (tooltip image)"},
  {"claim": "Ninja's Jagged Scythe of Solar Flare (locale:131991) and Ninja's Shadow Blade of Solar Flare are different items and are not used as sources here", "source": "locale:131991; repo:prototype/osfr-tools/data/content/vendors.json:6410, :9627"}
 ],
 "confidence": 0.7,
 "open": [
  "Live status unconfirmed. No retirement note in the evidence; the Dizzy Toad stock snapshot is from 2013-10-03 and the Coin Shop listing is from the wiki coins field. Verify against a current client vendor table or live listing before wiring as live.",
  "The 1055-coin price appears in two places (wiki Coin Shop coins field and the Dizzy Toad stores.json reference price), but neither is a captured in-game quote. Treat as reference, not confirmed.",
  "Dizzy Toad: the vendors.json price is a stores.json reference, so the NPC's actual price is unverified. Member price 949 and sell-back 527 are reference values only.",
  "Prize wheels (Bone Bog Cemetery, Thugawug Bandits!, Venemous Frogs!): no wheel cost or odds in evidence. Correction to the critique: the Bone Bog entry is the Ninja prize-wheel row, not a Battle Item Mystery Pack reward; the Ninja mystery pack row was not separately evidenced for this scythe.",
  "No Station Cash marketplace source: the page has 'Marketplace Items' but no 'SC Marketplace' category and no station_cash price."
 ]}
