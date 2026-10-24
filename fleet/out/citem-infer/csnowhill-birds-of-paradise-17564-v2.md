<!-- fleet job=citem-infer id=csnowhill-birds-of-paradise-17564-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[5573, 9388, 6, 2007] model=claude-haiku-5-5 -->
# Snowhill Birds of Paradise

{"item": {"name": "Snowhill Birds of Paradise", "locale_id": 17564, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 1 (item_definition_id 9196, entry id 1825) of the 'Exotic [Snowhill] Flowers' collection (collection id 243, name locale 17581). The acquisition route that fills this collection is not sourced; no source names how the card is obtained.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18468-18485 (id 243, entries[0]); wiki 'List of Collections' (https://freerealms.fandom.com/wiki/List_of_Collections) lists 'Exotic [Snowhill] Flowers'; locale:17590"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 17564 is named 'Snowhill Birds of Paradise'; its description says it can be added to the Exotic Snowhill Flowers Collection.", "source": "locale:17564; locale:132500"},
  {"claim": "Definition 9196 is entry 1 of collection 243 'Exotic Snowhill Flowers' (name locale 17581), alongside Snowhill Orchid (locale 17565).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18468-18490"},
  {"claim": "The collection 'Exotic [Snowhill] Flowers' appears on the wiki's List of Collections page.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "The flowers in the collection are rare Snowhill flowers; legend says about 1 in 9 flowers found is this rare.", "source": "locale:17590"},
  {"claim": "No wiki page, article, video, or client line names a vendor, quest, drop, or event that gives this item. The lookup returns only the client name line.", "source": "lookup 'Snowhill Birds of Paradise' (wiki, client, articles, video)"},
  {"claim": "No coin store price is confirmed for definition 9196. The client definition has no coin_store_prices. stores.json has a row keyed item_id 17564 (10000 coins, member 9000, no_sale true), but that key is the name locale id, not definition 9196, so it is not used as a price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4355; repo:collection_catalogue.json:18483"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition route unknown. The only verified source is membership in collection 243 'Exotic [Snowhill] Flowers'. The route that fills that collection (gathering, drop, or other) is not in any source here, so no source beyond collection membership is recorded.",
  "wireable: false. A collection-membership entry has no price, quest, drop, or event, so the item cannot be wired as acquirable from this evidence.",
  "Coin price unconfirmed. stores.json row item_id 17564 (10000 coins, member 9000) is keyed on the name locale id and may not refer to definition 9196. Keep price null until the store key mapping is checked.",
  "Location unknown. 'Snowhill' is only the wiki grouping of the flower family, not a place where the card is obtained.",
  "Live and retired status unsure. The collection is on a 2013 wiki list (revision 27852) with no retirement note; the first-pass 'live: yes' is not sourced.",
  "The 'Birds of Paradise' wiki entries (locale 66645, 67665, 132446) refer to a different collection and are not used here."
 ]}
