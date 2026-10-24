<!-- fleet job=citem-infer id=cstockings-134357-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[8386, 9085, 8, 2183] model=claude-haiku-5-5 -->
# Stockings

{"item": {"name": "Stockings", "locale_id": 134357, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, 100 coins (member price 90 coins, 10% member discount). Store row is flagged no_sale: true, so it appears to have been removed from sale. The vendor/shop name is not given in the store data.", "where": null, "price": "100 coins (member 90 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2712 (category 52, purchase_price_coins 100, no_sale true)"},
  {"type": "event", "detail": "Snow Days Gift Box - Decorations (Day 5 of the 12 Days of Presents). The box holds house decor: Holiday Wreath x4, Stockings x4, Snowman x2, Garland x4.", "where": null, "price": null, "currency": null, "source": "wiki: Snow Days; wiki: 12 Days of Presents (Day 5: Snow Days Gift Box - Decorations)"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 2712 is named 'Stockings' (locale 134357), with description 'Coal not included...', one definition, furniture-type slot 0, model hsg_xmas_stocking_01.adr", "source": "client definition (locale:134357; definition_id 2712)"},
  {"claim": "Coin store sale price is 100 coins, member price 90 coins, flagged no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2712"},
  {"claim": "Snow Days Gift Box - Decorations contains Stockings x4 (with Holiday Wreath x4, Snowman x2, Garland x4)", "source": "wiki: Snow Days"},
  {"claim": "The Snow Days Gift Box - Decorations is the Day 5 reward of the 12 Days of Presents event", "source": "wiki: 12 Days of Presents"},
  {"claim": "Client line 'Holiday stockings on the feet would be more fashionable.' is an NPC dialog about stockings; the item line 'Stockings come stuffed with holiday fireworks!' (locale:134549) belongs to the Holiday Fireworks item, not Stockings", "source": "locale:134569; locale:134549"}
 ],
 "confidence": 0.6,
 "open": [
  "The first-pass tag said 'vendor'. Only the coin store row supports a vendor sale, and the vendor/shop name is missing. Which coin vendor sold it, and when, is unknown.",
  "The store row has no_sale true, so the coin sale appears to have ended. The end date is not confirmed by any source.",
  "The Snow Days dates are not confirmed in the pack. The 12 Days of Presents and Snow Days pages describe the event but give no date range here.",
  "Live status is unsure. The item may still be obtainable through a holiday reward or a later event. Check the current store data before marking it live.",
  "Coin price of 100 is the store-data price; the wiki gives no separate price for Stockings.",
  "The Snow Days box (Decorations) may have had a different reward list in other years. Only the wiki version is evidenced here."
 ]}
