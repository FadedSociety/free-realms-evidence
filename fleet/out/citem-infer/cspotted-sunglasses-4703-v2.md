<!-- fleet job=citem-infer id=cspotted-sunglasses-4703-v2 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[5756, 9085, 6, 1722] model=claude-haiku-5-5 -->
# Spotted Sunglasses

{"item": {"name": "Spotted Sunglasses", "locale_id": 4703, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Spotted Sunglasses' is locale 4703; description locale 4706 reads 'Perfect for hiding in a crowd…of lady bugs.'", "source": "locale:4703; locale:4706"},
  {"claim": "Client definition 1204, slot 17 (head), class 1, one definition, model freestyle_<race>_<gender>_head_roundsunglasses.adr.", "source": "client definition pack for item 1204"},
  {"claim": "Legacy store row for item 1204 exists: category 101, tint group 2, purchase_price_coins 270, member_price_coins 243, sell_price_coins null, no_sale true, source_tags L1,L2,L4,R2,L3,L3. The L3 tag is Legacy ClientItemDefinitions.NoSale and L2 is Legacy ClientItemDefinitions.Cost, so the 270 is a Cost field value, not a verified sale listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 423; source_tags legend lines 26-42 (L2 line 28, L3 line 29)"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock list, quest reward, drop or event names Spotted Sunglasses. A lookup of the name returns only the two client locale lines.", "source": "lookup (wiki, articles, video, client) for 'Spotted Sunglasses'"}
 ],
 "confidence": 0.15,
 "open": [
  "No source establishes a coin vendor, Coin Shop, Station Cash Marketplace, quest, drop, event, prize wheel, crafting or promotion source. The previous answer's Coin Shop listing is not supported: the only store row (stores.json line 423) is flagged no_sale true, which means the Legacy row is not a sold coin-store item by its own flag.",
  "The 270-coin figure is the Legacy Cost field (tag L2), with member price 243 derived by the 10% discount (R2). It is not a wiki or vendor price. It also matches the client definition's coin_store_prices [270], which comes from the same Legacy source, so it is not an independent confirmation.",
  "The 'same 270-coin tier' comparison with items 76, 106 and 124 was dropped: it only shows the shared Cost value, not any sale.",
  "The absence of a T638 tag does not establish currency. Currency stays unknown.",
  "Retirement status is unknown: no source says when or whether the item was sold or removed.",
  "The Fritz (locale 4698-4699) and Kiva (locale 4708) lines and the Plain Umbrella and Bubble Wand lines share the client cluster, which hints at a shared promotion set, but no source confirms it. Not used as evidence.",
  "Next step: find a wiki, forum or video source for a Spotted Sunglasses sale or drop, or confirm the Legacy NoSale flag meaning for item 1204 before any source is added."
 ]}
