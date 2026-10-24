<!-- fleet job=citem-infer id=cn-ninja-s-shadow-blade-of-shadow-armies-pl-ninja-s-shadow-bl-131998-v2 status=done turns=3 usd=0.0046 tokens(read,write,in,out)=[20856, 23943, 8, 2859] model=claude-haiku-5-5 -->
# {n}Ninja's Shadow Blade of Shadow Armies{pl="Ninja's Shadow Blade of Shadow Armies"}

{"item": {"name": "Ninja's Shadow Blade of Shadow Armies", "locale_id": 131998, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Hidden Dragon (npc_id 9500000691), 'Sells' section; listed as 'Ninja's Shadow Blade of Shadow Armies' (item 75114). Vendor description also names 'five Shadow Blades (... Shadow Armies ...)'.", "where": "shrouded_glade.json (Shrouded Glade)", "price": "2152 coins list; 1936 coins member price (10% off); sell-back 215 coins. These are stores.json reference prices, not a captured NPC quote.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:29917-29944 and :30030-30071 (Hidden Dragon stock entry, item 75114); wiki 'Hidden Dragon' Sells section, revision 2013-10-02 (https://freerealms.fandom.com/wiki/Hidden_Dragon)"},
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 16 Ninja blade (store row item 75114). Wiki says it is acquired from the Coin Shop, but the wiki's price text is blank in the extract.", "where": "Coin Shop", "price": "2152 coins list (reference); 1936 member; sell-back 215", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15130 (item 75114, purchase_price_coins 2152, member_price_coins 1936, sell_price_coins 215); wiki weapons list entry 'Ninja's Shadow Blade of Shadow Armies is a level 16 Ninja weapon. It is acquired from the Coin Shop...' (freerealms-wiki/harvest/lists/weapons.json:28097)"},
  {"type": "prize_wheel", "detail": "Prize wheel, Trail of Betrayal (battle prize wheel). Wiki-only claim; no drop rate or wheel tier found.", "where": "Trail of Betrayal", "price": null, "currency": null, "source": "wiki weapons list entry (freerealms-wiki/harvest/lists/weapons.json:28097: 'it is also acquired from the prize wheel at Trail of Betrayal'). Same wording as sibling level 16 weapons, so treat as unverified."}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 131998 is \"Ninja's Shadow Blade of Shadow Armies\"; definition 75114, slot 7, class 6, model sword_ar_ag_weapon_shadowblade.adr", "source": "locale:131998; client definition in pack"},
  {"claim": "Store data sells item 75114 for 2152 coins list, 1936 member price, sell_price 215, category 207, tint group 1", "source": "repo:prototype/osfr-tools/data/content/stores.json:15130"},
  {"claim": "Hidden Dragon (npc 9500000691, shrouded_glade.json) stocks item 75114 under the wiki name, from the wiki 'Hidden Dragon' Sells section (rev 2013-10-02). The vendor stock entry is marked partial_evidence_reference and its price is the stores.json reference price.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:29917-29944, 30030-30071"},
  {"claim": "Wiki weapon-list entry: level 16 Ninja weapon, acquired from the Coin Shop (price blank in extract) and from the prize wheel at Trail of Betrayal", "source": "freerealms-wiki/harvest/lists/weapons.json:28097"},
  {"claim": "Sibling Ninja blades 131993-132003 share the naming pattern; Hidden Dragon's stock list names five of them, including this one", "source": "locale:131993-132003; repo vendors.json:29920"},
  {"claim": "Client text has the same name in several locale strings (ucdt 1884337011, ugdt 2338193637), so the name is stable across the client", "source": "opening-anvil-placement-v1/locale/en_us_data.dat:49726, :61509 (same in other locale dumps)"}
 ],
 "confidence": 0.7,
 "open": [
  "Coin Shop price: the wiki's own price text is blank in the extract. The 2152/1936/215 figures are stores.json reference prices, not captured NPC or shop quotes. Treat them as reference values.",
  "Prize wheel source rests on one wiki line in the harvest list. No article, video, or quest text confirms it, and no wheel tier or drop rate is known.",
  "Hidden Dragon stock comes from a 2013-10-02 wiki snapshot. Current availability is unknown.",
  "Retirement is not established. No source says the blade was retired or removed. Store row source_tags (L1, L2, L4, R2, T633, R1) are undecoded.",
  "No quest reward, enemy drop, or event source was found.",
  "The earlier answer cited a wiki page with this title. The wiki text in the extract was blank, so only the weapons-list line is cited here."
 ]}
