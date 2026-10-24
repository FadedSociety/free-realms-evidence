<!-- fleet job=citem-infer id=cglistening-wand-100526-v4 status=nothing_found turns=4 usd=0.0035 tokens(read,write,in,out)=[36507, 15826, 10, 2245] model=claude-haiku-5-5 -->
# Glistening Wand

{"item": {"name": "Glistening Wand", "locale_id": 100526, "kind": "weapon"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Glistening Wand' is locale 100526, in a set with Glistening Shadowblade, Axe, Hammer, Bow and Shockrod (locale 100525, 100527-100530).", "source": "locale:100526; locale:100525-100530"},
  {"claim": "The value 2204 is a generic 'cost' field shared by many unrelated weapons, so it is not a store price.", "source": "prototype/osfr-tools/data/reference/weapons.json:16830, 16844, 20342 (all cost 2204 on different weapons)"},
  {"claim": "The coin-store table has a row for Id 48152 with CategoryId 207 and no price or currency. Category 207 has no name in the refs.", "source": "refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json lines 59703-59704"},
  {"claim": "The only Glistening Scythes quest text is the Blacksmith quest (Billie JoBob). It concerns Scythes, not the Wand.", "source": "locale:95170; locale:95171; locale:95172"},
  {"claim": "No wiki page, image, article, video frame, vendor, quest, drop or event names the Glistening Wand. Lookup returns only the client line locale:100526.", "source": "lookup (client, wiki, articles, video) for 'Glistening Wand'"},
  {"claim": "The id locale:671336603 cited in the earlier pack does not exist as a locale id. It is a note-file reference in the Blacksmith guide, and it was removed from this answer.", "source": "notes/Build Guides/Content/Jobs/Blacksmith.md:372"}
 ],
 "confidence": 0.15,
 "open": [
  "No confirmed acquisition source. The coin-store row (48152, category 207) is presence only, with no price or currency and no named store section, so it is not a coin vendor sale and no source is wired.",
  "coin_store_prices [2204] is the generic cost field (see weapons.json), not a store price. Do not wire it as a price.",
  "No quest, drop, event, crafting recipe, collection or vendor source found. The Glistening set's Blacksmith link covers Scythes only.",
  "Retired status and current availability are unknown; no source states them.",
  "Two client definitions (29938, 48152) share the name and model; the variant that is in the coin-store table is 48152 only."
 ]}
