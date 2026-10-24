<!-- fleet job=citem-infer id=cpitiful-fossil-41022-v4 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5846, 8475, 6, 1767] model=claude-haiku-5-5 -->
# Pitiful Fossil

{"item": {"name": "Pitiful Fossil", "locale_id": 41022, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item locale 41022 is 'Pitiful Fossil'; its description is 'This item can be added to the Mini Fossils Collection' (locale:132361 is the Mini Fossils Collection UI string).", "source": "locale:41022; locale:132361"},
  {"claim": "Collection 102 'Mini Fossils' lists this piece as entry 8 of 8: item_definition_id 3806, name_id 41022. Entries 1-7 are definitions 3799-3805.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8303"},
  {"claim": "Set-completion reward for collection 102 is 7 coins, item 3814 x1, 50 XP. This is a reward for finishing the whole set, not a price or source for Pitiful Fossil itself.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8307-8326"},
  {"claim": "The wiki 'List of Collections' page lists '[Mini] [Fossils]' among its collections, confirming the set is a wiki-listed collection. This is a collection listing, not an acquisition source.", "source": "wiki page: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "The only price hit is repo:data/content/stores.json:12554 {item_id 41022, category 101, tint group 3, purchase 9453 coins, member 8507, sell 945}. The same 9453/8507/945 triple repeats across many unrelated rows (41017, 41018, 41023, and rows like 41012 with 828), so it reads as a reconstructed shared-pattern price. Our stores.json is a reconstructed reference, not client evidence. Its id type is unresolved and no vendor name for category 101 was found. Not listed as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12552-12555"},
  {"claim": "No stores.json row keys on definition 3806, and the client coin_store_prices list is empty. No vendor stock, wiki article, article fact or video names the item.", "source": "repo:prototype/osfr-tools/data/content (search for 3806); lookup wiki/articles/video"}
 ],
 "confidence": 0.3,
 "open": [
  "Possible coin vendor source: stores.json:12554 at 9453 coins (member 8507), category 101. Unlisted because the id type (definition vs name_id) is unresolved, the price pattern is shared across many rows, and the category's vendor is unknown. If confirmed as this item, add a vendor source and set live to 'yes'.",
  "The 7-coin collection reward is for completing the Mini Fossils set, not a purchase price; not listed as a source.",
  "No drop source is evidenced. The earlier 'sparkling spawn' drop was removed: the wiki only says collection pieces come from sparkling spawn objects in general.",
  "Live status is unsure: the item exists in the client and the wiki collections list, but no source shows it was obtainable. No retirement date is sourced.",
  "Icon tint variant and drop rate are unsourced."
 ]}
