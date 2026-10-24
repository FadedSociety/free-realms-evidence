<!-- fleet job=citem-infer id=cwooden-plate-66860-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[12181, 7311, 8, 2057] model=claude-haiku-5-5 -->
# Wooden Plate

{"item": {"name": "Wooden Plate", "locale_id": 66860, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Plates collection (collection id 155, name locale 67521 'Plates'), entry index 5, item_definition_id 23247. Added to the collection; the item itself is not a vendor, quest, drop or store item in any source found.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11922-11975 (collection 155 and entry 1122); locale:67521; locale:132414 (item description 'This item can be added to the Plates Collection')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Wooden Plate' is locale 66860, item definition 23247, slot/class 0, no coin store price in the client definition.", "source": "locale:66860"},
  {"claim": "Locale 132414 is the item description 'This item can be added to the Plates Collection', not the collection name. The collection name is locale 67521 = 'Plates'.", "source": "locale:132414; locale:67521"},
  {"claim": "Catalogue collection 155 (name_id 67521) lists Wooden Plate as entry index 5 (item 23247, icon 2190), with item_link 'sanctuary', so the membership data comes from Sanctuary-linked content, not confirmed live behaviour.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11970-11975"},
  {"claim": "Collection 155 completion grants item 17646 x1. That reward is for completing the collection; it is not an acquisition route for the individual Wooden Plate. Item 17646 has no resolved name in the repo or client text.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12004-12016"},
  {"claim": "No wiki page, article, video frame or vendor stock entry names Wooden Plate or the Plates collection. The lookup on 'Wooden Plate' returned only the client text entry.", "source": "lookup: wiki, client, articles, video"}
 ],
 "confidence": 0.4,
 "open": [
  "Collection 155 (Plates) itself has no documented acquisition source: no quest, vendor, or Meta-collection link was found for it. The pack's Adventurer-wiki note about Plates parts is not tied to this item and is not used.",
  "Membership comes from the Sanctuary-linked catalogue entry (item_link 'sanctuary'). Live behaviour is not verified.",
  "Item 17646 (completion reward of collection 155) is unnamed; it is not counted as a Wooden Plate source.",
  "Retired status and live status are unknown: no retirement notice found either way.",
  "Critique 1 (fixed): the previous answer cited locale 132414 as the collection name. It is the item description; the collection name is locale 67521 'Plates'.",
  "Critique 2 (fixed): the previous answer omitted item_link 'sanctuary' from the catalogue entry (collection_catalogue.json:11974). It is now recorded above as provenance.",
  "Critique 3 (addressed): item 17646 is kept as a completion reward only, not a Wooden Plate source.",
  "Critique 4 (addressed): retired and live are left null/unsure with the reason stated, since no evidence either way exists."
 ]}
