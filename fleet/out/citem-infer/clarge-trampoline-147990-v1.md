<!-- fleet job=citem-infer id=clarge-trampoline-147990-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[9063, 8970, 8, 2014] model=claude-haiku-5-5 -->
# Large Trampoline

{"item": {"name": "Large Trampoline", "locale_id": 147990, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor (store category 57). Store row lists 50 coins purchase, 45 coins member price, 5 coins sell price for item 18161 (tint group 1, the orange-tint variant has no tint group). Item 18162 has the same 50-coin price. The vendor NPC is not identified in the repo data, so this is an open point.", "where": null, "price": "50 coins (45 coins for members, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 18161 and item 18162"},
  {"type": "promotion", "detail": "Day 6 login gift (listed as 'Grand trampoline' in the article's Day 6 entry). Probably the large trampoline given as a login-calendar reward, which the article describes.", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2138"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Large Trampoline' is client locale 147990, with the orange variant at 147992 ('Large Orange Trampoline').", "source": "locale:147990; locale:147992"},
  {"claim": "Client definitions 18161 and 18162 (two variants, tint group 1 and none) both priced at 50 coins in the coin store data.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 18161; item 18162"},
  {"claim": "Article says the Day 6 login gift was a large trampoline (Grand trampoline).", "source": "http://www.freerealms.com/article/detail.action?articleId=2138"},
  {"claim": "Client asset names are hsg_trampoline_large_01.adr and hsg_trampoline_large_01_orange.adr, with slot 0 and class 0, which fits a housing furniture item.", "source": "client definition pack (models, slots, class_ids)"},
  {"claim": "Name's cluster (Telephone Booth, Festival Tent, Festival Pavilion, Festival Stand, Medium Trampoline) is a set of housing/furniture items, which supports kind furniture.", "source": "client_cluster locale:147986-147995"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin vendor that sells item 18161/18162 at 50 coins is not named in the repo data (no vendor_stock in the pack). Store category 57 is the only link. Need the vendor NPC and zone to complete the vendor source.",
  "The login gift article only names the item on Day 6; it does not say which calendar, year, or whether it is still given. Retired status is unknown.",
  "No wiki page or video frame covers this item. Live status is unsure; the coin price suggests it was on sale but the repo does not confirm the sale window.",
  "Locale 147994 is a misspelled duplicate of Medium Trampoline (147993), not this item. Locale 427852 is an internal asset name, not a player-facing name."
 ]}
