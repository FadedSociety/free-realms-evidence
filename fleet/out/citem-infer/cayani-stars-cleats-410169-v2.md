<!-- fleet job=citem-infer id=cayani-stars-cleats-410169-v2 status=nothing_found turns=2 usd=0.0022 tokens(read,write,in,out)=[5539, 9907, 6, 1782] model=claude-haiku-5-5 -->
# Ayani Stars Cleats

{"item": {"name": "Ayani Stars Cleats", "locale_id": 410169, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ayani Stars Cleats' is locale 410169, item definition 68181, slot 0, class 0, no models and no coin store price.", "source": "locale:410169; repo:prototype/osfr-tools/data/content/collection_catalogue.json:22127-22130"},
  {"claim": "Item is entry 6 of 8 in the Soccer Cleats collection (collection 293, name locale 410162, description locale 410163). This is membership only, not an acquisition source.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:22070-22166; locale:410162; locale:410163"},
  {"claim": "Item description (UI text) reads 'This item can be added to the Soccer Cleats Collection'.", "source": "locale:132507"},
  {"claim": "Repo search for 68181, 410169 and 'Ayani' finds only the collection catalogue entry; no vendor, store, quest, drop or event row names this item.", "source": "search repo: prototype/osfr-tools/data/content/*"},
  {"claim": "Client lookup finds no wiki page, article or video naming the item or the Soccer Cleats collection.", "source": "lookup client/wiki/articles/video 'Ayani Stars Cleats OR Soccer Cleats collection'"},
  {"claim": "The Soccer Star note groups 'Ayani Stars' with cleats 3831876483 and jersey 3116720492. That id is not 68181 and the link is unverified, so it is not used as support for kind or source.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:240 (unverified lead)"},
  {"claim": "The Snowhill Getaway cluster (locale 410173-410175) is a separate fishing-tournament quest that does not name the cleats; not a source.", "source": "locale:410173; locale:410174"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced. Collection membership (collection 293, entry 6 of 8) says where the item is filed, not how a player gets it, so it is not listed as a source.",
  "How the collection is completed and what the reward (definition 68175, 10 coins, adds collection 292) requires is unknown; the reward item's source is also unknown.",
  "Kind is 'other' (Soccer Cleats collection member). 'clothing' was dropped: slot 0 / class 0 with no models does not establish it, and the Soccer Star link is unverified.",
  "Price, currency and retired status are unknown. No coin store price exists in the client definition.",
  "Live status is unsure: the collection exists in the client but no in-game acquisition is confirmed. Not wireable from this evidence.",
  "Next step: check whether item 3831876483 (Soccer Star Ayani cleats) is the same item as definition 68181, and find the source of the Soccer Cleats collection reward."
 ]}
