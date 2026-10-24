<!-- fleet job=citem-infer id=celite-pink-bone-wand-13902-v2 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5153, 6323, 6, 1604] model=claude-haiku-5-5 -->
# Elite Pink Bone Wand

{"item": {"name": "Elite Pink Bone Wand", "locale_id": 13902, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin store vendor (stores.json lists definition 7215 with no vendor id; no vendor name resolved in repo or wiki)", "where": null, "price": "928 coins (member price 835 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7215 (line 1947: purchase_price_coins 928, member_price_coins 835, sell_price_coins 92, category_id 207, source_tags L1,L2,L4,R2,T633,R1)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Elite Pink Bone Wand', locale 13902, definition_id 7215, weapon slot 7, class 10, model wand_ar_ag_weapon_bone.adr", "source": "locale:13902"},
  {"claim": "Coin store price row for item 7215 at 928 coins, member price 835 coins, sell price 92 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1947"},
  {"claim": "Lookup of the client text and wiki finds no wiki page naming the Elite Pink Bone Wand; only the client locale string exists for 13902", "source": "lookup: locale:13902; wiki Items page (no Elite Pink entry)"},
  {"claim": "Sibling Elite Black Bone Wand (definition 7216) has an identical store row (928/835) in stores.json, so the pair is likely priced together; this is an inference from identical rows, not from a cited pack", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1948"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor not identified: stores.json has no vendor field for item 7215, and vendor_stock in the pack is empty. The 'vendor' type reflects only a coin-store price row.",
  "The citation to quest-lines/citem-packs.json 'celite-black-bone-wand-13903' was removed: no such entry was found for 13903 or 13902 in the repo.",
  "Retired status unknown: no dated source (wiki, article or forum) covers this item.",
  "Live status unsure: the store row and source tags suggest it was sold, but no dated source confirms availability.",
  "The 928-coin price matches many unrelated items, so it is a suggestive match only.",
  "Decorative Bone Wand (wiki, Lost Treasures Month 2013) and Ceremonial Bone Wand are related wands but do not name the Elite Pink wand; they are context only and are not sources."
 ]}
