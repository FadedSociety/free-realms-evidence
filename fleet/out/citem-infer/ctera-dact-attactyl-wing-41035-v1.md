<!-- fleet job=citem-infer id=ctera-dact-attactyl-wing-41035-v1 status=done turns=5 usd=0.0023 tokens(read,write,in,out)=[20807, 7263, 12, 2275] model=claude-haiku-5-5 -->
# Tera-dact-attactyl Wing

{"item": {"name": "Tera-dact-attactyl Wing", "locale_id": 41035, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item definition 3819 is one of the 'Bird Wing Fossils' collection entries (collection id 104, name_id 7755, description_id 7831 'A collection of bird wing fossils'); entry id 751, index 5, icon_tint_id 112, item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8479-8483"},
  {"claim": "Collection 104 is the 'Bird Wing Fossils' collection, listed on the wiki's List of Collections under the Rare category as '[Bird] [Wing] [Fossils]'.", "source": "repo:prototype/osfr-tools/data/content/collections.json:11186-11213 (wiki:7:220, List_of_Collections); wiki page List of Collections"},
  {"claim": "Client UI text states the item 'can be added to the Bird Wing Fossils Collection'.", "source": "locale:132363 and locale:41035"},
  {"claim": "The item's sibling wings (41031-41038) and skulls/teeth sit in the same catalogue family; the set is the fossil-collection line, not a vendor or store item.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8431-8490; client_cluster locales 41030-41040"},
  {"claim": "No coin store price, vendor stock, quest reward, enemy drop or event link was found for definition 3819.", "source": "client definition coin_store_prices [] ; vendor_stock []; mentioned_by_other_answers []; wiki page null"}
 ],
 "confidence": 0.55,
 "open": [
  "No acquisition source is evidenced. The item is a collection entry; how players obtained the wing (drop, collection turn-in, event, or promotion) is not stated in any wiki, article, video or repo source checked. Needs a source before adding sources.",
  "The catalogue marks the entry item_link 'sanctuary', so it may have been obtained on Sanctuary-era content only; confirm whether the item existed in the live 2009-2014 game.",
  "The wiki List of Collections has no per-item reward or spawn details for Bird Wing Fossils (reward null, entries_known false in our data); the collection's own reward is unknown.",
  "The jev_first_pass 'live: yes' is only a hint; no wiki or video evidence confirms the item in live play, hence 'unsure'."
 ]}
