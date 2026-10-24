<!-- fleet job=citem-infer id=ct-rexy-spine-41047-v1 status=done turns=11 usd=0.0055 tokens(read,write,in,out)=[111090, 15935, 24, 4696] model=claude-haiku-5-5 -->
# T-Rexy Spine

{"item": {"name": "T-Rexy Spine", "locale_id": 41047, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry (index 1, 'T-Rexy Spine', item_definition_id 3831) of the 'Spine Fossils' collection (catalogue id 106, name_id 7757). Its description, 'This item can be added to the Spine Fossils Collection', is locale:132365. Only collection members are added by this item.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8638-8654; locale:132365; wiki 'List of Collections' lists 'Spine Fossils' (repo:prototype/osfr-tools/data/content/collections.json:11074-11101, key wiki:7:216)"},
  {"type": "collection", "detail": "Reward for completing the fossil collection catalogue id 103 (name_id 7754). The reward block grants 8 coins, 50 profile-16 XP, item 3831 (T-Rexy Spine) x1, and unlocks collection 106 (Spine Fossils).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8410-8428 (reward block inside id 103, which spans lines 8329-8431)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item 3831 is a member of the 'Spine Fossils' collection (entry index 1), with name_id 41047 and description locale:132365.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8638-8654; locale:132365"},
  {"claim": "The 'Spine Fossils' collection exists on the wiki List of Collections under Rare/Fossils group.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); repo:prototype/osfr-tools/data/content/collections.json:11074-11101"},
  {"claim": "Item 3831 is also granted as a reward of collection catalogue id 103 (the earlier fossil collection), together with 8 coins and 50 XP.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8410-8428"},
  {"claim": "The client's name cluster (locale 41042-41052) is a set of fossil collection items: Sabertooth teeth/skull, T-Rexy, Brachio-sore-ous, Stego-limp-ous, Veloci-rapture, Seismo-trucka-saurus, Galli-mimimimus spines.", "source": "client text cluster in the evidence pack (locale:41042-41052)"}
 ],
 "confidence": 0.6,
 "open": [
  "No coin store price in the client definition (coin_store_prices empty), so there is no coin vendor or Station Cash source for this item.",
  "No wiki article or video names T-Rexy Spine. The wiki list only confirms the Spine Fossils collection exists, with no entry list or reward.",
  "Collection 103's wiki name is unresolved: name_id 7754 is not in the client locale table. The list of wiki-named fossil collections suggests it is a fossil set, but the exact name is not confirmed.",
  "How the player gets the collection-103 reward (quest, drop, or dig) is not in the repo data. The catalogue shows the reward, not the trigger.",
  "Source type is 'collection' and the reward is 'collection' by catalogue wiring. The item is not a standalone purchasable item.",
  "Retired status is unknown. No source states that the Spine Fossils collection or its reward was retired or made unobtainable."
 ]}
