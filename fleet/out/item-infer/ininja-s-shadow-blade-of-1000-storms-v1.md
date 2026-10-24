<!-- fleet job=item-infer id=ininja-s-shadow-blade-of-1000-storms-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[12562, 11569, 8, 4015] model=claude-haiku-5-5 -->
# Ninja's Shadow Blade of 1000 Storms

{"item": {"name": "Ninja's Shadow Blade of 1000 Storms", "locale_id": 131995, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop, Ninja Level 16 weapon (Power 5)", "where": "Coin Shop", "price": "2152", "currency": "coins", "source": "wiki page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms (rev 32888): categories 'Coin Shop', 'Coin Shop Weapons'; wiki coins field 2152. Page prose says it sells for a price but the figure is blank in the text."},
  {"type": "vendor", "detail": "Crouching Tiger (Chunin Ninja set vendor; sells Shadow Blades of Deception, Mysticism, Solar Flare, 1000 Storms, Dragonstrike)", "where": "Briarwood (repo npc_content_file briarwood.json)", "price": "2152 (member price 1936; sell-back 1076)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:9585-9590 (item 75111, citing wiki page https://freerealms.fandom.com/wiki/Crouching_Tiger rev 2013-09-16, section Sells)"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel at Snowy Canyon (Battle Item Mystery Pack also listed on that page)", "where": "Snowy Canyon", "price": "117 coins per wheel spin (the spin cost, not the item price)", "currency": "coins", "source": "wiki page Snowy Canyon (page:ns0) lists 'Ninja's Shadow Blade of 1000 Storms' on the Ninja Prize Wheel; the item page text also says it comes from the prize wheels at Snowy Canyon"},
  {"type": "prize_wheel", "detail": "Wraiths of Wrath! prize wheel", "where": "Wraiths of Wrath!", "price": null, "currency": null, "source": "wiki page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms (text: 'prize wheels at Snowy Canyon and Wraiths of Wrath!'; category 'Prize Wheel Weapons'). No wheel price or wheel page checked."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale 131995, \"Ninja's Shadow Blade of 1000 Storms\"", "source": "locale:131995"},
  {"claim": "Level 16 Ninja weapon, Power 5, Lightning Strike 2372 dmg and 1000 Storms 8302 dmg", "source": "wiki page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"claim": "Coin Shop price 2152 coins", "source": "wiki page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms (coins field, category Coin Shop Weapons)"},
  {"claim": "Sold by Crouching Tiger for 2152 coins (member 1936), part of the Chunin Ninja set added 27 Aug 2013", "source": "repo:prototype/osfr-tools/data/content/vendors.json:9515 and :9585-9590"},
  {"claim": "Dropped from Ninja Prize Wheel at Snowy Canyon (117-coin spin)", "source": "wiki page Snowy Canyon (lookup page:ns0)"},
  {"claim": "Prize wheel at Wraiths of Wrath!", "source": "wiki page https://freerealms.fandom.com/wiki/Ninja's_Shadow_Blade_of_1000_Storms"},
  {"claim": "Resell value 215 (not a source; sell-back figure only)", "source": "wiki image item_tooltip for Ninja's Shadow Blade of 1000 Storms"}
 ],
 "confidence": 0.6,
 "open": [
  "Crouching Tiger price 2152 comes from repo stores.json reference price, not a captured NPC quote (price_basis in vendors.json:9550). Treat as reference until verified in-game.",
  "The wiki item page gives the Coin Shop price only as a coins field; the prose price is blank. Confirm 2152 against a dated Coin Shop capture.",
  "Wraiths of Wrath! prize wheel is only in the wiki prose; no wheel page or spin cost was checked.",
  "Wiki category 'Marketplace Items' is present but no Station Cash price is given, so no marketplace source is listed. Confirm whether it was ever sold on the SC Marketplace.",
  "Do not confuse with 'Ninja's Blade of 1000 Storms' (Danger Peaks, 70-coin wheel) or 'Ninja's Jagged Scythe / Scythe of 1000 Storms', which are different items.",
  "No retirement evidence in the pack. Retired status and later availability are unknown; live status is unsure."
 ]}
