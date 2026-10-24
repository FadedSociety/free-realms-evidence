<!-- fleet job=citem-infer id=cdrill-hammer-98097-v2 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[15453, 9381, 8, 2732] model=claude-haiku-5-5 -->
# Drill Hammer

{"item": {"name": "Drill Hammer (Brawler's Drill Hammer family: of Chucking / Pummeling / Rumbling / Sweeps / Cheapshot / Dirt Kick / Roundhouse / Slammage)", "locale_id": 98097, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store category 207, tint group 1 (item 37536). Which named variant this entry sells is not confirmed; the other 15 definitions were not individually checked.", "where": "Coin Shop (category 207)", "price": "1431 coins (member price 1287 coins, 10% discount; sell-back 143 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12273 (item_id 37536)"},
  {"type": "vendor", "detail": "Evander, Brawler Job merchant, Mire's Edge (Blackspore Swamp). Wiki Sells list names Brawler's Drill Hammer of Chucking, of Pummeling, of Rumbling and of Sweeps. No NPC price captured.", "where": "Mire's Edge, Blackspore Swamp", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Evander (Sells list, lookup snippet)"},
  {"type": "coin_shop", "detail": "Brawler's Drill Hammer of Pummeling is acquired from the Coin Shop (wiki). Price missing from the wiki snippet.", "where": "Coin Shop", "price": null, "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Drill_Hammer_of_Pummeling"},
  {"type": "prize_wheel", "detail": "Brawler's Drill Hammer of Pummeling, acquired from the prize wheels at Brugo's Fishing (wiki).", "where": "Brugo's Fishing", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Drill_Hammer_of_Pummeling"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Drill Hammer' is locale 98097; the cluster names (locale 131926-131933) are named Brawler's Drill Hammer variants.", "source": "locale:98097; locale:131926-131933"},
  {"claim": "stores.json item 37536 (category 207, tint group 1) costs 1431 coins, member 1287, sell 143.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12273"},
  {"claim": "Pummeling is a level 12 Brawler weapon, acquired from the Coin Shop and from Brugo's Fishing prize wheels (wiki text only).", "source": "https://freerealms.fandom.com/wiki/Brawler's_Drill_Hammer_of_Pummeling"},
  {"claim": "Evander's wiki Sells list includes Chucking, Pummeling, Rumbling and Sweeps Drill Hammers.", "source": "https://freerealms.fandom.com/wiki/Evander"},
  {"claim": "Tooltips for Brawler's Drill Hammer of Slammage and of Chucking show Level 12, Brawler, Power 4, Resell Value 150. These apply to those two variants only.", "source": "image:item_tooltip (Slammage and Chucking wiki tooltips)"},
  {"claim": "Video frames show Brawler's Drill Hammer of Sweeps and of Pummeling as Croaking Vale / Brawlers minigame win items and Daily Grab Bag contents.", "source": "video:H4v00arihLk/00294.jpg; video:H4v00arihLk/00060.jpg; video:vokALCeGZqY/00010.jpg"}
 ],
 "confidence": 0.4,
 "open": [
  "Variant-to-item-id mapping is unconfirmed. Item 37536 is one of 16 definitions; the 1431 price is verified for 37536 only, not for the other definitions or the named variants.",
  "The Evander 1504-coin (member 1353, sell 150) reference price for Sweeps/Rumbling (vendors.json items 75042/75043) was not re-verified in this pass. It is a stored reference value, not a captured NPC quote, so no vendor price is listed. Price conflict with 1431 is unresolved.",
  "Pummeling's coin-shop price is missing from the wiki snippet. Read the full page to get it.",
  "Stats (level 12, Power 4, resell 150) are verified by tooltip only for Slammage and Chucking. Sweeps, Rumbling and Pummeling stats are wiki-text only (level 12 Brawler weapon).",
  "Drop and minigame sources (Croaking Vale win, Brawlers minigame, Daily Grab Bag) appear only as video items seen. Not listed as sources.",
  "Retirement status is not stated by any source. Evander's wiki page was revised 2023-05-28, so these variants were still sold then. Check later retirement."
 ]}
