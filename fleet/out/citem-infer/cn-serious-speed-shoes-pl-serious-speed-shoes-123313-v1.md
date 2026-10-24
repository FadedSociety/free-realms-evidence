<!-- fleet job=citem-infer id=cn-serious-speed-shoes-pl-serious-speed-shoes-123313-v1 status=nothing_found turns=5 usd=0.0031 tokens(read,write,in,out)=[25425, 12270, 12, 2674] model=claude-haiku-5-5 -->
# {n}Serious Speed Shoes{pl="Serious Speed Shoes"}

{"item": {"name": "Serious Speed Shoes", "locale_id": 123313, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 43314 'Serious Speed Shoes' (NameId 123313, Class 24, Slot 5, CategoryId 105, MinProfileRank 20, Cost 1266, MemberDiscount 10, tintable, model freestyle_<race>_<gender>_feet_shoeswsocks.adr). Cost 1266 is the client's own cost field, not a store listing.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:924905-924925"},
  {"claim": "Locale name string for 123313 is the item name; the set (Serious Speed Jacket 123312, Gloves 123314, Helmet 123315, Pants 123322) shares the name pattern, but no text in the client explains how the set is obtained.", "source": "locale:123313; locale:123312; locale:123314; locale:123315; locale:123322"},
  {"claim": "No wiki page, article, video frame, quest, enemy drop, or coin vendor stock names this item in the available sources.", "source": "lookup (client, wiki, articles, video) 'Serious Speed Shoes'; repo search for 'Speed Shoes' returned no matches"},
  {"claim": "The repo's coin store data (stores.json) has no entry for definition id 43314 or the other definition ids in the pack. Entries priced 1266 exist there but are for other item_ids (e.g. 597, 615, 642), so they do not confirm a sale of this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json (lines 289-3715, no item_id 43314)"},
  {"claim": "The client definition lists 12 definition ids (43314 to 43435) and 16 definitions in total, which looks like tint/race variants of one item rather than separate items.", "source": "pack client_definition; repo:FreeRealms-Legacy ClientItemDefinitions.json"}
 ],
 "confidence": 0.2,
 "open": [
  "No verified acquisition source. The first-pass guess 'vendor' has no evidence behind it; the pack's vendor_stock is empty and no store row matches id 43314.",
  "The pack's coin_store_prices [433, 1266] are not confirmed. 1266 matches the client Cost field; 433 has no matching source in the pack or repo. Treat both as unverified until a store row for this item is found.",
  "Serious Speed set (Jacket 123312, Gloves 123314, Helmet 123315, Pants 123322) looks like a themed set; its acquisition (quest, event, or prize) is unknown and not in the pack. Check the set's other items for a source.",
  "MinProfileRank 20 suggests a mid-level reward or store item, but this is an inference only.",
  "Live status is unconfirmed. Being in the client does not prove it was sold; retirement status needs a wiki or article source."
 ]}
