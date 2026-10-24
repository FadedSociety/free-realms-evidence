<!-- fleet job=citem-infer id=cn-wacky-crash-gloves-pl-wacky-crash-gloves-28051-v1 status=done turns=9 usd=0.0067 tokens(read,write,in,out)=[104874, 24572, 20, 5198] model=claude-haiku-5-5 -->
# {n}Wacky Crash Gloves{pl="Wacky Crash Gloves"}

{"item": {"name": "Wacky Crash Gloves", "locale_id": 28051, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, definition 606 (Cost 1266 coins); the store row for item 606 is not in stores.json, so the vendor is unconfirmed", "where": null, "price": "1266 coins (member price 1139 coins, 10% member discount, if the stores.json pattern applies)", "currency": "coins", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/ClientItemDefinitions.json:12941-12960 (Id 606, Cost 1266, MemberDiscount 10); repo:prototype/osfr-tools/data/content/stores.json lines 289-352 hold other items priced 1266 but none with item_id 606"},
  {"type": "vendor", "detail": "Definition 609 and 611 carry Cost 9453 coins; 611 has MinProfileRank 20. Not confirmed as sold anywhere", "where": null, "price": "9453 coins (client Cost field only; likely not a live sale)", "currency": "coins", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/ClientItemDefinitions.json:13004-13062 (Id 609, 611)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Name locale 28051 is '{n}Wacky Crash Gloves'; 27611 Shirt, 27851 Boots, 28320 Helmet, 28943 Pants are the same Wacky Crash set; Elite Pink/Black variants are 69354-69388", "source": "locale:28051; locale:27611; locale:27851; locale:28320; locale:28943; locale:69354-69388"},
  {"claim": "Client definition 606 is a slot-2 (hands) item, class 22, model freestyle_<race>_<gender>_hands_fingerlessgloves.adr, Cost 1266, MemberDiscount 10, MinProfileRank 1, DescriptionId 1114 shared with other gloves", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/ClientItemDefinitions.json:12941-12960"},
  {"claim": "Demo Derby Driver job-rank unlock at rank 20 is the Elite Pink Wacky Crash Helmet (item 599, name 69379), not the gloves; the gloves are not named in that table", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:175"},
  {"claim": "No wiki page, article, video frame, quest, drop or vendor answer names the Wacky Crash Gloves; the wiki search found only the 'Wacky Waving Arm' quest items", "source": "lookup wiki 'Wacky' (no gloves hit)"}
 ],
 "confidence": 0.25,
 "open": [
  "No confirmed source. The 1266-coin Cost is a client definition field; no stores.json row for item 606 was found, so a coin vendor sale is unverified.",
  "The 291-coin store price in the pack does not match any of the gloves' definitions (606 = 1266, 609/611 = 9453). Its origin is unknown.",
  "Demo Derby Driver rank-20 gear (Elite Pink Wacky Crash Helmet) suggests the Wacky Crash set is tied to derby job rank gear, but the gloves are not listed in that rank table. Check whether a 611 (MinProfileRank 20) style rank reward exists.",
  "Definitions 14194-14209 were not individually checked; they may hold the Elite variants and their own prices.",
  "Retired status and whether the item is still live are unknown. Needs a wiki or forum check for Wacky Crash set releases (rank rewards, promotions, or Coin Shop listings)."
 ]}
