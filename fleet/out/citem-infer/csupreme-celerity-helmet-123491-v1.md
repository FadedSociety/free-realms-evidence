<!-- fleet job=citem-infer id=csupreme-celerity-helmet-123491-v1 status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[62842, 25436, 14, 4263] model=claude-haiku-5-5 -->
# Supreme Celerity Helmet

{"item": {"name": "Supreme Celerity Helmet", "locale_id": 123491, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store (Legacy CoinStoreItems listing, category 101, tint group 1) for definition 43492; purchase price 1266 coins, member price 1139 coins, resale 126 coins. No NPC vendor named in our data.", "where": "Coin Shop (coin store)", "price": "1266 coins (member price 1139 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 43492 (line 12862)"},
  {"type": "vendor", "detail": "Coin store listing, category 101, tint group 2 for definition 43499; purchase price 9453 coins, member price 8507 coins, resale 945 coins.", "where": "Coin Shop (coin store)", "price": "9453 coins (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 43499 (line 12863)"},
  {"type": "vendor", "detail": "Coin store listing, category 101, tint group 3 for definition 43506; purchase price 9453 coins, member price 8507 coins, resale 945 coins.", "where": "Coin Shop (coin store)", "price": "9453 coins (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 43506 (line 12864)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Supreme Celerity Helmet' (locale 123491), in the same set as Supreme Celerity Jacket/Shoes/Gloves/Pants (123488-123494).", "source": "locale:123491"},
  {"claim": "Of the 16 client definitions, only 3 (43492, 43499, 43506) have a coin store row; the 'coin_store_prices' in the pack (1266 and 9453) are prices, resolved here to these rows by the matching item ids.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12862-12864"},
  {"claim": "Store rows are Legacy CoinStoreItems data (source tag L1), with member discount 10% and sell price 10% of purchase.", "source": "repo:prototype/osfr-tools/data/content/stores.json header source_tags L1, T633"},
  {"claim": "Sibling helmets (Extreme/Ultimate Celerity Helmet) exist in the client but no wiki page or article covers Supreme Celerity Helmet; no lookup hit for 'Supreme Celerity' in wiki, articles or video.", "source": "lookup: client, wiki, articles, video (no matches beyond locale:123491)"}
 ],
 "confidence": 0.5,
 "open": [
  "Nine of the 16 definitions (43514, 43520, 43528, 43535, 43543, 43548, 43557, 43562, 43569) have no coin store row in stores.json, so their source and price are unknown; they may be non-coin or unsold variants.",
  "The coin store rows name no NPC vendor or shop location; the 'Coin Shop' label is inferred from the Legacy coin store data, not from a wiki page. Exact vendor and zone unknown.",
  "No wiki page, image, article or video names this helmet, so the wiki-side source and any retirement date are unverified.",
  "Live status is unsure: the coin store rows show a live price, but no retirement or availability source was found.",
  "The pack's wiki price check and Coin Shop/SC Marketplace category could not be confirmed for this item.",
  "The client's shared 'Celerity' rank-unlock entries (repo: scripts/pieces/piece_041.py, restoration/piece_041.rs) cover Extreme/Ultimate Celerity Jacket, not Supreme; not confirmed as a source for this helmet."
 ]}
