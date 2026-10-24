<!-- fleet job=citem-infer id=cmetallic-spectral-necklace-69694-v1 status=nothing_found turns=5 usd=0.0051 tokens(read,write,in,out)=[51493, 25286, 12, 2867] model=claude-haiku-5-5 -->
# Metallic Spectral Necklace

{"item": {"name": "Metallic Spectral Necklace", "locale_id": 69694, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item: locale 69694 'Metallic Spectral Necklace', two definitions (22792, 22799), accessory slots 8 and 9 (Ring/Necklace), class 50, no coin store price.", "source": "locale:69694; repo:notes/Build Guides/Gameplay/Items and Inventory.md:94 (slot 8/9 = Accessory1/Accessory2, named Ring and Necklace)"},
  {"claim": "It is one of a material-by-suffix family of Spectral necklaces (Hardwood 69671, Granite 69688, Metallic 69694, Jeweled 69708, and Dull/Rascal/Intern/Sneak/Grunt/Sage Spectral in 86525-86570). The same family also appears as Champion Spectral Necklace (86615, definition 22624, coin price none).", "source": "lookup client: locale:69671, 69688, 69694, 69708, 86525-86570; refs quest-lines/citem-packs.json (Champion Spectral Necklace entry)"},
  {"claim": "The neighbouring Granite and Metallic necklace names (e.g. Granite Dreadful, Metallic Dreadful, Metallic Phantasmal) share this naming pattern, but none of them has a wiki page, a coin vendor price, or a named source in the repo.", "source": "lookup client: locale:69682-69699; locale search 'Necklace'"},
  {"claim": "Searches of the repo, refs, wiki, articles and video for 'Metallic Spectral', 'Spectral Necklace', definition ids 22792/22799 and locale 69694 returned no source. The only repo hit is the Prize Wheel necklace line ('of Bark Skin' / 'of Vitality'), which does not name Spectral.", "source": "search repo/refs; lookup wiki/articles/video (no matches); repo:notes/Build Guides/Gameplay/Items and Inventory.md:192"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. The first-pass guess of 'drop' is unsupported: no enemy, quest, vendor, event or prize-wheel text names this item.",
  "Live status is unverified. The client defines the item, but that alone does not show it was sold or awarded on the live server.",
  "The Spectral family's source is unknown. The name pattern (material + suffix, Halloween-style 'Spectral' ghost theme) suggests a themed event or collection, but this is a guess, not evidence. Check the Halloween/Super Spooktacular wiki pages and the Spectral family members for a shared source.",
  "Variant note: the item has two definitions (22792, 22799) and two slots (8, 9). Whether the two definitions differ in tint or race was not checked.",
  "No description text, price, or video frame was found for this item."
 ]}
