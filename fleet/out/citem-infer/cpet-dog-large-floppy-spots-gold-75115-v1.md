<!-- fleet job=citem-infer id=cpet-dog-large-floppy-spots-gold-75115-v1 status=done turns=7 usd=0.0065 tokens(read,write,in,out)=[78584, 27149, 16, 4543] model=claude-haiku-5-5 -->
# Pet: Dog: Large Floppy: spots-gold

{"item": {"name": "Pet: Dog: Large Floppy: spots-gold", "locale_id": 75115, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Legacy coin store (CoinStoreItems row for item 23965; the 540-coin price is the coin store price in the client definition)", "where": "coin store (Legacy CoinStoreItems)", "price": "540 coins (member price 486 coins, 10% member discount; resale 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23965 (line 6842, purchase_price_coins 540, member_price_coins 486, sell_price_coins 54, source_tags L1/L2/L4/R2/T633/R1)"},
  {"type": "vendor", "detail": "Cragara, the Mysterious Merchant: the Floppy-dog species (Peccadillo, item 23964, same model dog_large_floppy.adr, texture alias 'spots') is sold there; wiki says the species is purchased from Cragara. Whether the spots-gold tint is sold by Cragara is not confirmed", "where": "Mysterious Merchant (Cragara)", "price": "399 Station Cash (member 359) per pets.json wiki record for the species; the wiki image shows 400 with a second price 360 or 250 that is not clearly tied to this tint", "currency": "station_cash", "source": "wiki page 'Pets' (Peccadillo row: 'Purchased from Cragara, the Mysterious Merchant'); wiki page 'Peccadillo' category Mysterious Merchant; repo:prototype/osfr-tools/data/content/pets.json line 18220-18245"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 75115 is 'Pet: Dog: Large Floppy: spots-gold', a dog_large_floppy.adr pet variant (one of 11 Dog pet names in the 75110-75120 cluster)", "source": "locale:75115"},
  {"claim": "Item 23965 is a Legacy coin store row priced 540 coins, member 486, resale 54, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23965"},
  {"claim": "The base Floppy-dog species Peccadillo (item 23964, texture 'spots', model dog_large_floppy.adr) is in the Pets list as purchased from Cragara, the Mysterious Merchant", "source": "wiki page 'Pets'; wiki page 'Peccadillo' (Category:Mysterious Merchant); repo:notes/Research/Pets Service.md line 155"},
  {"claim": "Sibling tint items 23925-23928, 23932-23945 etc. in the same Legacy coin block also sell for 540 coins, so the 540-coin Legacy store block covers this pet family", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6800-6834"},
  {"claim": "Peccadillo's Valentine's promo bundle (Doggy Cardboard Bot Outfit) is tied to item 23964, not to 23965", "source": "locale:3675; articles fact:pet articleId=2521"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page or article names 'spots-gold' specifically; the wiki covers only the base Peccadillo species, so the tint-to-sale mapping is inferred.",
  "The 540-coin Legacy coin store price is the only item-specific price; no vendor NPC in the repo is confirmed to stock item 23965, so the coin vendor is unnamed.",
  "Cragara's Station Cash price (399 SC, 359 member, per pets.json) and the 400 vs 360/250 figures on the wiki image are not reconciled; the 250 figure appears next to a different pet (Rascal).",
  "Whether the Legacy coin sale was retired is not documented in the pack; live status is unsure.",
  "Other Floppy tints (spots-brown, spots-rusty, spots-charcoal, spots-tan, darkmark-*) share the same 540 coin price block but were not individually verified."
 ]}
