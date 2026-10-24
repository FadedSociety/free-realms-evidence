<!-- fleet job=citem-infer id=cteeny-fossil-41018-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5517, 8439, 6, 1907] model=claude-haiku-5-5 -->
# Teeny Fossil

{"item": {"name": "Teeny Fossil", "locale_id": 41018, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 3802 is named 'Teeny Fossil' (locale 41018) and its description reads 'This item can be added to the Mini Fossils Collection'", "source": "locale:41018; locale:132361"},
  {"claim": "The Mini Fossils collection exists on the wiki's List of Collections page, listed as '[Mini] [Fossils]' under Rare", "source": "wiki: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); locale:7829 ('A collection of delicate mini-sized fossils.')"},
  {"claim": "Teeny Fossil is catalogue index 4 of the Mini Fossils set, with name_id 41018 and item_definition_id 3802", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 8262-8269"},
  {"claim": "stores.json has a coin row keyed item_id 41018 (category 104, tint group 2): purchase 9453 coins, member price 8507, sell 945, no_sale false. The same 9453 price also appears on item_ids 41017, 41022, 41023, so it looks like a shared price tier. The row is keyed by a name-range id, and the client definition (3802) has an empty coin_store_prices, so it is not confirmed that this row is for Teeny Fossil", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12552-12555"},
  {"claim": "No vendor, quest, drop, event or wiki page in the pack names Teeny Fossil as obtainable from any source", "source": "lookup of client and wiki text found only the collection entry; pack vendor_stock and mentioned_by_other_answers are empty"}
 ],
 "confidence": 0.25,
 "open": [
  "No confirmed acquisition source. The only price evidence is the stores.json row keyed item_id 41018; the critique showed the same 9453-coin price on several other ids, so this may be a shared tier and not a listing for this item. The mapping from stores item_id to definition 3802 is unconfirmed, and no vendor or store name is in the data. Do not treat the coin row as a source until the mapping and vendor are shown.",
  "The client definition's coin_store_prices is empty, which conflicts with the stores.json row. Unresolved.",
  "How Mini Fossils pieces are obtained (dig, drop, quest, purchase) is not documented in the pack or wiki. Check the Mini Fossils collection page on the wiki or a source naming it.",
  "The catalogue item_link 'sanctuary' is an unverified field value, not evidence of a source, so it was not used.",
  "Retired status and whether it is still obtainable are unknown."
 ]}
