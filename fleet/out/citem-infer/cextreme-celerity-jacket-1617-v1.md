<!-- fleet job=citem-infer id=cextreme-celerity-jacket-1617-v1 status=done turns=8 usd=0.0076 tokens(read,write,in,out)=[103816, 31949, 18, 5230] model=claude-haiku-5-5 -->
# Extreme Celerity Jacket

{"item": {"name": "Extreme Celerity Jacket", "locale_id": 1617, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row for definition 1783 (tint group 1), purchase price 1266 coins, member price 1139 coins (10% member discount), sell price 126 coins. Store row is in the coin-store data; the vendor/NPC is not named in our data.", "where": "coin store (category 103)", "price": "1266 coins (member 1139 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:5833 (item 1783)"},
  {"type": "vendor", "detail": "Coin store rows for definitions 1785 (tint group 2) and 1786 (tint group 3), purchase price 9453 coins each, member price 8507 coins, sell price 945 coins. Second price is the member price, not a sale.", "where": "coin store (category 103)", "price": "9453 coins (member 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:5834 (item 1785) and :5835 (item 1786)"},
  {"type": "other", "detail": "Kart Driver job gear, unlocked by Kart Driver job level: rank 5 gives definition 1789 (this name, 104 catalogue rows incl. colour and race variants) and rank 20 gives definition 1783 (609 catalogue rows). Obtained by reaching the job level, not from a quest or drop.", "where": "Kart Driver job (kart racing zones: Wildwood, Tangletrack, Thunder Falls, Frost Ridge, Sandstorm)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:137 and :152 (KART_DRIVER_GEAR table, 'Kart Driver gear rows, ItemClasses.txt class 24'); job level context: repo:notes/Build Guides/Gameplay/Kart Racing.md:23"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Extreme Celerity Jacket' (locale 1617), clothing class 24, chest slot 3, 16 definitions incl. 1783, 1785, 1786, 1789 used by this name.", "source": "locale:1617; client definition pack"},
  {"claim": "Coin store price rows exist for definitions 1783 (1266 coins) and 1785/1786 (9453 coins).", "source": "repo:prototype/osfr-tools/data/content/stores.json:5833-5835"},
  {"claim": "Name is rank-gated Kart Driver gear: rank 5 = definition 1789, rank 20 = definition 1783.", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:137, :152"},
  {"claim": "Sibling Kart Driver gear (Steady Pace Jacket, High/Top Speed, Ultimate Celerity) follows the same rank ladder, so this is the job's gear set, not a promo item.", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:133-152"},
  {"claim": "Kart Driver is a job with levels and trainers; kart races give XP toward it.", "source": "repo:notes/Build Guides/Gameplay/Kart Racing.md:18-25"},
  {"claim": "Locale neighbours (1613-1622) are Elite High Speed Jerseys, Steady Pace Jacket, pirate and pet items; the Thanksgiving text at 1615/1616 is an unrelated news blurb (not_live) and does not name this item.", "source": "client_cluster in pack; locale:1615, locale:1616"}
 ],
 "confidence": 0.4,
 "open": [
  "No wiki page, image, article or video names this item; no wiki price or category to cross-check the coin store prices.",
  "The coin store rows (1266 and 9453) are in our reconstructed store data; the vendor NPC, zone and whether they are live today are not recovered. The 9453 price is shared by many unrelated items, so it may be a placeholder.",
  "The rank-20 gear (definition 1783) and the coin store row for it both exist; whether the rank-5 item (1789) is sold for coins is not shown (no store row for 1789 found).",
  "Whether the job-level reward is the only way to get the jacket, or whether a Kart Driver level reward is still given in the live game, is not confirmed.",
  "The job-gear rank table is our own restoration code; the rank-to-item mapping is not checked against a retail source.",
  "Retired status and live status are unknown; the first-pass tag 'live: yes' is a hint only.",
  "Price per tint: the pack's 'coin_store_prices' gives values, not definition ids, so the mapping to specific tints is from stores.json only."
 ]}
