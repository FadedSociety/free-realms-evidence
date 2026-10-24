<!-- fleet job=event-infer id=vpumpkin-prince-v6 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[12232, 13268, 6, 4183] model=claude-haiku-5-5 -->
# Pumpkin Prince

```json
{
 "event": {
   "name": "Pumpkin Prince",
   "aliases": ["Pumpkin Prince world event", "Pumpkin Prince boss fight", "Rey Calabaza / Príncipe de Calabaza (Spanish)"]
 },
 "kind": "other",
 "live": "unsure",
 "occurrences": [
   {"year": 2010, "when": "October 2010 (month only; the Prince content is in undated posts)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845 (October month); http://www.freerealms.com:80/article/detail.action?articleId=1854 (Prince world event, no absolute date)"},
   {"year": 2011, "when": "Oct 13 - Nov 23, 2011 (the Prince world event ran inside the Super Spooktacular run)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"}
 ],
 "recurring": null,
 "zones": ["Snowhill", "Stillwater Crossing", "Bristlewood", "Bone Bog Cemetery (members battle instance, not a world-event zone)"],
 "npcs": ["Pumpkin Prince", "Ghost Hunters (Snowhill, Stillwater Crossing, Bristlewood)", "Lucinda (helps defeat the Prince in Bone Bog Cemetery)"],
 "quests": ["Guardians of the Tomb", "Sealed with a Signet"],
 "activities": [
   "Talk to the Ghost Hunters in Snowhill, Stillwater Crossing or Bristlewood to scare off the Prince's ghosts and ghouls (world event)",
   "Fight the Pumpkin Prince in Bone Bog Cemetery with Lucinda's help (quest line, locale 415338)",
   "Vampires vs. Werewolves Dance Off for the Prince, choosing Team Vampire or Team Werewolf (article 1854; wiki Vampires vs. Werewolves Dance-off)"
 ],
 "items": [
   {"name": "Team Vampire / Team Werewolf costume items (Bat, T-Shirt, Outfit, Fangs)", "price": null, "currency": null, "source": "wiki page: Vampires vs. Werewolves Dance-off (wiki only; no price or date)"}
 ],
 "rewards": [
   "Special cake from the Pumpkin Prince for the winning Dance Off side (http://www.freerealms.com:80/article/detail.action?articleId=1862; full reward text not checked)",
   "Prize for taking part in a battle against the Prince (wiki page: Ghost Hunters; amount not verified)"
 ],
 "evidence": [
   {"claim": "The Pumpkin Prince sends ghosts and ghouls to the surface; players talk to Ghost Hunters in Snowhill, Stillwater Crossing and Bristlewood to scare them off", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854; http://www.freerealms.com:80/article/detail.action?articleId=2304"},
   {"claim": "Client text: the Prince moves around and appears at Snowhill, Bristlewood or Stillwater Crossing", "source": "locale:416782"},
   {"claim": "Quest 'Guardians of the Tomb': the Prince's tomb in Blackspore, sealed by spectral guardians near the warpstones in Sacred Grove", "source": "locale:415331 (title); locale:415330 (objective text)"},
   {"claim": "Quest 'Sealed with a Signet': the Prince's ghosts reopen the tomb; players meet Lucinda in Bone Bog Cemetery to send the Prince back", "source": "locale:415335 (title); locale:415338 (text)"},
   {"claim": "Oct 2010 is a Super Spooktacular month with community events", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845"},
   {"claim": "The Prince's world event is in the 2011 Super Spooktacular run, Oct 13 - Nov 23, 2011", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
   {"claim": "Dance Off between Vampires and Werewolves; winners get cake from the Prince", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854; http://www.freerealms.com:80/article/detail.action?articleId=1862"},
   {"claim": "Pumpkin Prince is an NPC boss and antagonist of Super Spooktacular (wiki category NPC, Holiday, Blackspore)", "source": "wiki page: Pumpkin Prince"}
 ],
 "confidence": 0.4,
 "open": [
   "Classification: the Pumpkin Prince is a boss and world-event sub-event of Super Spooktacular (Halloween), not a standalone holiday. Create a separate record for the parent Super Spooktacular. Its dated runs are: 2009 Oct 14 - Nov 11 (articleId=476 is the primary source; tentonhammer node/75739 is secondary), 2010 October (article 1845, month only), 2011 Oct 13 - Nov 23 (article 2304), 2013 Oct 1 - Nov 12 (article 2949). Pixiewood, Sanctuary, Halloween Harry, Madam Zelda, the /scare trick-or-treat mechanic and daily quests belong to the parent.",
   "No 2009 Prince occurrence is recorded: the 2009 source gives only the parent event dates, and the Prince's 2009 presence is not verified.",
   "The 2010 occurrence is month-level only. Articles 1857, 1860 and 1861 repeat article 1854 and are not independent sources.",
   "Recurrence is unverified for the Prince. Yearly recurrence applies to the parent event only, and the Prince's presence in each year is not confirmed.",
   "Numbering conflict: article 2949 calls 2013 the 'fourth annual'; articles 1854, 1860 and 1861 call 2010 the 'second year'. Unresolved.",
   "Spawn timing conflict: the wiki says every 15 minutes with server broadcasts; article 1854 says 'unpredictable locations'. Unresolved; no fixed cadence is recorded.",
   "Mansagua Pass, Thornwood and Florestaespina appear only in Spanish and French quotes and are not listed as zones.",
   "'A Ghostly Discovery' and 'A Trip to the Swamp' are dropped: no source ties them to the Prince. Locale ids 415327 and 415319 are the titles only.",
   "'The Great Scare' and 'The Pumpkin Prince' (quest answers) are unresolved and not listed. The client title for 'The Pumpkin Prince' is not confirmed.",
   "'A Formal Report' is excluded: its title is locale 415315 (not 415316, an objective), and the Prince link is not shown.",
   "'Spectral Spectacles': locale 119241 is the item name; no client quest_title was found, and locale 415389 is an objective. Excluded.",
   "Necrowart Wrist Wraps and Chatty Costume are dropped: wiki-only, no price, and no source tying them to the Prince. Super Spooktacular Parachute (899 station_cash) is dropped: only a video frame, not verified against a store record.",
   "Ghost Vision achievement is dropped: its only source is 'Template:News', and no client achievement id was found.",
   "Trick-or-Treat, Bag Snatchers and Candy Gram are wiki-only parent-event material, not checked, and excluded here.",
   "Super Spooktacular 2009 Member Pack (locale 156839), Pumpkin Prince's Treasure (locale 432069), and the Pumpkin Prince and Bundle Trading Card Game items (locale 9919, 9921) are not tied to the Prince and are excluded.",
   "Madam Zelda is in article 1854 only. Greyli Dustywings may appear at locale 415979, which was not checked here. Neither is listed.",
   "Duplicate NPC name: locales 416102 and 5102926 are both 'Pumpkin Prince'. Not checked which is live.",
   "Dance Off items are wiki-only and undated. Full Dance Off cake reward (article 1862), the Pumpkin Carver and Prince Slayer achievements, and battle prizes are not verified.",
   "Live status is unsure. The latest dated occurrence is 2011, and no 2026 run is shown. Locale 436400 ('Super Spooktacular - Now Live!') is undated.",
   "Not wireable: the Prince needs its own dated source before it can be scheduled."
 ]
}
```
