<!-- fleet job=citem-infer id=cfisher-s-rollcast-necklace-30638-v1 status=nothing_found turns=6 usd=0.0049 tokens(read,write,in,out)=[60133, 21209, 14, 3330] model=claude-haiku-5-5 -->
# Fisher's Rollcast Necklace

{"item": {"name": "Fisher's Rollcast Necklace", "locale_id": 30638, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition: Id 2124, NameId 30638, Type 1, Class 139, Slot 9 (necklace/accessory slot), CategoryId 108, MinProfileRank 10, PowerRating 3, Cost 866, MemberDiscount 10, TintAlias dyetint, shared DescriptionId 1114 (same description as the other Rollcast/Algae necklaces).", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:40664-40682"},
  {"claim": "Name is a fishing-set tier entry: 'Fisher's Rollcast Necklace' sits in a family of Algae, Backwater, Livebox and Rollcast necklaces, rings and square shards with tier prefixes Amatuer, Fisher's, Angler's, Troller's, Pro and All-Star. Tier order, stats and levels are unknown.", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:291; locale:30633-30643"},
  {"claim": "No coin store price: stores.json has no row for item 2124 (no 'coin_store_prices' entry in the pack and no matching id in repo data). The Cost 866 field is the definition's internal cost, not a sale price, so it is not used as a price.", "source": "repo search for item id 2124 in data/content/*.json (no stores.json hit)"},
  {"claim": "No wiki article, article fact, video frame, quest, enemy drop, crafting recipe or vendor entry names this item. Fishing lure and tackle data in the Fisherman guide list the shards only as client names with no sources.", "source": "lookup client/wiki/articles/video for 'Rollcast' (only client name rows returned); repo:notes/Build Guides/Content/Jobs/Fisherman.md:291"},
  {"claim": "The Fisherman guide lists the Rollcast necklace (Angler's variant, 3565605294) and the Fisher's Livebox Ring as client-only names with no acquisition info.", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:291"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found anywhere in the evidence. The family's likely origin is fishing (job set), but no quest, vendor, drop, crafting or event evidence names it, so no source is asserted.",
  "The first-pass tag 'live: yes, source_guess: drop' is a hint only. Nothing confirms it is live, and nothing confirms a drop.",
  "Kind is set to 'clothing' from slot 9 and the necklace class; the item may be a fishing accessory rather than wearable clothing. Check the class 139 meaning.",
  "Retired status unknown: no source says whether the Rollcast tier was removed or is still obtainable.",
  "Price unknown: no coin store row or Station Cash listing found. The 866 'Cost' field is not a sale price.",
  "Tier order and the Fisher's tier's rank (MinProfileRank 10) need a source to confirm where it sits among Amatuer, Angler's, Troller's, Pro and All-Star variants.",
  "Suggested checks: fishing-job reward tables, the Fisherman job's achievement/collection 'Fisherman Shards' (4157167645) and 'Fisherman Accessories' (4239768659) contents, and any fishing tournament or event rewards."
 ]}
