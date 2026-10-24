<!-- fleet job=citem-infer id=cblack-arch-tiger-block-30223-v2 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[5647, 6431, 6, 1195] model=claude-haiku-5-5 -->
# Black Arch Tiger Block

{"item": {"name": "Black Arch Tiger Block", "locale_id": 30223, "kind": "furniture"},
 "sources": [{"type": "coin_shop", "detail": "Coin store listing, store category 147 (unnamed in our data); no NPC vendor or location identified", "where": null, "price": "400 coins (member price 360 coins, 10% member discount; sell price 40 coins)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json:16456 (item_id 77125, category_id 147, purchase_price_coins 400, member_discount_percent 10, member_price_coins 360, sell_price_coins 40)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale:30223 'Black Arch Tiger Block', definition 77125, model hsg_block_arch_01.adr, description 'Great for stackability.'", "source": "locale:30223; client definition"},
  {"claim": "Coin store row for item 77125 exists at 400 coins, member price 360, with source tags L1, L2, L4, R2, T633, R1", "source": "prototype/osfr-tools/data/content/stores.json:16456"},
  {"claim": "Sits in a Tiger block set of client items (Pink/Purple/Red/Teal/White Tall Rectangle, Blue/Green/Orange/Pink/Purple Arch Tiger Block, locale 30218-30228)", "source": "locale:30218 through locale:30228"},
  {"claim": "Negative finding: a client lookup for 'Black Arch Tiger Block' returns only the client name line; no wiki page, article or video covers this item", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.4,
 "open": [
  "Source type is a coin store listing, not an NPC vendor: no NPC vendor stock row names this item, and category 147 is a shared store grouping in stores.json.",
  "Current availability is unverified. The source tags (L1, L2, L4, R2, T633, R1) appear on many store rows and their meaning is not documented in the pack, so 'live' is unsure. The store row shows only that the listing exists in our data.",
  "No wiki, article or community source confirms the coin store sale or its price; the 400-coin price rests on the store data alone.",
  "Sibling Tiger block items (Tall Rectangle and other Arch variants, locale 30218-30228) were not checked for prices or sources, and their sources should not be inferred from this name cluster.",
  "Retirement status unknown: no source states whether the listing was removed."
 ]}
