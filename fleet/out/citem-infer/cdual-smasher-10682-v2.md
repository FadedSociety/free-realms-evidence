<!-- fleet job=citem-infer id=cdual-smasher-10682-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[5476, 11269, 6, 2355] model=claude-haiku-5-5 -->
# Dual Smasher

{"item": {"name": "Dual Smasher", "locale_id": 10682, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Quartermaster Fizzi (gear merchant), vendor sale of the Warrior weapon, ended by retirement", "where": "Sanctuary", "price": "1236 coins (wiki; conflicts with store row 618)", "currency": "coins", "source": "wiki page 'Dual Smasher' (\"previously sold by Quartermaster Fizzi in Sanctuary for 1236 coins\"); NPC-page note only: prototype/osfr-tools/data/content/npcs/sanctuary.json:45619 and notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:94 (no price on those lines)"},
  {"type": "vendor", "detail": "Coin store row for item_id 10682 (tint group 3); the store row does not name Fizzi, so the vendor binding is from the wiki only", "where": "Coin store (category 106)", "price": "618 coins (member price 556 coins, 10% member discount; sell price 61)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3107 (item_id 10682)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Dual Smasher is a level 12 Warrior weapon, previously sold by Quartermaster Fizzi in Sanctuary for 1236 coins, retired December 14, 2009; wiki says it can presently be acquired only through trade", "source": "wiki page: Dual Smasher"},
  {"claim": "Wiki Warrior page lists Dual Smasher (Level 11 section), and the Warrior weapons were retired 14 December 2009", "source": "wiki page: Warrior; notes/Build Guides/Content/Jobs/Warrior.md:72"},
  {"claim": "Client name resolves to locale 10682 'Dual Smasher'", "source": "locale:10682"},
  {"claim": "stores.json has a coin purchase row for item_id 10682: purchase 618 coins, member 556 coins, sell 61 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3107"},
  {"claim": "Wiki effects: Sweeping Slash 1492 damage; Spinning Attack 2707 damage", "source": "wiki page: Dual Smasher"},
  {"claim": "The wiki 1236 price is exactly 2x the store row's 618; treated as a conflicting figure, not confirmed", "source": "wiki page: Dual Smasher; repo:prototype/osfr-tools/data/content/stores.json:3107"}
 ],
 "confidence": 0.5,
 "open": [
  "Price conflict: stores.json:3107 gives 618 coins for item_id 10682, the wiki gives 1236 coins under Fizzi. Not resolved. The wiki figure may be a different tier or a pre-change price; the store row may be the true coin price. Check against an in-game or archived price before using either.",
  "The client definition's coin_store_price 281 is not a row for 10682. It matches store rows for item_ids 4540-4545 (category 207, 281 coins, e.g. stores.json:854), which are the first definition IDs in the 4540-4551 set. Whether those rows are this weapon's other tints or a different item is unverified. Our store data does not tie them to Dual Smasher.",
  "Fizzi-to-item link rests on the wiki and NPC-page notes; sanctuary.json:45619 is a free-text note with no price, not a stock row.",
  "Live status is unsure: the store row for 10682 exists and the wiki says trade-only now, but neither confirms current sale status. Retirement date (14 Dec 2009) is from the wiki and the Warrior page.",
  "The trade-only availability is a player-to-player route, not a vendor or drop. Not verified in-game and not listed as a source.",
  "No quest reward, drop, event, prize-wheel, or collection source found for this item."
 ]}
