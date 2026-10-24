<!-- fleet job=citem-infer id=csnowhill-birds-of-paradise-17564-v1 status=done turns=7 usd=0.0062 tokens(read,write,in,out)=[93514, 22888, 16, 4822] model=claude-haiku-5-5 -->
# Snowhill Birds of Paradise

{"item": {"name": "Snowhill Birds of Paradise", "locale_id": 17564, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 1 of the 'Exotic Snowhill Flowers' collection (collection id 243, name locale 17581; entry item_definition_id 9196). Client text 132500: 'This item can be added to the Exotic Snowhill Flowers Collection'. It is a collection-card item, not a purchasable or questable item; it is obtained by collecting the flower item in the collection, and the wiki gives no separate acquisition route for it.", "where": "Snowhill", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18468-18485 (id 243, entries[0]); locale:132500; locale:17590 ('A collection of rare Snowhill flowers. Legend says only 1 out of every 9 flowers found is this rare.'); wiki page 'List of Collections' (lists 'Exotic Snowhill Flowers' and 'Snowhill' flower collections, revision 27852, 2013-07-13)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 17564 is named 'Snowhill Birds of Paradise' and its description says it can be added to the Exotic Snowhill Flowers Collection.", "source": "locale:17564; locale:132500"},
  {"claim": "Item definition 9196 is entry 1 of collection 243 'Exotic Snowhill Flowers' (name locale 17581), alongside Snowhill Orchid (9197, locale 17565).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18468-18485"},
  {"claim": "The collection 'Exotic Snowhill Flowers' is listed on the wiki's List of Collections page.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections, revision 27852); repo:prototype/osfr-tools/data/content/collections.json:6035 (wiki:3:97)"},
  {"claim": "The flowers in this collection are rare Snowhill flowers, about 1 in 9 flowers found is this rare.", "source": "locale:17590"},
  {"claim": "The 'Birds of Paradise' name on the wiki list (locale 66645, 'birds of paradise flowers' 67665, 'Birds of Paradise Collection' 132446) is a separate collection, not the Exotic Snowhill Flowers entry; it is not this item's collection.", "source": "locale:66645; locale:67665; locale:132446; repo:collections.json:5979"},
  {"claim": "Repo store table has rows keyed item_id 17549-17566 (Snowhill flower range) at 10000 coins (member 9000), 15000 for 17554, and no row for definition 9196.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4340-4356"}
 ],
 "confidence": 0.3,
 "open": [
  "No wiki page, article, video or vendor names a way to get Snowhill Birds of Paradise. Its only verified source is membership in the Exotic Snowhill Flowers collection (collection 243); the gathering or drop route that fills the collection is unverified.",
  "Coin price conflict: client definition coin_store_prices is empty, but repo stores.json has rows with item_id 17564 (tint group 3, 10000 coins, member 9000, category 200, no_sale true). The row is keyed on the name locale id, not definition 9196 (no row for 9196 exists), so it may not be this item. Do not record it as a coin sale until the store key mapping is confirmed.",
  "Live status: the first pass says live, but no source dates the item. Since the collection appears on a 2013 wiki list, treat as possibly retired; 'live' is unsure.",
  "Retired status unknown: the wiki list gives no retirement note for the Exotic Snowhill Flowers collection.",
  "Video and article searches for 'Snowhill Birds of Paradise' returned nothing; the 'Birds of Paradise' wiki entries refer to a different collection."
 ]}
