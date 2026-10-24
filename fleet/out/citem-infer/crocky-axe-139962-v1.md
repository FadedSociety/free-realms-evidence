<!-- fleet job=citem-infer id=crocky-axe-139962-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[19589, 11777, 10, 2557] model=claude-haiku-5-5 -->
# Rocky Axe

{"item": {"name": "Rocky Axe", "locale_id": 139962, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 207 (vendor not named in the store row; source_tags L1, L2, L4, R2, T633, R1)", "where": null, "price": "811 coins (member price 729 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 48212 (also reference/weapons.json client_items id 48212, cost 811)"},
  {"type": "other", "detail": "Trade only, per wiki (Blue Text weapon); no vendor or quest named", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Rocky_Axe"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Level 5 Warrior weapon, Power 3, Blue Text weapon, Sweeping Slash 853 dmg, Spinning Attack 1548 dmg; only acquired through trade; in Retired Weapons category", "source": "https://freerealms.fandom.com/wiki/Rocky_Axe"},
  {"claim": "Client name locale 139962 'Rocky Axe'; sits in the Rocky/Gravel weapon set (locale 139957-139967) with Rocky Bow, Rocky Kendama Hammer, Rocky Scalpel, Rocky Blade, Rocky Wand", "source": "locale:139962"},
  {"claim": "Store row: item 48212 category 207, purchase 811 coins, member 729 coins, sell 81 coins; same block of items 48191-48213 all priced identically", "source": "repo:data/content/stores.json item 48212"},
  {"claim": "Wiki Blue Text weapon page lists [Rocky] Axe in the Rocky set alongside Rocky Bow, Kendama Hammer, Scalpel, Blade, Wand", "source": "https://freerealms.fandom.com/wiki/Blue_Text_weapon"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says trade-only, but the store data lists a 811-coin coin-store price for item 48212. Treated as a coin vendor source per the rule, but the vendor NPC/shop for store category 207 is not named in the repo row, so the vendor identity and location are unresolved.",
  "Store price 811 coins is from repo store data, not a wiki-cited price; no wiki or article price was found to confirm or give a sale price.",
  "Dates of store availability and retirement are not given in any source; retired status is taken from the wiki's Retired Weapons category only.",
  "Wiki gives no price for trade; trade partner/mechanism is not documented.",
  "Client description is empty; no images or video frames found for this item beyond wiki file names (File:Rocky Axe item.jpg, File:Rocky Axe held.jpg, not transcribed)."
 ]}
