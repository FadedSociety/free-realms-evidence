<!-- fleet job=citem-infer id=cblue-carnation-67111-v2 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[5401, 7516, 6, 1702] model=claude-haiku-5-5 -->
# Blue Carnation

{"item": {"name": "Blue Carnation", "locale_id": 67111, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:67111 is 'Blue Carnation'; the item definition is 23498, and the client definition has no coin_store_prices entry, so no coin vendor sale is evidenced.", "source": "locale:67111; repo:prototype/osfr-tools/data/content/collection_catalogue.json:14987-14990"},
  {"claim": "Blue Carnation is entry index 8 (id 1373) of collection 186, whose name is 'Carnations' (name_id 67552, description 'A collection of carnations, big, bright, and beautiful.' locale:67664). Its entries are name_ids 67104-67111 (Red, Pink, Purple, Orange, White, Yellow, Green, Blue Carnation), all with item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14912-15014; locale:67552, locale:67104-67111"},
  {"claim": "The item's in-game line 'This item can be added to the Carnations Collection' is locale:132445.", "source": "locale:132445"},
  {"claim": "Collection 186's completion reward is 9 coins, item 9122 x1, 50 XP (profile 14), and collection_add 122. This is the set reward, not a per-item acquisition source for Blue Carnation.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14994-15013"},
  {"claim": "Bird of Paradise entries (locale 67112-67116) are a separate group and are not part of the Carnations set. The previous answer's 'nine entries' count and locale:3530009112 citation were wrong; locale:3530009112 does not exist. Locale 132498 is the separate 'Snowhill Carnations Collection' line.", "source": "locale lookup; id_check in pack"},
  {"claim": "No wiki page, article, video frame, vendor stock, quest reward, or drop names Blue Carnation. lookup for 'Blue Carnation' returns only the client text entry locale:67111.", "source": "lookup (client, wiki, articles, video) for 'Blue Carnation'"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition is not established. The first-pass 'drop' guess has no evidence and is not listed as a source.",
  "Catalogue item_link 'sanctuary' suggests the item is tied to the Sanctuary community server data, not to a verified live source. Live status is therefore unsure, not confirmed yes.",
  "The collection 186 completion reward (9 coins, item 9122, 50 XP) is the set's reward and is not listed as a source for the item.",
  "Needs a wiki page, article, or video that names how a Blue Carnation is obtained, or a confirmation that it is a collection-only entry, before it is wireable."
 ]}
