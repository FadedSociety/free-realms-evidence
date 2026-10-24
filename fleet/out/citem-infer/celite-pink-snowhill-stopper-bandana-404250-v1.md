<!-- fleet job=citem-infer id=celite-pink-snowhill-stopper-bandana-404250-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[22326, 12479, 10, 2082] model=claude-haiku-5-5 -->
# Elite Pink Snowhill Stopper Bandana

{"item": {"name": "Elite Pink Snowhill Stopper Bandana", "locale_id": 404250, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale of the Elite Pink Snowhill Stopper Bandana (store item 61820, category 101, the same category as other clothing listings). The record gives a purchase price of 9453 coins; members get 10% off (8507 coins). Vendor/shop name is not given in the record.", "where": null, "price": "9453 coins (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14512 (item_id 61820)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name for definition 61820 is 'Elite Pink Snowhill Stopper Bandana' (locale 404250), slot 1 (head), class 134, model athletics_<race>_<gender>_head_bandana.adr", "source": "locale:404250"},
  {"claim": "Same-name cluster: Snowhill Stopper Bandana (404245) and Elite Black Snowhill Stopper Bandana (404251); the Elite Pink variant is one of a set of bandana colours", "source": "locale:404245, locale:404251"},
  {"claim": "Coin store record for item 61820 exists: purchase 9453 coins, member price 8507 coins, sell price 945 coins, not flagged no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:14512"},
  {"claim": "No wiki page, article fact, video frame, vendor stock list, quest reward or drop names this item in the pack", "source": "lookup of wiki, articles, client and video for 'Snowhill Stopper Bandana' returned only the three client locale lines"}],
 "confidence": 0.5,
 "open": ["The store record does not name the vendor or shop; 'coin_shop' is inferred from the coin store price, not from a wiki category. Confirm whether it is the Coin Shop or a coin vendor.",
  "No wiki or forum source confirms when it was sold or whether it was retired. The store record's no_sale=false suggests it was still sellable in the data snapshot, but the date is unknown.",
  "The stores.json source_tags (L1, L2, L4, R2, T633, R1) are build tags, not named sources, so they were not used as evidence.",
  "The description is empty, and the 'Elite' versus plain Snowhill bandana difference (Elite tint or stat tier) is not stated in the pack.",
  "Other sources (quest, drop, prize wheel, event) were not checked beyond the pack."]}
