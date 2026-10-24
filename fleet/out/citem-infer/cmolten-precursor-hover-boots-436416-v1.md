<!-- fleet job=citem-infer id=cmolten-precursor-hover-boots-436416-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[4130, 6400, 6, 2284] model=claude-haiku-5-5 -->
# Molten Precursor Hover Boots

{"item": {"name": "Molten Precursor Hover Boots", "locale_id": 436416, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, 3 tint variants (definition ids 79373, 79374, 79375); purchase price 1000 coins, member price 900 coins (10% member discount)", "where": "coin store listing, category 105 (shop/zone not named in the store data; source_tags L1, L2, L4, R2, T633, R1)", "price": "1000 coins (900 coins for members)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79373 (lines 17127-17129, items 79373-79375); also notes/Autopilot/T633.md:184-186"},
  {"type": "other", "detail": "Series 1 Mystery Chest (random reward; the wiki lists Molten Precursor Hover Boots among possible chest contents)", "where": null, "price": null, "currency": null, "source": "wiki: Mystery Chest (Series 1: Original); wiki: Molten Precursor Hover Boots; locale:436415 ('These boots were unlocked from a Mystery Chest.')"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Name string is locale 436416 'Molten Precursor Hover Boots'; description (locale 436415) says it was unlocked from a Mystery Chest", "source": "locale:436416; locale:436415"},
  {"claim": "Three definitions (79373, 79374, 79375), feet slot 5, class 148, coin store price 1000 for each", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79373-79375"},
  {"claim": "Wiki says the boots are acquired by opening Series 1 Mystery Chests or through trade; cannot be sold; Freestyle Jobs feet clothing", "source": "wiki: Molten Precursor Hover Boots"},
  {"claim": "Mystery Chest Series 1 'Original' lists Molten Precursor Hover Boots as a possible item", "source": "wiki: Mystery Chest"},
  {"claim": "Item tooltip: Required Level 1, Freestyle Jobs; cannot sell; resell value 0", "source": "image:item_tooltip (Molten Precursor Hover Boots)"},
  {"claim": "Video frame shows Molten Precursor Hover Boots in an item list with other freestyle shoes", "source": "video:ip2vKMeCU6U/00168.jpg"},
  {"claim": "Research note says the Mystery Chest restoration catalogue includes 79373 Molten Precursor Hover Boots", "source": "notes/Research/Mystery Chest Restoration.md:13"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store listing (1000 coins) conflicts with the wiki's 'acquired through Mystery Chests or trade' and 'Cannot sell'. Confirm the store listing is live and which shop/zone it sits in; source_tags are codes, not names.",
  "stores.json gives sell_price_coins 100 while the tooltip says Resell Value 0 and Cannot Sell; treat the 100 as unverified.",
  "Trade source named by the wiki has no detail (who trades, from which player or event); left open.",
  "Mystery Chest drop rate and which chest series or vendor sells the chests are not established by the pack; the chest source is listed as 'other' with the wiki page as evidence.",
  "Duplicate client string locale 436417 carries the same description as 436415 and is flagged duplicate; it is not a separate item and was not counted as a source.",
  "The 'Molten' tint variant is not confirmed as a different tint from the base Precursor Hover Boots (locale 436414, id 79370); the wiki lists both as Mystery Chest items.",
  "Retired status unknown: no retirement date or source found."
 ]}
