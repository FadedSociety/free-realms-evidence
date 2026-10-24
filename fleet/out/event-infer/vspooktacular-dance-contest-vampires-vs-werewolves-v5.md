<!-- fleet job=event-infer id=vspooktacular-dance-contest-vampires-vs-werewolves-v5 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[19085, 11414, 8, 4211] model=claude-haiku-5-5 -->
# Spooktacular dance contest (Vampires vs. Werewolves)

```json
{
 "event": {
  "name": "Vampires vs. Werewolves dance-off (Spooktacular season contest)",
  "aliases": ["Vampires vs. Werewolves Dance-Off", "Vampires vs Werewolves Dance-off", "Vampire vs Werewolf dance contest", "Spooktacular dance contest (Vampires vs. Werewolves)"]
 },
 "kind": "contest",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Oct 13 - Nov 23, 2011 (Spooktacular season; dance-off listed in that season's article)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304 (lookup fact:event confirms the dance-off is listed; the 2011 season dates come from the earlier pass, not re-read; this article's summary says it gives no exact post date)"},
  {"year": 2010, "when": "about October 2010 (inferred only)", "source": "http://www.freerealms.com/article/detail.action?articleId=1867 summary: 'posted 7 months, 2 weeks ago' relative to capture 2011-06-04. This is a relative date, not a stated date, so it is NOT counted as an occurrence."}
 ],
 "recurring": null,
 "zones": [
  "Blackspore (locale:5197 'about to kick-off in Blackspore'; article 1862 fact:quest: Madam Zelda in Blackspore, on the road to Bone Bog Cemetery just south of the Haunted Mines)",
  "Blackspore Swamp, near Bone Bog Cemetery (locale:436401 'dance off in Blackspore Swamp'; article 1854 and article 2304 fact:event: near Bone Bog Cemetery)",
  "Esporaumbria / Shadowbrook: conflicting Spanish-summary wording, unresolved (see open)"
 ],
 "npcs": ["Madame Zelda (starts the side choice; articles 1862, 1866)", "Pumpkin Prince (judges the dance-off; locale:432206; article 1862; also called Pumpkin King / Rey Calabaza in translated articles, assumed the same NPC)", "Jake Blackforest (werewolf side, sabotage quest; locale:432023)", "Ed Sullenfangs (vampire side, sabotage quest; locale:432025)", "Halloween Harry (Pixiewood trick-or-treat; locale:436401 text, but this line is about the wider Super Spooktacular, not the dance-off)"],
 "quests": ["Pumpkin Prince (locale:432206, quest_dialog)", "Howl of Warning (locale:432288)", "Another One Bites the Muck (locale:432254)", "Werewolf Dance Practice (locale:432023, objective title)", "Vampire Dance Practice (locale:432025, objective title)"],
 "activities": [
  "Visit Madame Zelda and choose Vampires or Werewolves (article 1862 fact:quest; article 1866)",
  "Wear vampire or werewolf costume pieces to show team support (article 1854; article 2304; article 1862)",
  "Join the vampire dance-off when the in-game announcement starts; the vampire outfit is needed for moves to count (locale:5197; locale:432254)",
  "Judging by the Pumpkin Prince: the side with the most frightening dance is crowned (article 1862 fact:event; locale:432206)",
  "Side-quest sabotage of the rival dance practice (locale:432288; locale:432023; locale:432025)"
 ],
 "items": [
  {"name": "Super Spooktacular Parachute", "price": "899 (video-only, unverified)", "currency": "station_cash", "source": "locale:5102560 (client name ties it to the Spooktacular event, not the dance-off); video:1TNyzyI62nc/00122 (price frame, not checked). No article dates this item, so it is NOT tied to the dance-off and is not scheduled to any occurrence."},
  {"name": "Team Werewolf / Team Vampire outfits (Boy and Girl)", "price": null, "currency": null, "source": "article 2304 (names the outfits as Marketplace items for the Spooktacular season). The client does not tie these names to the event, so they stay unconfirmed as event items."}
 ],
 "rewards": ["A piece of the Pumpkin Prince's special cake for the winning side (article 1867; locale:432206)", "Scariest-monster title for the winning side (article 1862 fact:event)"],
 "evidence": [
  {"claim": "Vampires and werewolves compete in a dance-off for the Pumpkin Prince near Bone Bog Cemetery; players wear costumes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854 (fact:event); http://www.freerealms.com:80/article/detail.action?articleId=2304 (fact:event)"},
  {"claim": "The dance-off is judged by the Pumpkin Prince; the side with the most frightening dance is crowned", "source": "http://www.freerealms.com/article/detail.action?articleId=1862 (fact:event); locale:432206"},
  {"claim": "The side choice starts with Madame Zelda in Blackspore", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1862 (fact:quest)"},
  {"claim": "The dance-off is announced as about to kick off in Blackspore", "source": "locale:5197 (npc_dialog)"},
  {"claim": "The dance-off appears in the 2011 Spooktacular season article", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304 (lookup fact:event and summary)"},
  {"claim": "The event is live in the client ('Super Spooktacular - Now Live!')", "source": "locale:436400 (npc_dialog)"}
 ],
 "confidence": 0.55,
 "open": [
  "Only one dated occurrence (2011, article 2304) ties the dance-off itself to a year, and that article's summary says it has no exact post date. The 2011 season dates (Oct 13 - Nov 23) come from the earlier pass and were not re-read here. Confirm before scheduling.",
  "2009 and 2013 (Super Spooktacular articles 476 and 2949) are the umbrella season. No source ties the dance-off to those years, so they are not listed as dance-off occurrences. Earlier draft merged them; that merge is rejected.",
  "Recurrence: the dance-off needs two sourced years to be called recurring. Only 2011 is sourced, so recurring is null. 2010 is inferred from a relative date only.",
  "Zone conflict: article 1866 and the Spanish summaries say Shadowbrook or Esporaumbria; articles 1862 and locale:5197 say Blackspore. Blackspore is best supported. Unresolved.",
  "Costume party (locale:14564 name, locale:14568 'Can we beat last year's party?') may be a separate event or an alias for the dance-off. Unresolved; not merged.",
  "Pumpkin Prince, Pumpkin King, Prince Pumpkin and Rey Calabaza are assumed to be one NPC; only translated articles use the other names.",
  "Quest 'Choose Vampires or Werewolves' appears in articles 1862 and 1866 but has no matched client title, so it is left out of quests.",
  "Super Spooktacular Parachute (899 station_cash) is a Spooktacular item, not a dance-off item. Price is from video only and unverified; year is unverified.",
  "Fog Machine, Flaming Skull Wobblehead and Eyeball mount are dropped: video description text only, no tie to this event.",
  "Halloween Harry / Pixiewood line (locale:436401) is about the wider Super Spooktacular, not the dance-off, and is kept out of the dance-off's NPCs in spirit; listed for context only.",
  "locale:119271 was flagged as a duplicate phrase and is dropped as evidence."
 ]
}
```
