<!-- fleet job=citem-infer id=cponytail-hair-style-card-114560-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6667, 9085, 6, 1955] model=claude-haiku-5-5 -->
# Ponytail Hair Style Card

{"item": {"name": "Ponytail Hair Style Card", "locale_id": 114560, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop hair style card, store category 141, store row for definition 6851 (no_sale false, sellable; sell-back 54 coins)", "where": "Coin Shop (stores.json category 141)", "price": "540 coins purchase; 486 coins member price (10% member discount in store data)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:1865"},
  {"type": "coin_shop", "detail": "Second category 141 row for definition 35947 (no_sale true, no sell-back value). Same purchase price as 6851, so it is also a buy listing, not a separate item", "where": "Coin Shop (stores.json category 141)", "price": "540 coins purchase; 486 coins member price", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11703"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ponytail Hair Style Card', description 'This haircut is simply cute.', slot 2, class 1, definitions 6851 and 35947", "source": "locale:114560; client definition"},
  {"claim": "Definition 6851 is a category 141 coin-store row: purchase 540, member_discount_percent 10, member_price 486, sell 54, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:1865"},
  {"claim": "Definition 35947 is a category 141 coin-store row: purchase 540, member 486, sell null, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:11703"},
  {"claim": "A lookup of the name across client, wiki and video returns only the client locale lines (114560 and the separate Bumpy Ponytail card 415864); no wiki page or video frame names Ponytail Hair Style Card", "source": "lookup 'Ponytail Hair Style Card' (client, wiki, video)"},
  {"claim": "Sibling hair style cards are shown at 486 coins in Oct 2013 video frames (Ragged, Spacey, Wolfy, Long Curly, Sassy). Not re-checked in this pass; taken from the prior answer", "source": "video:1xtVveaQ3XI/00124.jpg, 00128.jpg, 00148.jpg, 00150.jpg (prior answer, unverified here)"},
  {"claim": "The earlier Super Spooktacular wiki citation was removed; it does not show these cards at 486", "source": "critique of prior answer"}
 ],
 "confidence": 0.5,
 "open": [
  "The Coin Shop listing is supported by store data only (stores.json rows for 6851 and 35947). No display frame or wiki page shows Ponytail itself, so the sale is not confirmed on screen.",
  "Price: store data says 540 purchase and 486 member price (the 486 is computed as a 10% member discount). Which price a non-member sees in the shop is not confirmed by a frame for Ponytail; the 486 figure for sibling cards comes from video frames not re-checked here.",
  "Sale window and dates are unknown. Nothing in the pack dates the listing, so retired is null and live is unsure.",
  "No drop, quest reward, crafting, prize wheel, or event source found for this card."
 ]}
