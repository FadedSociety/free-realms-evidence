<!-- fleet job=citem-infer id=ckitty-metal-collar-89058-v3 status=nothing_found turns=2 usd=0.0022 tokens(read,write,in,out)=[6393, 10131, 6, 1781] model=claude-haiku-5-5 -->
# Kitty Metal Collar

{"item": {"name": "Kitty Metal Collar", "locale_id": 89058, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Kitty Metal Collar' is locale 89058 with no description, slot 6, item class 61, model pet_cat_<descriptor>_shoulders_singleornament.adr, 36 definitions (ids 29711-29722 listed in the pack).", "source": "locale:89058"},
  {"claim": "stores.json has a category 6 row for item 29711 at purchase_price_coins 270, member 243, sell 27, with tags L1,L2,L4,R2,T633,R1. The rows 29699-29717 I checked carry identical values and tags, so this looks like a uniform Cost-derived batch rather than a per-item price. The row names no NPC or shop.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 10876-10894 (item 29711 at line 10888)"},
  {"claim": "The Coin Shop note defines R1 as 'unknown or defaulted values', says the Cost-as-regular-price mapping has not been checked against a real client transaction, and says member price and sell price are arithmetic from the purchase price.", "source": "notes/Research/Coin Shop.md:33-34, 36-38"},
  {"claim": "Lookup of 'Kitty Metal Collar' across client, wiki, articles and video returns only the client locale line 89058. No wiki page, article fact, or video frame names the item.", "source": "lookup (client, wiki, articles, video)"},
  {"claim": "The pet-collar vendor in our notes (Brent, Pet Adoption Center, Sanctuary) sells differently named Kitty collars (Kitty pirate collar, Kitty leather collar), not this item.", "source": "notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:86; repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:8893"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced acquisition source. The only link is the stores.json category 6 row for 29711 (270 coins), which is R1-tagged, shares its values with a block of neighbouring rows, and names no vendor. It is not counted as a source, and it is not a confirmed price. A real vendor, wiki price or transaction is needed.",
  "Vendor unknown. Brent sells differently named collars, so he cannot be cited.",
  "Definitions 29712-29722 and the other 24 of the 36 definitions were not checked against stores.json or any other source.",
  "Retirement status is unknown. No source covers it either way.",
  "No quest reward, enemy drop, event, prize wheel, crafting, collection, membership or promotion source was found.",
  "Kind is clothing from slot 6 and the cat shoulder model. It could be a pet accessory instead.",
  "Critique fixes applied: the 270-coin row is no longer presented as a vendor sale; the 36-definition count is stated with only 12 ids listed; live is unsure; wireable is false until a source is evidenced."
 ]}
