<!-- fleet job=citem-infer id=crock-digger-hat-6129-v2 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[17419, 9309, 10, 2075] model=claude-haiku-5-5 -->
# Rock Digger Hat

{"item": {"name": "Rock Digger Hat", "locale_id": 6129, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, store category 101 (vendor not identified in repo data); base 270 coins, member price 243 coins. Rows exist for definition ids 237 (tint_group 1), 2489 (tint_group 2) and 2490 (tint_group 3).", "where": null, "price": "270 coins (member 243 coins; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 150 (item 237), line 669 (item 2489), line 670 (item 2490)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name string exists: locale:6129 'Rock Digger Hat'. It belongs to the Rock Digger / Dirt Farmer worker-outfit family (6123 Rock Digger Helmet, 6125/6126 Elite Pink/Black Rock Digger Helmet, 6128/6132/6134 Dirt Farmer Hat variants, 6140 Rock Digger Overalls, 6141 Rock Digger Pants).", "source": "locale:6129; locale:6123; locale:6125; locale:6126; locale:6128; locale:6132; locale:6134; locale:6140; locale:6141"},
 {"claim": "Store data has coin-store rows for three of the hat's definition ids (237, 2489, 2490), each purchase 270 coins, member 243 coins, sell 27 coins, category 101, no_sale false. The previous answer's claim that the store entry is keyed only to item 270 was wrong: item 270 is a separate item, and no store row for item_id 270 was found in the check.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 150, 669, 670"},
 {"claim": "The store rows carry source tags L1, L2, L4, R2, T633, R1 and no_sale false. Those tags are undecoded, but no_sale false means the row is an active sale entry, so the hat is treated as live. Other category 101 rows share the same 270-coin price, so the price alone is not unique to this hat.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 150, 669, 670; same tags on other category 101 rows (e.g. item 76, 106, 124)"},
 {"claim": "Name lookup across client, wiki, articles and video returned only client text; no wiki page, article, video frame, quest reward or drop names the hat.", "source": "lookup: 'Rock Digger Hat OR Dirt Farmer Hat OR Prospector Hat' (client, wiki, articles)"}],
 "confidence": 0.5,
 "open": ["The vendor NPC or shop that sells category 101 item 237/2489/2490 is not named in the repo data; the coin-store sale is confirmed only by the store row. Identify the vendor or shop before wiring it as a specific vendor.",
 "The store row for 21637-21652 (the other definition ids) was not checked; only 237, 2489 and 2490 were confirmed.",
 "No wiki, article, video or quest evidence confirms the hat or its set; the worker-outfit set origin is unverified.",
 "Retired status is unknown: no source states that the store entry was removed.",
 "Client description is empty, so no in-game text confirms availability."]}
