<!-- fleet job=citem-infer id=cparty-wand-139945-v4 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6755, 9267, 6, 1936] model=claude-haiku-5-5 -->
# Party Wand

{"item": {"name": "Party Wand", "locale_id": 139945, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin-store purchase row, no vendor or NPC identified (stores category 207 is unmapped; its rows share one price tier and source_tags L1, L2, L4, R2, T633, R1)", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; sell 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48195 (line 13244, no_sale false); client definition coin_store_prices [811]"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. No price or NPC documented", "where": null, "price": null, "currency": null, "source": "wiki page: Party Wand (ns0)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Party Wand is a level 5 Wizard, Power 3, Blue Text weapon; the wiki says it can only be acquired through trade", "source": "wiki page: Party Wand (ns0)"},
  {"claim": "The wiki page is in Category:Retired Weapons", "source": "wiki page: Party Wand (category list)"},
  {"claim": "stores.json item 48195 is a coin purchase row: 811 coins, member 729 (10% discount), sell 81, no_sale false, category 207", "source": "repo:prototype/osfr-tools/data/content/stores.json:13244 (re-read and confirmed)"},
  {"claim": "Name is locale 139945, in the Party group of Blue Text weapons (Party Bow, Kendama Hammer, Scalpel, Blade, Axe, Wand)", "source": "locale:139945; locale:139940-139944; wiki page: Blue Text weapon"},
  {"claim": "Wiki 'Blue Text weapon' says these weapons were members-only and were acquired in dungeons where they were dropped (category-level, not Party Wand-specific)", "source": "wiki page: Blue Text weapon (ns0)"},
  {"claim": "Tooltip Resell Value 81 matches the store sell price 81. Consistency check only, not source confirmation", "source": "image:item_tooltip Party Wand"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the wiki says trade-only, while stores.json item 48195 has an 811-coin non-no_sale purchase row. Category 207 is not mapped to any vendor or NPC in the repo, so the vendor source has no identified seller, location or sale dates. Map category 207 to a vendor before wiring it.",
  "Live status is unresolved. Retired is supported only by the wiki Retired Weapons category. The store row is undated, so live cannot be set to 'no' with confidence yet.",
  "Unverified lead: the wiki Blue Text weapon page says these weapons were dungeon drops (members only) before retirement. The dungeon, drop source and rate are not identified, so this is not listed as a source.",
  "Not wireable as-is: the coin row has no vendor, and trade has no mechanism or price. The critiques' request to remove the vendor row was not followed, because the coin-store row is evidence of a coin sale under the store rules. It is kept but flagged as unmapped.",
  "The Party Bow, Kendama Hammer, Scalpel, Blade and Axe items share the same store pattern and were not individually checked.",
  "No event, holiday, quest or enemy-drop source found in the evidence pack. This means none found, not confirmed absent."
 ]}
