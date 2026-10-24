<!-- fleet job=citem-infer id=cponytail-hair-style-card-114560-v2 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[15331, 10113, 8, 2033] model=claude-haiku-5-5 -->
# Ponytail Hair Style Card

{"item": {"name": "Ponytail Hair Style Card", "locale_id": 114560, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop hair style card (store category 141), inferred from store data for definition 6851; no display frame names Ponytail, so this is store-data only", "where": "Coin Shop (stores.json category 141)", "price": "540 coins (store purchase_price_coins); 486 coins displayed in sibling Coin Shop frames", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:1865 (item 6851, purchase_price_coins 540, member_price_coins 486, no_sale false); video:1xtVveaQ3XI/00124.jpg, 00128.jpg, 00148.jpg, 00150.jpg (sibling style cards Ragged, Spacey, Wolfy, Long Curly, Sassy shown at 486 coins)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ponytail Hair Style Card', locale 114560, description 'This haircut is simply cute.', slot 2, class 1, two definitions (6851, 35947)", "source": "locale:114560; client definition"},
  {"claim": "Definition 6851 is a Coin Shop row in category 141 at 540 coins list, 486 member price, sell 54, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:1865"},
  {"claim": "Definition 35947 is a second category 141 row at 540 coins, no_sale true, no sell price; it is not a sellable source", "source": "repo:prototype/osfr-tools/data/content/stores.json:11703"},
  {"claim": "Sibling hair style cards (Ragged, Spacey, Wolfy, Long Curly, Sassy) display at 486 coins in the Coin Shop category in Oct 2013 video frames", "source": "video:1xtVveaQ3XI/00124.jpg, 00128.jpg, 00148.jpg, 00150.jpg"},
  {"claim": "No video frame or wiki page names Ponytail Hair Style Card directly (lookup returns only the client locale line)", "source": "lookup of 'Ponytail hair style card' across client, wiki, video, articles"},
  {"claim": "Name is in a cluster of hair style card lines (Curly, Pigtails, Ragged, Low Pigtail, Long Curly, Wolfy)", "source": "locale:114555-114565"},
  {"claim": "A separate item 'Bumpy Ponytail Hair Style Card' (locale 415864) exists and is not the same card", "source": "locale:415864"}
 ],
 "confidence": 0.45,
 "open": [
  "Coin Shop sale is inferred from store data (definition 6851, category 141) and sibling cards; no frame or wiki page shows Ponytail itself.",
  "Displayed price in frames is 486 coins for siblings; store data lists 540 purchase and 486 member price. Which one a player paid is unconfirmed; the 486 vs 540 relationship is not stated by any source.",
  "Sale window/dates are unknown; nothing in the pack dates the Ponytail listing, so live status is unsure and retired status is unknown.",
  "Definition 35947 (no_sale true) role is unexplained; it is not treated as a source.",
  "The earlier Super Spooktacular wiki citation for the 486 prices was dropped; it does not show these cards in the snippet reviewed.",
  "No drop, quest, crafting, prize wheel, or event source found for this card."
 ]}
