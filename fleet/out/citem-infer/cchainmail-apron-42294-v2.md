<!-- fleet job=citem-infer id=cchainmail-apron-42294-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[10554, 9605, 8, 1534] model=claude-haiku-5-5 -->
# Chainmail Apron

{"item": {"name": "Chainmail Apron", "locale_id": 42294, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale, 3 definition ids (tint groups 1, 2, 3) of Chainmail Apron; vendor/NPC not named in the store data", "where": null, "price": "1761 coins (member price 1584 coins, 10% member discount)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json item_id 10918 (line 3209), 10942 (line 3223), 76765 (line 16315): category_id 104, purchase_price_coins 1761, member_price_coins 1584, no_sale true, source_tags L1,L2,L4,R2,L3,L3"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Chainmail Apron' is locale:42294 (item), description 'In case the weapons you make ever turn on you...'; 3 definition ids 10918, 10942, 76765; slot 4; class 14; model worker_<race>_<gender>_legs_apronwpants.adr.", "source": "locale:42294; client definition in pack"},
  {"claim": "Each of the three definition ids has a stores.json coin-store row at 1761 coins, member price 1584, no_sale true, category 104.", "source": "prototype/osfr-tools/data/content/stores.json lines 3209, 3223, 16315 (verified by search)"},
  {"claim": "No wiki page, image, article fact, video frame, quest reward, drop or event mentions Chainmail Apron. Same client cluster as Astronaut Helm (locale:42289) and Iron Golem Goggleguard (locale:42292), but no source names the set.", "source": "lookup client/wiki/articles/video (no matches); locale:42289, locale:42292"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor/NPC that sells it is not named: the stores.json rows carry no vendor id, and vendor_stock is empty. Check vendors.json against item ids 10918/10942/76765.",
  "Meaning of store category_id 104 and of source tags L1/L2/L4/R2/L3 was not confirmed in the repo; the tags are cited as recorded only.",
  "Live and retired status are unknown. The stores.json rows carry no date, and no source says it was retired or unobtainable. The 'no_sale' flag only means it cannot be resold.",
  "locale:150503 ('This is a Chainmail Apron item.') is a FLAGGED placeholder and is dropped from evidence.",
  "The client-cluster link to Astronaut Helm and Iron Golem Goggleguard is unconfirmed; it is not used as a source.",
  "The three definition ids are probably tint groups of one item, so the price is cited once per id and not as three sources."
 ]}
