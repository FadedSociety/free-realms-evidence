<!-- fleet job=citem-infer id=cbrawler-s-power-shard-of-vitality-iv-131036-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6397, 9658, 6, 2081] model=claude-haiku-5-5 -->
# Brawler's Power Shard of Vitality IV

{"item": {"name": "Brawler's Power Shard of Vitality IV", "locale_id": 131036, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Keren (Stick and Move Brawler set vendor; Brawler job items)", "where": "Lakeshore, south of the Thunder Falls Speedway", "price": "1504 coins (reference price; member 1353, 10% discount; sell-back 150)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Keren (Sells section lists \"Brawler's Power Shard of Vitality IV\", revision 2023-05-28, confirmed via lookup snippet); repo:prototype/osfr-tools/data/content/vendors.json:41694-41733 (npc 9500000913). Price is the stores.json reference, not a captured NPC quote (vendors.json:41702)."},
  {"type": "coin_shop", "detail": "Coin store record for item 75292 (category 121); same reference price as the Keren row, not a separately observed listing", "where": "Coin Shop", "price": "1504 coins (member 1353, sell 150)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15242 (also client coin_store_prices [1504])"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name and id: Brawler's Power Shard of Vitality IV, locale 131036, definition 75292, slot 12, class 25", "source": "locale:131036"},
  {"claim": "Keren's wiki Sells list includes Brawler's Power Shard of Vitality IV", "source": "https://freerealms.fandom.com/wiki/Keren; repo:prototype/osfr-tools/data/content/vendors.json:41694-41733"},
  {"claim": "Coin store reference record: purchase 1504, member 1353 (10% off), sell 150, category 121", "source": "repo:prototype/osfr-tools/data/content/stores.json:15242"},
  {"claim": "Item appears in gameplay video alongside Brawler's Ring of Regeneration IV and Drill Hammer of Sweeps, a Daily Grab Bag (450 station cash) store listing, and a Battle Item Mystery Pack reward screen; context only, not a confirmed source", "source": "video:H4v00arihLk/00060.jpg; video:H4v00arihLk/00294.jpg"}
 ],
 "confidence": 0.7,
 "open": [
  "The 1504 / 1353 / 150 prices are the repo's stores.json reference values, not an observed in-game NPC quote or captured Coin Shop page. The coin_shop row rests on the same record as the vendor price, so it is not independent confirmation of price.",
  "The Keren Sells snippet read was truncated; the Vitality IV line was confirmed in the lookup result, but the exact Keren price was not read.",
  "No wiki page exists for item IV itself. Claims that sibling Vitality I/II/III/V pages say 'sold at the Coin Shop' were not verified and are removed. Brawler Prize Wheel lists name Vitality shards generally, but none was shown to list item IV, so Prize Wheel is not a source.",
  "The video frames show the item beside a Daily Grab Bag listing and a Battle Item Mystery Pack reward screen. No frame shows it as a drop or reward; the Daily Grab Bag is not evidenced as containing it.",
  "Retirement status not established; no source states it was retired or unobtainable. Live status rests on the Keren listing and the store record."
 ]
}
