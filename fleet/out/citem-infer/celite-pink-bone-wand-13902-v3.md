<!-- fleet job=citem-infer id=celite-pink-bone-wand-13902-v3 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5949, 9467, 6, 1698] model=claude-haiku-5-5 -->
# Elite Pink Bone Wand

{"item": {"name": "Elite Pink Bone Wand", "locale_id": 13902, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Coin-store price row only (definition 7215). No vendor id, vendor name or stock entry is resolved in the repo, and the wiki has no entry for it. Re-typed from 'vendor' per critiques.", "where": null, "price": "928 coins (member price 835 coins, 10% member discount; sell price 92 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7215 (line 1947: category_id 207, purchase_price_coins 928, member_price_coins 835, sell_price_coins 92, source_tags L1,L2,L4,R2,T633,R1)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Elite Pink Bone Wand', locale 13902, definition_id 7215, weapon slot 7, class 10, model wand_ar_ag_weapon_bone.adr", "source": "locale:13902"},
  {"claim": "Coin store price row for item 7215 exists at 928 coins, member price 835, sell price 92 (verified in this pass)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1947"},
  {"claim": "The source_tags set L1,L2,L4,R2,T633,R1 is shared by many unrelated store rows (e.g. items 27215, 7176, 7180, 7210), so it does not identify a shop", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1947, 9721"},
  {"claim": "Wiki search finds no page or entry naming the Elite Pink Bone Wand; the Items page has no Elite Pink entry, and the client text exists only as locale 13902", "source": "lookup: locale:13902; wiki page Items"},
  {"claim": "Sibling Elite Black Bone Wand (locale 13903, definition 7216) has an identical 928/835 store row, so the pairing is an inference from identical rows only, not a cited pack", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1948"},
  {"claim": "Decorative Bone Wand (Lost Treasures Month 2013, Hunting Treasure) is a related wand but does not name the Elite Pink wand; context only, not a source", "source": "wiki Decorative Bone Wand (as cited in pack)"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor not identified: stores.json has no vendor field for item 7215 and vendor_stock is empty. Category 207 is not named in the repo as a vendor.",
  "The citem-packs.json 'celite-black-bone-wand-13903' citation was dropped: no such entry was found.",
  "Retired status unknown: no dated source (wiki, article or forum) covers this item.",
  "Live status unsure: availability rests only on the undated stores.json row.",
  "The 928-coin price matches many unrelated items, so it is a suggestive match only.",
  "Acquisition method (which shop or event sells it) is unresolved; the Elite Pink wand is not on any wiki page or video frame in the pack."
 ]}
