<!-- fleet job=citem-infer id=cspectrum-bow-139988-v3 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6295, 7879, 6, 1671] model=claude-haiku-5-5 -->
# Spectrum Bow

{"item": {"name": "Spectrum Bow", "locale_id": 139988, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for item 48238 (store category 207; category name not confirmed). No vendor identified: no vendors.json row sells 48238.", "where": "Coin store, category 207", "price": "1431 coins (purchase_price_coins); the row also lists member_price_coins 1287 at 10% member discount, which the pack itself does not explain as a sale price", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13287; client definition coin_store_prices [1431]; FreeRealms-Legacy CoinStoreItems.json Id 48238, CategoryId 207"},
  {"type": "drop", "detail": "Blue Text weapons were members-only weapons acquired in dungeons where they were dropped. The specific dungeon and enemy for Spectrum Bow are not named in any source.", "where": "dungeons (unspecified)", "price": null, "currency": null, "source": "wiki: Blue Text weapon"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 139988 'Spectrum Bow', in the Blue Text weapon group with Rainbow and Spectrum tier weapons (139983-139993).", "source": "locale:139988; locale:139983-139993"},
  {"claim": "Store row for item 48238 exists at purchase price 1431 coins, category 207, with member price 1287 and sell price 143; the client definition carries coin_store_prices [1431].", "source": "repo:prototype/osfr-tools/data/content/stores.json:13287; client definition coin_store_prices [1431]"},
  {"claim": "Wiki Blue Text weapon page: names used to appear in blue font before being retired; they were members-only weapons acquired in dungeons where they were dropped.", "source": "wiki: Blue Text weapon"},
  {"claim": "The wiki page's retirement wording says Blue Text weapons are retired. The retrieved text did not show the Dec 14, 2009 date or a trade-only statement, so those are not used here.", "source": "wiki: Blue Text weapon"}
 ],
 "confidence": 0.35,
 "open": [
  "Sale window of the 1431-coin store row is undated. The wiki says the weapon is retired, but no source gives when the coin sale started or ended, so it is not known whether it was sold while live.",
  "Coin store vendor/NPC is not identified; no vendors.json row sells 48238. The category 207 name (Coin Shop tie) is unconfirmed.",
  "Meaning of member_price_coins 1287 and source tags T633, R1 in the store row is unexplained by any source.",
  "Dungeon and enemy that drop Spectrum Bow are not named; the drop source rests only on the general Blue Text weapon page.",
  "Trade-only status and the Dec 14, 2009 retirement date claimed in the earlier answer were not confirmed in the retrieved wiki text; treat as unverified.",
  "Spectrum Wand 'Resell Value: 143' is not used as a price match; it is a sell value for a different item in the tier.",
  "No crafting, prize wheel, event, quest reward, or collection source found."
 ]}
