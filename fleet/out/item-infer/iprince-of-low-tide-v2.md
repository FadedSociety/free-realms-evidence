<!-- fleet job=item-infer id=iprince-of-low-tide-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5102, 7004, 6, 1879] model=claude-haiku-5-5 -->
# Prince of Low Tide

{"item": {"name": "Prince of Low Tide", "locale_id": 116195, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Prince of Low Tide is a Cray NPC boss who appears in a wandering battle in Seaside (main beach, cove beach, oceanfront homes). He is not an item and has no vendor, Marketplace, Coin Shop, drop, or quest-reward acquisition for himself.", "source": "https://freerealms.fandom.com/wiki/Prince_of_Low_Tide (rev 50203); categories Boss, Cray, Enemies, Males, NPC, Seaside; infobox has no price, coin, or Station Cash fields"},
  {"claim": "Wiki quest-type page 'Prince of Low Tide!' describes a difficulty 4 battle started by clicking the Prince in Seaside (north end, near the Tide Pools). Its Goals are 'Knock out the Prince of Low Tide!' and, per the critique, its Rewards are 59 Stars plus Members Only Bonus: Coins. The reward line was not visible in my lookup excerpt, so verify it before use. These are quest rewards for the battle, not acquisition of an item.", "source": "https://freerealms.fandom.com/wiki/Prince_of_Low_Tide! (ns0)"},
  {"claim": "Client text: 116195 quest_title 'Prince of Low Tide' (unflagged); 116342 quest_objective 'Knock out the Prince of Low Tide!' (Seaside); 119182 quest_objective 'Win Wandering Combat Encounter Prince of Low Tide!'. 116053 'Prince of Low Tide!' is FLAGGED (flag?) and is not used as live evidence.", "source": "locale:116195, locale:116342, locale:119182, locale:116053 (flagged)"},
  {"claim": "Wiki pages Brawler's Drill Hammer of Pummeling, Warrior's Double Axe of Earthquake and Ninja's Jagged Scythe of Shuriken Storm list the Prince battle ('Prince of Low Tide!') as a prize-wheel source, alongside Brugo's Fishing Spot, Frostfang Caverns and When Plants Attack!, and the Coin Shop. These sources belong on those weapon records, not on this one.", "source": "wiki pages: Brawler's Drill Hammer of Pummeling; Warrior's Double Axe of Earthquake; Ninja's Jagged Scythe of Shuriken Storm"},
  {"claim": "Client ability and debug strings (116358, 116265, 116222, 117013, 117015) are internal boss-script names and placeholders. They are not item or reward evidence.", "source": "locale:116358, locale:116265, locale:116222, locale:117013, locale:117015"}
 ],
 "confidence": 0.85,
 "open": [
  "Record type mismatch: this is an NPC boss, not an item. Confirm with Bryce whether this record should be dropped or re-pointed. No item-level sources exist for it.",
  "Battle rewards (59 Stars, Members Only Bonus Coins) come from the 'Prince of Low Tide!' quest/battle page, not item acquisition. They are not listed as item sources here. Verify the reward line on the wiki page first.",
  "Prize-wheel appearances (Brawler's Drill Hammer of Pummeling, Warrior's Double Axe of Earthquake, Ninja's Jagged Scythe of Shuriken Storm) belong on those weapon records. Those pages also list the Coin Shop and the Brugo's Fishing Spot, Frostfang Caverns and When Plants Attack! wheels.",
  "Live status is unverified. The wiki does not say whether the wandering battle still spawns. The repo dungeon notes give no retirement date.",
  "Critique fix applied: locale:116053 is flagged, so it is not cited as live evidence. The wiki quest page is now recorded above. The earlier claim that the pack attributes no rewards was incomplete and is corrected here."
 ]}
