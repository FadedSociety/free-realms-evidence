<!-- fleet job=citem-infer id=cn-crazy-crunch-pants-pl-crazy-crunch-pants-121684-v1 status=done turns=11 usd=0.0083 tokens(read,write,in,out)=[178523, 32327, 24, 4995] model=claude-haiku-5-5 -->
# {n}Crazy Crunch Pants{pl="Crazy Crunch Pants"}

{"item": {"name": "Crazy Crunch Pants", "locale_id": 121684, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Demolition Derby Driver job gear, rank-gated (ItemClasses class 22 'Demolition Derby Driver Gear'). Pants are one of the job's gear rows; the rank at which the pants unlock is not recorded. The only rank row in the Crazy Crunch set is the Crazy Crunch Shirt (locale 121680) at rank 3.", "where": "Demo Derby Driver job progression (trainers: Mad Jack at Wildwood, Crash Davis at Thunder Falls, Burt Wrecking Crewe at Frost Ridge)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:159 (DEMO_DERBY_DRIVER_GEAR rank 3, Crazy Crunch Shirt); repo:prototype/osfr-tools/src/restoration/piece_041.rs:68-69"},
  {"type": "coin_shop", "detail": "Coin store sale, price listed in the client definition (320 coins). Store row not located.", "where": null, "price": "320", "currency": "coins", "source": "client definition coin_store_prices (pack); repo:data/content/stores.json item lookup for definition ids 41685-41740 returned no match"},
  {"type": "coin_shop", "detail": "Coin store sale, price listed in the client definition (1266 coins); probably a later or second listing, not confirmed as a sale price.", "where": null, "price": "1266", "currency": "coins", "source": "client definition coin_store_prices (pack); repo:data/content/stores.json item lookup returned no match"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Crazy Crunch Pants' is locale 121684; 16 definitions (ids 41685-41740 in the pack's 12 listed ids) share the name.", "source": "locale:121684; client definition pack"},
  {"claim": "Crazy Crunch set (Shirt 121680, Boots 121681, Gloves 121682, Helmet 121683, Pants 121684) is the Demolition Derby Driver gear set, class 22 'Demolition Derby Driver Gear' (profile name id 17401).", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:68-70, 159"},
  {"claim": "Demo Derby Driver is a job (max rank 20); gear unlocks by job rank, and the client says Demo Derby Driver levelling gives new items at trainers.", "source": "repo:notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:223 (client locale 3308382417, 3932018899)"},
  {"claim": "Coin store prices 320 and 1266 are attached to the item in the client definition.", "source": "client definition coin_store_prices (pack)"},
  {"claim": "Client has no wiki article, article fact, video frame or vendor row naming Crazy Crunch Pants; lookup of 'Crazy Crunch' and 'Crunch Pants' returned no matches.", "source": "lookup wiki/articles/video, no matches"}
 ],
 "confidence": 0.3,
 "open": [
  "Coin store rows for 320 and 1266 are not in repo data/content/stores.json under the definition ids; need the store row to confirm which shop, the sale price and whether the 1266 price is a sale price or a second listing.",
  "Rank at which Crazy Crunch Pants unlock from Demo Derby Driver is unknown; the rank table only records the shirt (rank 3).",
  "Whether the Demo Derby Driver gear is sold by a trainer ('Demolition Derby Equipment' vendor:unknown, repo:prototype/osfr-tools/data/content/npcs_unresolved.json) is unverified.",
  "No wiki or video evidence for the pants; live status and retirement are unknown. First-pass 'live: yes' is a hint only and was not confirmed.",
  "Kind 'clothing' is from the client item class (slot 4, legs), not from a source.",
  "The 12 definition ids in the pack vs. the 16 definition count: the other 4 variants were not listed."
 ]}
