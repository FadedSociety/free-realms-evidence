<!-- fleet job=citem-infer id=croyal-doll-shirt-40748-v1 status=no_submit turns=6 usd=0.0051 tokens(read,write,in,out)=[67784, 21979, 14, 3334] model=claude-haiku-5-5 -->
# Royal Doll Shirt

```json
{"item": {"name": "Royal Doll Shirt", "locale_id": 40748, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Royal Doll Collection (wiki 'Royal Doll', 8 pieces: Gown, Shirt, Pants, Accessories, Gloves, Shoes, Boots, Crown). Completing it gives Queen Royal Doll plus 21 coins. The client text at locale:132327 says this item 'can be added to the Royal Doll Collection'.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json (key wiki:4:118, client_id 1073741942, name_id 7719, reward wiki_lines 'Queen Royal Doll', '21'); wiki page 'Toys (Collections)' (https://freerealms.fandom.com/wiki/Toys_(Collections), revision 31048); locale:132327; locale:7719"},
  {"type": "drop", "detail": "Robgoblin (collection-level spawn_type 'Robgoblin'). Per-piece drop not confirmed for the Shirt.", "where": "Central Wilds", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json (key wiki:4:118, spawn_type 'Robgoblin', area 'Central Wilds')"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Royal Doll Shirt' is locale 40748, definition id 3532, slot 0, class 0, with no models and no coin store price.", "source": "locale:40748; client definition supplied in the pack"},
  {"claim": "Client text says the item can be added to the Royal Doll Collection.", "source": "locale:132327"},
  {"claim": "The wiki collection 'Royal Doll' lists Royal Doll Shirt as one of its 8 entries, with reward Queen Royal Doll and 21 coins.", "source": "repo:prototype/osfr-tools/data/content/collections.json wiki:4:118; wiki page 'Toys (Collections)'"},
  {"claim": "The wiki 'List of Collections' page lists '[Royal] [Doll]' as a collection.", "source": "lookup wiki page 'List of Collections'"},
  {"claim": "The wiki 'Toys (Collections)' page lists [Royal] [Doll] Shirt among the doll collection pieces.", "source": "lookup wiki page 'Toys (Collections)'"},
  {"claim": "The first-pass tag 'collection' agrees with the wiki and client text. It is a hint only.", "source": "jev_first_pass"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki or repo source says the Shirt can be bought from a coin vendor, the Station Cash Marketplace or the Coin Shop. No coin store price exists for definition 3532.",
  "The Robgoblin/Central Wilds entry is the collection's spawn_type. It is not confirmed that single pieces drop from Robgoblins, so the drop source is weak.",
  "The reward is 'Queen Royal Doll' plus 21 coins, from the wiki collection record. Whether the reward is coins, the doll, or both is not clear from the record.",
  "Retirement status is unknown. No source gives a date or says it was removed.",
  "Two rows in the collection are not confirmed: the wiki list says 'Royal Doll Shoes' while the client also has 'Royal Doll Boots'. These are not checked against each other."
 ]}
```
