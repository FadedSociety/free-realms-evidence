<!-- fleet job=event-infer id=vcake-fights-v7 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[9023, 9840, 6, 4299] model=claude-haiku-5-5 -->
# Cake fights

{"event": {"name": "Free Realms Birthday Celebration (Birthday Bash)", "aliases": ["Birthday Bash", "birthday party", "anniversary celebration", "1st/2nd/3rd/4th birthday party"]},
"kind": "holiday",
"live": "yes",
"occurrences": [
 {"year": 2010, "when": "Party ran from the posting day until May 10, 2010 (start date of posting not confirmed by the summary I could re-read; the anniversary date April 28/29, 2010 is not confirmed)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 (run to May 10, 2010, from posting day); articleId=1330 (ends May 10, 2010)"},
 {"year": 2011, "when": "Anniversary April 28, 2011; party to May 18, 2011 (start approximate)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099; http://www.freerealms.com/article/detail.action?articleId=2107; articleId=2106"},
 {"year": 2012, "when": "April 28, 2012 (login Birthday Cake hat; Station Cash tripled on 4/28/2012) through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; articleId=2578"},
 {"year": 2013, "when": "4th birthday April 29, 2013 (start only; end not in pack)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"}
],
"recurring": "Annual, anchored on the late-April anniversary (April 28-29) and running into May. Dated occurrences: 2010, 2011, 2012, 2013. Window end varies (May 10, May 18, May 24). Wiki Events lists Birthday Bash as an annual event (wiki:Events).",
"zones": ["Sanctuary"],
"npcs": ["Camellia (Sanctuary; articleId=1267, 2107)", "Queen Valerian, Sanctuary (articleId=2580)", "Cakenstein (wiki:Cakenstein; locale:9043; articleId=2099, 1267)", "Cakelings, Cakenstein's minions (articleId=2099; locale:428041)", "Chef Jarvie (articleId=1293; locale:428045)", "Glerga (articleId=1293; locale:428065)"],
"quests": ["Cakenstein Attacks! (locale:4917)", "Defeat Cakenstein! (locale:4948)", "Glerga's Birthday Cake (locale:5170; articleId=1293; 2010 run only per article)"],
"activities": ["Daily party-prep quests from Camellia and Sanctuary residents, plus subscriber-only party quests (articleId=2106, 2107)", "Fight Cakenstein and its cakelings (articleId=2099, 1267; wiki:Cakenstein)", "Log in during the Bash for a free Birthday Cake hat (articleId=2580, 2578)", "Dance and socialize at the Birthday Bash area in Sanctuary (articleId=2924)", "Community Team party with cake handouts (articleId=1197)"],
"items": [
 {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:14419 (collect the area cakes for a free Boss Birthday Cake); articleId=2107, 2106"},
 {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "articleId=2580; articleId=2578"},
 {"name": "Balloon Bow", "price": null, "currency": null, "source": "locale:6792 ('Must own the Balloon Bow from the Cakenstein Attacks! combat encounter to buy'); locale:17871"},
 {"name": "Balloon Wand", "price": null, "currency": null, "source": "locale:6797 ('Must own the Balloon Wand from the Cakenstein Attacks! combat encounter to buy')"},
 {"name": "Birthday Crates (party supplies)", "price": null, "currency": null, "source": "articleId=2106; articleId=1261"},
 {"name": "Birthday Bash Marketplace furniture (Wall Sconce, Chair, Floor Lamp, Dining Table, Bed)", "price": null, "currency": null, "source": "wiki:Template:News/Archive (April 24, 2012 Marketplace update)"}
],
"rewards": ["Balloon weapons from Cakenstein Attacks! (locale:6792, 6797; Bow and Wand confirmed; others per locale:6793-6796 unverified)", "Different t-shirt per party area and illusions (articleId=2106)", "Birthday Cake Hat (articleId=2580, 2578)", "Boss Birthday Cake for collecting the area cakes (locale:14419)"],
"evidence": [
 {"claim": "The first-anniversary party ran from the posting day to May 10, 2010, with party areas, Camellia's birthday quests in Sanctuary, and party items for sale.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
 {"claim": "A 2010-04-02 pre-launch repost said large-scale cake fights would come soon and that the anniversary celebration would be April 28, 2010. This is a plan, not a confirmed live run.", "source": "http://www.tentonhammer.com:80/node/83041"},
 {"claim": "The 2011 second-anniversary party ran to May 18, 2011 with party zones, quests, items and the Cakenstein/Kuchenstein fight.", "source": "articleId=2099; articleId=2107; articleId=2106"},
 {"claim": "The 2012 Birthday Bash ran through May 24, 2012; logging in gave a Birthday Cake hat; Station Cash was tripled on 4/28/2012.", "source": "articleId=2580; articleId=2578"},
 {"claim": "Free Realms celebrated its 4th birthday on April 29, 2013 with dancing at the Birthday Bash area in Sanctuary.", "source": "articleId=2924"},
 {"claim": "Balloon Bow and Balloon Wand can be bought only after owning them from the Cakenstein Attacks! encounter.", "source": "locale:6792; locale:6797"},
 {"claim": "Cakenstein is the boss; the quest titles 'Cakenstein Attacks!' and 'Defeat Cakenstein!' exist in the client.", "source": "locale:9043; locale:4917; locale:4948; wiki:Cakenstein"}
],
"confidence": 0.5,
"open": [
 "Name merge: 'Cake fights' (the pack's title) is a feature of the anniversary Bash, not a separate event. The 2010 tentonhammer 83041 item is a pre-launch plan.",
 "Zones: the eight party-area zones are not confirmed. The critique's list (Joyful Vale, Criqueville, Snow Hill, Misty Glade, Wugachug, Blackspore, Heather Moor, Sanctuary) is not visible in the articleId=1267 summary I re-read, so it is not used. Only Sanctuary is confirmed. Happy Valley, Robgoblin Camp and Sacred Grove are removed: no source ties them to the party as a zone. Sacred Grove (locale:707) is a separate cake-competition reference.",
 "2010 anniversary date: articleId=1267 is recorded as running from the posting day to May 10, 2010. The critique says the article gives April 29, 2010 as the anniversary, but my re-read did not show that, so it is not used. The April 28, 2010 plan from tentonhammer 83041 is only a plan. 2010 start remains unconfirmed.",
 "2011 start is approximate (inferred from a 2011-04-30 capture). The 2012 end (May 24) comes from the articleId=2580 summary only. 2013 end date is not in the pack.",
 "Cakenstein conflict: wiki:Cakenstein says he appears 'during the only Birthday Bash and in Treasure War', which conflicts with the yearly boss in 2011-2012. The 'only' wording is not reliable and the Treasure War appearance is unexplained.",
 "Roaming Cakenstein: client strings (locale 38764221, 105084494) describe Cakenstein terrorizing Merry Vale, Seaside, Wugachug, Snowhill, Shrouded Glade, Briarwood and Blackspore. This looks like a separate roaming world event and is not counted as a Bash occurrence until a source ties it to the April-May window.",
 "Cake count: the eight-cake Boss Birthday Cake reward (locale:14419) is not reconciled with a seven-Mystery-Meat-cake Glerga storyline in the pack (articles/articles.json:21124, undated). It is treated as a separate, undated feature and not folded into the yearly Bash. Eight zone cakes are not named or priced in evidence.",
 "Balloon weapons: Bow (locale:6792) and Wand (locale:6797) are confirmed; Hammer, Saw, Sword and Axe are not re-verified here.",
 "Recurrence anchor: wiki:Birthday Bash describes an annual April event tied to the April 29, 2009 launch. The 2010-2013 dates above are the source-backed evidence.",
 "Excluded: Cake-Fight Cake (locale 428147) and Cake-Fight Pile Spawner (locale 4852) are name-only matches. Mystery Cake and Shrouded Glade Birthday Cake have no tie to the event. Article 1306 is a separate Gétostein announcement. Queensfields (article 1282) is undated.",
 "Prices and currency for Birthday Crates, the eight zone cakes and the furniture are not in evidence.",
 "Aliases 'Anniversary Bash' and '1st birthday celebration' were removed as guesses. 'Kuchenstein' is the German boss name, not an event alias."
]}
