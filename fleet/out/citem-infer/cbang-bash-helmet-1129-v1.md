<!-- fleet job=citem-infer id=cbang-bash-helmet-1129-v1 status=done turns=10 usd=0.0070 tokens(read,write,in,out)=[135724, 24347, 22, 5216] model=claude-haiku-5-5 -->
# Bang Bash Helmet

{"item": {"name": "Bang Bash Helmet", "locale_id": 1129, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for the Bang Bash Helmet tint variants (store item ids 685, 687, 688 confirmed in the store data; purchase price 291 coins, member price 261 coins, 10% member discount, sell-back 29 coins). Other variants (689, 691, 693, 14698-14706) carry the same 291 price in the client definition but their store rows were not confirmed by my lookup.", "where": "Coin Shop (coin store, category 101)", "price": "291 coins (member 261 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 685 (line 324), item 687 (line 326), item 688 (line 327); client definition coin_store_prices 291"},
  {"type": "other", "detail": "Demolition Derby Driver job gear unlock at job rank 10 (Demolition Derby Driver job id 49, gear class 22 'Demolition Derby Driver Gear'). Recovered as a rank-gated catalogue row; this is a gear unlock tied to derby progression, not a confirmed vendor sale.", "where": "Demo Derby Driver job progression", "price": null, "currency": null, "source": "repo:scripts/pieces/piece_041.py:84 (rank_unlock 10, item 685, name id 1129, 184); repo:prototype/osfr-tools/src/restoration/piece_041.rs:165 (rank_unlock(10, 685, 1129, \"Bang Bash Helmet\", 184)); repo:prototype/osfr-tools/src/restoration/piece_041.rs:19-22 (derby gear rank gates)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Bang Bash Helmet' is locale 1129, Hidden Valley, item class 22 slot 1, with 18 definitions sharing the name", "source": "locale:1129"},
  {"claim": "Store data lists item 685, 687 and 688 at 291 coins purchase, 261 coins member price, sell-back 29 coins, category 101", "source": "repo:prototype/osfr-tools/data/content/stores.json item 685 / 687 / 688"},
  {"claim": "Bang Bash Helmet is a Demolition Derby Driver gear item gated at job rank 10 (item 685, name id 1129, value 184)", "source": "repo:scripts/pieces/piece_041.py:84; repo:prototype/osfr-tools/src/restoration/piece_041.rs:165"},
  {"claim": "Its client cluster (Roar Ram Pants/Boots, Bang Bash Gloves/Jacket, Wham Whack Helmet, Crash Crunch Helmet) sits with the same Hidden Valley set text; no wiki page, video frame, article or vendor stock names the helmet", "source": "locale:1125, locale:1127, locale:1131, locale:1133, locale:1139, locale:1149"},
  {"claim": "Wiki and article lookups for 'Bang Bash' returned no matches", "source": "lookup wiki/articles, query 'Bang Bash' and 'Bang Bash Helmet'"}
 ],
 "confidence": 0.5,
 "open": [
  "Which coin vendor or Coin Shop page actually sells it: the store data gives price and category only, no vendor or NPC name. Confirm the storefront name.",
  "Store rows for the other variant definition ids (689, 691, 693, 14698, 14700, 14702, 14703, 14705, 14706) were not confirmed in stores.json; only 685, 687 and 688 matched.",
  "Whether the derby job rank-10 gear is also purchasable with coins, or only unlocked by rank; the repo does not say whether the job-rank row and the coin listing are the same sale.",
  "No wiki article, video or forum source names the Bang Bash Helmet, so the Hidden Valley zone attribution and any event or retirement date are unverified. Retired status unknown.",
  "The first-pass tag said vendor; the repo evidence supports Coin Shop and job-rank unlock, not a coin vendor NPC."
 ]}
