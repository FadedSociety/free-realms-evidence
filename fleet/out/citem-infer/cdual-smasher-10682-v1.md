<!-- fleet job=citem-infer id=cdual-smasher-10682-v1 status=done turns=5 usd=0.0025 tokens(read,write,in,out)=[26231, 9686, 12, 2012] model=claude-haiku-5-5 -->
# Dual Smasher

{"item": {"name": "Dual Smasher", "locale_id": 10682, "kind": "weapon"},
 "sources": [{"type": "vendor", "detail": "Quartermaster Fizzi (gear merchant)", "where": "Sanctuary", "price": "1236 coins", "currency": "coins", "source": "wiki page 'Dual Smasher' (\"previously sold by Quartermaster Fizzi in Sanctuary for 1236 coins\"); prototype/osfr-tools/data/content/npcs/sanctuary.json:45619 (Fizzi vendor_stock lists Dual Smasher)"}],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Dual Smasher is a level 12 Warrior weapon, sold by Quartermaster Fizzi in Sanctuary for 1236 coins until retired on December 14, 2009", "source": "wiki page: Dual Smasher"},
  {"claim": "Wiki says it can presently be acquired only through trade (player-to-player), not from any vendor", "source": "wiki page: Dual Smasher"},
  {"claim": "Quartermaster Fizzi is the Sanctuary gear merchant that stocked Dual Smasher", "source": "notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:94; prototype/osfr-tools/data/content/npcs/sanctuary.json:45587"},
  {"claim": "Warrior weapons incl. Dual Smasher were all retired 14 December 2009", "source": "notes/Build Guides/Content/Jobs/Warrior.md:72; wiki page: Warrior"},
  {"claim": "Client name resolves to locale 10682 'Dual Smasher'", "source": "locale:10682"},
  {"claim": "Wiki effects: Sweeping Slash 1492 damage; Spinning Attack 2707 damage", "source": "wiki page: Dual Smasher"}
 ],
 "confidence": 0.8,
 "open": [
  "The pack's client coin_store_prices value 281 could not be matched: stores.json has no item_id 281 row, and the 1236-coin price appears in stores.json only on other item IDs (e.g. 4148, 6863). Unverified whether 281 is a store-row or item reference; the 1236-coin price rests on the wiki, not on the store data.",
  "Wiki gives Dual Smasher's item level as 12, while the Warrior job page's internal note lists 11 (notes/Build Guides/Content/Jobs/Warrior.md:226). Not resolved by the client; the wiki value is used here.",
  "Trade availability is a player-to-player source, not a vendor/drop; no trade source was documented beyond the wiki sentence. Live status set to 'no' since the vendor sale ended; the trade-only remark is not verified in-game.",
  "No quest reward, drop, event, or prize-wheel source found for this item; none listed."
 ]}
