<!-- fleet job=citem-infer id=csuper-star-booster-2440-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3780, 5553, 6, 1862] model=claude-haiku-5-5 -->
# Super Star Booster

{"item": {"name": "Super Star Booster", "locale_id": 2440, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash item sold in the SC shop (wiki calls it 'SC Shop'; category 'SC Supplies')", "where": "SC Marketplace", "price": "200 SC", "currency": "station_cash", "source": "wiki page 'Super Star Booster' (ns0): 'acquired from the SC Shop where it sells for 200 SC'; wiki category 'SC Supplies'"},
  {"type": "event", "detail": "Super Spooktacular 2013 (Oct 1 - Nov 12, 2013) day rewards, one of four days' rewards alongside a Graveyard Flambe, Noxious Pork Chops and a Prospector's Scroll", "where": null, "price": null, "currency": null, "source": "wiki page 'Super Spooktacular' (ns0): 'The rewards for the 4 days were a Graveyard Flambe, a [Super] [Star] [Booster] scroll, ...'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name and description: locale 2440 'Super Star Booster'; description 'Use this scroll to earn extra stars when playing your favorite Job for a while.'", "source": "locale:2440"},
  {"claim": "Wiki: level 1 scroll usable in any job, +50% Stars, Cannot Sell / Cannot Trade, sells for 200 SC in the SC Shop", "source": "wiki page: Super Star Booster"},
  {"claim": "Wiki tooltip image shows Resell Value 0, Required Level 1 Any Job, Activatable +50% Stars", "source": "image:item_tooltip Super Star Booster.jpg"},
  {"claim": "Listed under the Items page's Trinkets section", "source": "wiki page: Items"},
  {"claim": "Given as a Super Spooktacular 2013 day reward", "source": "wiki page: Super Spooktacular"},
  {"claim": "Appears in a 2013-era trade lobby screenshot", "source": "video:UFsVcZ3X5iA/00048.jpg and video:cViT3FQobGg/00386.jpg (inventory frames)"}
 ],
 "confidence": 0.6,
 "open": [
  "Client definition has no coin store price (coin_store_prices empty), so the 200 SC price rests only on the wiki; the store data in repo was not checked for it, and the wiki price is not confirmed as a sale price or a launch price.",
  "Client definition ids 78 and 11644 (2 definitions) - not matched in repo data; unclear which variant the wiki/event sources refer to.",
  "No retirement date found; the wiki gives no 'retired' label, so retired is null. Whether the SC shop still sells it at the time of the revival is unknown.",
  "Super Spooktacular 2013 reward: the wiki names the scroll only as a day reward; the event's exact day and whether it was a general or a per-player reward is not stated.",
  "Item classes: class_ids [9] and slot 0 were not mapped to a category; kind 'consumable' is from the first-pass guess plus the scroll wording, not from the data.",
  "Jev's first-pass 'source_guess: unknown' is superseded by the wiki/marketplace evidence above; 'live: yes' is only partly supported (the item is in the client and in a 2013 event, but no later source confirms it)."
 ]}
