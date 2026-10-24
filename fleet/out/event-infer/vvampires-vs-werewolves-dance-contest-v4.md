<!-- fleet job=event-infer id=vvampires-vs-werewolves-dance-contest-v4 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[25165, 14158, 8, 3840] model=claude-haiku-5-5 -->
# Vampires vs. Werewolves dance contest

```json
{
 "event": {
  "name": "Vampires vs. Werewolves dance contest",
  "aliases": [
   "Vampires vs Werewolves Dance-off (locale:5197 announcement; wiki page 'Vampires vs. Werewolves Dance-off')",
   "Werewolves vs. Vampires Dance Off (articleId=1854 and 2304 wording; wiki file 'The Were Wolf VS Vampires Dance Off')"
  ]
 },
 "kind": "contest",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Super Spooktacular ran Oct 13 - Nov 23, 2011; the dance-off's own dates are not stated", "source": "http://www.freerealms.com/article/detail.action?articleId=2304"},
  {"year": 2013, "when": "October; holiday run Oct 1 - Nov 12, 2013; dance-off named in Game Update 115 (10/15/2013)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949 (holiday dates, summary); wiki Template:News (Game Update 115 note, pack-supplied, not re-checked)"}
 ],
 "recurring": null,
 "zones": ["Blackspore (Madame Zelda starts the mission)", "Bone Bog Cemetery, outside the gates (contest site)"],
 "npcs": ["Madame Zelda (starts the mission; articleId=1862; wiki Madam Zelda)", "Pumpkin Prince (judges the dance; articleId=1854, 1862, 2304; wiki Blackspore Swamp)"],
 "quests": ["Join Team Vampire (locale:5102484 text confirmed; tie to the dance-off is by objective text only, locale:432314 'Join Team Vampire in the dance-off')"],
 "activities": [
  "Talk to Madame Zelda in Blackspore to start the mission and choose Vampires or Werewolves (articleId=1862)",
  "Wait for the in-game announcement that the dance-off is starting (locale:5197)",
  "Go to the site outside Bone Bog Cemetery wearing Vampire or Werewolf costume pieces (articleId=1862, 1854, 2304)",
  "Dance for the Pumpkin Prince; the side with the most fans wins (articleId=1862)"
 ],
 "items": [
  {"name": "Vampire Cake Slice", "price": null, "currency": "reward", "source": "wiki Super Spooktacular (reward line); client locale:6628"},
  {"name": "Werewolf Cake Slice", "price": null, "currency": "reward", "source": "wiki Super Spooktacular (reward line); client locale:7336"},
  {"name": "Vampire Outfit", "price": null, "currency": null, "source": "wiki Vampires vs. Werewolves Dance-off (Team Vampire items); client locale:14688"},
  {"name": "Team Vampire T-Shirt", "price": null, "currency": null, "source": "wiki Vampires vs. Werewolves Dance-off; client locale:14692"},
  {"name": "Vampire Fangs", "price": null, "currency": null, "source": "wiki Vampires vs. Werewolves Dance-off; client locale:7366"},
  {"name": "Grey Werewolf Outfit", "price": null, "currency": "station_cash", "source": "wiki Template:News (Game Update 115, 10/15/2013: qualifies as a Werewolf dance-off outfit); price text blank in wiki extract"}
 ],
 "rewards": [
  "A piece of the Pumpkin Prince's special cake for the winning side (articleId=1862, 1878)",
  "Vampire Cake Slice (Vampire win) or Werewolf Cake Slice (Werewolf win) per the wiki Super Spooktacular line"
 ],
 "evidence": [
  {"claim": "Client announcement: 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!'", "source": "locale:5197 (re-checked)"},
  {"claim": "Client text 'Join Team Vampire' exists (re-checked)", "source": "locale:5102484"},
  {"claim": "Dance-off run as part of the Spooktacular event, judged by the Pumpkin Prince; Madame Zelda starts it in Blackspore; side with most fans wins special cake", "source": "http://www.freerealms.com/article/detail.action?articleId=1862"},
  {"claim": "Vampires and Werewolves compete in a Dance Off for the Pumpkin Prince near Bone Bog Cemetery during the second annual Super Spooktacular (undated post)", "source": "http://www.freerealms.com/article/detail.action?articleId=1854"},
  {"claim": "Super Spooktacular ran Oct 13 - Nov 23, 2011; same post describes the Dance Off for the Pumpkin Prince near Bone Bog Cemetery", "source": "http://www.freerealms.com/article/detail.action?articleId=2304"},
  {"claim": "Dance-off site is just outside the gates of Bone Bog Cemetery, hosted by the Pumpkin Prince", "source": "wiki Blackspore Swamp (re-checked)"},
  {"claim": "Dance-off is a sub-event of the Super Spooktacular questline (Madame Zelda hosts the quest)", "source": "wiki Super Spooktacular (re-checked)"},
  {"claim": "Fourth Annual Super Spooktacular ran Oct 1 - Nov 12, 2013", "source": "http://www.freerealms.com/article/detail.action?articleId=2949 (summary, pack-supplied)"}
 ],
 "confidence": 0.55,
 "open": [
  "Parent event: this is a sub-event of Super Spooktacular (articleId=1862 'part of the Spooktacular event'; wiki Super Spooktacular). Schedule it as a window inside the holiday run, not as an independent yearly event.",
  "Occurrences: only 2011 (articleId=2304) and 2013 (wiki Template:News, plus holiday run dates from articleId=2949) are supported. The 2010 occurrence was dropped: it rested only on the undated articleId=1854 'second annual' wording and gave no month. 2009 has no dance-off mention in the sources (articleId=476; tentonhammer node/75739). 2012 was not checked.",
  "Recurring: not confirmed. Two observed years (2011, 2013) with a gap year unchecked do not establish a yearly rule, so recurring is null.",
  "Wireable: no source gives the dance-off's own dates in any year, so the calendar can only hold the holiday window (2011: Oct 13 - Nov 23; 2013: Oct 1 - Nov 12).",
  "Pumpkin King vs Pumpkin Prince: articleId=1862, 1866, 1867 say 'Pumpkin King'; 1854, 1878, 2304, the wiki and the client say 'Pumpkin Prince'. The single-source identity claim (articleId=1867, 'Rey Calabaza') was removed from aliases and stays unresolved.",
  "Zelda location conflict: Blackspore (articleId=1854, 1862, 1878; wiki) vs Shadowmoor/Esporaumbria (articleId=1866, 1867). Blackspore is better supported. The Boneyard direction conflict inside articleId=1878 is also unresolved.",
  "Cake reward mapping per team comes only from the wiki Super Spooktacular line; the articles say only 'a piece of the special cake'.",
  "Quest title 'Join Team Vampire' is tied to the dance only by objective text; the Werewolf-side quest title was not found.",
  "Werewolf Outfit (locale:14690), Team Werewolf T-Shirt (locale:14694), Werewolf Tail (locale:7365) not verified. Team Vampire Bundle (locale:432410) is not tied to the contest by a source. Boy/Girl Team Werewolf and Team Vampire Marketplace outfits named in articleId=2304 do not match checked client names and are not listed.",
  "Grey Werewolf Outfit is a 2013 change, not a 2011 item; price is unknown.",
  "The 2009 LIMITED EDITION Werewolf Outfit has no source tying it to the dance-off and is not listed.",
  "'Vampires vs. Werewolves Costume Party' (locale:14564) may be a separate event; not merged.",
  "Articles 1854-1878 carry no dates in the pack; their years are unfixed. Wiki Category:Super Spooktacular was only partly checked.",
  "The 'Pumpkin King dance contest' alias is removed. The pack's own 'Shadowbrook' summary conflicts with the 1866 fact text and was not used."
 ]
}
```
