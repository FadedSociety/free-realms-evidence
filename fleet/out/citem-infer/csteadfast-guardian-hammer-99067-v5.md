<!-- fleet job=citem-infer id=csteadfast-guardian-hammer-99067-v5 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6281, 8760, 6, 2096] model=claude-haiku-5-5 -->
# Steadfast Guardian Hammer

{"item": {"name": "Steadfast Guardian Hammer", "locale_id": 99067, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player trade only, per wiki prose ('can only be acquired through trade'). No counterparty, no price; not wireable as a purchase source.", "where": null, "price": null, "currency": null, "source": "wiki page: Steadfast Guardian Hammer"},
  {"type": "coin_shop", "detail": "UNVERIFIED coin-store data row only: definitions 38506 and 38509 (tint groups 1-2) at 1656 coins (member 1490); 38512 (tint group 3) at 1431 coins (member 1287). Category 207 with the same source_tags as about 20 other category-207 rows; no vendor, shop section, wiki or article names it. Conflicts with the wiki's trade-only statement, so treat as a possible data leftover, not a confirmed sale.", "where": null, "price": "1656 coins (member 1490) for 38506/38509; 1431 coins (member 1287) for 38512", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12370-12372"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Steadfast Guardian Hammer', locale 99067; item class 17, slot 7, 10 definitions, model hammer_ar_ag_weapon_doublehead.adr", "source": "locale:99067"},
  {"claim": "Wiki: level 16 Warrior weapon, Green Text weapon, 'can only be acquired through trade'; Sweeping Slash 2609 dmg, Spinning Attack 4732 dmg; page categories include Category:Retired Weapons", "source": "wiki page: Steadfast Guardian Hammer"},
  {"claim": "Green Text weapon wiki table lists a 'Steadfast Guardian Hammer' row, but the retrieved snippet does not show which column (Blacksmith-made vs trade-only) it falls in; no crafted source is confirmed", "source": "wiki page: Green Text weapon"},
  {"claim": "Coin store rows: 38506 and 38509 at 1656 (member 1490), 38512 at 1431 (member 1287), category 207, no vendor named", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12370-12372"},
  {"claim": "Wiki Warrior weapon list places Steadfast Guardian Hammer at Level 16 and also a Level 17 entry of the same name, so the name spans more than one level listing", "source": "wiki page: Warrior"}
 ],
 "confidence": 0.4,
 "open": [
  "Source conflict unresolved: wiki says trade-only; stores.json has a category-207 coin price row with no named vendor. The coin row is kept only as unverified; wireable as a purchase source is false until a named vendor or live store section is found.",
  "Green Text weapon table: the Steadfast row's column (Blacksmith-made vs trade-only) is not legible in the retrieved snippet; do not cite it as crafted or trade-only proof without reading the full table.",
  "Wiki Warrior page lists a Steadfast Guardian Hammer at both Level 16 and Level 17 entries; the item page covers only the Level 16 version. Confirm whether these are distinct items or one item's listing.",
  "Definitions 38515, 38518, 38521, 38525, 38529, 38533, 38537 have no store price in the data; their sale status is unknown.",
  "Retirement: Category:Retired Weapons supports retired: true, but no item-specific retirement date is evidenced. The 2009-12-14 Green Text date is category-level only and is not attached here.",
  "No dungeon boss, quest, event, crafting, prize wheel, or collection source is evidenced. Client description is empty."
 ],
 "wireable": false}
