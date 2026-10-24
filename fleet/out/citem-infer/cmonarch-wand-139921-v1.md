<!-- fleet job=citem-infer id=cmonarch-wand-139921-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[3774, 7380, 6, 1829] model=claude-haiku-5-5 -->
# Monarch Wand

{"item": {"name": "Monarch Wand", "locale_id": 139921, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only; the wiki says it 'can only be acquired through trade' (not a vendor, quest, or drop source)", "where": null, "price": null, "currency": null, "source": "wiki page: Monarch Wand"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Monarch Wand is a level 1 Wizard weapon, Blue Text weapon, acquirable only through trade", "source": "wiki page: Monarch Wand"},
  {"claim": "Wiki page is in Category:Retired Weapons, so the item is retired", "source": "wiki page: Monarch Wand (categories)"},
  {"claim": "Client name string for item 48171 is 'Monarch Wand'; it sits in a 'Monarch' set with Monarch Bow, Log Hammer, Scalpel, Blade, Club (locale 139916-139920)", "source": "locale:139921"},
  {"claim": "Item tooltip shows Power 5, Required Level 1 Wizard, Resell Value 64, Zap (279 dmg) and Lightning Blast (1143 dmg)", "source": "image:item_tooltip Monarch Wand item.jpg"},
  {"claim": "Client definition carries a coin store price of 640; repo stores.json has rows with purchase_price_coins 640 / member 576 / sell 64, matching the tooltip resell value 64", "source": "repo:prototype/osfr-tools/data/content/stores.json (e.g. item 4113, category 207)"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store price 640 is in the client definition but the definition id 48171 does not appear in stores.json, so the specific coin-vendor row (and vendor name/zone) is unidentified. The 640 price cannot be tied to this item by id; it may not be a real vendor sale. Not listed as a vendor source.",
  "The first-pass tag 'vendor' is unsupported: no vendor_stock entries, no wiki vendor/Coin Shop/SC Marketplace category. Rejected.",
  "No date for when trade-only status ended or when the item was retired; no source for the trade mechanic beyond the wiki sentence.",
  "Wiki page has no price; the tooltip Resell Value 64 is a sell price, not a purchase price."
 ]}
