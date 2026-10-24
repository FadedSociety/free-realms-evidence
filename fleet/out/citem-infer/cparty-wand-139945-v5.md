<!-- fleet job=citem-infer id=cparty-wand-139945-v5 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6540, 8860, 6, 1915] model=claude-haiku-5-5 -->
# Party Wand

{"item": {"name": "Party Wand", "locale_id": 139945, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin-store purchase row, seller/NPC not identified. stores.json category 207 has no mapped vendor. Row sits in a contiguous block of item ids 48187 onward, all at 811 coins, so the price is shared across the block, not unique to this item", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; sell 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13244 (item 48195, category 207, no_sale false); client definition coin_store_prices [811]"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. No price, mechanism or NPC documented", "where": null, "price": null, "currency": null, "source": "wiki page: Party Wand (ns0)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Party Wand is a level 5 Wizard, Power 3, Blue Text weapon; the wiki says it can only be acquired through trade", "source": "wiki page: Party Wand (ns0)"},
  {"claim": "The wiki page is in Category:Retired Weapons", "source": "wiki page: Party Wand (category list)"},
  {"claim": "stores.json item 48195 is a coin purchase row: 811 coins, member 729 (10% discount), sell 81, no_sale false, category 207", "source": "repo:prototype/osfr-tools/data/content/stores.json:13244 (re-read; neighbouring rows 48187-48203 carry the same 811 tier)"},
  {"claim": "Name is locale 139945, in the Party group of Blue Text weapons (Party Bow, Kendama Hammer, Scalpel, Blade, Axe, Wand)", "source": "locale:139945; locale:139940-139944"},
  {"claim": "Tooltip Resell Value 81 matches the store sell price 81. Consistency check only, not source confirmation", "source": "image:item_tooltip Party Wand"}
 ],
 "confidence": 0.35,
 "open": [
  "Conflict: the wiki says trade-only, while stores.json item 48195 has an 811-coin purchase row. Both are recorded; neither is confirmed as the acquisition path. Category 207 needs mapping to a seller, location and sale dates before the coin_shop row is wired as a vendor sale.",
  "Unverified lead (not a source): wiki page 'Blue Text weapon' says these weapons were members-only and acquired in dungeons where they were dropped. This is category-level, the dungeon, drop source and rate for Party Wand are unidentified.",
  "Live status unresolved. Retired is supported only by the wiki Category:Retired Weapons. The store row is undated, so live cannot be set to 'no' with confidence.",
  "The Party Bow, Kendama Hammer, Scalpel, Blade and Axe items share the same store pattern and were not individually checked.",
  "No event, holiday, quest, enemy-drop or prize-wheel source found in the evidence pack. This means none found, not confirmed absent.",
  "Critique note: the earlier claim that category 207 is a single shared tier with unrelated prices was checked. The block at 48187-48203 is uniform at 811, but other category 207 lines carry different prices, so the tier is per id block, not per category."
 ]}
