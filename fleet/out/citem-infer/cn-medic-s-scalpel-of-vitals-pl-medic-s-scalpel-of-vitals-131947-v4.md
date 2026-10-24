<!-- fleet job=citem-infer id=cn-medic-s-scalpel-of-vitals-pl-medic-s-scalpel-of-vitals-131947-v4 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[21177, 13964, 8, 3142] model=claude-haiku-5-5 -->
# {n}Medic's Scalpel of Vitals{pl="Medic's Scalpel of Vitals"}

{"item": {"name": "Medic's Scalpel of Vitals", "locale_id": 131947, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale, Medic level 5 weapon (definition 75063). The wiki sentence names the Coin Shop but its price is blank. The 850-coin figure (member 765) is a repo stores.json reference price, not a captured quote.", "where": "Coin Shop", "price": "850 coins (member 765) reference price, unverified", "currency": "coins", "source": "wiki page \"Medic's Scalpel of Vitals\" (freerealms-wiki/wikitext/3970-42725-b4f480078845.wiki line 1, sale sentence with price blank); repo:prototype/osfr-tools/data/content/stores.json:15079 (item 75063, purchase_price_coins 850, member_price_coins 765, category 207)"},
  {"type": "vendor", "detail": "Gaius (Pixie Medic merchant, sells only Medic items), Sells list", "where": "Seaside, near the Information Center (seaside.json, npc 9500000585)", "price": null, "currency": null, "source": "wiki page \"Gaius\" (freerealms-wiki/wikitext/10726-31699-bf0371ace165.wiki lines 11 and 24). repo:prototype/osfr-tools/data/content/vendors.json:25588-25596 gives 850/765/sell 85, but its price_basis says it is copied from the stores.json reference price, so it is not independent price evidence."},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Danger Peaks dungeon", "where": "Danger Peaks", "price": null, "currency": null, "source": "wiki page \"Medic's Scalpel of Vitals\" (item sentence lists Danger Peaks); wiki page \"Danger Peaks\""},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Ice Troll Scout! dungeon", "where": "Ice Troll Scout!", "price": null, "currency": null, "source": "wiki page \"Medic's Scalpel of Vitals\"; wiki page \"Ice Troll Scout!\""},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Pixie Hunters! dungeon", "where": "Pixie Hunters!", "price": null, "currency": null, "source": "wiki page \"Medic's Scalpel of Vitals\" (item sentence lists Pixie Hunters!). The Pixie Hunters! page lookup shows a [Medic] [Prize] [Wheel] heading but the excerpt does not list the scalpel, so this is unconfirmed on the dungeon page."},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Sweetwater Climb dungeon", "where": "Sweetwater Climb", "price": null, "currency": null, "source": "wiki page \"Medic's Scalpel of Vitals\"; wiki page \"Sweetwater Climb\""},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Thugawug Sneak! dungeon", "where": "Thugawug Sneak!", "price": null, "currency": null, "source": "wiki page \"Thugawug Sneak!\" (Medic Prize Wheel list includes Medic's Scalpel of Vitals, per prior pack); repo thugawug_sneak.json:1519 is name-only and not used"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131947 is \"Medic's Scalpel of Vitals\", slot 7, class 20, definition 75063", "source": "locale:131947"},
  {"claim": "Wiki page says it is a level 5 Medic weapon acquired from the Coin Shop (sale price blank in the wiki text) and from prize wheels at Danger Peaks, Ice Troll Scout!, Pixie Hunters! and Sweetwater Climb", "source": "wiki page \"Medic's Scalpel of Vitals\" (freerealms-wiki/wikitext/3970-42725-b4f480078845.wiki line 1)"},
  {"claim": "Store row for item 75063: purchase 850, member 765, sell 85, category 207", "source": "repo:prototype/osfr-tools/data/content/stores.json:15079"},
  {"claim": "Gaius Sells list includes Medic's Scalpel of Vitals; vendors.json price is copied from the stores.json reference price, with no captured NPC quote", "source": "wiki page \"Gaius\" (10726-31699-bf0371ace165.wiki lines 11, 24); repo:prototype/osfr-tools/data/content/vendors.json:25588-25596"},
  {"claim": "Medic's Forged Scalpel of Vitals is a separate crafted item and is not merged here", "source": "locale:442473"},
  {"claim": "Sibling items locale 131942-131952 are separate items", "source": "locale:131942 through locale:131952"}
 ],
 "confidence": 0.6,
 "open": [
  "The 850 coin price is a stores.json reference price (vendors.json price_basis: no captured retail quote). The wiki sale sentence has the price blank, so no captured Coin Shop price exists. Member 765 is repo-only.",
  "Coin Shop and Gaius may be the same coin sale recorded twice. Gaius is kept as a vendor source with price null so it is not counted as a second price source.",
  "Wheel spin costs are not established, so prize wheel prices are null.",
  "Pixie Hunters! wheel listing rests on the item page sentence. The dungeon page excerpt did not show the scalpel.",
  "Thugawug Sneak! wheel rests on the prior pack's report of the wiki Thugawug page, not re-checked here.",
  "No retirement or end-of-sale source found, and no current-sale source found either, so retired is null and live is unsure."
 ]}
