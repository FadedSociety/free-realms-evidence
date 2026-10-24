<!-- fleet job=citem-infer id=call-weather-tires-67373-v2 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[12424, 7498, 8, 1821] model=claude-haiku-5-5 -->
# All-weather Tires

{"item": {"name": "All-weather Tires", "locale_id": 67373, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 6 of 8 in the Kart Race Tires collection (collection id 219, name locale 67585). Membership only; the repo gives no acquisition route for the individual tire (item definition 23760).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16876-16956 (entry at line 16936); locale:67585 'Kart Race Tires'; locale:132476 'This item can be added to the Kart Race Tires Collection'"},
  {"type": "other", "detail": "Completing collection 219 grants 2 coins and Robgoblin's Race Fuel (item 23763) and unlocks collection 220 (Race Fuel). Catalogue-only; not verified against a wiki or client source.", "where": null, "price": "2 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16958-16973"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'All-weather Tires' is locale 67373; its description says it can be added to the Kart Race Tires Collection.", "source": "locale:67373; locale:132476"},
  {"claim": "Collection 219 'Kart Race Tires' (name locale 67585, confirmed by the locale table as 'Kart Race Tires') lists All-weather Tires as entry index 6 with item definition 23760 among eight tire types (67368-67375).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16876-16956; locale:67585"},
  {"claim": "Item definition 23760 appears only once in the repo, in the collection catalogue. No vendor, store, drop or quest reward references it.", "source": "repo search for 23760 / All-weather"},
  {"claim": "Coin store prices for this item: none in the client definition. No coin vendor sale is evidenced.", "source": "pack client_definition coin_store_prices []"},
  {"claim": "No wiki page, article fact, or video frame names this item. Lookup by name errored in this pass, so the wiki check rests on the pack's null wiki_page and empty video fields.", "source": "pack fields wiki_page null, video []"},
  {"claim": "The earlier citation of notes/Build Guides/Content/Jobs/Kart Driver.md:153 was removed: that note covers Race Fuel items and collection ids, not the tire entries.", "source": "critique 'evidence' pass"}
 ],
 "confidence": 0.4,
 "open": [
  "No acquisition route for the individual tire is sourced. The collection entry shows membership, not how a player gets the tire. Kart shop, Kart Driver rewards, drops and race prizes are all unsourced guesses.",
  "The 2-coin plus Robgoblin's Race Fuel reward for completing collection 219 is from the repo catalogue alone and is unverified against the live game.",
  "Live status is unsure. The catalogue flags the collection (flag6=1), but no wiki page, article or video confirms it was sold or awarded in 2009-2014, and no retirement source was found.",
  "The 'Extra Grip Tires' kart part (10 coins) in the Kart Driver note is a different item and is not linked to this one."
 ]}
