<!-- fleet job=event-infer id=vbirthday-party-locations-v8 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8911, 10707, 6, 3443] model=claude-haiku-5-5 -->
# Birthday party locations

{"event": {"name": "Free Realms Birthday Bash (anniversary party)", "aliases": ["Birthday Bash", "Die Free Realms Geburtstagsfeier! (German article title, articleId 1268)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "First anniversary party; ran until May 10, 2010 (start not printed; article date 2010-04-22 is inferred from capture)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268 (summary; end date not quoted)"},
  {"year": 2011, "when": "Second anniversary (anniversary stated as April 28); ran until May 18 per summary. Start inferred from capture 2011-04-30", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (summary only)"},
  {"year": 2012, "when": "Third anniversary Birthday Bash; ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (fact:event quote: 'The Birthday Bash runs through May 24, 2012')"},
  {"year": 2013, "when": "4th birthday, April 29, 2013 (per pack summary; not re-opened)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (summary only)"}
 ],
 "recurring": "Observed in four years in the articles (2010-2013), each around the late-April anniversary and running into May. Not verified for 2014 or later. No fixed schedule is asserted.",
 "zones": ["Sanctuary (2012 cake bake-off storyline and Camellia start point, locale:707)", "Sacred Grove (2012 chefs competing, locale:707)", "2010 party zones per articleId 1268 summary: Jubeltal, Sanddorf, Schneehügel, Schleierwiese, Wugachug, Pfifferdorf, Dornenwald, Freistätte (summary list, not quoted)"],
 "npcs": ["Camellia (starts the 2012 quests, locale:707)", "Queen Valerian (2012 bake-off, articleId 2580 summary)", "Cakenstein / Kuchenstein (boss; locale:4948, 4949)", "Cakelings (minions; locale:4732)"],
 "quests": [],
 "activities": ["Speak to Camellia to start the birthday cake competition (2012, locale:707)", "Stop Cakenstein and the cakelings (locale:707, 4949)", "Defeat the cakelings before they get stronger (locale:4732)", "Invite someone to the birthday bash (locale:4952)", "Dance with the Ambassadors at the Sanctuary Birthday Bash area (2013, articleId 2924 summary)"],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350 Station Cash", "currency": "station_cash", "source": "locale:691, locale:692 (client text names the Bash and gives the price)"},
  {"name": "Free Realms Birthday T-Shirt", "price": null, "currency": null, "source": "locale:5721 (names Free Realms birthday; no event tie or price)"},
  {"name": "Birthday Party Crate", "price": null, "currency": null, "source": "locale:5664 (party supplies; not tied to a dated Bash)"}
 ],
 "rewards": ["Birthday Cake hat exists (locale:694); how it was obtained is not sourced"],
 "evidence": [
  {"claim": "The 2012 Birthday Bash was Free Realms' third-anniversary celebration and ran through May 24, 2012.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.", "source": "locale:695"},
  {"claim": "In 2012, Sacred Grove chefs competed in a birthday cake competition; Camellia near the great tree in Sanctuary starts it; Cakenstein and cakelings must be stopped.", "source": "locale:707"},
  {"claim": "Cakenstein is the boss of the Bash; cakelings are his minions.", "source": "locale:4948, locale:4949, locale:4732"},
  {"claim": "The 2010 party ran until May 10, 2010 (summary).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268 (summary)"},
  {"claim": "The 2011 party was the second anniversary, running until May 18 (summary).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (summary)"}
 ],
 "confidence": 0.5,
 "open": [
  "Anniversary date conflict: articleId 2099 summary says April 28; articleId 1268 and 2924 (and the wiki) say April 29. Unresolved; do not generalise one date.",
  "2010 start date not printed; 2010-04-22 is inferred from capture. End (May 10) is from summary only.",
  "2011 start and May 18 end are from the pack summary of articleId 2099; no quote. The eight-cake collection reward is removed (no quote).",
  "Birthday Cake hat: the 'free for logging in' claim is removed. articleId 2580 was not verified for it. Only the client item exists (locale:694).",
  "Camellia meeting-point quote 'Treffe dich mit Camellia, um loszulegen.' could not be confirmed in either article 1268 or 2099; removed from evidence.",
  "Quest titles: 'Free Realms Turns Three!' (locale:706) was not confirmed in this pass; the quest list is empty until its title is checked. 'Undelivered Confections' removed (no year, weak tie).",
  "Cakenstein Attacks! (locale:4917), Birthday Bash! (locale:29341), Cakenstein has risen (locale:6707-6713) are excluded: tied by name only or undated.",
  "Birthday Bash bed/chair/sofa/table/sconce items (locale:436980-436983, 666) are not tied to a sourced sale; excluded except the furniture bundle named with the Bash.",
  "locale:428192 is a flagged dev_note and is not used as evidence.",
  "Wiki says Cakenstein appears only in 'the only Bash', which conflicts with the annual articles; articles treated as authoritative.",
  "Pack mixes years and the title 'Birthday party locations' is not an event name; not used as an alias. The German title is used as an alias only.",
  "2014 and later not verified. Furniture bundle price is from client text, not a dated sale article."
 ]}
