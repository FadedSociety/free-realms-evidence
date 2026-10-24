<!-- fleet job=event-infer id=vdefenders-storyline-v6 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[17805, 10864, 8, 3919] model=claude-haiku-5-5 -->
# Defenders storyline

```json
{
 "event": {
  "name": "Heroes TCG set 4: Realmkeepers vs. Baron von Darkcheat storyline",
  "aliases": ["TCG Set 4: HEROES (locale:17472)", "Realmkeepers storyline", "Defenders storyline (Spanish article 2737 translation; 'Defensores')", "Baron Trampaoscura (Spanish name for Baron von Darkcheat, article 2737)"]
 },
 "kind": "other",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [
  "Sunstone Valley (lead-in: 'Card Duelist: The Realmkeepers Are Missing!', locale:5100175, 5100176; Madam Zelda searches for the missing Realmkeepers there; boundary with Heroes unverified)",
  "Blackspore Swamp (Madam Zelda starts the Heroes series; article 2734 fact:quest; article 2746 fact:npc)",
  "Seaside (play Baron von Darkcheat for a few games while the Realmkeepers train; locale:7961)",
  "Sporeshade Swamp appears in article 2740; conflicts with Blackspore Swamp in article 2734. Unresolved."
 ],
 "npcs": [
  "Madam Zelda (article 2733 fact:npc; article 2734; article 2746; wiki 'Madam Zelda')",
  "Baron von Darkcheat (locale:7961; article 2734; wiki 'Baron von Darkcheat')",
  "Ghostshadow (Bryce; article 2733 fact:npc; wiki 'Ghostshadow')",
  "Magetech (Nathan; article 2733 fact:npc; wiki 'Magetech')",
  "Wildclaw (Kade in article 2733; wiki 'Wildclaw')",
  "Crackshot (wiki 'Crackshot'; wiki 'Realmkeepers')",
  "Jessica (article 2733 fact:npc; article 2737 summary)"
 ],
 "quests": [
  "Card Duelist: The Realmkeepers Are Missing! (locale:5100175; Sunstone Valley lead-in, not verified as part of Heroes)",
  "Card Duelist: Meet the Boss (locale:7961, Seaside objective)"
 ],
 "activities": [
  "Play Trading Card Game matches against Baron von Darkcheat and his cronies while the Realmkeepers train (article 2734 fact:quest; locale:7961)",
  "Complete the Heroes TCG quest line, ending in a final reckoning with the Baron (article 2734 fact:quest; article 2746 fact:quest)",
  "Buy and open Heroes TCG booster packs (locale:17470 name)"
 ],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470 (name only)"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "from prior pack, locale:7973 not re-checked in this pass; treat as unverified"}
 ],
 "rewards": [
  "'Amazing new loot!' for the Set 4 release (locale:17473; no item named)",
  "New quests for Level 20 Card Duelists (locale:17473)",
  "Baron von Darkcheat costume: prior pack cites locale:391 and a wiki page; neither re-verified here, so not listed as a reward of this event"
 ],
 "evidence": [
  {"claim": "Heroes is the fourth TCG series. It begins after Baron von Darkcheat is defeated, with Madam Zelda in Blackspore Swamp starting it, and ends in a final reckoning with the Baron.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734 (fact:quest)"},
  {"claim": "Madam Zelda gathers four child heroes, the Realmkeepers, and trains them to defend Free Realms against Darkcheat.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 (fact:npc)"},
  {"claim": "Heroes is described as the story of the Realmkeepers in Blackspore Swamp (French article).", "source": "http://www.freerealms.com/article/detail.action?articleId=2746 (fact:npc, fact:quest)"},
  {"claim": "The Spanish article gives the storyline as the Defenders, with the fight lasting until their training is complete. It has no absolute date.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737 (fact:event; date null)"},
  {"claim": "The client names the set 'TCG Set 4: HEROES Available Now!'.", "source": "locale:17472"},
  {"claim": "The client announces 'The newest Free Realms Trading Card Game Set is here!' with new loot and quests for level 20 Card Duelists, and says Quests for TCG Sets 1-4 are free to play. It does not say Heroes itself is free.", "source": "locale:17473"},
  {"claim": "Realmkeepers are four heroes: Ghostshadow (leader), Magetech, Wildclaw, Crackshot.", "source": "wiki page 'Realmkeepers'; wiki page 'Category:Realmkeepers'"},
  {"claim": "Seaside objective: play Baron von Darkcheat for a few games to keep him busy while the Realmkeepers get into position.", "source": "locale:7961"},
  {"claim": "Sunstone Valley lead-in quest: help Madam Zelda search for the missing Realmkeepers.", "source": "locale:5100175; locale:5100176"}
 ],
 "confidence": 0.3,
 "open": [
  "No absolute date anywhere in the pack. Article 2737 has only a relative date. The 2012-08-25 launch date from the prior answer rests on one Ten Ton Hammer summary that was not reopened, so it is dropped. Needs a dated second source before any occurrence is added.",
  "Not wireable as a bounded event: no start, end or recurrence is sourced. It is a TCG expansion storyline.",
  "Kid names conflict: article 2733 gives Bryce, Nathan, Kade, Jessica; article 2737 gives Onofre in place of Kade. Unresolved.",
  "Zone conflict: Blackspore Swamp (article 2734) vs Sporeshade Swamp (article 2740). Unresolved.",
  "The bare alias 'Heroes' is dropped. It would merge this TCG set with the separate Heroes Journal / Hero Rises content, which is outside this pack's evidence.",
  "The Sunstone Valley Realmkeepers quest (locale:5100175) is listed as a lead-in only. Whether it belongs to Heroes is not confirmed by any source here.",
  "Locale:7960 and 7948 (Meet the Boss, Heart of Darkness) were not re-checked in this pass. 7966 is a flagged duplicate and is not used. Locale:7973 (Bundle) and 391 (costume) are unverified here.",
  "Prices and currency for the booster pack and bundle are not in any source: null.",
  "The final challenge's special prize is not named in any source.",
  "Series 3 vs Series 4 separation for the Baron von Darkcheat costume is not resolved here."
 ]
}
```
