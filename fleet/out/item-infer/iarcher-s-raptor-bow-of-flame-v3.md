<!-- fleet job=item-infer id=iarcher-s-raptor-bow-of-flame-v3 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6799, 9840, 6, 2516] model=claude-haiku-5-5 -->
# Archer's Raptor Bow of Flame

{"item": {"name": "Archer's Raptor Bow of Flame", "locale_id": 131909, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Elinor, Archer gear merchant (Sells list); stock row only, price is a reference figure", "where": "Shrouded Glade (near the Shrouded Glade Pet Center)", "price": "2152 coins (reference price from stores.json, not a captured in-game quote; member price 1936, sell price 1076)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:29620-29660 (item_id 75025; stock_source wiki page Elinor, section Sells, revision 2025-08-04; price_basis '(R) stores.json reference price; no captured retail NPC quote'); repo:prototype/osfr-tools/data/content/stores.json:15036; repo:prototype/osfr-tools/data/content/npcs/shrouded_glade.json:14613"},
  {"type": "coin_shop", "detail": "Coin Shop, Archer weapon listing (category only)", "where": "Coin Shop", "price": "unconfirmed (wiki article price sentence is blank; the 2152 coins field on the wiki page matches the Elinor reference price, so it is not an independent confirmation)", "currency": "coins", "source": "wiki: Archer's Raptor Bow of Flame (rev 32760), text 'acquired from the Coin Shop', categories 'Coin Shop' and 'Coin Shop Weapons'"},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel", "where": "Briarheart Caverns", "price": null, "currency": null, "source": "wiki: Archer's Raptor Bow of Flame ('acquired from the prize wheel at Briarheart Caverns'), category 'Prize Wheel Weapons'; repo:prototype/osfr-tools/data/content/dungeons/briarheart_caverns.json:773 and :2394 (target_name matches, target_id unresolved); notes/Build Guides/Content/Dungeons/Briarheart Caverns.md:86"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is Archer's Raptor Bow of Flame (name id 131909)", "source": "locale:131909"},
  {"claim": "Level 16 Archer weapon, Power 5; Smoldering Shot 2609 damage; Flaming Arrow 10674 damage", "source": "wiki: Archer's Raptor Bow of Flame"},
  {"claim": "Tooltip 'Resell Value' 215 is a resell value, not a purchase price", "source": "image:item_tooltip"},
  {"claim": "Elinor's Sells stock lists this bow; the 2152/1936/1076 figures are stores.json reference prices, not captured quotes", "source": "repo:prototype/osfr-tools/data/content/vendors.json:29620-29660; repo:stores.json:15036"},
  {"claim": "Wiki article says the bow is acquired from the Coin Shop and from the Briarheart Caverns prize wheel; the price sentence is blank", "source": "wiki: Archer's Raptor Bow of Flame"},
  {"claim": "Categories include Coin Shop, Coin Shop Weapons, Prize Wheel Weapons, Marketplace Items; no SC Marketplace category", "source": "wiki: Archer's Raptor Bow of Flame"}
 ],
 "confidence": 0.5,
 "open": [
  "Elinor price 2152 coins is a stores.json reference price (price_basis says so). Confirm the live price in game before treating it as current.",
  "Coin Shop price is unconfirmed. The wiki coins field (2152) matches the Elinor reference price, so it is probably the same figure; it is not a second confirmation. The wiki price sentence is blank.",
  "Prize wheel spin cost is unknown. The '281 Coins' figure on the Briarheart Caverns page is not established as a spin price. The repo target_id for the prize-wheel entry is unresolved (briarheart_caverns.json:2394), so the item mapping is not yet wireable.",
  "'Marketplace Items' is a wiki category, but there is no 'SC Marketplace' category and no station_cash entry in the pack. No Station Cash source is listed. Treat the marketplace reading as unresolved.",
  "Retirement is not stated anywhere in the pack. The Elinor stock row (wiki rev 2025-08-04) and runtime_eligible true suggest it was still sold there at that revision. Whether the Coin Shop listing persists is unknown.",
  "The Elinor wiki page was not re-fetched in this pass (a lookup query failed on the apostrophe); the stock evidence rests on the vendors.json stock_source citation.",
  "No quest reward, enemy drop, event, crafting, or collection source was found in the pack."
 ]
}
