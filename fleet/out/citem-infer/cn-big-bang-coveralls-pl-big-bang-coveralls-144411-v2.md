<!-- fleet job=citem-infer id=cn-big-bang-coveralls-pl-big-bang-coveralls-144411-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[11020, 6445, 8, 2294] model=claude-haiku-5-5 -->
# {n}Big Bang Coveralls{pl="Big Bang Coveralls"}

{"item": {"name": "Big Bang Coveralls", "locale_id": 144411, "kind": "clothing"},
 "sources": [
   {"type": "coin_shop", "detail": "Coin store row for definition 52529 (tint group 1), store category 103, flagged no_sale: true, sell_price null; no vendor named in the row", "where": "coin store category 103 (unvendored)", "price": "9453 coins (member price 8507 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json:8322 (item_id 52529)"},
   {"type": "coin_shop", "detail": "Coin store row for definition 52544 (tint group 2), store category 103, flagged no_sale: true, sell_price null; no vendor named in the row", "where": "coin store category 103 (unvendored)", "price": "1761 coins (member price 1584 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json:8323 (item_id 52544)"},
   {"type": "coin_shop", "detail": "Coin store row for definition 76760 (tint group 2), store category 103, flagged no_sale: true, sell_price null; no vendor named in the row", "where": "coin store category 103 (unvendored)", "price": "1761 coins (member price 1584 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json:16312 (item_id 76760)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
   {"claim": "Client name is 'Big Bang Coveralls' (locale 144411); generic item line is 'This is a Big Bang Coveralls item.' (locale 150498)", "source": "locale:144411; locale:150498"},
   {"claim": "Three client definitions (52529, 52544, 76760) share the name, slot 3 (chest), class 12, and the model worker_<race>_<gender>_chest_tuckedcoverallswkerchief.adr; they look like tint/race variants of one item", "source": "client definition in pack"},
   {"claim": "Store rows match by item_id: 52529 at 9453 coins (member 8507), 52544 at 1761 coins (member 1584), 76760 at 1761 coins (member 1584), all in category 103", "source": "repo:data/content/stores.json:8322, :8323, :16312 (verified; file path is prototype/osfr-tools/data/content/stores.json)"},
   {"claim": "All three rows have no_sale: true and sell_price_coins null, and no row names a vendor, so the rows show a price listing only, not a current or confirmed sale", "source": "repo:data/content/stores.json:8322, :8323, :16312"},
   {"claim": "Wiki, article, and video lookups for 'Big Bang Coveralls' return no page, fact, or frame; no quest, enemy drop, or event names it", "source": "lookup wiki/articles/video, no matches"},
   {"claim": "'Big Bang' in client text refers only to Big Bang Entertainment LLC, the minigame developer, and does not name this item", "source": "locale:432569; locale:408320; locale:432530"}
 ],
 "confidence": 0.3,
 "open": [
   "No vendor stocks this item in the repo or any answer; the coin store rows name no vendor, so no vendor source can be cited.",
   "All three store rows are no_sale: true with null sell price. Whether it was ever sold for coins at 9453 or 1761 is unconfirmed; the prices may be stale or placeholder store data. Those price values repeat on many other rows, so they are row values only.",
   "Which tint or race each definition covers is not stated; treated as variants of one item.",
   "The description ('Don't stand too close to open flames...') and name suggest a worker or mining outfit, possibly part of a set or promotion, but no set or promotion is confirmed.",
   "Retirement status is unknown: no source says retired, and the no_sale flag is the only hint it is no longer sold. Live status is unsure."
 ],
 "critique_response": "Evidence critique applied: the three store rows are now typed coin_shop (coin store price data), not vendor; no vendor or current sale is claimed; retired is null (unknown) rather than retired; live is unsure; the item_id link is stated as direct and the price values are noted as shared with other rows."
}
