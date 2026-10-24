<!-- fleet job=citem-infer id=cjuicy-apricot-hair-color-card-414077-v3 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[14480, 8940, 8, 1905] model=claude-haiku-5-5 -->
# Juicy Apricot Hair Color Card

{"item": {"name": "Juicy Apricot Hair Color Card", "locale_id": 414077, "kind": "card"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop store-data listing, item 35972 (category 142), a hair color card. Store row flagged no_sale=true, so it is a listed row, not a confirmed active sale. Sibling hair color cards in the same Coin Shop section are shown at 162 coins in video frames.", "where": "Coin Shop (store category 142; shop name not decoded)", "price": "180 coins list (purchase_price_coins); 162 coins member price (10% member discount). Sibling cards displayed at 162 coins in video.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7905 (item 35972); video:1xtVveaQ3XI/00112.jpg and video:1xtVveaQ3XI/00116.jpg (sibling cards Gold Rush, Atomic Blast, Sun Kissed, Shock Wave at 162 coins; this card not in frame)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 414077 is 'Juicy Apricot Hair Color Card'; description: changes hair color; class 1, slot 3; definition ids 35972 and 68839 (68839 has no store row).", "source": "locale:414077; client definition"},
  {"claim": "Store row item 35972: category 142, purchase_price_coins 180, member_discount_percent 10, member_price_coins 162, no_sale true. Rows 35963-35979 share identical values.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7896-7912 (re-read and confirmed)"},
  {"claim": "Coin Shop frames list sibling hair color cards (Gold Rush, Atomic Blast, Sun Kissed, Shock Wave) at 162 coins, and hair style cards at 486 coins. Juicy Apricot is not named in these frames.", "source": "video:1xtVveaQ3XI/00112.jpg; video:1xtVveaQ3XI/00116.jpg"},
  {"claim": "No wiki page, article, quest, drop, event, prize wheel, crafting, collection, membership or promotion source names this card.", "source": "lookup over client, wiki, articles, video (no hits for this card)"}
 ],
 "confidence": 0.35,
 "open": [
  "The Coin Shop source rests on a store-data row flagged no_sale=true plus frames showing sibling colour cards, not this card. Treat as a probable coin-shop listing, not a confirmed sale.",
  "Price to wire is unresolved: the store row says 180 list / 162 member, but the frames show sibling cards displayed at 162. Whether a buyer sees 162 or 180 is not confirmed for this card.",
  "Live status unsure; retirement unknown. no_sale=true may mean it is no longer sold for coins; no dated source confirms either way.",
  "Definition 68839 has no store row; unclear whether it is a tint or a separate variant.",
  "Store category 142 and source tags (L1, L2, L3, L4, R2) are not decoded, so the exact shop and location are unconfirmed.",
  "No quest, drop, event, prize wheel, crafting, collection, membership or promotion source was found."
 ]}
