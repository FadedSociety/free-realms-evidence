<!-- fleet job=citem-infer id=cn-storm-strike-gloves-pl-storm-strike-gloves-633-v2 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[20108, 15643, 8, 2933] model=claude-haiku-5-5 -->
# {n}Storm Strike Gloves{pl="Storm Strike Gloves"}

{"item": {"name": "Storm Strike Gloves", "locale_id": 633, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, vendor not named in any source. Only the client definition Cost field (item definition 1284) shows a price; no stock row, vendor or zone is evidenced", "where": null, "price": "291 coins (member price 261 coins with 10% member discount, as the Cost and MemberDiscount fields imply)", "currency": "coins", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 25915-25936 (Id 1284, NameId 633, Cost 291, MemberDiscount 10)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition 1284 is named Storm Strike Gloves, NameId 633, slot 2, class 16, CategoryId 102, MinProfileRank 10, PowerRating 3, model archer_<race>_<gender>_hands_shortarmorglvs.adr", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 25915-25936; locale:633"},
  {"claim": "Cost 291 and MemberDiscount 10 on item 1284; the same Cost 291 and MemberDiscount 10 appear on Storm Strike Boots (1283)", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 25893-25914 and 25915-25936"},
  {"claim": "Storm Strike set names (Hoodie 623, Boots 628, Gloves 633, Leggings 638, Quiver 643) exist in client text", "source": "lookup client results for 'Storm Strike'; locale:628, locale:633, locale:638"},
  {"claim": "repo prototype/osfr-tools/data/content/stores.json has no row for item 1284. The only 291/member-261 row found is item_id 11284 (a different item), so the store-data check does not confirm this listing", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3284"},
  {"claim": "No wiki page, wiki image, article or video names Storm Strike Gloves. Wiki hits for 'Storm Strike' are only unrelated 1000 Storms / Lightning Strike ninja pages", "source": "lookup wiki/articles/video 'Storm Strike' (no matching page)"}
 ],
 "confidence": 0.25,
 "open": [
  "Vendor, zone and sale window are unknown. The coin price is a legacy client Cost field; no store row for item 1284 exists in our stores.json (only item 11284 at the same 291/261 price, which is a different item). Treat the coin shop source as unverified until a stores.json row or wiki entry names the vendor.",
  "Live status is unsure. No source confirms the sale ran late in the game or was retired. The first-pass 'live yes / coin_shop' is a hint only.",
  "Wireable is false: a builder cannot set a real acquisition from this answer until a vendor, stock row or other acquisition source is found for item 1284 or its variants.",
  "Variants: the 18 definitions (ids 370, 1226, 1284, 1313, 11445-11461) were not individually checked for tints, races or separate sources.",
  "Treasure War (locale 629, flagged not_live), the Savage Sting Bow recipe and the Mystery Chest promo text are not tied to this item by any source. They are not claimed as sources.",
  "Quest reward, enemy drop, crafting, collection, event and prize wheel sources: none found in the pack; not claimed."
 ]}
