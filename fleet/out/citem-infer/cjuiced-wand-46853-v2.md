<!-- fleet job=citem-infer id=cjuiced-wand-46853-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6395, 8822, 6, 1870] model=claude-haiku-5-5 -->
# Juiced Wand

{"item": {"name": "Juiced Wand", "locale_id": 46853, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of store item 48146 (client definition 48146). The store row names no NPC, so the vendor is unknown. Category 207 in the store file.", "where": null, "price": "1236 coins (member price 1112 coins, 10% member discount; sell-back 123 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48146 (line 13202)"},
  {"type": "other", "detail": "Wiki's only acquisition statement: the weapon 'can only be acquired through trade' (player-to-player). Conflicts with the coin-store row above; recorded as a conflict note, not a confirmed source.", "where": null, "price": null, "currency": null, "source": "wiki page 'Juiced Wand'"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Juiced Wand is a level 8 Wizard Blue Text weapon, Power 4, and the wiki lists it in Category:Retired Weapons.", "source": "wiki page 'Juiced Wand'"},
  {"claim": "Blue Text weapons were members-only weapons whose names once appeared in blue before being retired, and the wiki says they were acquired in dungeons where they were dropped. This is the category-level statement; the Juiced Wand page itself names no dungeon or enemy.", "source": "wiki page 'Blue Text weapon'"},
  {"claim": "Client name for 46853 is 'Juiced Wand'; it sits in a set with Juiced Scythe, Juiced Hammer, Bubbleburst and Nature's items (46850-46858).", "source": "locale:46853; locale:46850; locale:46856"},
  {"claim": "Store row for item 48146 is category 207, purchase 1236 coins, member price 1112 coins, sell 123 coins; the row's source_tags (L1, L2, L4, R2, T633, R1) are unexplained.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48146 (line 13202)"},
  {"claim": "The wiki's Electric Oil Flair Shard page says it duplicates the Juiced Wand particle effect; it names no Juiced Wand source.", "source": "wiki page 'Electric Oil Flair Shard'"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor NPC and zone for store item 48146 are not named in the repo. Find the vendor that sells category 207 at 1236 coins with a dated capture.",
  "Conflict: wiki says 'acquired through trade' only, while the store row shows a 1236-coin sale. Either the store row is stale or pre-retirement, or the wiki is incomplete. Needs a dated vendor capture.",
  "No specific drop source for Juiced Wand. The Blue Text dungeon-drop statement is category-level and not confirmed for this item.",
  "Retirement date and last sale date are not in the pack. The wiki Retired Weapons category supports 'retired'.",
  "First-pass 'live: yes' is not supported by the wiki's retired category; recorded as 'no'.",
  "Client definition 22103 shares the name but has no store row; its source is unknown."
 ]}
