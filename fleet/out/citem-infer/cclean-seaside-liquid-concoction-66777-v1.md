<!-- fleet job=citem-infer id=cclean-seaside-liquid-concoction-66777-v1 status=done turns=10 usd=0.0053 tokens(read,write,in,out)=[87693, 15426, 22, 4998] model=claude-haiku-5-5 -->
# Clean Seaside Liquid Concoction

{"item": {"name": "Clean Seaside Liquid Concoction", "locale_id": 66777, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry (slot 2 of 8) in the Seaside Liquid Concoction Collection (catalogue id 145, name locale 67511); the collection's own reward is 1 item 23212 plus 4 coins and collection_add 151", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11030-11056 (record id 145, item_definition_id 23164 at index 2); wiki:List of Collections (Seaside [Liquid] [Concoction], wiki:8:239 in repo:prototype/osfr-tools/data/content/collections.json:11718-11745)"},
  {"type": "quest_reward", "detail": "Reward for completing the Seaside Water Samples collection (catalogue id 117, name locale 7768): 7 coins, 1 x item 23164, XP 50, collection_add 145. Listed as a collection-completion reward, not a quest or vendor sale", "where": "Seaside", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9743-9844 (record 117, reward block at 9824-9843); locale:7768 'Seaside Water Samples'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client definition: item definition 23164, name locale 66777 'Clean Seaside Liquid Concoction', description 'This item can be added to the Seaside Liquid Concoction Collection' (locale:132404 family), no coin store price, no model files", "source": "locale:66777; locale:132404"},
  {"claim": "Seaside Liquid Concoction collection (id 145) lists item 23164 as one of its eight entries, alongside Toxic (23163), Purified (23165), Dirty (23166), Boiling (23167), Freezing (23168), Magical (23169), Mystical (23170)", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11030-11111"},
  {"claim": "Item 23164 is also in the reward block of the Seaside Water Samples collection (id 117), which rewards it with 7 coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9824-9843"},
  {"claim": "The wiki List of Collections includes 'Seaside [Liquid] [Concoction]' as a collection, so the collection is a real live collection on the wiki", "source": "wiki:List of Collections (revision 27852, 2013-07-13)"},
  {"claim": "Sibling items Clean/Toxic/Purified Merry Vale and Sanctuary concoctions share the same collection pattern and text, supporting that these are collection-only entries", "source": "locale:66769, locale:66768, locale:66792-66799, locale:132406"}
 ],
 "confidence": 0.6,
 "open": [
  "No wiki page, article, image or video names this item directly; the collection-entry and reward evidence come only from the repo catalogue, not from a player-facing source.",
  "No coin store price in repo:data/content/stores.json and no coin vendor stocks it, so no vendor or Coin Shop source is claimed.",
  "The Seaside Water Samples reward (catalogue 117) lists entries with item_link 'sanctuary' and Sanctuary-area item ids (3919-3926); the reward linkage may be a catalogue data error. Verify against a live reward or wiki Seaside Water Samples page before relying on it.",
  "Whether the item was a one-time reward or repeatable, and its exact drop/craft origin, are unknown; the 'Clean' variant is one of eight Seaside concoction tints, the collection tag says 'Liquid Concoction', and the first-pass guess 'live: yes' is not independently confirmed.",
  "Exact completion requirement for collection 145 (all 8 entries) is not stated in the pack; the reward of collection 145 itself (item 23212, 4 coins) is unverified against the wiki."
 ]}
