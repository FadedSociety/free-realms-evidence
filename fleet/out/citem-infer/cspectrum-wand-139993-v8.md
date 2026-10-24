<!-- fleet job=citem-infer id=cspectrum-wand-139993-v8 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6800, 11222, 6, 2162] model=claude-haiku-5-5 -->
# Spectrum Wand

{"item": {"name": "Spectrum Wand", "locale_id": 139993, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only (wiki: 'can only be acquired through trade')", "where": null, "price": null, "currency": null, "source": "wiki page Spectrum Wand (ns0): 'It is a Blue Text weapon and can only be acquired through trade.'"},
  {"type": "coin_shop", "detail": "Unnamed coin store listing. Item 48243 is one of 24 identical category-207 rows (48220-48243) all at 1431 coins, so this looks like a generic tier price, not a Spectrum-specific listing. No vendor, shop or date is named.", "where": null, "price": "1431 coins (member price 1287 coins, 10% member discount; sell 143)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48243 (line 13292; block 13269-13292 at 48220-48243); client coin_store_prices [1431] for definition 48243"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Spectrum Wand is a level 13 Wizard Blue Text weapon; acquirable only through trade per the wiki.", "source": "wiki page Spectrum Wand (ns0)"},
  {"claim": "Item tooltip shows Power 5, Required Level 13 Wizard, Resell Value 143.", "source": "image:item_tooltip Spectrum Wand item.jpg"},
  {"claim": "Wiki page is in Category:Retired Weapons and Category:Blue Text Weapons. No retirement date is in the pack.", "source": "wiki page Spectrum Wand category list"},
  {"claim": "Store row 48243 is 1431 coins, member 1287, sell 143, no_sale false, but it shares an identical value and source-tag block with items 48220-48243 (the 48217-48219 rows are 811), so the price is a tier price, not evidence of a named vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13269-13292"},
  {"claim": "Client name locale 139993 'Spectrum Wand' is in the Spectrum set cluster with Bow, Anvil, Bonesaw, Scythe, Hammer (139988-139992).", "source": "locale:139993; locale:139988-139992"},
  {"claim": "The Blue Text weapon table excerpt reads '[Spectrum] [Wand] 5 3' and the column order is ambiguous, so it is not used for level or power. Level 13 and Power 5 come from the page and tooltip.", "source": "wiki page Blue Text weapon (ns0) excerpt; image:item_tooltip"}
 ],
 "confidence": 0.35,
 "open": [
  "Coin price: the 1431-coin row is a shared tier price (48220-48243, 24 items at the same price). No vendor, Coin Shop listing or sale date is named, so it is not a confirmed sale of this item. It conflicts with the wiki's trade-only statement and with 'retired'. Before wiring it as a vendor sale, find the vendor or the dated listing.",
  "Retirement: 'retired: true' rests only on Category:Retired Weapons. No dated source. If the coin row is live, retirement is in doubt.",
  "Live status is unresolved: the coin row and the trade-only statement disagree. Set to unsure, not no.",
  "The wiki's claim that Blue Text weapons dropped from unnamed dungeon bosses is not in the pack. No drop source is listed.",
  "No zone, NPC, quest, event, crafting, collection, prize-wheel or promotion source found.",
  "Wireable only as a trade-only item with no price. The coin row can be stored as an unverified tier price, not as a vendor sale."
 ]}
