<!-- fleet job=citem-infer id=ctera-dactyl-opter-wing-41031-v3 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5814, 6914, 6, 1804] model=claude-haiku-5-5 -->
# Tera-dactyl-opter Wing

{"item": {"name": "Tera-dactyl-opter Wing", "locale_id": 41031, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 'Tera-dactyl-opter Wing' is locale 41031 and item definition 3815.", "source": "locale:41031; repo:prototype/osfr-tools/data/content/collection_catalogue.json:8443-8446"},
  {"claim": "The item's client description reads 'This item can be added to the Bird Wing Fossils Collection'.", "source": "locale:132363 (ui - Bird Wing Fossils Collection)"},
  {"claim": "The collection is named 'Bird Wing Fossils' (locale 7755) with description 'A collection of bird wing fossils. Buffalo dinosaur wings anyone?' (locale 7831).", "source": "locale:7755; locale:7831"},
  {"claim": "Bird Wing Fossils appears as '[Bird] [Wing] [Fossils]' under the 'Rare' group in the wiki's List of Collections (rev 27852, 2013-07-13). The 'Archaic' parent was not visible in the returned page text, so only 'Rare' is verified.", "source": "wiki:List of Collections; repo:prototype/osfr-tools/data/content/collections.json key wiki:7:220"},
  {"claim": "item_link 'sanctuary' is a collection-wide rule, not a piece-specific hint: the catalogue's item_link_rule says it resolves Sanctuary Entries[].ItemDefinitionId, and the tag is set on many entries across the catalogue (e.g. lines 35-245), including Bird Wing Fossils entries (8447, 8456). It does not identify a source for this piece.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6, 8447, 8456"},
  {"claim": "The 'turn-in' mechanic stated in the earlier answer is unsupported; the pack shows only collection membership (entry 747, index 1, collection 104).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8431-8448; locale:132363"},
  {"claim": "No coin store price exists for item 3815 (coin_store_prices empty in the client definition), and no vendor stock, quest reward, drop, event, SC Marketplace, Coin Shop or prize wheel source was found for it.", "source": "client definition in evidence pack; vendor_stock and mentioned_by_other_answers empty"}
 ],
 "confidence": 0.3,
 "open": [
  "No source gives how players obtain the individual Tera-dactyl-opter Wing piece (drop, dig, quest, vendor, event or marketplace). Zero acquisition sources are recorded; the collection membership is not an acquisition source.",
  "The collection's reward is unknown (reward null in collections.json); the turn-in mechanic is therefore unverified and was removed.",
  "The 'Archaic' parent of Rare in the wiki List of Collections is not confirmed by the returned text.",
  "Retired status and later availability are unknown; the 2013 wiki snapshot lists the collection but does not confirm current availability.",
  "Wireable: false. Do not set an acquisition source for item 3815 from current evidence.",
  "Client and wiki text search by the hyphenated item name was not completed (FTS error on hyphen)."
 ]}
