<!-- fleet job=citem-infer id=cspectrum-wand-139993-v6 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6482, 9978, 6, 1701] model=claude-haiku-5-5 -->
# Spectrum Wand

{"item": {"name": "Spectrum Wand", "locale_id": 139993, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only, per the wiki page. No vendor, NPC, quest, drop, event or crafting source is named for this item.", "where": null, "price": null, "currency": null, "source": "page:ns0 Spectrum Wand (wiki): 'can only be acquired through trade'"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Spectrum Wand is a level 13 Wizard Blue Text weapon (Power 5), acquirable only through trade per the wiki. Zap 853 damage, Lightning Blast 3492.", "source": "page:ns0 Spectrum Wand (wiki); image:item_tooltip Spectrum Wand item.jpg"},
  {"claim": "The wiki page is in Category:Retired Weapons and Category:Blue Text Weapons; Blue Text weapons were retired (names moved to white font).", "source": "page:ns0 Spectrum Wand category list; page:ns14 Category:Blue Text Weapons (wiki)"},
  {"claim": "Spectrum Wand is listed with the Spectrum set (Bow, Anvil, Bonesaw, Scythe, Hammer) in the Blue Text weapon table.", "source": "page:ns0 Blue Text weapon (wiki), weapon table"},
  {"claim": "Client name is locale 139993 'Spectrum Wand', clustered with locale 139988-139992 (Spectrum Bow, Anvil, Bonesaw, Scythe, Hammer).", "source": "locale:139993; locale:139988-139992"},
  {"claim": "Store row for item 48243 (category 207, purchase 1431 coins, member price 1287, sell 143) is one of an identical block covering items 48231-48243 (same tier values), with no vendor, shop, zone or date named. The client coin_store_prices [1431] and the tooltip Resell Value 143 match this row. Not counted as a sale source because the row is a shared tier and the wiki says trade only.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13280-13292"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the wiki says trade-only, but stores.json item 48243 (category 207, 1431 coins, member 1287, sell 143) and client coin_store_prices [1431] show a coin-store price. The row sits in an identical block for items 48231-48243 with no vendor, shop or date, so it may be a generic tier price. Needs a dated vendor or Coin Shop listing to confirm or refute. If confirmed, add a coin_shop source at 1431 coins (member 1287).",
  "Blue Text weapon class note: wiki says Blue Text weapons dropped in dungeons from unnamed boss enemies before retirement. No boss, dungeon or drop table names Spectrum Wand, so no drop source is listed.",
  "No zone, NPC, shop, quest, event, crafting, collection or prize-wheel source found for this item.",
  "Retirement date (14 Dec 2009) comes from the wiki category. Whether the item was ever sold at the coin store, and when, is undated, so live:'no' is not fully settled.",
  "Not wireable: the only evidenced source is trade, which has no price, NPC or event for a builder to set."
 ]}
