<!-- fleet job=citem-infer id=cadvanced-pet-conditioner-24600-v1 status=nothing_found turns=5 usd=0.0047 tokens(read,write,in,out)=[43220, 22748, 12, 2875] model=claude-haiku-5-5 -->
# Advanced Pet Conditioner

{"item": {"name": "Advanced Pet Conditioner", "locale_id": 24600, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Advanced Pet Conditioner' as locale 24600 (definition 10522, one definition, no coin store price). Description: 'This conditioner moderately improves the cleanliness of your pet.'", "source": "locale:24600; pack client_definition"},
  {"claim": "Client item list also names 'Advanced Pet Conditioner' as ucdt id 1034174162 and ugdt id 1029489877, so it is a real client name, not a stray string.", "source": "opening-mining-starter-20261009T180011Z/locale/en_us_data.dat lines 27281 and 27398 (repo data dump)"},
  {"claim": "The conditioner family (Basic, Advanced, Super, Scented, Coat Guard, Coat Guard Ultra) is listed in the Pet Trainer job guide as client-only pet care items; no vendor, quest or price is given for any of them.", "source": "notes/Build Guides/Content/Jobs/Pet Trainer.md:245"},
  {"claim": "Conditioner is consumed when grooming a pet; the bowl and brush are kept.", "source": "notes/Build Guides/Gameplay/Pets.md:22; repo prototype/osfr-tools/data/content/pets.json lines 1537-1558 (Basic Pet Conditioner, definition 10521, restore 35)"},
  {"claim": "The Pet Tutorial grooming step asks the player to select conditioner from their own inventory; it is optional and is not a source of the item.", "source": "locale:141140 (quest_dialog, Pet Tutorial: Grooming)"},
  {"claim": "Pack's first-pass 'vendor' guess is unsupported: no coin store price in client definition, no vendor stock, no wiki page, no article, no video, and no other answer mentions this item.", "source": "pack fields vendor_stock, mentioned_by_other_answers, coin_store_prices (all empty); lookup of client/wiki/articles/video returned only locale:24600"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Not confirmed as a coin vendor, Coin Shop, Marketplace, quest reward, drop, event or prize item. The 'vendor' guess is not evidenced.",
  "Repo data has no store entry for definition 10522 in data/content/stores.json; the pet-care reference item list covers only the Basic conditioner (10521) and its ids need client confirmation.",
  "Retired status unknown: no wiki page or dated source states whether it was sold, removed or still available.",
  "Live status is 'unsure': it is in the client's item table and the pet care family, but no source confirms it was obtainable on the 2009-2014 server.",
  "Needed next: a wiki or forum page for Pet Conditioners (Coin Shop or vendor list for Jennifer/Gloria in Cobblestone), or video frames of a pet shop showing 'Advanced Pet Conditioner' with a price."
 ]}
