<!-- fleet job=citem-infer id=candy-hair-style-card-114550-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[25136, 16163, 10, 2742] model=claude-haiku-5-5 -->
# Andy Hair Style Card

{"item": {"name": "Andy Hair Style Card", "locale_id": 114550, "kind": "card"},
 "sources": [{"type": "vendor", "detail": "Coin store sale of the Andy Hair Style Card (store entry for definition 35937, category 141, purchase price 540 coins, member price 486 coins, no_sale true). The stores file names no vendor or shop, so the exact vendor/shop is unresolved.", "where": null, "price": "540 coins (member price 486 coins, about 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 35937"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name is locale:114550 'Andy Hair Style Card', description 'You'll be a Sites for sore eyes.', slot 2, class 1, with 2 definitions (6841 and 35937); the coin store price 540 comes from definition 35937.", "source": "locale:114550; client definition pack"},
  {"claim": "Store entry for item 35937 is category 141 at 540 coins, but it is flagged no_sale: true, so it is not currently sellable in that entry.", "source": "repo:data/content/stores.json item 35937"},
  {"claim": "Definition 6841 has no store entry of its own; it sits in a block of category 141 entries (item_ids 6826-6846, all 540 coins, sell price 54 coins, no_sale false) that look like the hair-card set, which suggests the card was sold at 540 coins in that block.", "source": "repo:data/content/stores.json lines 1841-1860"},
  {"claim": "Sibling hair style cards (Spacey 114545, Jubei 114546, Mane 114547, Sassy 114548, Silky 114549, Mohawk 114552, Reagan 114553, Bob 114554, Curly 114555) share the 'Hair Style Card' naming and cluster with this item in the client text table.", "source": "locale:114545-114555 (client text cluster)"},
  {"claim": "Wiki Super Spooktacular page (week 1, 10/1/2013) notes that new hair color/style cards were introduced in October 2013 (Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum). Andy is not named there, so its release date is unconfirmed.", "source": "wiki: Super Spooktacular"}],
 "confidence": 0.4,
 "open": ["The exact vendor or shop that sells the card is not named in the repo store data (category 141 has no name) and no wiki page covers Andy. Needs a wiki Coin Shop or hair-card category check.",
  "Whether the card is still sold is unclear: the 35937 entry is no_sale, while the 6826-6846 block is on sale. Need to confirm which definition is live.",
  "No wiki price or second source for the 540-coin price. Not checked against a sale price.",
  "No quest, drop, event, or collection source found; the cluster lookup returned no other sources.",
  "The wiki text for hair cards was only found in the Super Spooktacular page, so the release window for Andy's card is unknown."]}
