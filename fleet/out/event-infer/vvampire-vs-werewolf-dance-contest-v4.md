<!-- fleet job=event-infer id=vvampire-vs-werewolf-dance-contest-v4 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[18969, 10840, 8, 4123] model=claude-haiku-5-5 -->
# Vampire vs. Werewolf dance contest

```json
{
 "event": {
  "name": "Vampires vs. Werewolves Dance-off",
  "aliases": ["Vampire vs. Werewolf dance contest", "Vampires vs. Werewolves Dance-Off", "Vampire vs. Werewolf Dance Off", "Pumpkin Prince dance-off"]
 },
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "October 2010 (Super Spooktacular month); dance-off dates not stated. Year inferred from article ordinal, not dated.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845 (October 2010 Super Spooktacular month); year link to the dance-off via http://www.freerealms.com/article/detail.action?articleId=1857 (undated)"},
  {"year": 2012, "when": "during the 2012 Halloween event (wiki says the Purebloods family was established then)", "source": "wiki page 'Eternal Purebloods' (Summary: 'Established in 2012 during the halloween event (Vampires vs. Werewolves Dance-off)')"},
  {"year": 2013, "when": "October 2013, inside Super Spooktacular Oct 1 to Nov 12, 2013; dance-off itself not dated in a source", "source": "wiki user blog 'Soe amnerys/Weekly Update - 10/22/13' (Game Update 116, dance-off eligibility change); parent dates from http://www.freerealms.com:80/article/detail.action?articleId=2949"}
 ],
 "recurring": "yearly in October, within the Super Spooktacular / Super Fantomastique Halloween holiday (wiki: 'annual event'); exact days not sourced",
 "zones": ["Bone Bog Cemetery", "Blackspore (Blackspore Swamp)"],
 "npcs": ["Pumpkin Prince", "Madame Zelda"],
 "quests": [],
 "activities": [
  "Pick a side (Vampires or Werewolves) via Madame Zelda at Blackspore (article 1862 summary)",
  "Wear Team Vampire or Team Werewolf costume pieces at Bone Bog Cemetery when the in-game announcement starts the dance-off (article 1862 summary; locale:5197)",
  "Dance; the team with the most frightening dance is crowned the scariest monster, judged by the Pumpkin Prince (article 1862)"
 ],
 "items": [
  {"name": "Grey Werewolf Outfit", "price": null, "currency": "station_cash", "source": "wiki user blog 'Soe amnerys/Weekly Update - 10/22/13' (qualifies as a Werewolf outfit for the dance-off); wiki Grey Werewolf Outfit (Station Cash Marketplace); client locale:5102477, locale:5102478 (name and description). Price not in sources."}
 ],
 "rewards": [
  "Vampire Cake Slice or Werewolf Cake Slice for the winning team, depending on which side wins (wiki 'Super Spooktacular', dance-off entry)",
  "Crowned 'scariest monster' for the team with the most frightening dance (article 1862)"
 ],
 "evidence": [
  {"claim": "Vaampires and Werewolves compete in a dance-off for the Pumpkin Prince near Bone Bog Cemetery; players wear vampire or werewolf costumes", "source": "http://www.freerealms.com/article/detail.action?articleId=1857 ; http://www.freerealms.com:80/article/detail.action?articleId=2304 (summary)"},
  {"claim": "Pumpkin Prince judges the dance; the most frightening dance team is crowned scariest monster", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1862 (fact and summary)"},
  {"claim": "Players pick a side via Madame Zelda at Blackspore, then wear costume pieces at Bone Bog Cemetery when the in-game announcement starts the dance-off", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1862 (summary)"},
  {"claim": "The dance-off is just outside the Bone Bog Cemetery gates, in Blackspore, hosted by the Pumpkin Prince, during the annual Super Spooktacular", "source": "wiki page 'Blackspore Swamp'; wiki page 'Vampires vs. Werewolves Dance-off' (located near Bone Bog Cemetery during Super Spooktacular)"},
  {"claim": "Dance-off announcement is client text", "source": "locale:5197"},
  {"claim": "Winning team gets Vampire or Werewolf Cake Slice", "source": "wiki page 'Super Spooktacular' (dance-off reward entry)"},
  {"claim": "Dance-off ran in 2012 (Purebloods established during it)", "source": "wiki page 'Eternal Purebloods'"},
  {"claim": "Dance-off eligibility was updated in the 10/22/13 update (Grey Werewolf Outfit qualifies)", "source": "wiki user blog 'Soe amnerys/Weekly Update - 10/22/13'"},
  {"claim": "Super Spooktacular 2013 ran Oct 1 to Nov 12", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949"}
 ],
 "confidence": 0.5,
 "open": [
  "Pack merges the dance-off (a world event inside the Super Spooktacular / Super Fantomastique holiday) with the parent holiday. Give the parent holiday its own row. The parent is annual, October, Oct 1 to Nov 12 in 2013 (article 2949).",
  "No article in the pack dates the dance-off itself. Article 1857, 1862 and 2304 are undated (relative 'Posted N months ago' only). Exact dance-off days for any year are unknown.",
  "2010 is inferred from the article ordinal (article 476 = 1st annual, 2009); not stated by a dated source for the dance-off.",
  "2013 rests on a wiki user blog (Weekly Update 10/22/13) that I could not open. Only the parent holiday dates are article-sourced.",
  "Dropped from items, unverified: Vampire Fangs and Werewolf Tail (locale:7363/7364 name Super Spooktacular; locale:7365/7366 are a parent-holiday wearing rule; locale 432411/432415 show SC bundle contents, not dance-off rewards).",
  "Unverified (the wiki dance-off page Items section was truncated in lookup): Vampire Outfit, Werewolf Outfit, Team Vampire T-Shirt, Team Werewolf T-Shirt, Vampire Bat. The wiki Bat page says the Bat comes from the Team Vampire Bundle in the SC Marketplace, which conflicts with a dance-off reward. Re-check the full wiki 'Vampires vs. Werewolves Dance-off' Items section before adding them.",
  "Cake Slice reward names come from the wiki Super Spooktacular page only. Not confirmed by a client item entry tied to the dance-off; locale:6628 and 7336 are not linked here.",
  "Quest titles not confirmed. Article 1867 mention of 'Choose the vampire or werewolf side' not verified as a quest title. Quests left empty.",
  "Prices are not in any source; all null. Pumpkin Prince Card and Bundle (locale:9919, 9921) belong to the Halloween TCG and are excluded. Article 2304 is undated and is not used as an occurrence. The 2009 Halloween Dance Party (articleId 484) is a different event.",
  "Vampire and Werewolf Dance Practice battles (Sinking Graveyard, locale:432022/432024) are a separate sub-event and are excluded. Give them their own row if needed.",
  "Madame Zelda side-pick is the entry to the Super Spooktacular questline, so it is listed under activities, citing article 1862 (article 1878 was not verified and is not cited).",
  "Alias 'Vampires vs. Werewolves Costume Party' (locale:14564) is unconfirmed and excluded.",
  "Article 1867 does not name a marsh location; the earlier claim is dropped. Bone Bog Cemetery is sourced to articles 1857 and 1862 and the wiki pages."
 ]
}
```
