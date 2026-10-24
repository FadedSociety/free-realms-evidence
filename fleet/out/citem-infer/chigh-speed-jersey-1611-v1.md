<!-- fleet job=citem-infer id=chigh-speed-jersey-1611-v1 status=done turns=5 usd=0.0039 tokens(read,write,in,out)=[36866, 16378, 12, 3025] model=claude-haiku-5-5 -->
# High Speed Jersey

{"item": {"name": "High Speed Jersey", "locale_id": 1611, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, base tint (store item 2800, tint group 1), listed at 1266 coins with a 10% member price of 1139 coins (sell-back 126)", "where": "unknown coin vendor (store category 103)", "price": "1266 coins (member price 1139 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 2800 (line 5896)"},
  {"type": "vendor", "detail": "Coin store sale, tinted variants (store items 13414 and 13415 in the same entry group; the other definitions share the name)", "where": "unknown coin vendor (store category 103)", "price": "291 coins (member price 261 coins)", "currency": "coins", "source": "repo:data/content/stores.json items 13414, 13415 (lines 6555-6556)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'High Speed Jersey' is locale 1611; 14 definitions share the name, slot 3 (chest), item class 24, model freestyle_<race>_<gender>_chest_jerseyovershortslvwgloves.adr", "source": "locale:1611; client definition ids 2800, 13414-13431"},
  {"claim": "Store data prices definition 2800 (tint 1) at 1266 coins and definitions 13414/13415 (tints 2-3) at 291 coins, both with 10% member discount", "source": "repo:data/content/stores.json item 2800 (line 5896); items 13414, 13415 (lines 6555-6556)"},
  {"claim": "Sibling client lines name Elite Pink and Elite Black High Speed Jersey variants and Slow Poke Jersey (same jersey family)", "source": "locale:1608, locale:1613, locale:1614"},
  {"claim": "No wiki page, article, image or video names this item; lookup of the name returns only the three client strings", "source": "lookup 'High Speed Jersey' (client, wiki, articles, video)"},
  {"claim": "Thanksgiving promo text (SC550 turkey mount) is a different item and does not name the jersey", "source": "locale:1616"}
 ],
 "confidence": 0.35,
 "open": [
  "The coin vendor that sells these is not identified: store category 103 is a broad category holding many unrelated items, so no vendor, zone or shop can be named from the repo data.",
  "No wiki or article evidence of the sale, its date, or whether it was retired; retired status and live status are unconfirmed (store rows carry tags L1/L2/L4/R2/T633/R1 but these are not a dated sale record).",
  "Mapping of the 14 definitions to tints and prices is incomplete: only 2800, 13414 and 13415 were checked against stores.json; the other definitions (13416-13431) were not confirmed as sold.",
  "No quest reward, enemy drop, event, prize wheel, crafting, collection, membership or promotion source was found; the first-pass 'vendor' guess rests only on the coin store price.",
  "The client description is empty, so no in-game text describes how the jersey is obtained."
 ]}
