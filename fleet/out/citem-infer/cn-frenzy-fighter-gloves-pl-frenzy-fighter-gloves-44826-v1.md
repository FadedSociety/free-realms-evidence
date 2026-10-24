<!-- fleet job=citem-infer id=cn-frenzy-fighter-gloves-pl-frenzy-fighter-gloves-44826-v1 status=done turns=8 usd=0.0072 tokens(read,write,in,out)=[134551, 30680, 18, 4128] model=claude-haiku-5-5 -->
# {n}Frenzy Fighter Gloves{pl="Frenzy Fighter Gloves"}

{"item": {"name": "Frenzy Fighter Gloves", "locale_id": 44826, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale of Frenzy Fighter Gloves: store entries for item_id 9851 (tint group 1) and item_id 9852 (tint group 2), category 102, each at 957 coins (member price 861 coins, 10% member discount; sell price 95 coins)", "where": null, "price": "957 coins (member price 861 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:4518-4519 (item 9851, 9852); the 957 price also matches the client-definition coin_store_prices value"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Frenzy Fighter Gloves' is locale 44826, a clothing item in slot 2, class 25, with 12 definition ids listed (pack says 13 definitions), sharing the name with variants.", "source": "locale:44826; client definition pack"},
  {"claim": "Store data lists item_ids 9851 and 9852 (inside the pack's definition-id list) in category 102 at purchase_price_coins 957, member_price_coins 861, sell_price_coins 95, not no_sale, with live-style source tags (L1, L2, L4, R2, T633, R1).", "source": "repo:prototype/osfr-tools/data/content/stores.json:4518-4519"},
  {"claim": "Same-set items Daring Destroyer Gloves (locale 44825), Elite Pink Frenzy Fighter Gloves (44829), Elite Black Frenzy Fighter Gloves (44831) and the Frenzy Fighter Boots/Pants/Shirt/Helmet/Pauldrons appear in the client text as one set.", "source": "locale:44825, locale:44829, locale:44831, locale:44896; client text lines"},
  {"claim": "No wiki page, image, article fact or video frame names Frenzy Fighter Gloves; the only wiki Frenzy Fighter item is the Frenzy Fighter Hammer (Blacksmith recipe), which is not this item.", "source": "lookup wiki results: 'Frenzy Fighter Hammer'"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor/shop location for the coin store sale is not stated in stores.json (the entries are CoinStoreItems by category, not by NPC); the 'where' field is left null.",
  "Only item_ids 9851 and 9852 of the 12 listed definition ids appear in the coin store data; 9825-9849 have no store entry, so they are likely non-store variants or drops/rewards, but no source for them was found.",
  "Pack says 13 definitions but lists 12 ids; one definition id is missing from the pack.",
  "item_id 9855 (tint group 3) is also priced at 957 coins in category 102 but is not in this pack's definition list; it may be another Frenzy/Daring set piece and was not verified.",
  "No quest reward, enemy drop, event, prize wheel, crafting, or collection source found in the pack or repo for this item.",
  "Retirement status unknown: no wiki or article source states whether the coin store sale ended; the store entry carries live-style tags but that is not a dated source.",
  "Client definition description is empty, so no in-game text confirms the item's acquisition."
 ]}
