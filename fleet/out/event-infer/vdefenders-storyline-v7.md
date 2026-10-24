<!-- fleet job=event-infer id=vdefenders-storyline-v7 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[16244, 12614, 8, 3660] model=claude-haiku-5-5 -->
# Defenders storyline

{
 "event": {
  "name": "TCG Set 4: Heroes (Realmkeepers vs. Baron von Darkcheat)",
  "aliases": ["TCG Set 4: HEROES (locale:17472)", "Realmkeepers storyline", "Defenders storyline (Spanish article 2737, 'Defensores')", "Baron Trampaoscura (Spanish name for Baron von Darkcheat, article 2737)"]
 },
 "kind": "other",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [
  "Sunstone Valley: Rumbledome lead-in, 'Card Duelist: The Realmkeepers Are Missing!' (locale:5100175, 5100176). Madam Zelda searches there for the captured Realmkeepers. Whether this belongs to Heroes is unverified; treat as the preceding arc.",
  "Blackspore Swamp: Madam Zelda starts the Heroes series (article 2734 fact:quest; article 2746 fact:npc; locale:7948, 7960). Article 2740 says Sporeshade Swamp instead; unresolved.",
  "Seaside: play Baron von Darkcheat for a few games while the Realmkeepers train (locale:7961, 'Card Duelist: Meet the Boss')."
 ],
 "npcs": [
  "Madam Zelda (article 2733 fact:npc; article 2734; article 2746; wiki 'Madam Zelda')",
  "Baron von Darkcheat (locale:7961; article 2734; wiki 'Baron von Darkcheat')",
  "Ghostshadow (wiki 'Ghostshadow' says it is Bryce; article 2733 names Bryce as Ghostshadow)",
  "Magetech (article 2733: Nathan; wiki 'Magetech')",
  "Wildclaw (article 2733: Kade; wiki 'Wildclaw')",
  "Crackshot (wiki 'Crackshot'; wiki 'Realmkeepers')",
  "Jessica (article 2733 fact:npc; article 2737 summary)"
 ],
 "quests": [
  "Card Duelist: The Realmkeepers Are Missing!",
  "Card Duelist: Meet the Boss"
 ],
 "activities": [
  "Play Trading Card Game matches against Baron von Darkcheat and his cronies while the Realmkeepers train (article 2734 fact:quest; locale:7961)",
  "Complete the Heroes quest line, ending in a final reckoning with the Baron (article 2734 fact:quest; article 2746 fact:quest)",
  "Buy and open Heroes TCG booster packs (locale:17470 name)"
 ],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470 (name only)"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:9403 'Save on TCG Set 4: Heroes Booster Bundles!' (cited by the critique; not re-read in this pass). Price unsourced."}
 ],
 "rewards": [
  "Each Set 4 pack holds 10 random TCG cards plus one loot card (locale:17471)",
  "'Amazing new loot!' and new quests for Level 20 Card Duelists (locale:17473)"
 ],
 "evidence": [
  {"claim": "Set 4 introduces the Realmkeepers, who help stop Baron von Darkcheat; each pack has 10 random cards plus one loot card.", "source": "locale:17471"},
  {"claim": "The client names the set 'TCG Set 4: HEROES Available Now!'.", "source": "locale:17472 (from prior pack; not re-read in this pass)"},
  {"claim": "Heroes is the fourth series. It begins after Baron von Darkcheat is defeated; Madam Zelda in Blackspore Swamp starts it; players keep the Baron busy while four Realmkeepers train; it ends in a final reckoning.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734 (fact:quest)"},
  {"claim": "Madam Zelda gathers four child heroes, the Realmkeepers, and trains them against Darkcheat.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 (fact:npc)"},
  {"claim": "Heroes series: Madame Zelda in Blackspore Swamp starts it and gathers the four Realmkeepers; the final showdown follows the four fights.", "source": "http://www.freerealms.com/article/detail.action?articleId=2746 (fact:npc, fact:quest)"},
  {"claim": "The Spanish article gives the storyline as the Defenders, fighting until their training is complete. It has no absolute date.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737 (date null)"},
  {"claim": "Seaside objective: play Baron von Darkcheat for a few games while the Realmkeepers get into position.", "source": "locale:7961"},
  {"claim": "Sunstone Valley lead-in: help Madam Zelda search for the missing Realmkeepers.", "source": "locale:5100175; locale:5100176"},
  {"claim": "Realmkeepers are four heroes: Ghostshadow (leader), Magetech, Wildclaw, Crackshot.", "source": "wiki 'Realmkeepers'; wiki 'Category:Realmkeepers'"}
 ],
 "confidence": 0.3,
 "open": [
  "No absolute date in any source. Article 2737 has only a relative date ('Publié il y a 2 mois, 6 jours'). The 2012-08-25 date from an earlier answer is dropped; it has no dated source in this pack. occurrences is empty until a dated second source is found.",
  "Not a bounded event: no start, end or recurrence is sourced. It is a TCG expansion storyline, so live is unsure.",
  "Name vs. Baron: the Baron fight (locale 7948-7961; Grimyfoot, Clancy Blackheart, Seaside) is the preceding arc. Locale 9922 bundles Baron and Heroes packs together and is not used as this event's item.",
  "Do not merge with 'Heroes Journal' / Hero Rises, which is separate content. The bare alias 'Heroes' is dropped.",
  "Kid names conflict: article 2733 gives Bryce, Nathan, Kade, Jessica; article 2737 gives Onofre for Kade. The Ghostshadow=Bryce and Wildclaw=Kade equivalences come from article 2733 and the wiki, not from a single source, and are unresolved.",
  "Zone conflict: Blackspore Swamp (article 2734) vs Sporeshade Swamp (article 2740). Unresolved.",
  "Whether the Sunstone Valley Realmkeepers quest chain (locale 5100175-5100637) belongs to Heroes is not confirmed by any source here.",
  "Locale 441610/441612 ('Complete the Heroes Questline.') and 9403 (bundle) were not re-read in this pass. Prices and currency for the pack and bundle are not in any source: null.",
  "The final challenge's special prize is not named in any source. Baron costume (locale:391, wiki) is not verified as a reward of this event and is left out.",
  "Critique notes: the calendar and evidence critiques (scores 2 and 3, both not wireable) have been applied where sources allow. The event is still not wireable: no dated source."
 ]
}
