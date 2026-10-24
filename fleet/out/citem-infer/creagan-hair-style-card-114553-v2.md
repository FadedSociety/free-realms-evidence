<!-- fleet job=citem-infer id=creagan-hair-style-card-114553-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6682, 9522, 6, 1534] model=claude-haiku-5-5 -->
# Reagan Hair Style Card

{"item": {"name": "Reagan Hair Style Card", "locale_id": 114553, "kind": "card"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop listing of Reagan Hair Style Card (item 6844). List price 540 coins; member price 486 coins (10% member discount). The Coin Shop frames show the 486-coin price for members, and 'You saved 54' appears beside the item.", "where": "Coin Shop", "price": "540 coins list; 486 coins member price", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1858 (item 6844: purchase_price_coins 540, member_discount_percent 10, member_price_coins 486, sell_price_coins 54); video:1xtVveaQ3XI/00124, video:1xtVveaQ3XI/00116, video:1xtVveaQ3XI/00128"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 114553 is 'Reagan Hair Style Card', description 'A very economical hair style.', slot 2, class 1.", "source": "locale:114553"},
  {"claim": "Store data lists item 6844 at 540 coins purchase, 10% member discount, 486 member price, sell price 54.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1858"},
  {"claim": "Coin Shop frames list Reagan Hair Style Card at 486 coins alongside Ragged, Spacey and Fauxhawk style cards, and show 'You saved 54' beside it.", "source": "video:1xtVveaQ3XI/00116, video:1xtVveaQ3XI/00124, video:1xtVveaQ3XI/00128"},
  {"claim": "The frames carry no date, so the listing cannot be tied to a specific event or week.", "source": "video:1xtVveaQ3XI frames (no date text in lookup results)"}
 ],
 "confidence": 0.6,
 "open": [
  "Retirement date unknown: no source states when the Coin Shop listing ended, so retired is null.",
  "Live status is unsure: no dated capture of the listing exists in the pack.",
  "Event attribution dropped: the earlier claim that the card belongs to Super Spooktacular week 1 (10/1/2013) had no source text in the pack and was not confirmed by lookup. Treat any event link as unverified.",
  "Item 35940 is a second definition with the same name, 540/486 coin prices and no_sale=true (repo:prototype/osfr-tools/data/content/stores.json line 11696). No wiki or video frame names it separately, so its source is unconfirmed; it is not listed as a separate source.",
  "No membership, promotion, drop, quest or vendor-stock source was found in the pack.",
  "Jev's first-pass 'vendor' guess is replaced by the Coin Shop evidence; the 486 figure is the member price, not a sale price."
 ]}
