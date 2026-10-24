<!-- fleet job=citem-infer id=cn-bobtailed-archer-leggings-pl-bobtailed-archer-leggings-132774-v4 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[15240, 8613, 8, 2415] model=claude-haiku-5-5 -->
# {n}Bobtailed Archer Leggings{pl="Bobtailed Archer Leggings"}

{"item": {"name": "Bobtailed Archer Leggings", "locale_id": 132774, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Oliver, Archer Job merchant (sells exclusively Archer job items; Sells list includes Bobtailed Archer Leggings)", "where": "Blackspore Swamp (north-east of the Blackspore Warpstone)", "price": null, "currency": null, "source": "wiki page: Oliver (Sells list, confirmed by lookup); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:94"},
  {"type": "vendor", "detail": "Catnis, Archer Job merchant (sells exclusively Archer job items; Sells list includes Bobtailed Archer Leggings)", "where": "Blackspore Swamp (north-western edge)", "price": null, "currency": null, "source": "wiki page: Catnis (Sells list, confirmed by lookup); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:95"},
  {"type": "coin_shop", "detail": "Coin store listing, store row for item 75766 (store category 104; channel not identified in the data). Purchase 752 coins, member price 676 coins (10% member discount); sell_price_coins 75 is a sell-back value, not an acquisition price", "where": "coin store (channel unidentified)", "price": "752 coins (member 676 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15547 (item_id 75766)"},
  {"type": "prize_wheel", "detail": "[Archer] Prize Wheel, Stealthy Despoilers dungeon (wheel contents list [Bobtailed] [Archer] [Leggings])", "where": "Stealthy Despoilers (dungeon)", "price": null, "currency": null, "source": "wiki page: Stealthy Despoilers (wheel contents, confirmed by lookup); the '37 Coins' line on that page is a Members Only Bonus under Rewards, not a wheel spin price"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132774 is 'Bobtailed Archer Leggings', slot 4 (legs), one definition (75766)", "source": "locale:132774"},
  {"claim": "Coin store row for item 75766: purchase 752 coins, member 676 coins, category 104", "source": "repo:prototype/osfr-tools/data/content/stores.json:15547"},
  {"claim": "Oliver's wiki page says he sells exclusively Archer job items and lists Bobtailed Archer Leggings under Sells (no prices shown)", "source": "wiki page: Oliver"},
  {"claim": "Catnis's wiki page says she sells exclusively Archer job items and lists Bobtailed Archer Leggings under Sells (no prices shown)", "source": "wiki page: Catnis"},
  {"claim": "Stealthy Despoilers wiki page lists [Bobtailed] [Archer] [Leggings] in the [Archer] Prize Wheel contents; the 37 Coins line is labelled 'Members Only Bonus' under Rewards (156 Stars), so it is not a wheel price", "source": "wiki page: Stealthy Despoilers"}
 ],
 "confidence": 0.55,
 "open": [
  "Vendor prices for Oliver and Catnis are unknown. The wiki Sells lists give no prices, and the 752/676 figures come from the coin-store row, not a captured NPC quote. Do not treat them as vendor prices.",
  "The channel for stores.json category 104 is not identified, so the coin_shop source is recorded as a coin store listing with unknown channel.",
  "Stealthy Despoilers prize wheel price is unknown. The 37 Coins line is a Members Only Bonus under Rewards; the Mugwort's Hollow 264 Coins figure above its Archer wheel has the same unverified layout reading and should be checked the same way.",
  "Retirement is not established. No dated source in the pack says the item was removed or is still obtainable. Live is 'unsure'.",
  "The 6 August 2013 date in the repo NPC note (lines 94-95) is when the Oliver and Catnis merchants were introduced, not a release date for the item."
 ]}
