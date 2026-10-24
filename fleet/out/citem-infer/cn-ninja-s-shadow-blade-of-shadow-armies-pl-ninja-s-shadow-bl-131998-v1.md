<!-- fleet job=citem-infer id=cn-ninja-s-shadow-blade-of-shadow-armies-pl-ninja-s-shadow-bl-131998-v1 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[27665, 11519, 12, 2998] model=claude-haiku-5-5 -->
# {n}Ninja's Shadow Blade of Shadow Armies{pl="Ninja's Shadow Blade of Shadow Armies"}

{"item": {"name": "Ninja's Shadow Blade of Shadow Armies", "locale_id": 131998, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 16 Ninja sword (client definition 75114, store row item_id 75114)", "where": "Coin Shop", "price": "2152 coins (list); 1936 coins with member discount (10%); sell-back 215 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15130 (item 75114, purchase_price_coins 2152); wiki page 'Ninja's Shadow Blade of Shadow Armies' (says it is acquired from the Coin Shop)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Trail of Betrayal (battle prize wheel)", "where": "Trail of Betrayal", "price": null, "currency": null, "source": "wiki page 'Ninja's Shadow Blade of Shadow Armies' (also acquired from the prize wheel at Trail of Betrayal)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 131998 is \"Ninja's Shadow Blade of Shadow Armies\"; definition 75114, slot 7, class 6, model sword_ar_ag_weapon_shadowblade.adr", "source": "locale:131998; client definition in pack"},
  {"claim": "Store data sells item 75114 for 2152 coins list, 1936 member price (10% off), sell_price 215, category 207, tint group 1", "source": "repo:prototype/osfr-tools/data/content/stores.json:15130"},
  {"claim": "Wiki: level 16 Ninja weapon, acquired from the Coin Shop and from the prize wheel at Trail of Betrayal", "source": "wiki page: Ninja's Shadow Blade of Shadow Armies"},
  {"claim": "Wiki tooltip image shows Resell Value 215, Power 5, Required Level 16 Ninja, technique 'Dark Assault'", "source": "wiki image:item_tooltip 'Ninja's Shadow Blade of Shadow Armies item.jpg'"},
  {"claim": "Sibling Ninja blades (Dragonstrike, 1000 Storms, Shuriken Storm, Flame Wave, Solar Flare, Dragon Breath, Mysticism, Soul Power, Deception, Jagged Scythe) share the same set naming; wiki Trail of Betrayal page lists this blade alongside them", "source": "locale:131993-132003; wiki page: Trail of Betrayal"}
 ],
 "confidence": 0.7,
 "open": [
  "The pack said wiki_page is null, but a wiki article exists under this exact title; its coin price text is blank in the extract ('sells for  and'), so the wiki's own Coin Shop price is unreadable here. The 2152 figure comes from our store data, and the wiki's tooltip 'Resell Value 215' matches the store sell_price_coins 215.",
  "Prize wheel entry is from the wiki's Trail of Betrayal statement; no drop rate or wheel-tier detail was found.",
  "Retirement status not established: no wiki or article says it was retired or removed; store row carries source tags L1, L2, L4, R2, T633, R1 which were not decoded here. Coin Shop availability after the original run is unverified.",
  "Pack's coin_store_prices [2152] is a price, not a store id; the store row is item_id 75114 at stores.json:15130.",
  "No quest, enemy-drop, or event sources found."
 ]}
