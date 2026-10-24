<!-- fleet job=citem-infer id=chasty-mailing-hat-26999-v1 status=done turns=8 usd=0.0071 tokens(read,write,in,out)=[123668, 29827, 18, 4337] model=claude-haiku-5-5 -->
# Hasty Mailing Hat

{"item": {"name": "Hasty Mailing Hat", "locale_id": 26999, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Legacy coin store sale (CoinStoreItems row 13117, tint group 1, the 291-coin variant); no coin vendor in our vendors data names this item, so the NPC is unknown", "where": "coin store (Legacy CoinStoreItems; the vendor/shop is not named)", "price": "291 coins (member price 261 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 13117"},
            {"type": "vendor", "detail": "Legacy coin store rows 13119 (tint group 2) and 13120 (tint group 3); unnamed vendor", "where": "coin store (Legacy CoinStoreItems; the vendor/shop is not named)", "price": "9453 coins (member price 8507 coins); the value looks like a placeholder, see open", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json items 13119, 13120"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client item name is 'Hasty Mailing Hat' (locale 26999); 16 definitions share the name, 12 listed definition ids, slot 1, class 3, model courier_<race>_<gender>_head_safarihat.adr", "source": "locale:26999"},
              {"claim": "Store rows exist for item ids 13117, 13119 and 13120 only, with coin prices 291, 9453 and 9453; the other listed definition ids (13123-13138) have no coin store row", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3596-3599"},
              {"claim": "Store rows carry Legacy CoinStoreItems provenance (L1) and no wiki or article price exists for the item", "source": "repo:prototype/osfr-tools/data/content/stores.json source_tags L1"},
              {"claim": "No wiki page, article, or video frame names the item; the vendor stock list is empty and no vendor record in vendors.json references item 13117, 13119 or 13120", "source": "lookup (wiki, articles, video: no matches); repo vendors.json search"}],
 "confidence": 0.3,
 "open": ["The coin store rows say a coin sale exists, but no vendor, NPC or shop name is linked to them; find the Legacy CoinStoreItems vendor binding before naming a vendor location.",
          "The 9453-coin price appears on many unrelated items in stores.json (for example item 87, 100, 102), so it is probably a Legacy placeholder and not a real price; treat it as unverified.",
          "Only 3 of the 12 listed definition ids have a coin store row; the other variants have no sale price in our data.",
          "No wiki, article or video evidence exists for this item, so the 'courier' theme (Royal Courier, Evil Postman) is unconfirmed as a source; the Royal Courier quest pays coins only.",
          "Whether the Legacy coin store sale was live at the 2009-2014 shutdown is not confirmed; the live status is unsure.",
          "The item's description is empty, so the set or promotion it belongs to is unknown."]}
