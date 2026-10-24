<!-- fleet job=citem-infer id=cpixiewood-doll-shirt-40596-v1 status=done turns=6 usd=0.0052 tokens(read,write,in,out)=[57275, 23093, 14, 3468] model=claude-haiku-5-5 -->
# Pixiewood Doll Shirt

{"item": {"name": "Pixiewood Doll Shirt", "locale_id": 40596, "kind": "collection"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, 358 coins (member price 322, sell-back 35); store row lists item_id 40596, category 102, no tint group recorded beyond tint_group_id 1. Mapping of store item_id to item definition is unverified: the row's id equals the locale id, not the definition id 3380, so treat this as probable, not confirmed.", "where": null, "price": "358 coins (member price 322 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12488 (item_id 40596)"},
  {"type": "collection", "detail": "Pixiewood Pixie Doll Collection (client locale:132308 'This item can be added to the Pixiewood Pixie Doll Collection'); item is entry 3 of the collection (definition 3380, icon 2730) in the Pixie Woods doll collection group (name locale 7700)", "where": null, "price": null, "currency": null, "source": "wiki: Toys (Collections) and List of Collections list 'Pixiewood Doll Shirt' under the Pixiewood Pixie Doll collection; repo:prototype/osfr-tools/data/content/collection_catalogue.json line 2764"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item name locale 40596 is 'Pixiewood Doll Shirt', in the Pixie Woods doll-piece set with 40594 Cap, 40595 Jacket, 40597 Pants, 40598 Gear, 40599 Ring, 40600/40601 Shoes/Boots", "source": "locale:40596"},
  {"claim": "Item definition 3380 is collection entry 3 of the Pixiewood doll collection group (name 7700 'Pixiewood Pixie Doll')", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json line 2764-2768"},
  {"claim": "Wiki Toys (Collections) page lists 'Pixiewood Doll Shirt' as a piece of the Pixiewood Pixie Doll collection", "source": "wiki page: Toys (Collections)"},
  {"claim": "Store data prices 40596 at 358 coins, category 102, same price as sibling pieces 40595 and 40600/40601", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12487-12490"},
  {"claim": "Client description says the item is added to the Pixiewood Pixie Doll Collection (not a standalone sale)", "source": "locale:132308"}
 ],
 "confidence": 0.5,
 "open": [
  "The pack's coin_store_prices is empty, but stores.json has an entry keyed 40596 at 358 coins. Whether that key is the item definition (3380) or the name locale id is not verified; the coin sale is unconfirmed until checked against the store's item-definition mapping.",
  "No store vendor name, zone, or shop was found for the coin sale; the 'where' field is null.",
  "The wiki gives no price or acquisition text for the piece itself; the collection's reward for completing the Pixiewood set is a separate item (the 'Pixiewood Pixie Doll' reward) and is not this shirt.",
  "No wiki page exists for this item; no quest, enemy drop, prize wheel, or event source was found.",
  "Retirement status is not stated by any source; the coin-store row has no no_sale flag set to true, so it is probably still sold, but this is unverified.",
  "Pack critique check: the pack carried no critiques to fix."
 ]}
