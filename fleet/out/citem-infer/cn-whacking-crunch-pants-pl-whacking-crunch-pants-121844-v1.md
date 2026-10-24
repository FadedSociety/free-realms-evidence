<!-- fleet job=citem-infer id=cn-whacking-crunch-pants-pl-whacking-crunch-pants-121844-v1 status=done turns=7 usd=0.0049 tokens(read,write,in,out)=[73637, 19204, 16, 3548] model=claude-haiku-5-5 -->
# {n}Whacking Crunch Pants{pl="Whacking Crunch Pants"}

{"item": {"name": "Whacking Crunch Pants", "locale_id": 121844, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Demo Derby Driver job rank 13 gear unlock (set-level: the sibling Whacking Crunch Jacket, def 41856 / name 121840, is listed at rank 13 with 45 catalogue rows; Pants is not named in that table, so its rank is unconfirmed)", "where": "Demo Derby Driver job", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:168"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 121844 is '{n}Whacking Crunch Pants{pl=\"Whacking Crunch Pants\"}', ucdt 1847814528 and ugdt 3564225033", "source": "locale:121844"},
  {"claim": "Whacking Crunch set (Jacket 121840, Boots 121841, Gloves 121842, Helmet 121843, Pants 121844) sits in one contiguous locale block, so it is one set", "source": "locale:121840-121844"},
  {"claim": "Whacking Crunch Jacket (name 121840, def 41856) is a Demo Derby Driver rank 13 unlock with 45 catalogue rows; the Crazy Crunch set (names 121680-121684) is the rank 3 Demo Derby set, so these crunch sets are that job's gear", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:159,168"},
  {"claim": "Demo Derby Driver is a Members Only job per a wiki news template (January Monthly Member Pack era)", "source": "wiki page:ns10 Template:News"},
  {"claim": "Coin store prices 1266 and 9453 are listed in the pack, and stores.json has many items at each price, but none of the store item_ids are the pack's definition ids (41845-41900), so the coin price does not tie to this item", "source": "repo:prototype/osfr-tools/data/content/stores.json (purchase_price_coins 1266 at lines 289-3715; 9453 at lines 80-241)"},
  {"claim": "No wiki page, article, video frame, vendor stock or quest reward names Whacking Crunch Pants", "source": "lookup of client/wiki/articles/video for 'Whacking Crunch' returned only locale lines"}
 ],
 "confidence": 0.35,
 "open": [
  "Coin price 1266/9453 is unverified: no store entry references definition ids 41845-41900. Do not record a coin vendor sale until a store row proves it.",
  "Pants rank/source is inferred from the set. The Demo Derby table only names the Jacket at rank 13; confirm the Pants unlock rank and whether it is a job reward at all.",
  "Whether the Demo Derby Driver job is live (members-only) in the revival is unconfirmed; retired status unknown.",
  "The 16 definitions (tints/races) were not checked individually; the pack gives 12 ids listed out of 16.",
  "No wiki, video or article evidence for acquiring this item; treat the job unlock as a claim for review, not a verified source."
 ]}
