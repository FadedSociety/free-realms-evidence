<!-- fleet job=event-infer id=vbirthday-party-locations-v7 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[9272, 10822, 6, 3967] model=claude-haiku-5-5 -->
# Birthday party locations

{"event": {"name": "Free Realms Birthday Bash (anniversary party)", "aliases": ["Geburtstagsfeier (official German name for the anniversary party)", "Birthday Bash"]},
"kind": "holiday",
"live": "yes",
"occurrences": [
 {"year": 2010, "when": "First anniversary party, running from the launch-day kickoff until May 10, 2010. Start day not printed in the article; the pack's date field 2010-04-22 is inferred from page capture.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268"},
 {"year": 2011, "when": "Second anniversary (anniversary April 28); post date not printed, capture dated 2011-04-30. The May 18 end comes from the pack summary only.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099"},
 {"year": 2012, "when": "Third anniversary (Birthday Bash 2012), ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
 {"year": 2013, "when": "April 29, 2013 (4th birthday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"}
],
"recurring": "Observed in 2010, 2011, 2012 and 2013, each around the April 28-29 anniversary, running into May. 2014 and later not verified. Do not generate a fixed yearly schedule beyond these four dated occurrences.",
"zones": [
 "2010: Jubeltal, Sanddorf, Schneehügel, Schleierwiese, Wugachug, Pfifferdorf, Dornenwald, Freistätte (articleId 1268)",
 "2011: party zones described in articleId 2099 (list not re-verified; the same eight appear in its summary)",
 "2012: Sanctuary, Sacred Grove (articleId 2580; locale:707)",
 "2013: Sanctuary Birthday Bash area (articleId 2924)"
],
"npcs": [
 "Camellia (party planner; starts the birthday quests; articleId 1268 and articleId 2099)",
 "Queen Valerian (2012 cake bake-off, articleId 2580)",
 "Cakenstein / Kuchenstein (boss; locale:428041)",
 "Cakeling (minions; locale:428041)",
 "the Ambassadors (2013 dance area, articleId 2924)"
],
"quests": [
 "Free Realms Turns Three! (locale:706; locale:707 says to speak to Camellia near the great tree in Sanctuary to start the birthday cake competition and to stop Cakenstein and the cakelings; 2012)",
 "Undelivered Confections (locale:428042; wiki Camellia; year not assigned)"
],
"activities": [
 "Start birthday quests by speaking to Camellia",
 "Compete in the birthday cake competition for Queen Valerian (2012)",
 "Defeat cakelings and Cakenstein",
 "Dance at the Birthday Bash area in Sanctuary (2013)",
 "Decorate with Birthday Bash furniture (video GTCg4dg9O-Y/00190.jpg; not dated)"
],
"items": [
 {"name": "Birthday Cake hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (free for logging in during the 2012 Bash; article not re-opened in this pass)"}
],
"rewards": [
 "Birthday Cake hat (2012, for logging in during the Bash)",
 "Eight-cake collection reward (2011; pack summary of articleId 2099 only, no quote found)"
],
"evidence": [
 {"claim": "The 2010 anniversary party ran from the launch-day kickoff until May 10, 2010, with party zones, new quests, party items, cakes and a Cakenstein boss fight.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268 (summary)"},
 {"claim": "The 2010 party zones were Jubeltal, Sanddorf, Schneehügel, Schleierwiese, Wugachug, Pfifferdorf, Dornenwald and Freistätte.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268"},
 {"claim": "Players start the birthday party by meeting Camellia, who is near the big tree in Freistätte (Sanctuary). Quote: 'Treffe dich mit Camellia, um loszulegen.'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268 (fact:npc); articleId 2099 (fact:event)"},
 {"claim": "The 2011 post announces the second-anniversary party (anniversary April 28) with party zones, birthday quests, a Kuchenstein boss and cakelings.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (summary)"},
 {"claim": "Birthday Bash 2012 marks the 3rd Anniversary of Free Realms; quests 'Free Realms Turns Three!' start with Camellia near the great tree in Sanctuary.", "source": "locale:695, locale:706, locale:707"},
 {"claim": "The 2012 Bash ran through May 24, 2012, and logging in gave a Birthday Cake hat.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (not re-opened)"},
 {"claim": "The 2013 4th birthday on April 29 invited players to the Birthday Bash area in Sanctuary to dance with the Ambassadors; no rewards listed.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
 {"claim": "Cakenstein (Kuchenstein) is the boss and Cakelings are his minions.", "source": "locale:428041; wiki Cakeling"}
],
"confidence": 0.6,
"open": [
 "Date conflict: articleId 2099 implies April 28 as the anniversary; articleId 1268, 2924 and the wiki say April 29. Unresolved.",
 "2010 start day not printed. The pack's date field 2010-04-22 is inferred from capture, not printed in the article. Only the May 10, 2010 end is stated, from the articleId 1268 summary (the earlier answer cited articleId 1267; that was a citation error).",
 "2011 year is inferred from the capture date. The May 18 end and eight-cake reward have no quote; the pack summary is the only source.",
 "The 2012 May 24 end and Birthday Cake hat reward cite articleId 2580, which was not re-opened in this pass.",
 "Cakenstein Attacks! (locale:4917) is a combat encounter; the balloon weapon items (locale:6792-6797) say they come from it. Its tie to the birthday party is by name only, so it is excluded from the quest list. Locale 6707-6713 ('Cakenstein has risen' in several zones) is a separate Cakenstein feature with no year, also excluded.",
 "Birthday Bash! (locale:29341) is tied by name only; excluded from the quest list. Invite someone to the birthday bash! (locale:4952) is also name-only.",
 "Furniture Bundle (locale:691, 1350 Station Cash), Birthday T-shirts, Birthday Bash Bed/Chair/Sofa/Dining Table/Wall Sconce (locale:436980-436983, locale:666), and Cakeling pet pal have no source tying them to a Bash sale or date. Excluded from items. The 2012 marketplace wiki entries suggest a 2012 sale but this is unconfirmed.",
 "Wiki says Cakenstein appears only during 'the only Bash', which conflicts with the annual articles. Articles treated as authoritative.",
 "Birthday Party Crate: currency and contents not confirmed; excluded.",
 "Excluded as not tied to the event: Chocolate Cupcake (locale:5037), Cupcake Hat (locale:5167), Big Birthday Cake (locale:4947). Cakenstein dev-note tiers (locale:428192, flagged dev_note; 428764, 428766) are internal, not event facts.",
 "NPC names Flitter, Quills, Helga and Bud Grimyfoot are not confirmed and are omitted.",
 "Wiki-only quest names 'Cake-Eating Cakelings', 'A Piece of Cake' and 'Birthday Cake Bake-off' have no client title; excluded.",
 "Pack merges years and may miss an alias. The pack title 'Birthday party locations' is not an official event name and is not used as an alias.",
 "2014 and later not verified. No event item has a sourced price."
]}
