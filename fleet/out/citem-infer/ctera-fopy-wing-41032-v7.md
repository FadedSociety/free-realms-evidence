<!-- fleet job=citem-infer id=ctera-fopy-wing-41032-v7 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[6002, 6852, 6, 1733] model=claude-haiku-5-5 -->
# Tera-fopy Wing

{"item": {"name": "Tera-fopy Wing", "locale_id": 41032, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Completion reward of the Sabertooth Fossils collection (collection 105, name_id 7756). The repo reward block grants 1x item 3816, 2 coins, 50 XP (profile 11) and collection_add 104 (Bird Wing Fossils). The in-game completion condition is NOT verified, so this is an unconfirmed acquisition path, not a wireable source.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8616-8635 (reward block, re-read and confirmed); locale:7756; locale:132364"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 'Tera-fopy Wing' is locale 41032, item_definition_id 3816, entry 748 of collection 104 (Bird Wing Fossils), item_link 'sanctuary'.", "source": "locale:41032; repo:prototype/osfr-tools/data/content/collection_catalogue.json:8449-8457"},
  {"claim": "Collection 105 is 'Sabertooth Fossils' (name_id 7756); its reward block grants item 3816 x1, 2 coins, 50 XP and collection_add 104.", "source": "locale:7756; repo:prototype/osfr-tools/data/content/collection_catalogue.json:8616-8635"},
  {"claim": "Bird Wing Fossils collection name is locale 7755; the item's description is locale 132363 ('This item can be added to the Bird Wing Fossils Collection').", "source": "locale:7755; locale:132363"},
  {"claim": "The wiki's List of Collections lists '[Bird] [Wing] [Fossils]' under the Rare heading with no retirement note.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "No coin store price (client coin_store_prices empty), no vendor stock, no drop, prize wheel, or marketplace listing found for item 3816.", "source": "client definition; repo search for 3816 (only collection_catalogue.json 8455 and 8620)"}
 ],
 "confidence": 0.3,
 "open": [
  "wireable: false. The only source is a collection-completion reward whose in-game completion condition is unverified; per the rules, no evidenced price, vendor, quest, drop or event source exists yet.",
  "The Sabertooth Fossils completion condition must be confirmed in-game or in a source before the reward link is wired.",
  "The Sabertooth-to-Bird-Wing cross-set link (collection_add 104) needs in-game verification.",
  "The item's entry in collection 104 carries item_link 'sanctuary'; this is not an acquisition source but is noted.",
  "Retired status unknown: the wiki list has no retirement note and no later source was found.",
  "Live status unverified: 'yes' from the first-pass tag and the wiki list is not an independent live check, so it stays 'unsure'.",
  "The earlier citations locale:2503781342 and articles collections.vm were removed: the id does not exist and the articles citation could not be verified.",
  "The earlier 'Shark Teeth' identification of collection 105 is withdrawn; 7756 is Sabertooth Fossils."
 ]}
