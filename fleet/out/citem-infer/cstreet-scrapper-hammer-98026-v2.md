<!-- fleet job=citem-infer id=cstreet-scrapper-hammer-98026-v2 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[18406, 13415, 8, 2399] model=claude-haiku-5-5 -->
# Street Scrapper Hammer

{"item": {"name": "Street Scrapper Hammer", "locale_id": 98026, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing (store category 207), tint groups 1 and 2 (item 37465, 37468). Vendor NPC not identified in any source.", "where": "unnamed coin store, category 207", "price": "866 coins (member price 779 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12264-12265 (items 37465, 37468); also reference/weapons.json cost 866"},
  {"type": "vendor", "detail": "Coin store listing (store category 207), tint group 3 (item 37471). Vendor NPC not identified.", "where": "unnamed coin store, category 207", "price": "760 coins (member price 684 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12266 (item 37471); reference/weapons.json cost 760"},
  {"type": "other", "detail": "Player-to-player trade only, per wiki. Conflicts with the coin store rows above; unresolved.", "where": null, "price": null, "currency": null, "source": "wiki page 'Street Scrapper Hammer' ('can only be acquired through trade')"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Street Scrapper Hammer' is locale 98026, item class 5, slot 7, with 10 definitions (37465-37496).", "source": "locale:98026; client definition pack"},
  {"claim": "Wiki: level 4 Brawler weapon, Green Text weapon, 'can only be acquired through trade'; Glancing Blow 776 damage, Leg Sweep 2716 damage. Page is in Category:Retired Weapons and Category:Green Text Weapons.", "source": "wiki page 'Street Scrapper Hammer'; wiki page 'Green Text weapon' lists it"},
  {"claim": "stores.json rows: 37465 and 37468 at 866 coins (member 779); 37471 at 760 (member 684); no_sale false; sell_price 86/86/76.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12264-12266"},
  {"claim": "reference/weapons.json lists a 'cost' for all 10 client items: 866 for 37465, 37468, 37474, 37477 and 760 for 37471; 37471 is power 2 and min profile rank 8, the others power 3 and rank 4.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:43278-43345"},
  {"claim": "Brawler weapon tier notes list Street Scrapper as the level 4 weapon.", "source": "notes/Build Guides/Content/Jobs/Brawler.md:210"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: wiki says 'can only be acquired through trade', but stores.json lists coin store rows with no_sale false. Unresolved; no source gives dates for either.",
  "Retired status rests only on the wiki's Retired Weapons category. No retirement date or last-sale date is in any source, so 'retired: true' is inferred.",
  "Vendor NPC and zone for store category 207 are not named in the pack or in vendors.json; the 'vendor' type is a store listing, not an identified NPC.",
  "Only 3 of 10 definitions have stores.json rows (37465, 37468, 37471). reference/weapons.json gives a cost for 37474 and 37477 too (866), with no store row; the other definitions (37480, 37484, 37487, 37491, 37496) were not checked and have no source.",
  "Dropped the pack's claim that Green Text weapons were the retired pre-existing names: no source says so.",
  "stores.json source_tags (L1, L2, L4, R2, T633, R1) are raw store tags; their meaning is not resolved, so they are not cited as locations.",
  "No price comparison: the wiki gives no separate sale price. Drop, quest, event and prize-wheel sources: none found in the pack or the repo search."
 ],
 "submit_note": ""}
