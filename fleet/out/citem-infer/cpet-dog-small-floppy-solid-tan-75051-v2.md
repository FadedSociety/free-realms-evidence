<!-- fleet job=citem-infer id=cpet-dog-small-floppy-solid-tan-75051-v2 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[5171, 8992, 6, 1832] model=claude-haiku-5-5 -->
# Pet: Dog: Small Floppy: solid-tan

{"item": {"name": "Pet: Dog: Small Floppy: solid-tan", "locale_id": 75051, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 23901 is named 'Pet: Dog: Small Floppy: solid-tan' at locale 75051. Locale and lookup confirm a Small Floppy dog cluster of 17 names: solid-charcoal, solid-tan, solid-sand, solid-rusty, solid-chocolate, darkmark-tan, darkmark-oreo, darkmark-gold, darkmark-chocolate, darkmark-gray (75050-75059), lightmark-rusty, lightmark-gold, lightmark-chocolate, lightmark-gray, lightmark-tan, lightmark-ivory (75060-75066), and solid-gold (75103). 75057-75059 are confirmed by lookup, so the earlier 75050-75056 cap was too narrow.", "source": "locale:75050-75066, locale:75103; lookup client 'Small Floppy dog pet'"},
  {"claim": "stores.json row for item 23901 lists purchase_price_coins 540, member price 486, sell 54, no_sale false, with no category, no vendor and no price_provenance note. This is a bulk table value. The identical row pattern covers 23900 and 23903-23905, 23907-23908.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6778 (compare :6777, :6780-6785)"},
  {"claim": "Neighbour 23902 has its 540 legacy coin cost explicitly cleared because no coin vendor stocks it; it is an SC Marketplace item at 400 SC. Item 23906 is handled the same way (225 SC, Barkley). Item 23901 has no such note, so its 540 coin price is not confirmed as a live coin vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6779, :6783"},
  {"claim": "No vendor stock row, quest, drop, wiki page, article or video frame names this pet variant. The only 'Floppy' hits are the Small Floppy Eared Dog food/illusion items (locale 3133, 147583, 150091, 150831, 382773), which are different items.", "source": "repo search of vendors/stores; lookup wiki/articles/video; locale:3133, locale:147583"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor, NPC, quest, event or other source is verified for item 23901. The only sourcing is the unsourced 540-coin bulk store row at stores.json:6778, which is not a stock row and appears to be a table default shared with neighbours.",
  "The earlier answer's 'vendor' source is withdrawn. Its vendor type, location and 'live' reading were not supported by the evidence.",
  "The 540-coin price should be treated as unverified legacy data until a vendor stock row or a wiki/article source names the item. The 23902 note suggests such legacy prices are cleared when no vendor stocks an item.",
  "Live status and any retirement date are unknown. No source says whether the solid-tan Small Floppy pet was ever sold, granted or obtainable.",
  "Check whether other Small Floppy variants (75050-75066, 75103) share the same unverified 540-coin store pattern before reconstructing prices for the family."
 ],
 "confidence_note": "Only the client definition and an unsourced store price row exist. No source of acquisition was found."}
