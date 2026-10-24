<!-- fleet job=event-infer id=vvampires-vs-werewolves-dance-contest-v5 status=done turns=2 usd=0.0040 tokens(read,write,in,out)=[8965, 15246, 6, 3961] model=claude-haiku-5-5 -->
# Vampires vs. Werewolves dance contest

{
 "event": {
  "name": "Vampires vs. Werewolves dance-off",
  "aliases": [
   "Vampires vs Werewolves Dance-off (locale:5197 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!')",
   "Vampire vs Werewolf Dance Off (articles/facts.json, articleId 2304 wording)",
   "Werewolves vs. Vampires Dance Off (wiki file title; not re-checked)"
  ]
 },
 "parent_event": "Super Spooktacular (Halloween holiday run). The dance-off is a sub-event inside the parent's run, not an independent yearly event. Schedule it as a window inside the Super Spooktacular dates.",
 "kind": "contest",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Super Spooktacular ran Oct 13 - Nov 23, 2011 (parent window). The dance-off's own dates are not stated. Contest window: unknown.", "source": "http://www.freerealms.com/article/detail.action?articleId=2304 (summary in articles.json: 'running October 13 to November 23, 2011 ... a Vampires vs. Werewolves Dance-Off')"},
  {"year": 2009, "when": "NOT an occurrence: the 2009 Super Spooktacular (Oct 14 - Nov 11, 2009) sources do not mention a dance-off.", "source": "http://www.freerealms.com/article/detail.action?articleId=476 (checked earlier, no mention)"}
 ],
 "recurring": null,
 "zones": [
  "Blackspore (Madame Zelda starts the mission; locale:432293 and fact text)",
  "Bone Bog Cemetery, outside the gates (dance site; articleId 2304 summary, fact 'near the Bone Bog Cemetery')"
 ],
 "npcs": [
  "Madame Zelda (starts the quest in Blackspore)",
  "Pumpkin Prince (judges; client name, locale:432206 'The Pumpkin Prince has offered a special prize')",
  "Pumpkin King (used in articleId 1866/1867 wording; same role, identity not confirmed)"
 ],
 "quests": [
  "Join Team Vampire (locale:5102484 exists; tied to the dance-off only by objective text locale:432314 'Join Team Vampire in the dance-off'; year unknown)"
 ],
 "activities": [
  "Talk to Madame Zelda in Blackspore to start the mission and choose a side (Vampire or Werewolf)",
  "Wear Vampire or Werewolf costume pieces openly (locale:432254 says the outfit is needed for moves to count)",
  "Wait for the in-game announcement that the dance-off is starting (locale:5197)",
  "Go to Bone Bog Cemetery and dance for the Pumpkin Prince; the side with the most fans wins a piece of the special cake"
 ],
 "items": [
  {"name": "Vampire Cake Slice", "price": null, "currency": "reward", "source": "wiki Super Spooktacular reward line (not re-checked this pass); client name locale:6628. Year unknown."},
  {"name": "Werewolf Cake Slice", "price": null, "currency": "reward", "source": "wiki Super Spooktacular reward line (not re-checked this pass); client name locale:7336. Year unknown."},
  {"name": "Vampire Fangs", "price": null, "currency": null, "source": "client locale:7366; wiki Vampires vs. Werewolves Dance-off. Year unknown."},
  {"name": "Team Vampire T-Shirt", "price": null, "currency": null, "source": "client locale:14692; wiki. Year unknown."},
  {"name": "Vampire Outfit", "price": null, "currency": null, "source": "client locale:14688 (Team Vampire items, wiki). Year unknown. locale:432320 says it can be bought from the marketplace."},
  {"name": "Grey Werewolf Outfit", "price": null, "currency": "station_cash", "source": "wiki Template:News, Game Update 115 (10/15/2013). NOT verified this pass. 2013 only, if verified. Price unknown."}
 ],
 "rewards": [
  "A piece of the Pumpkin Prince's special cake for the winning side (articleId 1862, 1878)",
  "Per-team cake mapping (Vampire Cake Slice / Werewolf Cake Slice): wiki Super Spooktacular only; articles say only 'a piece of the special cake'"
 ],
 "evidence": [
  {"claim": "Dance-off named in the 2011 Super Spooktacular (Oct 13 - Nov 23, 2011) news post, which lists a Vampires vs. Werewolves Dance-Off", "source": "http://www.freerealms.com/article/detail.action?articleId=2304"},
  {"claim": "Dance-off is part of the Spooktacular event, judged by the Pumpkin Prince; Madame Zelda starts it in Blackspore; side with most fans wins special cake", "source": "http://www.freerealms.com/article/detail.action?articleId=1862 ; http://www.freerealms.com/article/detail.action?articleId=1878"},
  {"claim": "Dance-off announcement in-game: 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!'", "source": "locale:5197"},
  {"claim": "Dance-off site: near Bone Bog Cemetery (Pumpkin Prince judges; wearing costume)", "source": "http://www.freerealms.com/article/detail.action?articleId=2304 ; locale:432206 and locale:432254"},
  {"claim": "Fourth Annual Super Spooktacular ran Oct 1 - Nov 12, 2013 (parent window only; no dance-off sentence seen)", "source": "http://www.freerealms.com/article/detail.action?articleId=2949 (summary in articles.json)"}
 ],
 "confidence": 0.5,
 "open": [
  "2013 occurrence NOT counted. The only dance-off link for 2013 is a wiki Template:News note (Game Update 115, 10/15/2013) that was not re-checked. The 2013 holiday window (articleId 2949) is confirmed, but it does not mention the dance-off. Add 2013 only after Game Update 115 is confirmed.",
  "Contest's own dates are unknown in every year. Occurrence entries give the parent Super Spooktacular window only.",
  "Recurring: null. Only 2011 is confirmed for the dance-off; 2012 unchecked; 2013 unconfirmed.",
  "Items are not tied to a year, except Grey Werewolf Outfit (2013, unverified). Do not assign the other items to 2011 or 2013.",
  "Team Vampire Bundle (locale:432411: Black Vampire Outfit, Black Bat Pet, Vampire Fangs, Team Vampire T-Shirt) and locale:432252 'put on your favorite vampire outfit' sit near dance-off text, but no source ties this bundle to this event. Left out of items.",
  "Quest 'Join Team Vampire' is tied only by objective text (locale:432314) and has no year. The Werewolf-side quest title was not confirmed; locale:432293 and 432298 are objective texts for 'join Team Werewolf in the dance-off'.",
  "Zelda location conflict: Blackspore (articleId 1854, 1862, 1878; client 432293) vs Shadowmoor/Esporaumbria (articleId 1866, 1867). The 1878 fact says 'just south of the Haunted Mines' with a Boneyard direction conflict; unresolved.",
  "Pumpkin King vs Pumpkin Prince: articleId 1866/1867 say 'Pumpkin King'; the client and 1854/1878/2304 say 'Pumpkin Prince'. Treated as one role; identity unresolved.",
  "Articles 1854-1878 carry no dates in the pack; their years are unfixed.",
  "'Vampires vs. Werewolves Costume Party' (locale:14564) may be a separate event; not merged.",
  "The 2009 Werewolf LIMITED EDITION outfit has no source tying it to the dance-off; not listed.",
  "Pack-supplied 2011 article summary and the 2011 dates were confirmed via the articles index (articles.json), not via a full article body fetch."
 ]
}
