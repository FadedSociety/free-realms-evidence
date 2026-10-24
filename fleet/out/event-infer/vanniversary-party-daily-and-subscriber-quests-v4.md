<!-- fleet job=event-infer id=vanniversary-party-daily-and-subscriber-quests-v4 status=done turns=2 usd=0.0040 tokens(read,write,in,out)=[10492, 12260, 6, 4757] model=claude-haiku-5-5 -->
# Anniversary party daily and subscriber quests

{"event": {"name": "Free Realms Anniversary Party (Birthday Bash)", "aliases": ["Birthday Bash", "Birthday Bash 2012", "Free Realms anniversary party", "Free Realms birthday party", "Aniversario do FreeRealms"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "First anniversary: anniversary April 29, 2010; party from the announcement until May 10, 2010", "source": "http://www.freerealms.com/article/detail.action?articleId=1261 (ran until May 10th); http://www.freerealms.com/article/detail.action?articleId=1267 (fell on April 29, 2010; party until May 10, 2010)"},
  {"year": 2011, "when": "Second anniversary: anniversary April 28; webcast kickoff on the 28th; party from the post date until May 18, 2011", "source": "http://www.freerealms.com/article/detail.action?articleId=2093 (2nd birthday on 28 April, webcast kickoff); http://www.freerealms.com:80/article/detail.action?articleId=2099 (ran from post date until May 18); http://www.freerealms.com/article/detail.action?articleId=2107 (until May 18). Year 2011 follows from 'second anniversary' of the April 2009 launch (tentonhammer 67373)"},
  {"year": 2012, "when": "Third anniversary, Birthday Bash 2012: login day April 28, 2012; party through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (ran through May 24, 2012); http://www.freerealms.com/article/detail.action?articleId=2578 (login 4/28/2012); locale:695 ('Birthday Bash 2012 marks the 3rd Anniversary of Free Realms')"},
  {"year": 2013, "when": "Fourth birthday, April 29, 2013; Birthday Bash area in Sanctuary; end date not stated", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (single source; not re-fetched in this pass)"}
 ],
 "recurring": "Yearly around the launch anniversary (April 28 or 29), with the party running into May. Four live editions (2010 to 2013) support this. The day and end date vary by edition, so store per-edition dates rather than one rule.",
 "zones": ["Sanctuary", "Joyful Vale", "Criqueville", "Snow Hill", "Misty Glade", "Wugachug", "Blackspore", "Heather Moor", "Sacred Grove", "Happy Valley"],
 "npcs": ["Camellia (Camilla)", "Queen Valerian", "Chef Jarvie", "Cakenstein (Kuchenstein in German)", "Ambassadors"],
 "quests": ["Birthday Bash!"],
 "activities": ["Daily and subscriber-only party quests from Camellia in Sanctuary (2011, article 2107)", "Collecting zone birthday cakes (2011, article 2107)", "Queen Valerian's cake bake-off in Sanctuary (2012, article 2580)", "Fighting Cakenstein and his cakelings in Sacred Grove (2012, article 2580; 2011, article 2099)", "Log in on 4/28/2012 for the cake hat (article 2578)", "Dancing with the Ambassadors in Sanctuary (2013, article 2924)"],
 "items": [
  {"name": "Birthday Party Crate", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (sold on SC Marketplace per wiki:Birthday Crates, which gives no price); wiki:Birthday Crates"},
  {"name": "Party t-shirts (one per party zone)", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (fact:item: party t-shirts among anniversary gift rewards, a different shirt for each party zone)"},
  {"name": "Birthday Cake (zone cakes)", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (eight zone cakes; currency inferred from wiki:Cake, price not in sources)"},
  {"name": "Birthday Cake hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2578; http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "rewards": ["Party t-shirts, one per party zone (article 2107)", "Birthday Cake hat for logging in 4/28/2012 (article 2578)", "Boss Birthday Cake for buying all eight zone cakes (articles 1261, 2106, 2100, 1267; edition year unknown)", "Station Cash bonus on the 4/28/2012 login day (article 2580)"],
 "evidence": [
  {"claim": "The first anniversary party (2010) ran from the announcement to May 10, 2010, with the anniversary on April 29, 2010.", "source": "http://www.freerealms.com/article/detail.action?articleId=1261; http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "2010 party areas were set up in eight zones: Joyful Vale, Criqueville, Snow Hill, Misty Glade, Wugachug, Blackspore, Heather Moor and Sanctuary.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 (fact:event)"},
  {"claim": "The second anniversary (2011) party ran from the post date until May 18, with the anniversary on April 28.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099; http://www.freerealms.com/article/detail.action?articleId=2107; http://www.freerealms.com/article/detail.action?articleId=2093"},
  {"claim": "2011 party quests were daily and subscriber-only, given by Camellia/Camilla in Sanctuary, and the party sold items on the Marketplace.", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (summary)"},
  {"claim": "2011 boss Kuchenstein (Cakenstein in English) with cakelings; Kuchenstein is the German spelling.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (summary)"},
  {"claim": "The third anniversary was branded Birthday Bash 2012, ran through May 24, 2012, with a Queen Valerian cake bake-off and Cakenstein in Sanctuary/Sacred Grove.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (summary); locale:695"},
  {"claim": "Login on 4/28/2012 gave the Birthday Cake hat.", "source": "http://www.freerealms.com/article/detail.action?articleId=2578"},
  {"claim": "The fourth birthday (April 29, 2013) had a Birthday Bash area in Sanctuary with Ambassadors. Single source.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
  {"claim": "Party t-shirts are one per party zone.", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (fact:item)"},
  {"claim": "Quest 'Birthday Bash!' matches the event by name only.", "source": "locale:29341 (quest_title)"},
  {"claim": "Cakenstein is a boss who fights in Sacred Grove; 'Defeat Cakenstein!' is a client quest line. Edition year not given by the locale.", "source": "locale:4949; locale:4918; http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "confidence": 0.6,
 "open": [
  "Aliases: 'Birthday Bash' is named for 2012 (locale:695). Applying it to 2010 and 2011 is an umbrella use. Store the name per edition.",
  "Dates vary by edition: 2010 Apr 29 to May 10; 2011 Apr 28 to May 18 (year inferred from 'second anniversary'); 2012 Apr 28 to May 24; 2013 Apr 29, end not stated. 2010 announcement dates vs. tentonhammer 83041 (April 28) conflict and are not resolved.",
  "The pack's zone list (Shrouded Glade, Seaside, Snowhill, Merry Vale) does not match article 1267's 2010 list (Joyful Vale, Criqueville, etc.). The 2011 zone list is not in the pack. Treat the zone list as edition-specific.",
  "2013 rests on article 2924 alone and was not re-fetched.",
  "Quests: only 'Birthday Bash!' (locale:29341) is named, by name only. The daily and subscriber quest titles from article 2107 are not given in any source. 2010 quest titles are not confirmed.",
  "Balloon weapons and illusions (named only in the pack summary of article 2107) are NOT claimed.",
  "Prices for the Birthday Party Crate and zone cakes are not in any source. The Station Cash currency for cakes is inferred from the wiki.",
  "Furniture items (Birthday Bash Bed, Chair, Sofa, Dining Table, locale 436980-436983) and the ability locale 428377 are unresolved and not included.",
  "Not included as this event: Celebrate Waldo's 25th Anniversary (locale:9144), Mystic Mayhem 3rd anniversary, Super Spooktacular 2nd anniversary (article 1870), Walmart 50th anniversary. Possibly separate: Summer Splash (locale:19968), Birthday Hide and Seek (locale:6540), Glerga's Birthday Cake (locale:5170), Blue and Orange Silly String (locale:14574, 14575).",
  "Locale ids 5664, 5666 (Birthday Party Crate placement text) were not re-confirmed in this pass; the crate claim rests on article 2106 and wiki:Birthday Crates.",
  "The pack title ('Anniversary party daily and subscriber quests') describes the 2011 edition only, so the pack merges editions. Treated here as one series with per-edition entries."
 ]}
