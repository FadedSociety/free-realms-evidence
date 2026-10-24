<!-- fleet job=citem-infer id=cn-elite-pink-rowdy-rumbler-pants-pl-elite-pink-rowdy-rumbler-44444-v1 status=no_submit turns=4 usd=0.0038 tokens(read,write,in,out)=[23172, 18502, 10, 2451] model=claude-haiku-5-5 -->
# {n}Elite Pink Rowdy Rumbler Pants{pl="Elite Pink Rowdy Rumbler Pants"}

```json
{"item": {"name": "Elite Pink Rowdy Rumbler Pants", "locale_id": 44444, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing for item 9443 (category 104). The specific vendor NPC is not identified in the repo or wiki.", "where": null, "price": "9453 coins (member price 8507 coins with 10% member discount; sell-back 945 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2733"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 44444 is 'Elite Pink Rowdy Rumbler Pants' (item text, definition id 9443, slot 4, class 25, model brawler_<race>_<gender>_legs_pantstucked.adr).", "source": "locale:44444"},
  {"claim": "The coin store data lists item_id 9443 with purchase_price_coins 9453, member_price_coins 8507, sell_price_coins 945, no_sale false, and source tags L1, L2, L4, R2, T633, R1.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2733"},
  {"claim": "The client cluster is the Feisty Fighter, Rowdy Rumbler, Elite Pink and Elite Black Rowdy Rumbler Pants set (locales 44440, 44441, 44444, 44446). Elite Pink is the tinted/elite variant of the Rowdy Rumbler line.", "source": "locale:44440, locale:44441, locale:44444, locale:44446"},
  {"claim": "The client lookup returns only the item name rows for 44441, 44444 and 44446. No wiki page, article, video frame, quest, drop or event names this item.", "source": "lookup (client, wiki, articles, video) for 'Elite Pink Rowdy Rumbler Pants' and 'Rowdy Rumbler Pants'"},
  {"claim": "The first-pass tag (live yes, kind clothing, source guess vendor) matches the store listing, but it is a hint only and is not used as evidence.", "source": "jev_first_pass"}
 ],
 "confidence": 0.35,
 "open": [
  "The vendor that sells item 9443 is not named. The stores.json row gives only a category id (104), so the NPC and zone are unknown.",
  "The price 9453 is the same value on many unrelated items in stores.json (for example 9373, 9375, 9408, 9410, 9478, 9480). It may be a catalogue default and not a verified price. Confirm it against a wiki or video source before relying on it.",
  "Nothing in the pack says whether the Elite Pink variant was ever sold for station cash, given as a promotion or reward, or retired. Retired status is therefore null.",
  "The Rowdy Rumbler and Feisty Fighter siblings are not covered by this pack. Their sources could confirm where the set was sold."
 ]}
```
