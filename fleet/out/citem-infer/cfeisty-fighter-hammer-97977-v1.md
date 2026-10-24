<!-- fleet job=citem-infer id=cfeisty-fighter-hammer-97977-v1 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[13611, 14134, 8, 3605] model=claude-haiku-5-5 -->
# Feisty Fighter Hammer

{"item": {"name": "Feisty Fighter Hammer", "locale_id": 97977, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store weapon category 207, tint 1 (item 37416), 640 coins; tint 2 (item 37420), 640 coins. Vendor NPC not identified in the pack.", "where": "Coin store weapon category 207 (vendor not identified)", "price": "640 coins (member price 576 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 37416 and item 37420 (lines 12260-12261)"},
  {"type": "vendor", "detail": "Coin store weapon category 207, tint 3 (item 37424), priced lower than the other two tints. Vendor NPC not identified in the pack.", "where": "Coin store weapon category 207 (vendor not identified)", "price": "582 coins (member price 523 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 37424 (line 12262)"},
  {"type": "other", "detail": "Player-to-player trade only, according to the wiki page. This is not a vendor or drop source; it is listed here because the wiki says it is the only acquisition route.", "where": null, "price": null, "currency": null, "source": "wiki: Feisty Fighter Hammer ('can only be acquired through trade')"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Feisty Fighter Hammer' is locale 97977, item class 71, slot 7, one model hammer_ar_ag_weapon_logjammer.adr across 10 definitions (37416-37459).", "source": "locale:97977; client definition from the evidence pack"},
  {"claim": "Store data prices 37416 and 37420 at 640 coins and 37424 at 582 coins, all in store category 207 with the same source tags as neighbouring weapons.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12260-12262"},
  {"claim": "Wiki: level 1 Warrior Green Text weapon, 'can only be acquired through trade'. Categorised Retired Weapons. Effects: Glancing Blow 444 damage, Leg Sweep 1554 damage.", "source": "wiki page: Feisty Fighter Hammer"},
  {"claim": "Wiki lists the Green Text weapon page as containing Feisty Fighter Hammer.", "source": "wiki page: Green Text weapon (lookup hit)"},
  {"claim": "Tentonhammer guide: Feisty Fighter Pants (clothing) came from a quest run reward, which is a separate item and does not confirm the hammer's source.", "source": "http://www.tentonhammer.com:80/node/67379"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says trade-only, but the store data lists coin purchase prices for all three tints. Either the store entries are stale data or the wiki is incomplete. Confirm with a live store capture or a dated vendor record before treating the coin store as a live source.",
  "The vendor NPC or store window for store category 207 is not identified in the pack. Check vendors.json for the store category.",
  "Retired status comes from the wiki's Retired Weapons category, with no retirement date. The last date it was sold is unknown.",
  "Live status is unsure. The store data shows sale entries, but the wiki says the item is retired and trade-only.",
  "Wiki and store data disagree on price history: the wiki page gives no coin price, so there is no sale-price comparison."
 ]}
