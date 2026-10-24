<!-- fleet job=citem-infer id=ctacky-holiday-tree-sweater-134464-v1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[20245, 13279, 10, 3125] model=claude-haiku-5-5 -->
# Tacky Holiday Tree Sweater

{"item": {"name": "Tacky Holiday Tree Sweater", "locale_id": 134464, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Gifting Tree (daily gift during the Snow Days holiday event; the sweater is one of the Tacky sweater gifts, received as a reward from the tree and its Candi Ivy quest chain, e.g. 'An Unexpected Gift')", "where": "Snowhill", "price": null, "currency": null, "source": "wiki page 'Snow Days' (Gifting Tree entry); video:2fhn8kePbKQ/00504 (Snowhill, 'An Unexpected Gift' return to Candi Ivy: 'You receive 1 [Tacky] Reindeer [Sweater]' alongside a Mini [Holiday] [Tree]); repo:prototype/osfr-tools/data/content/npcs/snowhill.json:6553 ('Daily gift from the Gifting Tree.')"},
  {"type": "vendor", "detail": "Coin store listing for item 76541 (store category 103, tint group 2). The row names no vendor, so the seller is unconfirmed.", "where": null, "price": "750 coins (member price 675 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 76541 (line 16168); client definition coin_store_prices 750"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name and description exist: 'Tacky Holiday Tree Sweater', one definition (76541), slot 3, class 1, model freestyle_<race>_<gender>_chest_sweater.adr", "source": "locale:134464; client definition pack"},
  {"claim": "The sweater sits in a set with the other Tacky sweaters (Gingerbread, Reindeer, Stockings, Gift Wrapped, Snowman) and Yellow Snowball, 2010 Glasses/Party Hat, Bah Humbug Hat, Reindeer Antlers", "source": "locale:134459-134469"},
  {"claim": "Snow Days wiki page lists the Gifting Tree as a source of holiday items, alongside Snow Days Membership Gift and the December 2011 Member's Pack", "source": "wiki page 'Snow Days'"},
  {"claim": "Video frame shows a Candi Ivy 'An Unexpected Gift' return giving a [Tacky] Reindeer [Sweater] (same family as this item)", "source": "video:2fhn8kePbKQ/00504"},
  {"claim": "The coin store row for 76541 sells at 750 coins, with a 10% member price of 675 and a sell price of 75", "source": "repo:prototype/osfr-tools/data/content/stores.json:16168"}
 ],
 "confidence": 0.5,
 "open": [
  "The sweater is not named in any wiki page or video frame directly; the Gifting Tree link is inferred from the Tacky-sweater family in the Candi Ivy quest frame and the Snow Days page, not from a per-item source line.",
  "The stores.json row for 76541 carries no vendor name, so it is unclear whether 750 coins is a real coin vendor price or a leftover price. Check the Coin Shop or a vendor before listing it as a coin sale.",
  "Whether the sweater is still obtainable (retired with Snow Days or kept as a holiday item) is not confirmed by any source in the pack.",
  "The Snow Days membership gift and the December 2011 Member's Pack are possible sources for this item but have no direct evidence here."
 ]}
