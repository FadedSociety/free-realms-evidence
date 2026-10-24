<!-- fleet job=citem-infer id=cmidnight-shadow-hair-color-card-414085-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[8520, 8106, 8, 2297] model=claude-haiku-5-5 -->
# Midnight Shadow Hair Color Card

{"item": {"name": "Midnight Shadow Hair Color Card", "locale_id": 414085, "kind": "card"},
 "sources": [{"type": "vendor", "detail": "Coin store vendor sale (exact NPC/shop not identified in our data; store category 142, unnamed)", "where": null, "price": "180 coins (member price 162 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7913 (item_id 35980, purchase_price_coins 180, member_price_coins 162); client definition coin_store_prices [180] for definition 35980"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client defines the item as 'Midnight Shadow Hair Color Card' (locale 414085), a style card that changes hair color, with 2 definitions (35980, 68847), slot 3, class 1.", "source": "locale:414085; client definition"},
  {"claim": "Store data lists definition 35980 in coin store category 142 at 180 coins, member price 162 coins, with no_sale true (cannot be sold back to vendors).", "source": "repo:prototype/osfr-tools/data/content/stores.json:7913"},
  {"claim": "Sibling hair color cards (e.g. 35950-35969) are listed in the same category 142 at the same 180-coin price with the same source tags, so the card belongs to a batch of style cards sold together.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7883-7902"},
  {"claim": "The wiki has pages for other hair color cards (Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum) introduced in the October 2013 Super Spooktacular update, but no page or image names Midnight Shadow.", "source": "wiki: Super Spooktacular; File:Snowstorm.PNG; lookup 'Midnight Shadow' returned no wiki, article or video hits"}],
 "confidence": 0.4,
 "open": ["The coin store vendor/NPC and zone for category 142 are not named in our data; the 'where' field is left null.",
  "The source_tags (L1, L2, L3, L4, R2) in stores.json are not decoded, so the location of the sale is unknown.",
  "No wiki, article, or video evidence names Midnight Shadow Hair Color Card. Its release date and any retirement are unverified. Live status is only inferred from the store entry.",
  "Definition 68847 has no store entry; it is unclear whether it is a tint or race variant that is sold differently.",
  "The first-pass tag said 'vendor', and that matches the store price. It is a hint only and is not used as evidence for the source list.",
  "Client cluster neighbours 414086/414087 (Ocean Depths) are a separate item family and were not used."]}
