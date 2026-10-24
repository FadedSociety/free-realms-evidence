<!-- fleet job=event-infer id=vvampire-vs-werewolf-dance-battle-v9 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[10608, 12809, 6, 4412] model=claude-haiku-5-5 -->
# Vampire vs Werewolf dance battle

```json
{
 "event": {
  "name": "Super Spooktacular",
  "aliases": ["Super Spooktacular", "Spooktacular"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "October 14 through November 11, 2009 (pre-event schedule, 'is scheduled to run'; actual run not confirmed)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476; http://www.tentonhammer.com:80/node/75739"},
  {"year": 2010, "when": "October 2010 ('Super Spooktacular month'); second annual; exact run days not stated", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845; http://www.freerealms.com/article/detail.action?articleId=1860 (second year); articleId=1854"},
  {"year": 2013, "when": "October 1 through November 12, 2013 ('Fourth Annual')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949"}
 ],
 "recurring": "Yearly in October, running into November (inferred from the exact 2009 and 2013 windows; 2010 is month-level only). Not stated as recurring by any article.",
 "zones": [
  "Bone Bog Cemetery (dance-off battle instance, near the Bone Bog; articleId=1862, 1854)",
  "Blackspore Swamp (dance-off kick-off and Madam Zelda quest start; client locale:5197, locale:436401; articleId=1862)",
  "Sanctuary (Halloween Harry candy cart and trick-or-treat party; client locale:415408, 415268; articleId=1864)"
 ],
 "npcs": [
  "Madam Zelda (starts the dance-off quest; articleId=1862, 1854)",
  "Pumpkin Prince (judge and prize giver for the dance-off; articleId=1862)",
  "Halloween Harry (Sanctuary candy cart; client locale:415408, 415268, 416849)"
 ],
 "quests": [
  "Choose Vampires or Werewolves Dance for the Pumpkin King (source: articleId=1862 only; client title not verified)"
 ],
 "activities": [
  "Pick a side (Vampires or Werewolves) through Madam Zelda and join the Vampires vs Werewolves dance-off battle near Bone Bog Cemetery (articleId=1854, 1862; client locale:5197)",
  "Dance-off judged by the Pumpkin Prince for the pumpkin prize (articleId=1862)",
  "Wear vampire or werewolf costume pieces to show team spirit (articleId=1860, 1861)",
  "Trick-or-treat with the /scare mechanic and daily quests (articleId=1860, 1861)",
  "Daily Trick or Treat quests and candy at the Sanctuary party (articleId=1864)"
 ],
 "items": [
  {"name": "Werewolf Tail", "price": null, "currency": null, "source": "client locale:7365 (names Super Spooktacular; cannot be worn with Vampire Fangs); articleId=1860"},
  {"name": "Vampire Fangs", "price": null, "currency": null, "source": "client locale:7366 (names Super Spooktacular); articleId=1860"}
 ],
 "rewards": [
  "Pumpkin prize for the winning side (articleId=1862; amount not verified)"
 ],
 "evidence": [
  {"claim": "The dance battle is a Super Spooktacular activity: Vampires vs Werewolves dance-off, pumpkin prize, Pumpkin Prince judge, started by Madam Zelda", "source": "http://www.freerealms.com/article/detail.action?articleId=1862; wiki 'Super Spooktacular' ('dance battle between Vampires and Werewolves, stationed near the Bone Bog Cemetery')"},
  {"claim": "The dance-off is in the 2010 edition (second year), with costumes for team spirit", "source": "http://www.freerealms.com/article/detail.action?articleId=1860; articleId=1861"},
  {"claim": "The client names the dance-off in Blackspore: 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!'", "source": "client locale:5197; locale:436401"},
  {"claim": "Halloween Harry is at his candy cart in Sanctuary", "source": "client locale:415408 ('at his candy cart in Sanctuary'), locale:415268"},
  {"claim": "October 2010 was Super Spooktacular month", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845"},
  {"claim": "2009 was scheduled Oct 14 to Nov 11", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476; http://www.tentonhammer.com:80/node/75739"},
  {"claim": "2013 ran Oct 1 to Nov 12 as 'Fourth Annual Super Spooktacular'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949"},
  {"claim": "Werewolf Tail and Vampire Fangs are event items that cannot be worn together", "source": "client locale:7365, 7366; articleId=1860"}
 ],
 "confidence": 0.6,
 "open": [
  "Scope: the pack's 'Vampire vs Werewolf dance battle' is one activity inside Super Spooktacular, not a separate event. Merged under the parent. 'Bone Marsh' in the pack is a translation of Bone Bog Cemetery.",
  "Dance-off year: sourced only to the 2010 edition (articleIds 1854, 1860, 1861, 1862). No source read confirms it in 2011-2013. Not a standing yearly activity by any source.",
  "2011: the Oct 13 to Nov 23 window was carried from a prior pass and is NOT verified. articleId=2304 was not re-fetched. Only an October 2011 webcast on the event (articleId=2301) is confirmed. No 2011 occurrence is listed.",
  "2012: only a wiki news-archive line (Oct 11, 2012 'Halloween Spooktacular Content' update). Start and end are unconfirmed, so no 2012 occurrence is listed.",
  "Zone conflict for the battle: articleId=1854 and client locale:5197/436401 say Blackspore; articleId=1861 says Sporeshade; articleId=1862 says Bone Bog Cemetery. Blackspore is the zone and Bone Bog is the sub-location, but Sporeshade is unresolved.",
  "Halloween Harry location conflict: client locale:436401 says 'Talk to Halloween Harry in Pixiewood'; about 30 other client lines (e.g. 415268, 415408, 416849) and articleId=1864 place him in Sanctuary. Sanctuary is recorded; the Pixiewood line is an unresolved conflict.",
  "Year-count conflict: articleId=2949 says 'Fourth Annual' for 2013, but 2009 'First Annual' and 2010 'second annual' imply 2013 is the fifth. Wording kept as quoted.",
  "Quest titles: 'Being Prepared (Team Vampire)', 'Being Prepared (Team Werewolf)', 'First Bite', 'Pre-Emptive Bite' and 'Another One Bites the Muck' come only from the wiki 'Super Spooktacular' page and are not matched in the client locale. Not listed as quests. The 'Howl...' title is truncated. Daily Trick or Treat titles were not recovered.",
  "Drake Sullenfangs and Ed Sullenfangs: wiki 'Super Spooktacular' only. Client dance-off storyline lines (e.g. locale 432223, 432244, 432288, 432314, 432333) were cited by a critic but not re-read this pass; Drake is not listed as an NPC.",
  "Items: Necrowart Wrist Wraps, Chatty Costume, Candy Corn, Super Spooktacular Parachute, Widow Candy and Pumpkin Patch Flooring rest on wiki text only (Pumpkin Patch Flooring cites articleId=2306, not read). Not listed, since no article or client text ties them to the event. Prices are blank everywhere, so currency is null for all items.",
  "Dance-off reward amounts and the pumpkin prize contents are unverified.",
  "The client quest 'Return to Madam Zelda' (locale:26473) belongs to the Blackspore card-duel line and is excluded.",
  "Excluded for lack of an event tie: Fog Machine, Flaming Skull Wobblehead, Eyeball mount, Dragonfire Broomstick.",
  "'Pumpkin Prince' and 'Pumpkin King' are both used for the same judge NPC. Treated as one NPC, not an event alias.",
  "Aliases: 'Halloween event (SOE wording)' and 'Halloween Spooktacular' are not quoted forms and are removed. Only 'Super Spooktacular' and 'Spooktacular' are kept."
 ]
}
```
