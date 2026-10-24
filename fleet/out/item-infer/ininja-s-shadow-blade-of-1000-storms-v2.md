<!-- fleet job=item-infer id=ininja-s-shadow-blade-of-1000-storms-v2 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[15425, 11196, 8, 3188] model=claude-haiku-5-5 -->
# Ninja's Shadow Blade of 1000 Storms

{"item": {"name": "Ninja's Shadow Blade of 1000 Storms", "locale_id": 131995, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop, Ninja level 16 weapon (Power 5). Same figure appears in the wiki coins field; the prose price is blank.", "where": "Coin Shop", "price": "2152", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms (rev 32888; categories 'Coin Shop', 'Coin Shop Weapons'; coins field 2152). Price is weak: one wiki field, no dated capture."},
  {"type": "vendor", "detail": "Crouching Tiger, Chunin Ninja set vendor (stock: Shadow Blades of Deception, Mysticism, Solar Flare, 1000 Storms, Dragonstrike; added 27 Aug 2013)", "where": "Briarwood per repo file briarwood.json (repo label). The wiki page places her near the Bristlewood Warpstone; the zone name is unverified.", "price": "2152 coins (member 1936; sell-back 1076). Reference price from repo stores.json, not a captured NPC quote.", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Crouching_Tiger (Sells section, rev 2013-09-16, lists this item; confirmed by lookup); repo:prototype/osfr-tools/data/content/vendors.json:9512-9592 (price_basis: stores.json reference)"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel at Snowy Canyon. Listed on the wheel; not a drop. Spin cost is 117 coins per spin, not the item price.", "where": "Snowy Canyon", "price": "117 coins per spin (spin cost)", "currency": "coins", "source": "wiki page 'Snowy Canyon' (lookup confirmed: Ninja Prize Wheel lists 'Ninja's Shadow Blade of 1000 Storms', 117 Coins); item page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"type": "prize_wheel", "detail": "Wraiths of Wrath! battle prize wheel", "where": "Wraiths of Wrath!", "price": "spin cost not checked", "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms (prose: 'prize wheels at Snowy Canyon and Wraiths of Wrath!'); same wording on sibling wiki pages (Warrior's Warlord Axe of Cleaving, Medic's Shockrod of Vitals, Wizard's Ornate Wand of Glaciers)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale 131995, \"Ninja's Shadow Blade of 1000 Storms\"", "source": "locale:131995"},
  {"claim": "Level 16 Ninja weapon, Power 5, Lightning Strike 2372 dmg, 1000 Storms 8302 dmg", "source": "https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"claim": "Coin Shop price field 2152 coins; prose price blank", "source": "https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"claim": "Crouching Tiger Sells list includes this item (rev 2013-09-16)", "source": "https://freerealms.fandom.com/wiki/Crouching_Tiger; repo:prototype/osfr-tools/data/content/vendors.json:9584-9592"},
  {"claim": "Vendor price 2152 / member 1936 / sell-back 1076 is a stores.json reference, not an NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:9592; stores.json:15122"},
  {"claim": "Snowy Canyon Ninja Prize Wheel lists this item, 117 coins per spin", "source": "wiki page 'Snowy Canyon' (lookup)"},
  {"claim": "Wraiths of Wrath! prize wheel listed in item prose", "source": "https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"claim": "Resell value 215 is a sell-back figure, not a source", "source": "wiki item_tooltip image for this item"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin Shop price 2152 and Crouching Tiger price 2152 are the same figure: the wiki coins field and a stores.json reference. They are not independent confirmation. Confirm with a dated Coin Shop or NPC capture.",
  "Crouching Tiger zone: repo says briarwood.json; wiki says near the Bristlewood Warpstone. Verify the in-game zone before wiring.",
  "Wraiths of Wrath! wheel: supported only by wiki prose and sibling pages, no wheel page or spin cost checked.",
  "Wiki category 'Marketplace Items' exists but no Station Cash price is given. No marketplace source is listed. Confirm whether it was ever sold on the SC Marketplace.",
  "Not the same as 'Ninja's Blade of 1000 Storms' (Danger Peaks, 70-coin wheel) or the Scythe of 1000 Storms variants.",
  "No retirement evidence in the pack; retired status and later availability are unknown; live is unsure."
 ]}
