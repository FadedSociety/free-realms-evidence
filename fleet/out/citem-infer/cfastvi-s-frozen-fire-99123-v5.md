<!-- fleet job=citem-infer id=cfastvi-s-frozen-fire-99123-v5 status=done turns=4 usd=0.0048 tokens(read,write,in,out)=[41813, 19025, 10, 3967] model=claude-haiku-5-5 -->
# Fastvi's Frozen Fire

{"item": {"name": "Fastvi's Frozen Fire", "locale_id": 99123, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin-store listing, category 207, for item 37010 (level 16 Warrior axe). Store row names no vendor. Client objective locale:130848 says 'Buy Fastvi's Frozen Fire from Steelbloom', so Steelbloom (Royal Blacksmith) is the likely seller, but the store row does not confirm it.", "where": "Sanctuary (suspected, Steelbloom per locale:130848; not confirmed by store data)", "price": "2204 coins (member price 1983 coins, 10% member discount); sell price 220 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12206 (item 37010, category 207); locale:130848"},
  {"type": "vendor", "detail": "Coin-store listing, category 207, for variant item 45092 (same store row pattern). Vendor not named.", "where": "Unknown (same unconfirmed Steelbloom link as above)", "price": "2204 coins (member 1983); sell 220", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12970 (item 45092, category 207)"},
  {"type": "vendor", "detail": "Coin-store listing, category 207, for variant item 38562. Vendor not named.", "where": "Unknown (same unconfirmed Steelbloom link as above)", "price": "2363 coins (member 2126); sell 236", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12378 (item 38562, category 207)"},
  {"type": "quest_reward", "detail": "Wiki-attributed only, unverified: 'Warrior: A Skilled Smith' (client title ucdt 4178272706). The repo has no quest record linking this title to the item. Warrior.md:131 flags the title as unresolved. The repo's Fastvi axe quest is W24 'Warrior: A Magical Boost' (Warrior.md:125).", "where": null, "price": null, "currency": null, "source": "wiki page Fastvi's Frozen Fire (acquired by completion of the quest Warrior: A Skilled Smith; Category:Quest Weapons); notes/Build Guides/Content/Jobs/Warrior.md:125, :131"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Level 16 Warrior weapon, Cannot Trade, Power 5; Sweeping Slash 2609 dmg, Spinning Attack 4732 dmg", "source": "wiki page Fastvi's Frozen Fire; wiki image item_tooltip"},
  {"claim": "Wiki says it is acquired by completing the quest 'Warrior: A Skilled Smith'", "source": "wiki page Fastvi's Frozen Fire"},
  {"claim": "Item 37010 is in coin-store category 207 at 2204 coins, member 1983, sell 220", "source": "repo:prototype/osfr-tools/data/content/stores.json:12206 (re-read this pass)"},
  {"claim": "Item 45092 is in category 207 at 2204 coins, member 1983, sell 220", "source": "repo:prototype/osfr-tools/data/content/stores.json:12970 (re-read this pass)"},
  {"claim": "Item 38562 is in category 207 at 2363 coins, member 2126, sell 236", "source": "repo:prototype/osfr-tools/data/content/stores.json:12378 (re-read this pass)"},
  {"claim": "Client objective text: 'Buy Fastvi's Frozen Fire from Steelbloom'", "source": "locale:130848 (verified)"},
  {"claim": "Steelbloom is the Royal Blacksmith in Sanctuary", "source": "locale:46166 / locale:46173 ('Hey there, I'm Steelbloom, the Royal Blacksmith'); locale:23534 'Steelbloom can be found in Sanctuary.'"},
  {"claim": "Repair chain: Steelbloom in Sanctuary repairs the axe, then return to Fastvi", "source": "locale:130852, locale:130854, locale:130874"},
  {"claim": "Category 207 tag set T633/L1/L2/L4/R1/R2 is shared by a block of many coin-store items (e.g. 36997-38609), so it does not single out this weapon", "source": "repo:prototype/osfr-tools/data/content/stores.json:12201-12215, 12376-12379"},
  {"claim": "Repo weapon reference lists the item with source wiki + client, power 5", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:16792-16800"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor is unconfirmed. The category 207 store rows carry no vendor field. The Steelbloom link rests only on client text locale:130848. Treat the coin-store listing as the evidenced sale and the vendor as unknown until a store record names Steelbloom.",
  "Quest source 'Warrior: A Skilled Smith' is wiki-only. No repo quest record links it to the item, and the title is unresolved in Warrior.md:131. The repo's Fastvi axe quest is W24 'Warrior: A Magical Boost'. The wiki and the repo conflict; the builder should not wire this as confirmed.",
  "Coin-store sale and quest reward are not reconciled. Both are listed separately; it is not shown whether one copy can come from both paths.",
  "Variants: only 37010 is tied to the level 16 tooltip. 38562 (2363) and 45092 (2204) have no level, rank, or source tie. Min-rank figures from earlier answers are not supported by any source and are dropped.",
  "Resell value conflict: wiki tooltip says Resell Value 22; stores.json sell_price_coins is 220 for 37010 and 236 for 38562. Unresolved 10x gap.",
  "Live status: no retirement source and no live sighting. The coin-store rows suggest a current listing, but this is unverified. Retired left null.",
  "Client definition has an empty description. The first-pass 'drop' guess has no support and is dropped."
 ],
 "critique_responses": "Evidence lens: vendor reframed as coin-store listing with unknown vendor; Steelbloom kept only as client-text hint; min-rank claims removed; T633 claim reframed as a shared tag. World lens: quest source restored as wiki-only with conflict noted; coin-store and quest paths listed separately and reconciliation left open."}
