<!-- fleet job=citem-infer id=ctera-fopy-wing-41032-v2 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[25244, 10179, 10, 2833] model=claude-haiku-5-5 -->
# Tera-fopy Wing

{"item": {"name": "Tera-fopy Wing", "locale_id": 41032, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Reward for completing collection id 105 (name_id 7756, Shark Teeth-set family, entries 3823-3830): grants 1x item 3816 (Tera-fopy Wing), 2 coins, 50 XP, and adds the item to collection 104 (Bird Wing Fossils). The completion condition of collection 105 is not yet verified.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8534-8636 (reward block 8616-8635)"},
  {"type": "collection", "detail": "Bird Wing Fossils collection (id 104, entry index 2): the item is a member entry of this collection; it is a collection piece, not a standalone vendor or drop item.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8452-8456; locale:7755; wiki List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections), Rare > [Bird] [Wing] [Fossils]"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item name 'Tera-fopy Wing' is locale 41032 and is entry 2 of collection 104 (Bird Wing Fossils), definition 3816.", "source": "locale:41032; repo:prototype/osfr-tools/data/content/collection_catalogue.json:8452-8456"},
  {"claim": "Collection 105's reward block grants 1x item 3816, 2 coins, 50 XP, and collection_add 104; the block sits inside collection 105's object (lines 8534-8636), so it is that collection's completion reward, not a misattributed block.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8616-8635"},
  {"claim": "The Bird Wing Fossils collection name is locale 7755 and its description is locale 7831 ('A collection of bird wing fossils. Buffalo dinosaur wings anyone?').", "source": "locale:7755; locale:7831; repo:prototype/osfr-tools/data/content/collections.json:11190"},
  {"claim": "The item description 'This item can be added to the Bird Wing Fossils Collection' is the UI string locale:132363.", "source": "locale:132363"},
  {"claim": "The wiki's List of Collections lists '[Bird] [Wing] [Fossils]' under Rare, with no retirement note.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "No coin vendor, marketplace, prize wheel, or drop listing for item 3816 was found; the client definition has no coin_store_prices.", "source": "client definition; lookup of wiki/client for 'Bird Wing Fossils'"}
 ],
 "confidence": 0.5,
 "open": [
  "Completion condition of collection 105 (the source of the reward) is not verified. Its name (name_id 7756) could not be looked up in the locale table; it appears to be the Shark Teeth Fossils set (the Shark Teeth UI string is locale 132362), but this is unconfirmed.",
  "The collection-105 reward granting a Bird Wing into collection 104 is an unusual cross-set link; confirm it against a live source before wiring.",
  "No coin store price (coin_store_prices empty) and no wiki or vendor price. Not sold per any source found.",
  "Retired status unknown: the wiki list (rev 27852, 2013-07-13) has no retirement note, and no later source was found.",
  "Live status rests on the first-pass tag and the wiki list entry, not an independent live check.",
  "Critique correction applied: the earlier citation locale:2503781342 does not exist and was replaced with locale:132363; the earlier collection name citation locale 1601176989 was replaced with locale:7755."
 ]}
