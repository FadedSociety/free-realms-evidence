<!-- fleet job=citem-infer id=cglacial-hammer-94238-v1 status=done turns=5 usd=0.0047 tokens(read,write,in,out)=[50914, 21992, 12, 2978] model=claude-haiku-5-5 -->
# Glacial Hammer

{"item": {"name": "Glacial Hammer", "locale_id": 94238, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing for item 48121 (the Glacial Hammer's second definition id), category 207, purchase price 2204 coins, member price 1983 coins. The store row does not name the vendor, and the same 2204 price is shared by many category 207 items.", "where": null, "price": "2204 coins (member price 1983 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48121 (line 13177)"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. Not a store or quest source.", "where": null, "price": null, "currency": null, "source": "wiki: Glacial Hammer (\"can only be acquired through trade\"); wiki category Blue Text Weapons"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Glacial Hammer' is locale 94238, in the Glacial weapon set (Blade 94235, Wand 94236, Axe 94237, Bow 94239, Shockrod 94240).", "source": "locale:94238; client_cluster in pack"},
  {"claim": "Wiki: level 16 Brawler weapon, Blue Text weapon, can only be acquired through trade. Effects: Glancing Blow 2372 damage; Leg Sweep 8302 damage.", "source": "wiki page: Glacial Hammer"},
  {"claim": "Wiki lists the item in Category:Retired Weapons.", "source": "wiki page: Glacial Hammer (category list)"},
  {"claim": "Store data prices definition id 48121 at 2204 coins purchase, 1983 member price, 220 sell price.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48121"},
  {"claim": "Wiki 'Blue Text weapon' page lists Glacial Hammer with the other Glacial weapons.", "source": "wiki: Blue Text weapon (search hit)"},
  {"claim": "Definition id 27933 has no store row in stores.json (only 48121 matched).", "source": "repo search for 27933|48121|94238 in data; stores.json search"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the store row (coin purchase, 2204 coins) contradicts the wiki's 'trade only' note. Either the coin listing was a retired or separate sale, or the wiki is wrong. Not resolved.",
  "The vendor and zone for store category 207 are not named in the repo data. Vendor and where are unknown.",
  "The 2204 coin price is shared by many category 207 items, so it may not be a price for this item alone. Verify the row against a vendor source.",
  "Retirement date not found. The wiki places it in Retired Weapons but gives no date.",
  "The pack gives no evidence for enemy drops, quest rewards, or events. None were checked.",
  "Wiki gives no price for trade; the trade price is unknown."
 ]}
