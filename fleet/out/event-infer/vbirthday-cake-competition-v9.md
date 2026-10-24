<!-- fleet job=event-infer id=vbirthday-cake-competition-v9 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8652, 9134, 6, 3715] model=claude-haiku-5-5 -->
# Birthday cake competition

{
 "event": {
  "name": "Free Realms Anniversary Birthday Bash",
  "aliases": ["Birthday Bash", "Birthday Bash 2012 (3rd anniversary)", "Birthday Bash 2013 (4th birthday)", "Birthday cake competition (sub-activity: Sacred Grove chefs' cake bake-off)"]
 },
 "kind": "holiday",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "3rd-anniversary Birthday Bash; ran through May 24, 2012 (start date not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695 ('Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.')"},
  {"year": 2013, "when": "4th birthday, announced for April 29, 2013; Birthday Bash area in Sanctuary (run end not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=2924"}
 ],
 "recurring": null,
 "zones": ["Sanctuary", "Sacred Grove"],
 "npcs": ["Camellia (locale:707: speak to her near the great tree in Sanctuary to start the cake competition)", "Queen Valerian (article 2580: hosted the cake bake-off in Sanctuary; conflicts with locale:707, unreconciled)", "Cakenstein (locale:4949; article 2580)", "Ambassadors (article 2924)"],
 "quests": ["Birthday Bash!"],
 "activities": [
  "Help Camellia with Sacred Grove's top chefs' birthday cake competition: speak to chefs, sponsor one, return to Camellia (locale:707, Birthday Bash 2012)",
  "Stop Cakenstein and the cakelings from ruining the cakes (locale:707; article 2580)",
  "Collect the eight area-themed birthday cakes (locale:14419)",
  "Dance and socialise at the Birthday Bash area in Sanctuary (article 2924, 2013)"
 ],
 "items": [
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "locale:694 (name); locale:707 ('All characters who log in during Birthday Bash 2012 will receive a free Birthday Cake Hat!')"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:14419 ('Collect all eight area-themed birthday cakes and get the Boss Birthday Cake FREE!'); year not stated"}
 ],
 "rewards": [
  "Birthday Cake Hat, free to characters who logged in during Birthday Bash 2012 (locale:707, locale:694)",
  "Boss Birthday Cake, free for collecting all eight area cakes (locale:14419; year not stated)"
 ],
 "evidence": [
  {"claim": "Birthday Bash 2012 was the 3rd anniversary of Free Realms", "source": "locale:695; http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "2012 Bash ran through May 24, 2012 (start not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Sacred Grove's top chefs hold a birthday cake competition; player helps Camellia; Cakenstein and cakelings threaten the cakes; login hat for Bash 2012", "source": "locale:707"},
  {"claim": "2013 4th birthday announced for April 29, 2013 with a Birthday Bash area in Sanctuary", "source": "http://www.freerealms.com/article/detail.action?articleId=2924"},
  {"claim": "Birthday Bash tagged to a 2013 blog post dated April 29, 2013", "source": "wiki: User blog:Soe amnerys/Happy 4th Birthday, Free Realms! (Category:Birthday Bash)"},
  {"claim": "Eight area cakes collected gives a free Boss Birthday Cake", "source": "locale:14419"}
 ],
 "confidence": 0.5,
 "open": [
  "Identity: the cake bake-off is one activity inside the Birthday Bash, not a separate event. The French guide (article 1300, Arbitre Ruby, undated) describes a first-anniversary party with the same cake contest, invitations, balloons, and Gâtostein quests. Its year is unconfirmed (probably ~2010, per its 'first-anniversary' wording). Not listed as an occurrence. Its activities are attributed to that party only, not to 2012 or 2013.",
  "2010 and 2011: not confirmed. Articles 1330 and 2107 were not retrieved. The May 10, 2010 end date has no source and is dropped.",
  "Recurrence: not established. Wiki Category:Birthday Bash Weapons says the event is active around April 29 each year, but only 2012 and 2013 are dated, and the pack's article 2107 summary says April 28 (unretrieved). Set to null until resolved.",
  "live = unsure: latest dated run is 2013 (article 2924). No source covers 2014 or later, and run end dates for 2012 and 2013 are unknown. Not wireable until a run window is confirmed.",
  "NPC conflict: locale:707 names Camellia as the cake-contest starter; article 2580 names Queen Valerian as the bake-off host. Both kept, unreconciled.",
  "Quests: the wiki Camellia page lists 'A Piece of Cake', 'Undelivered Confections' and a bracketed '[Birthday] Cake Bake-off' (likely 'Birthday Cake Bake-off'), but these were not checked against a retrieved source this pass, so they are not listed as quests. 'Birthday Bash!' (locale:29341) is a client quest_title; its storyline role is unconfirmed.",
  "Items with no year: wiki Birthday T-shirts (Sanctuary, Seaside, Briarwood, Wugachug, Snowhill, Blackspore Swamp, Merry Vale, Shrouded Glade, Free Realms), Cupcake pet pal, and furniture (Birthday Bash Bed/Chair/Sofa/Dining Table/Floor Lamp/Wall Sconce, locale:436980-437014, 666). Each is tied to the Bash by wiki category or name only, with no run year, so they are not placed in 2012 or 2013. Furniture Bundle price 1350 station_cash (locale:692) was not re-read and is not used.",
  "Dropped: 'Birthday cake samples' (locale:17803-17810, placeholder-flagged, no Bash tie). Also not counted: Birthday Cake (427853), Big Birthday Cake (428028), Birthday Cake Samples (9391), Birthday Party Crate (video C3fysVLxrMg), Cakenstein Attacks! (locale:4917).",
  "Aliases: 'Anniversary Bash' and 'Birthday Bash 2013' as a separate alias are unsourced and removed as aliases; they are only descriptive.",
  "Zone list is incomplete. The eight-zone claim comes from unretrieved article 2107."
 ]
}
