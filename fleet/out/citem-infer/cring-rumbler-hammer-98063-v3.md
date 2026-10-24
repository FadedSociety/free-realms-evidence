<!-- fleet job=citem-infer id=cring-rumbler-hammer-98063-v3 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6447, 8925, 6, 1777] model=claude-haiku-5-5 -->
# Ring Rumbler Hammer

{"item": {"name": "Ring Rumbler Hammer", "locale_id": 98063, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only (Green Text weapon tier), per wiki", "where": null, "price": null, "currency": null, "source": "wiki page: Ring Rumbler Hammer ('can only be acquired through trade'); wiki page: Green Text weapon lists it"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name locale 98063 'Ring Rumbler Hammer', item kind; ten definition ids 37502-37534, slot 7, class 5", "source": "locale:98063; client definition pack"},
  {"claim": "Wiki: level 12 Brawler weapon, Green Text weapon, Glancing Blow 1357 damage, Leg Sweep 4750 damage, acquired only through trade", "source": "wiki page: Ring Rumbler Hammer"},
  {"claim": "Wiki category Retired Weapons is present; no retirement date found in any source checked", "source": "wiki page: Ring Rumbler Hammer (Category:Retired Weapons)"},
  {"claim": "stores.json category 207 rows exist for item ids 37502 and 37505 (purchase 1236 coins, member 1112) and 37508 (purchase 1069 coins, member 962), but they carry no NPC, zone or stock link and the same source_tags set (L1,L2,L4,R2,T633,R1) and 10% member discount as many unrelated category-207 rows, so they look like a shared price template, not a confirmed listing", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12268-12270 (verified by read)"},
  {"claim": "Price rows exist only for definition ids 37502, 37505 and 37508; 37512, 37515, 37518, 37522, 37525, 37530 and 37534 have no price or source in the pack", "source": "repo:stores.json; client definition pack"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict unresolved: wiki says trade-only; stores.json category 207 rows (1236 coins for 37502/37505, 1069 coins for 37508) suggest a coin price but are unverified. No selling NPC, zone or vendor stock row names this item, so they are NOT listed as a vendor source. If a vendor is confirmed, add it with price 1236 coins (member 1112) or 1069 coins (member 962) and cite the stores.json rows.",
  "Retirement date unknown; the wiki Retired Weapons category is the only retirement evidence. Live status unknown: the first-pass client flag 'yes' is only a hint and was not used.",
  "Definition ids 37512, 37515, 37518, 37522, 37525, 37530, 37534 have no source or price in the pack; acquisition unknown.",
  "Wiki Green Text weapon tier meaning was not checked against an independent source.",
  "Wiki media files (File:Ring Rumbler Hammer held.jpg, File:Ring Rumbler Hammer item.jpg) exist but their transcribed text was not checked for sources.",
  "Not wireable: the only evidenced acquisition is player trade, which is not a sellable source in the rebuild."
 ],
 "wireable": false}
