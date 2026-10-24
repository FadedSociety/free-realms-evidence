<!-- fleet job=citem-infer id=cfrostflame-bow-94394-v4 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6844, 9272, 6, 2194] model=claude-haiku-5-5 -->
# Frostflame Bow

{"item": {"name": "Frostflame Bow", "locale_id": 94394, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only. The wiki says the bow 'can only be acquired through trade'; no trade record, NPC or mechanism is named.", "where": null, "price": null, "currency": null, "source": "wiki page: Frostflame Bow (lead text)"},
  {"type": "other", "detail": "UNCONFIRMED store-table price record, not a shown sale: no vendor, NPC, shop page or stock row names where it was sold. Row sits in a block of category 207 rows (48110-48124) that share identical source_tags and no price_provenance. Client definition also lists coin_store_prices 1656.", "where": null, "price": "1656 coins purchase; 1490 coins member price (derived: 10% member discount, not a separately recorded value); resell 165 coins per stores.json and tooltip (weapons.json:19000-19011 says resell 0)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48111 (line 13167); repo:prototype/osfr-tools/data/reference/weapons.json:19000-19011; image:item_tooltip Frostflame Bow"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Frostflame Bow' is locale 94394; Archer weapon, level 12, Power 5, Blue Text weapon", "source": "locale:94394; wiki page: Frostflame Bow; image:item_tooltip Frostflame Bow"},
  {"claim": "Wiki says the item can only be acquired through trade", "source": "wiki page: Frostflame Bow (lead text)"},
  {"claim": "Wiki Category:Retired Weapons applies; no retirement date in any source", "source": "wiki page: Frostflame Bow (categories)"},
  {"claim": "Blue Text weapon list includes Frostflame Bow alongside Drill, Saw, Scythe, Hammer and Wand", "source": "wiki page: Blue Text weapon"},
  {"claim": "stores.json row 48111 (category 207): purchase 1656, member 1490, sell 165, tags L1,L2,L4,R2,T633,R1, no price_provenance, no date; tooltip Resell Value 165 agrees", "source": "repo:prototype/osfr-tools/data/content/stores.json:13167; image:item_tooltip Frostflame Bow"},
  {"claim": "weapons.json lists cost 1656 with resell 0 for both definitions 27940 and 48111; stores.json and tooltip say 165. Definition 27940 has no store row", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:19000-19011"},
  {"claim": "Client coin_store_prices for this item is 1656", "source": "client definition (definition_ids 27940, 48111)"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict unresolved: wiki says trade-only and retired, but stores.json row 48111 carries coin prices. The row's source tags are unexplained and it is not evidenced as a sale. It is kept as a price record, not an acquisition path, until a vendor or shop is found.",
  "Price conflict: resell 165 (stores.json, tooltip) vs 0 (weapons.json:19000-19011). Purchase 1656 agrees across client, stores and weapons.json.",
  "Definition 27940 carries the 1656 price in weapons.json but has no store row; price is attached to 48111 only.",
  "Retirement date unknown; retired flag comes only from the wiki category. A coin price alongside a trade-only, retired status is not reconciled.",
  "Wiki damage figures (Barrage 2609, Volley 4732) not verified against the client.",
  "Player trade is a wiki statement only; no trade record exists, and no trade price is known."
 ]}
