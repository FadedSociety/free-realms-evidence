<!-- fleet job=citem-infer id=cn-wild-crash-pants-pl-wild-crash-pants-29021-v3 status=nothing_found turns=2 usd=0.0020 tokens(read,write,in,out)=[6044, 8269, 6, 1890] model=claude-haiku-5-5 -->
# {n}Wild Crash Pants{pl="Wild Crash Pants"}

{"item": {"name": "Wild Crash Pants", "locale_id": 29021, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name for locale 29021 is 'Wild Crash Pants' (client definition: slot 4 legs, item class 22, 14 definitions, one shared model freestyle_<race>_<gender>_legs_tuckedpantswpads.adr).", "source": "locale:29021"},
  {"claim": "Elite Pink and Elite Black Wild Crash Pants exist as separate client names (69466, 69467), so later variants are present in the client.", "source": "locale:69466; locale:69467"},
  {"claim": "The only store row matching the definition's coin_store_prices id 534 is prototype/osfr-tools/data/content/stores.json item_id 534: category 101, tint_group 3, purchase 270 coins, member price 243 coins, sell 27 coins. The row has no name field, so nothing in the repo links it to Wild Crash Pants.", "source": "prototype/osfr-tools/data/content/stores.json:256"},
  {"claim": "Store id 1266 does not appear as an item_id in prototype/osfr-tools/data/content/stores.json (exact-id search over all JSON found only 534).", "source": "repo search: item_id 1266 / 534 in *.json"},
  {"claim": "Lookup of 'Wild Crash Pants' across client, wiki, articles and video returned only the client locale lines (29021, 69466, 69467). No wiki page, article fact or video frame names the item.", "source": "lookup: 'Wild Crash Pants'"},
  {"claim": "piece_041.rs:166 has a rank unlock for the Wild Crash Jacket (item 27412), not for these pants. The same family has a rank-unlock path, but the pants are not named in it.", "source": "prototype/osfr-tools/src/restoration/piece_041.rs:166"}
 ],
 "confidence": 0.15,
 "open": [
  "No confirmed acquisition source. The definition's coin_store_prices [534, 1266] are bare numbers. The client definition does not state that they are stores.json item_ids, and no name or definition link ties store row 534 (270 coins, member 243) to this item. Store row 534 is a candidate coin-vendor sale only, unconfirmed. The previous answer's price of 270 coins is not a verified price for this item. 1266 has no store row in stores.json and should be dropped.",
  "Check whether the coin_store_prices ids are store item_ids or another id space (e.g. definition ids). If they are store item_ids, store 534 is a candidate vendor sale at 270 coins (member 243); if not, it is unrelated.",
  "The Wild Crash Jacket rank unlock (piece_041.rs:166) is a family lead. Check whether the pants share that unlock or another path.",
  "The Demo Derby locale neighbours (29026) are a naming cluster only. No source says these pants are a derby job or quest reward.",
  "Retired and live status are unknown. Elite variants (69466/69467) suggest later additions, but no dated source was found. The first-pass 'live: yes' tag is a hint only.",
  "Needed to close: a wiki or forum page for the Wild Crash set, a store listing by name, or a video frame showing the pants worn or sold."
 ]}
