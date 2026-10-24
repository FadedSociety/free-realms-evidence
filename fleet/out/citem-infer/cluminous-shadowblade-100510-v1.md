<!-- fleet job=citem-infer id=cluminous-shadowblade-100510-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[8366, 8248, 8, 2384] model=claude-haiku-5-5 -->
# Luminous Shadowblade

{"item": {"name": "Luminous Shadowblade", "locale_id": 100510, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 207 (unnamed vendor in our data; the row for definition 48135 is priced 2204 coins, member price 1983)", "where": null, "price": "2204", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13191 (item_id 48135, purchase_price_coins 2204); client coin_store_prices [2204]"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki (Blue Text weapon); not a vendor, quest, or drop source", "where": null, "price": null, "currency": null, "source": "wiki: Luminous Shadowblade (\"can only be acquired through trade\"); wiki: Blue Text weapon (same trade wording for the whole Luminous set)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client item name is locale 100510 'Luminous Shadowblade', part of the Luminous weapon set (100511-100515: Wand, Axe, Hammer, Bow, Shockrod); two definitions (29931, 48135); slot 7; class 6; model sword_ar_ag_weapon_shadowblade.adr", "source": "locale:100510; client definition"},
  {"claim": "Level 16 Ninja weapon, Blue Text, acquired only through trade; Dragonstrike 10674 damage, Flame Flash 2372 damage", "source": "wiki: Luminous Shadowblade"},
  {"claim": "Wiki categories Retired Weapons, Blue Text Weapons, Level 16 Weapons", "source": "wiki: Luminous Shadowblade (category tags)"},
  {"claim": "Store row for definition 48135 exists at 2204 coins (member 1983), sell 220, in category 207 with the same tags as many other rows at 2204", "source": "repo:prototype/osfr-tools/data/content/stores.json:13191"},
  {"claim": "Sister Luminous weapons also listed as trade-only, level 16 Warrior/Archer/Wizard/Medic/Brawler", "source": "wiki: Luminous Axe, Luminous Bow, Luminous Wand, Luminous Shockrod, Luminous Hammer"}
 ],
 "confidence": 0.5,
 "open": [
  "CONFLICT: stores.json lists definition 48135 at 2204 coins in category 207, but the wiki says the item is trade-only. The store row may be a stale or unrelated entry; the category 207 price is shared by many rows, so it may not be specific to this weapon. Needs a check against a 2009-2014 coin-store snapshot before it is listed as a live vendor sale.",
  "Vendor name and zone for category 207 not identified in the repo data; the vendor field is left as unnamed.",
  "The jev first-pass tag said live=yes, source_guess=vendor. The wiki's Retired Weapons category and trade-only text contradict the live and vendor guess, so the tag was not used.",
  "No quest, drop, or event source found. Wiki images (File:Luminous Shadowblade item.jpg, held.jpg) were listed but not read.",
  "Price 2204 coins is from the store data only; no wiki price is given."
 ]}
