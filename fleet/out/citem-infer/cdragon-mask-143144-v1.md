<!-- fleet job=citem-infer id=cdragon-mask-143144-v1 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[3234, 5041, 6, 1671] model=claude-haiku-5-5 -->
# Dragon Mask

{"item": {"name": "Dragon Mask", "locale_id": 143144, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Cragara (Mysterious Merchant category), regular price for everyone", "where": "Coin store (stores.json category 101, item 15684)", "price": "270 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15684 (purchase_price_coins 270); wiki page 'Dragon Mask' (sold by Cragara, Category:Mysterious Merchant)"},
  {"type": "vendor", "detail": "Cragara, Members 10% discount price", "where": "Coin store (stores.json category 101, item 15684)", "price": "243 coins (member price, 10% off 270)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15684 (member_price_coins 243, member_discount_percent 10); wiki page 'Dragon Mask' (10% member discount)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Item 15684 is in the coin store data at 270 coins, members 243 (10% off), category 101", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15684"},
  {"claim": "Wiki says the Dragon Mask is bought through Cragara by everyone at the regular price and by Members at a 10% discount; it is in Category:Mysterious Merchant, Freestyle Jobs, Head, Clothing", "source": "wiki page 'Dragon Mask'"},
  {"claim": "Client name 'Dragon Mask' with description 'Strike fear into small animals and gallant knights!' is locale 143144; the item has a companion line at locale 150466", "source": "locale:143144; locale:150466"},
  {"claim": "Head slot (slot 12) clothing, class 1, one model family freestyle_<race>_<gender>_head_longfaceanimal.adr", "source": "client definition pack"}],
 "confidence": 0.7,
 "open": ["The wiki price figures are blank in the text we have (\"regular price of  ... .\"), so the 270 / 243 figures come from the store data, not a wiki quote; the 10% member discount matches the store data.",
  "Only the Mysterious Merchant category is named as a source; the Cragara vendor is named on the wiki but no repo vendor file was checked for the Cragara stock list, so the vendor link rests on the wiki text.",
  "Retired status is unknown: no source states whether Cragara/Mysterious Merchant still sells it or when it was removed.",
  "Client definition lists 37 definitions but only 12 ids were given; tints/races variants were not individually checked for price differences.",
  "No quest, drop, event, or crafting source found in the pack; none were checked beyond these."]}
