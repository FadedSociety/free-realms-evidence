<!-- fleet job=citem-infer id=cpet-dog-small-floppy-darkmark-gray-75059-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[11808, 9562, 8, 2015] model=claude-haiku-5-5 -->
# Pet: Dog: Small Floppy: darkmark-gray

{"item": {"name": "Pet: Dog: Small Floppy: darkmark-gray", "locale_id": 75059, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Coin store entry with no named vendor, NPC, or store id. Price row only; the stores.json record has no price_provenance and no vendor link, unlike the reconstructed SC siblings. Placement unknown.", "where": null, "price": "540 coins (member price 486 coins; sell price 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6786 (item_id 23909); client coin_store_prices 540"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name locale 75059 is 'Pet: Dog: Small Floppy: darkmark-gray', one of the Small Floppy dog color variants (locale 75054-75064), all using model dog_small_floppy.adr.", "source": "locale:75059; client cluster locale:75054 to 75064; lookup client results for locale:75055-75059"},
  {"claim": "stores.json has a coin purchase row for item 23909: 540 coins, 10% member discount, member 486, sell 54, not no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6786"},
  {"claim": "Items 23902, 23906, 23912 and 23913 have coin cost cleared and carry reconstructed SC prices (400 SC, 225 SC, 225 SC, 225 SC) with price_provenance stating no coin vendor stocks them. Those are not 23909's rows, and 23909 has no such provenance, so its 540-coin row is unexplained rather than confirmed as an SC item.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6779, 6783, 6789, 6790"},
  {"claim": "No wiki page, image, article fact, video frame, quest reward, drop, or other answer names this color variant. A search of the repo finds no other reference to item 23909.", "source": "lookup wiki/articles/video/client 'Small Floppy dog pet darkmark'; repo search for '23909|Floppy'"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor not identified: the only sale evidence is the stores.json price row. No store or NPC id lists item 23909, so the vendor type is a price-row claim only. Do not place it at a vendor until a store listing is found.",
  "Mixed sourcing in the set: 23902, 23906, 23912, 23913 were reconstructed as SC Marketplace items with coin cost cleared (wiki pages Summer, Barkley, Taz, Pavel, which the stores data cites). 23909 has the plain 540-coin row. Whether 23909 is a coin item or an SC item is unresolved; the set needs a store-level check.",
  "No wiki page or video frame covers this variant, so sale dates and retirement are unverified. Retired: null.",
  "Critique 2 asked for a wireable flag. The output schema has no such field; the wireable status is effectively 'partially': price is recorded, placement is unknown.",
  "Critique 1 (type 'vendor' without a vendor): kept as type 'vendor' because the rules treat a coin store price as vendor-sale evidence, but detail and where are null and the open note above flags it."
 ]}
