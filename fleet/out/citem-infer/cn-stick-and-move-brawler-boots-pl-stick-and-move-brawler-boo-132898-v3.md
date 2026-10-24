<!-- fleet job=citem-infer id=cn-stick-and-move-brawler-boots-pl-stick-and-move-brawler-boo-132898-v3 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7502, 10982, 6, 2451] model=claude-haiku-5-5 -->
# {n}Stick and Move Brawler Boots{pl="Stick and Move Brawler Boots"}

{"item": {"name": "Stick and Move Brawler Boots", "locale_id": 132898, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, client definition 75890 coin_store_prices [902]; store row purchase 902 coins, member price 811 coins (10% member discount), sell price 90 coins", "where": "stores.json category 105 (shop name unmapped; not confirmed as the Coin Shop)", "price": "902 coins (member 811 coins)", "currency": "coins", "source": "client definition 75890 coin_store_prices [902]; repo:prototype/osfr-tools/data/content/stores.json:15646"},
  {"type": "vendor", "detail": "Keren (Brawler job gear vendor; Stick and Move Brawler Boots in her Sells list)", "where": "Lakeshore, south of Thunder Falls Speedway (wiki; location naming unresolved)", "price": null, "currency": "unknown", "source": "wiki page Keren; repo:prototype/osfr-tools/data/content/vendors.json:41456-41474 (item 75890 in item_ids)"},
  {"type": "prize_wheel", "detail": "Brawler job prize wheel, one of five items beside the 162 Coins slot (no drop rate)", "where": "Grexan's Camp", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:61, :74 (wiki)"},
  {"type": "prize_wheel", "detail": "Brawler job prize wheel row with the same Boots piece (no drop rate)", "where": "Oasis of Peril", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Oasis of Peril.md:67; wiki page Oasis of Peril"},
  {"type": "other", "detail": "Bonus-goal clothing: one random piece from the job's set (Brawler: Barnburner or Stick and Move), random colour and slot, awarded to everyone in the instance; no per-piece rate", "where": "Grexan's Camp (set also appears in other Brawler dungeon rows)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:63, :80 (wiki)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132898 is 'Stick and Move Brawler Boots'; client definition 75890, slot 5, class 25", "source": "locale:132898; client definition 75890"},
  {"claim": "Client definition carries coin_store_prices [902]", "source": "client definition 75890"},
  {"claim": "stores.json row for item 75890: category 105, purchase 902, member 811, sell 90. Category 105 is shared with other items and is not mapped to a shop name in the repo, so the shop is unconfirmed", "source": "repo:prototype/osfr-tools/data/content/stores.json:15646"},
  {"claim": "Keren's stock list includes item 75890; wiki Sells list includes the Boots with no price shown", "source": "repo:prototype/osfr-tools/data/content/vendors.json:41456-41474; wiki page Keren"},
  {"claim": "Brawler prize wheel at Grexan's Camp lists the Boots among five items, alongside a 162 Coins slot", "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:61, :74"},
  {"claim": "Bonus-goal clothing is one random piece from the job's set, Brawler set = Barnburner or Stick and Move", "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:63, :80"},
  {"claim": "Prior answer's 68 Coins figure was unsupported and is dropped; the 162 and 176 Coins figures are wheel/member bonus values, not Boots prices", "source": "repo:notes/Build Guides/Content/Dungeons/Grexan's Camp.md:61-62"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin store: the 902-coin price is confirmed by the client definition, but the shop behind stores.json category 105 is unmapped. Do not call it the Coin Shop or Marketplace until mapped.",
  "Keren: no price on the wiki; her coin price for the Boots is unknown and may or may not be the 902-coin store offer. Location naming (Thunder Falls Speedway vs Raceway; Lakeshore vs Central Wilds) is unresolved.",
  "Wheel vs bonus-goal: wheel and bonus-goal drop rates are unknown. Oasis of Peril row was cited from the notes but not re-read in this pass.",
  "Live status: no retirement evidence for this item. The store row and vendor stock are undated, so live stays 'unsure' and retired stays null.",
  "No wiki, video, article, collection, event or membership source names this item."
 ]}
