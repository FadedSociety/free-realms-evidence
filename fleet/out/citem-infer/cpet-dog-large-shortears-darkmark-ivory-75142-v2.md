<!-- fleet job=citem-infer id=cpet-dog-large-shortears-darkmark-ivory-75142-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5799, 8719, 6, 1725] model=claude-haiku-5-5 -->
# Pet: Dog: Large Shortears: darkmark-ivory

{"item": {"name": "Pet: Dog: Large Shortears: darkmark-ivory", "locale_id": 75142, "kind": "pet"},
 "sources": [{"type": "coin_shop", "detail": "Legacy coin-store row for the Large Shortears dog pet, darkmark-ivory tint (tint_group_id 2). No vendor NPC or shop category is named; category_id is null.", "where": null, "price": "540 coins (member price 486 coins, 10% member discount); sell-back 54 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23992 (line 6869)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "stores.json item 23992 has purchase_price_coins 540, member_discount_percent 10, member_price_coins 486, sell_price_coins 54, tint_group_id 2, category null, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23992 (line 6869)"},
  {"claim": "The client definition for 23992 (definition 23992, model dog_large_shortears.adr, slot 0, class 0) carries coin store price 540.", "source": "client definition in evidence pack; locale:75142"},
  {"claim": "The name sits in an 11-entry client cluster of Large Shortears dog pet tints, locale:75137 to locale:75147; the text has no quest, enemy, event, or wiki mention.", "source": "locale:75137 to locale:75147; lookup client for 'Large Shortears dog pet' returned only the locale rows"},
  {"claim": "The same 540/486/54 price and source tags (L1, L2, L4, R2, T633, R1) appear on many neighbouring rows (23983 to 23998 and beyond), so the 540 looks like the Legacy CoinStoreItems block value rather than a price checked per item.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6860-6875"},
  {"claim": "No wiki page, image, article fact, or video frame names this tint; no vendor stocks it in the pack.", "source": "lookup across client, wiki, articles, video for 'Large Shortears dog pet': no matches beyond locale rows"}
 ],
 "confidence": 0.35,
 "open": [
  "The coin_shop source rests only on a Legacy stores.json row. The same 540 value is shared by many rows with the same tags, so it is not an independently verified live price. Treat it as a Legacy-derived price.",
  "No vendor NPC, shop, or zone is identified; where is null. Nothing in the pack places this pet in a stocked live shop.",
  "No wiki or article evidence confirms this item was sold in the live game, so live stays 'unsure' and retired stays null. Whether it was retired or never sold is unknown.",
  "Critique feedback applied: the earlier claim that the 540 price is 'not a shared placeholder' is withdrawn, and row 23990 (SC Marketplace, 400 SC via a reconstructed wiki price on Diego) is not used as confirmation because it is no_sale and reconstructed.",
  "Confidence lowered from 0.6 to 0.35 for these reasons."
 ],
 "confidence_note": "0.35"}
