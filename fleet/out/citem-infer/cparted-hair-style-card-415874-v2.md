<!-- fleet job=citem-infer id=cparted-hair-style-card-415874-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[11041, 8764, 8, 1812] model=claude-haiku-5-5 -->
# Parted Hair Style Card

{"item": {"name": "Parted Hair Style Card", "locale_id": 415874, "kind": "card"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop hair style card (store item 69020, category 141). Store row lists 540 coins list price; 486 coins member price (10% member discount). Row is flagged no_sale: true.", "where": "Coin Shop", "price": "540 coins (list); 486 coins (member price)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14763 (item_id 69020); the same row shape runs across items 69009-69025 (lines 14752-14768), so this is a category price, not a per-card sale record"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines Parted Hair Style Card as locale 415874, description 'Parting is such sweet sorrow.', slot 2, class 1, one definition (69020).", "source": "locale:415874; client definition pack"},
  {"claim": "Store data lists item 69020 in category 141 at 540 coins list, 486 member price, no_sale true.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14763"},
  {"claim": "The client name cluster locale:415869 to 415879 is a set of hair style cards (Updo, Buzzed, Cornrow, Metal, Mullet, Parted, Short Parted, Spiked, Swirly, Top Knot, Buzzed Top Knot).", "source": "locale:415869-415879"},
  {"claim": "Sister hair style cards (Frosty, Flame, Wavy, Fauxhawk, Sassy, Marie) were listed in the Coin Shop at 486 coins in the Super Spooktacular period (Oct 2013). This is sibling context only; no source names Parted itself.", "source": "wiki: Super Spooktacular; video:1xtVveaQ3XI/00150.jpg; video:1xtVveaQ3XI/00124.jpg"}
 ],
 "confidence": 0.4,
 "open": [
  "No wiki page, image, article fact, or video frame names the Parted Hair Style Card. The Coin Shop source rests only on the store data row.",
  "Every row in the 69009-69025 block carries no_sale: true, including the Parted row. That flag suggests the card is not currently sold in the coin store, but no source gives a retirement date or a removal date, so retired is null and live is unsure.",
  "540 list vs 486 member: the store data gives both. The wiki's 486 figure matches the member price for sibling cards, so it is probably the member or sale price. Which price a non-member paid for Parted is unconfirmed.",
  "Not checked or not evidenced: enemy drops, quest rewards, promotions, prize wheel, membership, or crafting sources for Parted. No evidence in the pack for any of them.",
  "The jev first-pass tag (vendor, live: yes) is a hint only and was not used as evidence."
 ]}
