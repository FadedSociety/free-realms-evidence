<!-- fleet job=citem-infer id=cn-kitty-frog-legs-pl-kitty-frog-legs-110377-v3 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[13735, 10376, 8, 2084] model=claude-haiku-5-5 -->
# {n}Kitty Frog Legs{pl="Kitty Frog Legs"}

{"item": {"name": "Kitty Frog Legs", "locale_id": 110397, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale; selling NPC not identified (store category 6 is shared by unrelated items, so it names no vendor)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell price 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 34568 (line 11138); same 270/243/27 row for items 34569-34592 (lines 11139-11162)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Kitty Frog Legs'. Locale 110377 is the raw-markup form ({n}Kitty Frog Legs{pl=...}); locale 110397 is the clean plain-text duplicate.", "source": "locale:110377; locale:110397"},
  {"claim": "Client definition: slot 5, class 61, model pet_cat_<descriptor>_feet_animalboots.adr (cat boots); 34 definitions, the listed ids are 34568-34579.", "source": "pack client_definition"},
  {"claim": "Store rows give 270 coins purchase, 243 member, 27 sell, category 6, with no tint group, for every id from 34568 through at least 34592. The rows are a block and do not show which NPC sells the item; they cannot be tied to the 12 item definitions alone.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11138-11162"},
  {"claim": "Lookup of 'Kitty Frog' finds only client strings (Kitty Frog Outfit 72335, Kitty Frog Suit 109957, Kitty Frog Skin 109977, Kitty Frog Face 110447, Kitty Frog Eyes 110467, Kitty Frog Collar 110572, Kitty Frog Fly Collar 110552). No wiki page, article, or video names Kitty Frog Legs, so no wiki, article, or video source exists for sale or retirement.", "source": "lookup client/wiki/articles, query 'Kitty Frog'"},
  {"claim": "The prior 'Coin Shop' guess has no support and was dropped.", "source": "lookup wiki/articles, no hits"}
 ],
 "confidence": 0.4,
 "open": [
  "The vendor source rests only on repo store rows (category 6, 270 coins). No NPC, zone, or stock file names a vendor for it, and no wiki or video confirms a sale. Treat it as a price note until the vendor/stock data maps category 6 rows to an NPC.",
  "The store block runs at least 34568-34592, wider than the item's 12 listed definitions (34568-34579) and the stated 34 definitions. The exact range of the 34-definition set (through 34601) was not verified; the stores.json check reached only 34592.",
  "The client definition carries coin_store_prices [270] in the pack; that figure is the same price as the store row and is not a separate source.",
  "Live status is unsure: no source confirms the item is currently or was ever sold in game. Retired status is unknown.",
  "Locale 110377 contains raw localization markup (dev_note); the rebuild should display 'Kitty Frog Legs' and key on the clean string 110397 (the id check flags 110397 as a duplicate, not as non-live). Name citations are client strings only, not live evidence.",
  "Sibling items (Kitty Frog Outfit 72335, Kitty Frog Suit 109957, Doggy Frog Legs 111077) have no linked source and do not bear on this item's status."
 ]}
