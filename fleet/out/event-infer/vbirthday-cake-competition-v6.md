<!-- fleet job=event-infer id=vbirthday-cake-competition-v6 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[9813, 11918, 6, 4130] model=claude-haiku-5-5 -->
# Birthday cake competition

{"event": {"name": "Birthday Bash", "aliases": ["Free Realms Birthday Bash", "Anniversary Bash", "Birthday Bash 2012 (3rd anniversary)", "Birthday cake competition (cake bake-off sub-activity, not a separate event)"]},
 "kind": "holiday",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "3rd-anniversary Birthday Bash; ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (summary: 'which ran through May 24, 2012'); locale:695 ('Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.')"},
  {"year": 2010, "when": "1st-anniversary party; pack quotes an end date of May 10, 2010 (start and posting date not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=1330 (pack quote only, not re-retrieved; unverified)"},
  {"year": 2011, "when": "2nd-anniversary party; pack summary says it ran from the posting date to May 18 (year inferred from numbering)", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (pack summary only, not re-retrieved; unverified)"}
 ],
 "recurring": "Annual, held in April around the launch anniversary and running into May, per the wiki Events page ('an annual event held throughout the month of April in celebration of launch day ... April 29th, 2009') and the wiki Birthday Bash page ('annual event'). Only 2012 is re-verified against an article; 2010 and 2011 rest on the pack and are unverified.",
 "zones": ["Sanctuary (Camellia near the great tree, locale:707)", "Sacred Grove (chef contest, locale:707; Cakelings appear throughout Sacred Grove per wiki Cakeling page)"],
 "npcs": ["Camellia (locale:707)", "Cakenstein (wiki Cakenstein page: main antagonist of the Birthday Bash)", "Cakelings (wiki Cakeling page)", "Queen Valerian (article 2580 summary: leads the cake bake-off storyline)"],
 "quests": [],
 "activities": [
  "Help Camellia run the birthday cake competition: speak to Sacred Grove chefs, sponsor one, return to Camellia (locale:707; article 1300 summary)",
  "Stop Cakenstein and the cakelings from ruining the Bash (locale:707)",
  "Find one of each balloon by trading to complete a balloon bundle for Quills in Sanctuary (locale:428078)",
  "Fight Cakenstein in Cakenstein Attacks! for the prize wheel (wiki Balloon Axe page)",
  "Log in during Birthday Bash 2012 to receive the Birthday Cake Hat (locale:707)"
 ],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350", "currency": "station_cash", "source": "locale:692 ('Get it now for only 1350 Station Cash. That's a 250 Station Cash savings!'); name per locale:691"},
  {"name": "Birthday Bash Wall Sconce", "price": null, "currency": null, "source": "locale:666; wiki Update of April 24, 2012 lists it under Marketplace Bash items"},
  {"name": "Birthday Bash Floor Lamp", "price": null, "currency": null, "source": "locale:437014; wiki Update of April 24, 2012 lists it under Marketplace Bash items"},
  {"name": "Birthday Bash Chair / Dining Table / Bed", "price": null, "currency": null, "source": "wiki Update of April 24, 2012 (Marketplace Bash items)"},
  {"name": "Box of Birthday Invitations", "price": null, "currency": null, "source": "locale:428668 (name only; tie to the Bash is by the Invitation item naming, not a quoted sentence)"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:14419 ('Collect all eight area-themed birthday cakes and get the Boss Birthday Cake FREE!')"},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "locale:707 ('All characters who log in during Birthday Bash 2012 will receive a free Birthday Cake Hat!')"}
 ],
 "rewards": ["Boss Birthday Cake (free for collecting all eight area-themed birthday cakes; locale:14419)", "Birthday Cake Hat (free for logging in during Birthday Bash 2012; locale:707)"],
 "evidence": [
  {"claim": "The 2012 Birthday Bash was the 3rd anniversary of Free Realms", "source": "locale:695"},
  {"claim": "Camellia runs a birthday cake competition with Sacred Grove chefs; Cakenstein and cakelings threaten it; Birthday Cake Hat for logging in during Birthday Bash 2012", "source": "locale:707"},
  {"claim": "The 2012 Bash ran through May 24, 2012; cake bake-off storyline led by Queen Valerian; Cakenstein monster", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (summary)"},
  {"claim": "Bash is an annual April event tied to launch day April 29, 2009", "source": "wiki page 'Events' and 'Birthday Bash' (wiki, not an article)"},
  {"claim": "Collecting all eight area-themed birthday cakes awards a free Boss Birthday Cake", "source": "locale:14419"},
  {"claim": "Birthday Bash Furniture Bundle costs 1350 Station Cash, saving 250", "source": "locale:692"},
  {"claim": "Cakenstein is the main antagonist of the Birthday Bash and appears only during it (and Treasure War)", "source": "wiki page 'Cakenstein'"},
  {"claim": "Birthday Bash marketplace furniture was released in the April 24, 2012 update", "source": "wiki Template:News/Archive, Update of April 24, 2012"}
 ],
 "confidence": 0.55,
 "open": [
  "live = unsure: no source shows a run after May 24, 2012. The scheduler must confirm whether the event is live now.",
  "Anniversary date conflict: wiki says launch day April 29, 2009; the pack's articles 2107 and 2580 say April 28. Article 2580 retrieved here does not mention April 28. Treat the anniversary date as unresolved.",
  "2010 and 2011 occurrences: articles 1330 and 2107 were not found in the lookup index. Their dates and the 2011 year are unverified. The 2010 article 1300 (cake contest) is undated.",
  "Event identity: the 'Birthday cake competition' is the cake bake-off sub-activity of the Birthday Bash, not a separate event. Client text (locale:428708, 428710, 428071) refers to the Bash itself.",
  "Quest titles: none verified this pass. 'Birthday Bash!' (locale:29341), 'Undelivered Confections', 'Downing Cakenstein', 'Cakey Madness' and \"Cakenstein's Last Stand\" (locale 428098/428096/428063) were not checked. The balloon quest (locale:428078) has no title.",
  "Zone list is incomplete: the full eight-zone list is not quoted in any retrieved source. The 2011 'eight zones' claim is unverified.",
  "Zone birthday cakes (8) sold on Station Cash marketplace: wiki 'Cake' statement only, not re-verified. Price not stated.",
  "Commandant Kagoul, Glerga, Helga, Papillonnette, Plumette, Arbitre Ruby: article 1300 summary only; not confirmed in client or wiki.",
  "Birthday Invitation item (locale:4951) and locale:4952 ('Invite someone to the birthday bash!') were not re-checked this pass; only 428668 name was seen.",
  "2013 (4th birthday, article 2924, April 29, 2013) was not retrieved and is not counted toward recurrence.",
  "Not included (no source ties them to the Bash): Birthday Cake (427853), Big Birthday Cake (428028), Large Birthday Cake (428031), Birthday Cake Samples (9391), Birthday Party Crate (video C3fysVLxrMg), Cakenstein Attacks! (locale:4917, although the wiki Balloon Axe page names it as the Bash encounter), Birthday T-shirts (no quote ties them to the Bash)."
 ]}
