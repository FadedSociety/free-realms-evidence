<!-- fleet job=citem-infer id=canguish-aid-shirt-974-v1 status=done turns=8 usd=0.0055 tokens(read,write,in,out)=[75593, 19697, 18, 4543] model=claude-haiku-5-5 -->
# Anguish Aid Shirt

{"item": {"name": "Anguish Aid Shirt", "locale_id": 974, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale (Coin Shop item-store entry for client definition 132, tint group 1); the store entry does not name the vendor NPC", "where": null, "price": "534 coins (member price 480 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 132 (category 103, purchase_price_coins 534; origin FreeRealms-Legacy CoinStoreItems.json)"},
  {"type": "vendor", "detail": "Coin store sale for client definition 540 (tint group 2) and definition 541 (tint group 3); same shirt in other tints", "where": null, "price": "291 coins (member price 261 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json items 540 and 541 (category 103)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client item name 'Anguish Aid Shirt' is locale 974, item class 7, slot 3, model military_<race>_<gender>_chest_longsleeve.adr, with 32 definitions across tints and races", "source": "locale:974; client definition supplied in pack"},
  {"claim": "Coin store entries exist for definitions 132 (534 coins) and 540/541 (291 coins each)", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 97, 258, 259"},
  {"claim": "Pack's coin_store_prices [291, 534] are prices; they map to definitions 540/541 and 132 respectively, not to item IDs 291 or 534. Store item 534 is a different definition (270 coins, category 101)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 256 and lines 97, 258-259"},
  {"claim": "Sibling items in the same set (Trauma Support Pants 969-972, Field Support Pants 973, Anguish Aid Boots 979, Elite Pink/Black variants 978, 32086) sit together in the client text table", "source": "locale:969-973, 978-979, 32086; locale:975-976 (Sunstone Valley promotion text)"},
  {"claim": "Wiki has no page for the shirt; the Medic/Blacksmith wiki pages cover only the Anguish Aid Bonesaw weapon (Blacksmith recipe, level 8 Medic), not this clothing", "source": "wiki page 'Anguish Aid Bonesaw'; wiki page 'Medic'"}],
 "confidence": 0.45,
 "open": ["Coin-store category 103 name and the vendor NPC that sells it are not in the repo data; the Coin Shop vs. a specific coin vendor is unconfirmed.",
  "Definitions 2232 and 18328-18334 (and the other ~24 of the 32 definitions) were not checked against store data; only 132, 540 and 541 have price entries.",
  "Live status: the store entry comes from the FreeRealms-Legacy reference data (revision 9e082025), not from a wiki or live-era source, so whether it was still sold late in the original run is unknown; retired is left null.",
  "The pack lists no wiki page, image, video or article for the shirt, and no quest, drop or event source; none could be found in the repo, client or wiki search.",
  "The Sunstone Valley text (locale 975-976) sits next to the set in the client table but was not tied to this shirt by any source; not used as a source.",
  "Chest slot/class from the client definition (slot 3, class 7) has not been checked against the wiki's clothing categories."]}
