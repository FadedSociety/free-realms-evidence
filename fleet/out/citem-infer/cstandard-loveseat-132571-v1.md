<!-- fleet job=citem-infer id=cstandard-loveseat-132571-v1 status=no_submit turns=6 usd=0.0041 tokens(read,write,in,out)=[55892, 18176, 14, 2476] model=claude-haiku-5-5 -->
# Standard Loveseat

```json
{"item": {"name": "Standard Loveseat", "locale_id": 132571, "kind": "furniture"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop purchase, housing furniture listing (store category 53). Two definitions, 15598 and 36158, both list 600 coins with a 10% member price of 540.", "where": "Coin Shop", "price": "600 coins (member price 540 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15598 (line 3991); repo:prototype/osfr-tools/data/content/stores.json item 36158 (line 11831); repo:notes/Research/Coin Shop.md lines 30-32 (stores.json rows are the CoinStoreItems catalogue)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for the item is 'Standard Loveseat', locale 132571, kind item.", "source": "locale:132571"},
  {"claim": "Client definition has two variants, 15598 and 36158, both with model hsg_loveseat_01.adr, slot 0, class 0.", "source": "client definition in pack"},
  {"claim": "Both variants have a coin store price of 600, with a 10% member price of 540 and a sell-back of 60 (sell-back is server policy, not a source).", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15598 (line 3991) and item 36158 (line 11831)"},
  {"claim": "The stores.json coin rows come from the reference CoinStoreItems catalogue, so they are Coin Shop prices and not vendor-stock records.", "source": "repo:notes/Research/Coin Shop.md lines 30-32"},
  {"claim": "Sister housing items in the same listing block (15586-15602, category 53) carry coin prices of 50 to 900, so the 600 price fits the same furniture shop.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3979-3995"},
  {"claim": "Client text cluster 132566-132576 is the housing set (lounge chairs, mailbox, microwave, mirrors, holiday lights), so the item belongs to a housing furniture group.", "source": "pack client_cluster, locale:132566-132576"},
  {"claim": "No wiki page, article, video frame, quest, drop or event names the Standard Loveseat.", "source": "lookup over wiki, articles and client returned only locale:132571; pack wiki_page null, video []"}
 ],
 "confidence": 0.55,
 "open": [
  "The source of the 600-coin price is the reference Coin Shop catalogue. No wiki page or live capture confirms the item is currently on sale in the Coin Shop, so availability today is unverified.",
  "Retirement status is unknown. No source says the item was delisted.",
  "The store data has no vendor record. No coin vendor NPC stocks it in the pack, so no vendor source is listed.",
  "The description is empty, so the item's housing function is inferred only from the cluster and model name.",
  "The two definitions (15598 and 36158) have different tint groups (1 and null). Whether they differ in look or are duplicates is not established."
 ]}
```
