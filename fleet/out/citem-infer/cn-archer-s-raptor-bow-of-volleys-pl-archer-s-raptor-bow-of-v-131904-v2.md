<!-- fleet job=citem-infer id=cn-archer-s-raptor-bow-of-volleys-pl-archer-s-raptor-bow-of-v-131904-v2 status=no_submit turns=3 usd=0.0032 tokens(read,write,in,out)=[16715, 12504, 8, 2900] model=claude-haiku-5-5 -->
# {n}Archer's Raptor Bow of Volleys{pl="Archer's Raptor Bow of Volleys"}

```json
{"item": {"name": "Archer's Raptor Bow of Volleys", "locale_id": 131904, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Elinor, Archer job vendor (Pin Hole Archer set and Archer's Raptor Bows)", "where": "Shrouded Glade Pet Park", "price": "2152 coins (non-member); 1936 coins (member, 10% off)", "currency": "coins", "source": "wiki page \"Elinor\" (Sells list includes \"Archer's [Raptor] [Bow] of [Volleys]\"; revision 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json:29468-29535 (npc 9500000676, item 75020); price from repo:prototype/osfr-tools/data/content/stores.json:15036 (reference price, not a captured NPC quote)"},
  {"type": "coin_shop", "detail": "Coin Shop sale, item 75020, category 207, tint group 1", "where": "Coin Shop", "price": "2152 coins (non-member); 1936 coins (member, 10% off)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15036; wiki page \"Archer's Raptor Bow of Volleys\" (says it is acquired from the Coin Shop; the wiki price field is blank)"},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel", "where": "Cray Caves", "price": null, "currency": null, "source": "wiki page \"Cray Caves\" (Archer Prize Wheel lists \"Archer's [Raptor] [Bow] of [Volleys]\"); also wiki page \"Archer's Raptor Bow of Volleys\""},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel", "where": "Mushroom Mania!", "price": null, "currency": null, "source": "wiki page \"Mushroom Mania!\" (Archer Prize Wheel lists \"Archer's [Raptor] [Bow] of [Volleys]\")"},
  {"type": "prize_wheel", "detail": "Archer prize wheel", "where": "Ambushed!", "price": null, "currency": null, "source": "wiki page \"Archer's Raptor Bow of Volleys\" (\"acquired from the prize wheel at Ambushed!, Cray Caves\"); not confirmed on a separate Ambushed! wheel page"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item is a level 16 Archer weapon, acquired from the Coin Shop and from the prize wheel at Ambushed! and Cray Caves", "source": "wiki page \"Archer's Raptor Bow of Volleys\""},
  {"claim": "Coin Shop row: item 75020, purchase 2152 coins, member 10% off = 1936, sell 215", "source": "repo:prototype/osfr-tools/data/content/stores.json:15036"},
  {"claim": "Elinor's wiki Sells list includes Archer's [Raptor] [Bow] of [Volleys]; the repo vendor entry maps it to item 75020 / name id 131904 at 2152 / 1936 coins", "source": "wiki page \"Elinor\" (Sells, revision 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json:29468-29535"},
  {"claim": "Archer Prize Wheel on the Cray Caves wiki page lists Archer's [Raptor] [Bow] of [Volleys]", "source": "wiki page \"Cray Caves\""},
  {"claim": "Archer Prize Wheel on the Mushroom Mania! wiki page lists Archer's [Raptor] [Bow] of [Volleys]", "source": "wiki page \"Mushroom Mania!\""},
  {"claim": "Client name for item 131904 is Archer's Raptor Bow of Volleys", "source": "locale:131904"},
  {"claim": "Wiki item images exist for the bow (item and held views)", "source": "wiki files \"File:Archer's Raptor Bow of Volleys item.jpg\" and \"held.jpg\""}
 ],
 "confidence": 0.8,
 "open": [
  "Coin prices (2152 / 1936) come from repo stores.json, not from a wiki-stated price. The wiki Coin Shop price field is blank, and the Elinor price basis is the same reference price, not a captured NPC quote. Treat as the reference sale price until confirmed in game.",
  "Prize wheel entries give no per-item odds or spin cost. The 77, 214 and 473 coin figures are spin costs for those wheels, not item prices, so none is attributed to this item.",
  "Ambushed! wheel rests only on the item page's own text; no separate Ambushed! wheel page was found.",
  "No source in the pack states retirement. Live status rests on the current store row and the 2025 Elinor wiki listing.",
  "The Pin Hole Archer set entry in vendors_unresolved.json is superseded by the Elinor vendor link above."
 ],
 "critiques_addressed": "Elinor vendor source added (world critique). Mushroom Mania! and Cray Caves wheel entries verified on their wiki pages (evidence and world critiques). Sibling-price claim from weapons.json dropped as unverified context."}
```
