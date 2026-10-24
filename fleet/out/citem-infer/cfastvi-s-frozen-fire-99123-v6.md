<!-- fleet job=citem-infer id=cfastvi-s-frozen-fire-99123-v6 status=done turns=2 usd=0.0042 tokens(read,write,in,out)=[8255, 18836, 6, 3623] model=claude-haiku-5-5 -->
# Fastvi's Frozen Fire

{"item": {"name": "Fastvi's Frozen Fire", "locale_id": 99123, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin-store listing, category 207, item 37010 (level 16 Warrior axe per wiki tooltip). Store row names no vendor. Steelbloom is only a client-text hint (locale:130848), not a store record.", "where": "unknown (coin store; vendor not named)", "price": "2204 coins (member price 1983, 10% member discount); sell price 220 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12206 (item 37010, category 207); locale:130848"},
  {"type": "vendor", "detail": "Coin-store listing, category 207, variant item 45092. Store row names no vendor and no level/variant tie to the level 16 tooltip.", "where": "unknown (coin store; vendor not named)", "price": "2204 coins (member price 1983); sell price 220 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12970"},
  {"type": "vendor", "detail": "Coin-store listing, category 207, variant item 38562. Store row names no vendor and no level/variant tie to the level 16 tooltip.", "where": "unknown (coin store; vendor not named)", "price": "2363 coins (member price 2126); sell price 236 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12378"},
  {"type": "quest_reward", "detail": "Quest 'Warrior: A Skilled Smith' (client title locale:4178272706). Wiki says the weapon is acquired by completing it. Repo quest notes tie the restoration reward line (locale:71524, 'The weapon has been restored? It is yours now') to this quest, but no record links that reward to item 37010 or its variants. Wiki-only attribution; conflicts with the repo's W24 'Warrior: A Magical Boost' (Warrior.md:125, :131).", "where": null, "price": null, "currency": null, "source": "wiki page Fastvi's Frozen Fire (acquired by completion of the quest Warrior: A Skilled Smith; Category:Quest Weapons); quest-lines/quests.json (locale 71524 tagged to 71522 Warrior: A Skilled Smith)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Level 16 Warrior weapon, Cannot Trade, Power 5; Sweeping Slash 2609 dmg, Spinning Attack 4732 dmg", "source": "wiki page Fastvi's Frozen Fire; wiki image item_tooltip"},
  {"claim": "Wiki says it is acquired by completing the quest 'Warrior: A Skilled Smith'", "source": "wiki page Fastvi's Frozen Fire"},
  {"claim": "Item 37010 is in coin-store category 207 at 2204 coins, member 1983, sell 220 (re-read)", "source": "repo:prototype/osfr-tools/data/content/stores.json:12206"},
  {"claim": "Item 45092 is in category 207 at 2204 coins, member 1983, sell 220 (re-read)", "source": "repo:prototype/osfr-tools/data/content/stores.json:12970"},
  {"claim": "Item 38562 is in category 207 at 2363 coins, member 2126, sell 236 (re-read)", "source": "repo:prototype/osfr-tools/data/content/stores.json:12378"},
  {"claim": "Quest title 'Warrior: A Skilled Smith' exists in client as 4178272706 (ucdt)", "source": "locale:4178272706 via client text search; quest-lines/quests.json (71522)"},
  {"claim": "Client objective 'Buy Fastvi's Frozen Fire from Steelbloom' and repair chain text (Steelbloom repairs axe, return to Fastvi)", "source": "locale:130848, locale:130852, locale:130854, locale:130874 (from pack; locale:130848 not re-fetched in this pass)"},
  {"claim": "Steelbloom is the Royal Blacksmith in Sanctuary", "source": "locale:46166"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor not named: the coin-store rows (stores.json 12206, 12970, 12378) carry no vendor field. Steelbloom is supported only by client objective text (locale:130848), so no vendor is confirmed.",
  "Quest source is wiki-only. 'Warrior: A Skilled Smith' is named by the wiki, and a repo quest note ties the restore reward line to it, but no record links the reward to item 37010 or its variants. The repo's Fastvi axe quest per Warrior.md is W24 'Warrior: A Magical Boost'; the two sources conflict and should not be wired as confirmed without a quest record.",
  "Coin-store sale and quest reward are listed as separate paths; it is not shown whether one copy can come from both, or which one a player would use.",
  "Variants: only 37010 is tied to the level 16 tooltip. 38562 (2363) and 45092 (2204) have no level, rank, or source tie.",
  "Resell value conflict: wiki tooltip says Resell Value 22; stores.json sell_price_coins is 220 (37010, 45092) and 236 (38562). Unresolved 10x gap.",
  "Live status: no retirement source and no live sighting. Coin-store rows with no_sale false suggest a current listing, but this is unverified. Retired left null.",
  "Client definition has an empty description. The first-pass 'drop' guess has no support and is dropped.",
  "Critique fixes applied: vendor reframed as unnamed coin-store listing; Steelbloom kept only as client-text hint; the Steelbloom link removed from variant rows; locale:46173 dropped as a duplicate; quest source kept as wiki-only with conflict noted."
 ]}
