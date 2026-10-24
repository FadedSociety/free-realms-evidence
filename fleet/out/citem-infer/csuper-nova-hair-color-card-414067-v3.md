<!-- fleet job=citem-infer id=csuper-nova-hair-color-card-414067-v3 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[6186, 8924, 6, 1270] model=claude-haiku-5-5 -->
# Super Nova Hair Color Card

{"item": {"name": "Super Nova Hair Color Card", "locale_id": 414067, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Super Nova Hair Color Card', description 'This style card allows you to change your hair color.'", "source": "locale:414067"},
  {"claim": "Store row item_id 35962, category 142, purchase_price_coins 180, member_price_coins 162, sell_price_coins null, no_sale true. Row is one of a uniform block (items 35952-35972) with identical values and no_sale true; the row does not name this card.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7895 (block 7885-7905)"},
  {"claim": "Lookup of the name across wiki, client, video and articles returns only the client locale entry. No wiki page, article, video frame, quest, drop, event or crafting source names this card.", "source": "lookup 'Super Nova Hair Color Card' (client only hit: locale:414067)"},
  {"claim": "The coin-store row is matched to client definition 35962 by number only. Definition 68829 has no store row and no source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7895; client definition ids 35962, 68829"}
 ],
 "confidence": 0.2,
 "open": [
  "No evidenced acquisition source. The prior coin_shop entry is withdrawn: the 180/162 price belongs to a 21-row no_sale block (35952-35972) and is not shown to name this card. The 'Coin Shop' label for category 142 and sibling prices (162 for Gold Rush, Atomic Blast, Sun Kissed, Shock Wave) came from frames not in this pack and do not name Super Nova.",
  "Live status: the only store row is no_sale with no sell price, so no current coin sale is evidenced. Treat as unknown.",
  "Retirement date not stated by any source.",
  "Definition 68829 is unverified.",
  "Needed to close: a wiki or video frame naming Super Nova Hair Color Card with its vendor/store, or a store row keyed to a named category/vendor for item 35962."
 ]}
