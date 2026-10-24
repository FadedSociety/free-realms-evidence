<!-- fleet job=citem-infer id=cgravel-wand-139969-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6647, 11038, 6, 2108] model=claude-haiku-5-5 -->
# Gravel Wand

{"item": {"name": "Gravel Wand", "locale_id": 139969, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (store row only). The row names no NPC; its source_tags (L1, L2, L4, R2, T633, R1) are shared by many unrelated rows and are not decoded, so the vendor and zone are unknown.", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; resell 81 coins)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json item_id 48219, category 207, no_sale false (line 13268); client coin_store_prices 811"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Gravel Wand is a level 5 Wizard Blue Text weapon, power 3, and is in Category:Retired Weapons; the wiki says it 'can only be acquired through trade' (player trade, not a game source).", "source": "wiki page: Gravel Wand"},
  {"claim": "Client name entry is locale:139969 'Gravel Wand'; definition 48219; slot 7; class 10; model wand_ar_ag_weapon_bolt.adr; sibling Gravel weapons (Bow, Kendama Hammer, Scalpel, Blade, Axe) are locale 139964-139968.", "source": "locale:139969 and client definition in pack"},
  {"claim": "Store row for item 48219 exists: purchase 811 coins, member 729 coins (10% discount), sell 81 coins, no_sale false. The 81 is the resell value shown on the tooltip, not a sale price. Adjacent Gravel-set rows (48206-48218, 48220+) carry identical prices, so the row is part of a bulk store block.", "source": "prototype/osfr-tools/data/content/stores.json lines 13255-13285"},
  {"claim": "Wiki tooltip shows Resell Value 81, Power 3, Required Level 5 Wizard, skills Zap and Lightning Blast (Zap 488 damage, Lightning Blast 1998 damage per wiki text).", "source": "wiki image:item_tooltip Gravel Wand item.jpg; wiki page: Gravel Wand"},
  {"claim": "The Blue Text weapon wiki page lists Gravel [Wand] in its table with other Gravel weapons, but the retrieved text names no dungeon or enemy as a source.", "source": "wiki page: Blue Text weapon (lookup excerpt)"}
 ],
 "confidence": 0.35,
 "open": [
  "The 811-coin store row is the only game-side source. The vendor NPC and zone are not identified; the store tags L1, L2, L4, R2, T633, R1 are not decoded in the repo.",
  "Conflict: the wiki marks the item retired (Category:Retired Weapons), yet the store row has no_sale false. Whether the coin sale was still offered after retirement is unconfirmed; no retirement date was found. Live status is therefore 'unsure'.",
  "The wiki's only acquisition statement is 'can only be acquired through trade' (player-to-player). Not listed as a game source.",
  "Blue Text weapons were described as dungeon drops in an earlier draft, but no retrieved source supports that for this item. Dropped from evidence; no drop source listed. Needs the full Blue Text weapon page to confirm.",
  "No quest reward, enemy drop, event, or prize-wheel source found for Gravel Wand in the pack."
 ],
 "critiques_addressed": "Evidence critique: store row verified and cited by full repo path; dungeon-drop claim removed as unsupported; live/retired conflict stated rather than resolved. World critique: store row kept as a price-only source with unknown vendor; citation corrected to prototype/osfr-tools path; trade noted as non-source."
}
