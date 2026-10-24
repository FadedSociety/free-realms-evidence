<!-- fleet job=citem-infer id=cn-stick-and-move-brawler-boots-pl-stick-and-move-brawler-boo-132898-v2 status=done turns=4 usd=0.0046 tokens(read,write,in,out)=[34025, 18938, 10, 3721] model=claude-haiku-5-5 -->
# {n}Stick and Move Brawler Boots{pl="Stick and Move Brawler Boots"}

{"item": {"name": "Stick and Move Brawler Boots", "locale_id": 132898, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of item 75890 (client definition 75890, coin_store_prices [902]); store row purchase_price_coins 902, member_price_coins 811 (10% member discount), sell_price_coins 90", "where": "Coin store (stores.json category 105)", "price": "902 coins (member price 811 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15646 (item_id 75890); client definition 75890 coin_store_prices [902]"},
  {"type": "vendor", "detail": "Keren (human merchant, sells exclusively Brawler job items; Boots listed in her Sells list)", "where": "Lakeshore, south of the Thunder Falls Speedway (wiki)", "price": null, "currency": null, "source": "wiki page Keren (Sells list includes Stick and Move Brawler Boots); repo:prototype/osfr-tools/data/content/vendors.json:41456-41469 (npc_name Keren, item 75890); repo:notes/Build Guides/Content/NPCs/NPCs - Wilds.md:186"},
  {"type": "drop", "detail": "Brawler per-job reward row (Battle Item Mystery Pack, Brawler's Drill Hammer, Necklace, Power Shard, Stick and Move Brawler Boots); a dungeon reward line, not a confirmed drop rate", "where": "Grexan's Camp", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:74; wiki page Grexan's Camp"},
  {"type": "drop", "detail": "Same Brawler per-job reward row as above, with the Boots piece", "where": "Oasis of Peril", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Oasis of Peril.md:67; wiki page Oasis of Peril"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132898 is 'Stick and Move Brawler Boots'; client definition 75890, slot 5, class 25", "source": "locale:132898; client definition 75890"},
  {"claim": "Coin store row for item 75890 is priced 902 coins, member price 811 coins, sell price 90", "source": "repo:prototype/osfr-tools/data/content/stores.json:15646"},
  {"claim": "Keren sells exclusively Brawler job items and her Sells list includes Stick and Move Brawler Boots; no price is shown beside Boots on her page", "source": "wiki page: Keren; repo:prototype/osfr-tools/data/content/vendors.json:41456"},
  {"claim": "Grexan's Camp and Oasis of Peril Brawler reward rows list Stick and Move Brawler Boots", "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:74; repo:notes/Build Guides/Content/Dungeons/Oasis of Peril.md:67"},
  {"claim": "The '162 Coins' and 'Coins' figures on the Grexan's Camp and Oasis of Peril wiki pages sit next to Bodkin Archer Boots and the Brawler Prize Wheel block, not a Stick and Move Boots price; the 68 Coins figure in the prior answer is unsupported and was dropped", "source": "wiki pages Grexan's Camp, Oasis of Peril!; wiki page Keren"},
  {"claim": "Stick and Move set pieces also appear in other Brawler dungeon rows (Bandit Hideout jacket, Briar Patch gloves, Darvon's Descent helmet, Frostfang shoulderpads, Moldy Shamblers jacket, Mugwort's Hollow pants, Shady Smugglers shoulderpads)", "source": "repo:notes/Build Guides/Content/Dungeons/*.md Brawler rows"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store price 902 coins is confirmed in stores.json for item 75890 (the prior answer's citation was right on the item but misread the row as absent). The store category 105 name is not mapped, so whether it is the Coin Shop or the vendor-sold coin list is not confirmed; treat as coin shop until checked.",
  "Keren's vendor price for the Boots is not on the wiki; the 902-coin store price may or may not be the same offer as Keren's sale. Keren's coin price is unknown.",
  "Dungeon rows are per-job reward lines (Battle Item Mystery Pack plus pieces); whether the Boots are a drop, a prize wheel result, or a bonus pick is not established, and no rate is known.",
  "Thunder Falls Speedway vs Raceway naming and Lakeshore vs Central Wilds ownership of Keren's location are unresolved.",
  "Live status: no retirement evidence found for this item; the Keren page date (2013) is not a retirement note. Also the wiki's 'Shutting again' thread about FreeRealms discontinuation is a general forum post, not item-specific.",
  "No wiki, video, article, or promotion source names this item with a collection, event, or membership source."
 ]}
