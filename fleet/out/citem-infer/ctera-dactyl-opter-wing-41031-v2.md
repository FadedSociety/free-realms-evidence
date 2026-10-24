<!-- fleet job=citem-infer id=ctera-dactyl-opter-wing-41031-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[13155, 9032, 8, 1998] model=claude-haiku-5-5 -->
# Tera-dactyl-opter Wing

{"item": {"name": "Tera-dactyl-opter Wing", "locale_id": 41031, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Piece (index 1, entry id 747, item definition 3815) of the Bird Wing Fossils collection (collection id 104, Archaic > Rare). Turn-in piece for the collection; no acquisition route for the individual piece is known.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8431-8448 (collection id 104, name_id 7755, description_id 7831, entry name_id 41031, item_definition_id 3815); wiki:List of Collections (rev 27852, 2013-07-13) lists Bird Wing Fossils under Archaic > Rare; locale:7755, locale:7831, locale:132363"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 'Tera-dactyl-opter Wing' is locale 41031 and item definition 3815.", "source": "locale:41031; repo:prototype/osfr-tools/data/content/collection_catalogue.json:8443-8446"},
  {"claim": "The item's client description reads 'This item can be added to the Bird Wing Fossils Collection'.", "source": "locale:132363"},
  {"claim": "The collection is named 'Bird Wing Fossils' (locale 7755) with description 'A collection of bird wing fossils. Buffalo dinosaur wings anyone?' (locale 7831).", "source": "locale:7755; locale:7831"},
  {"claim": "Bird Wing Fossils is listed under Archaic > Rare in the wiki's List of Collections (rev 27852, 2013-07-13).", "source": "wiki:List of Collections; repo:prototype/osfr-tools/data/content/collections.json key wiki:7:220 (client_id 1073742044)"},
  {"claim": "The collection's catalogue entry is tagged item_link 'sanctuary' for this piece; the meaning of that tag is not documented in the pack.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8447"},
  {"claim": "Corrections to the prior answer: the locale IDs 2503781342 and 2926419700 do not exist in the locale table; the correct IDs are 132363 (item description), 7831 (collection description) and 7755 (collection name).", "source": "locale lookups in this review"}
 ],
 "confidence": 0.5,
 "open": [
  "No source gives how players obtain the individual Tera-dactyl-opter Wing piece (drop, dig, quest, vendor or event). Not listed as a source; needs a per-piece source.",
  "No coin store price exists for item 3815 (coin_store_prices is empty); no Station Cash, Coin Shop or SC Marketplace source is known.",
  "The collection's reward is unknown (reward null in collections.json).",
  "Retired status and later availability are unknown; the 2013 wiki snapshot lists the collection but nothing confirms current availability.",
  "The meaning of item_link 'sanctuary' in the catalogue entry is undocumented; it may hint at a Sanctuary-linked turn-in but this is unverified.",
  "Wireable: false. Collection membership only; do not set acquisition for this item from current evidence.",
  "The lookup tool returned FTS errors for the name query with a hyphen; client/wiki text search for the item name was not completed."
 ]}
