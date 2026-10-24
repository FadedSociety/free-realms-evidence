<!-- fleet job=citem-infer id=csea-serpent-wrecker-chassis-114842-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[12774, 12802, 8, 2239] model=claude-haiku-5-5 -->
# Sea Serpent Wrecker Chassis

{"item": {"name": "Sea Serpent Wrecker Chassis", "locale_id": 114842, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Sea Serpent Wrecker Chassis' (locale 114842) has 2 definitions (58594, 60661), class_ids 76 and 106, slot 0, no models, and no coin store price. Its description is 'The chassis for the Sea Serpent Wrecker.' (locale 114656 is the kart's name line, 'Sea Serpent Wrecker').", "source": "locale:114842; locale:114656; repo client definition pack"},
  {"claim": "The item is one part of a derby kart. A derby kart is a chassis plus per-kart customised parts (engine, turbo, mod, steering, shocks, springs, boosters). The Tank Wrecker's chassis (1167221491) is the parallel example.", "source": "repo:notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197"},
  {"claim": "Sea Serpent Wrecker (the whole kart) is listed in the wiki Derby Karts category and was sold in the Station Cash Marketplace with a 10 percent member discount. The note gives no price for this kart and does not say the chassis is sold separately.", "source": "repo:notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197 (cites wiki Derby Karts pages)"},
  {"claim": "A separate autopilot match lists Sea Serpent Wrecker as matched without a Station Cash store row, which conflicts with the wiki Marketplace claim.", "source": "repo:notes/Autopilot/T634.md:65"},
  {"claim": "Sibling chassis Cutlass Wrecker costs 700 Station Cash (630 for members) in the SC Marketplace. This is the only price in the derby-kart notes and is for the kart, not a chassis.", "source": "repo:notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197"}
 ],
 "confidence": 0.2,
 "open": [
  "No wiki page, article, video or vendor data names the Sea Serpent Wrecker Chassis as a sellable item. Its sources are unknown.",
  "It is likely a kart component bundled with the Sea Serpent Wrecker kart (SC Marketplace per the derby note, but unverified). It is not known whether the chassis is sold on its own, so no source is listed.",
  "The conflicting Marketplace evidence for the kart (wiki claim versus the T634 no-store-row match) needs a check against the wiki Derby Karts pages and the stores data.",
  "Retired and live status is unknown. The definition exists in the client, but no source says whether it was sold or is still obtainable.",
  "No store price exists in the client definition (coin_store_prices empty), and no Station Cash price is evidenced for this chassis."
 ]}
