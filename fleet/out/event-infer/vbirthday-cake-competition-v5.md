<!-- fleet job=event-infer id=vbirthday-cake-competition-v5 status=done turns=4 usd=0.0047 tokens(read,write,in,out)=[31275, 11982, 10, 5696] model=claude-haiku-5-5 -->
# Birthday cake competition

```json
{
 "event": {
  "name": "Birthday Bash",
  "aliases": ["Free Realms Birthday Bash", "Anniversary Bash", "Birthday Bash 2012 (3rd anniversary)", "Birthday cake competition (sub-activity: Sacred Grove cake bake-off)"]
 },
 "kind": "holiday",
 "live": "no",
 "occurrences": [
  {"year": 2010, "when": "1st anniversary party; ended May 10, 2010 (posting day not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=1330 (fact: 'se termineront le [10] [mai] [2010]'); articleId=1300 (cake contest, undated capture)"},
  {"year": 2011, "when": "2nd anniversary party, anniversary April 28; started on posting date, scheduled to end May 18 (year 2011 inferred from anniversary numbering, not stated in the summary)", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (summary: 'running from the posting date until May 18 ([anniversary] on [April] [28])')"},
  {"year": 2012, "when": "3rd anniversary Birthday Bash; ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (fact:event: 'ran through [May] [24], [2012]'; summary describes the cake bake-off and Cakenstein); locale:707 ('Sanctuary Free Realms Turns Three!')"}
 ],
 "recurring": "Yearly, tied to the Free Realms anniversary (April 28 per articles 2107 and 2580), running into late May. Three occurrences (2010, 2011, 2012) are sourced; 2011 year is inferred.",
 "zones": ["Sanctuary (Camellia hub; cake contest starts near the great tree; locale:707)", "Sacred Grove (chef contest; locale:707)"],
 "npcs": ["Camellia (locale:707; article 2107)", "Queen Valerian (article 2580 summary: leads the 2012 cake bake-off storyline)", "Cakenstein (boss; locale:428098, 428096, 428063)", "Glerga (undated client quests; article 1300 summary)", "Sal Monella (undated client quests locale:428708, 428710)", "Commandant Kagoul, Helga, Papillonnette, Plumette, Arbitre Ruby (article 1300 summary only)"],
 "quests": ["Birthday Bash!", "Undelivered Confections", "Downing Cakenstein", "Cakey Madness", "Cakenstein's Last Stand"],
 "activities": [
  "Help Camellia run the birthday cake competition: speak to Sacred Grove chefs, sponsor one, return to Camellia; one chef per day (article 1300 fact; locale:707)",
  "Distribute Birthday Invitations (article 1300 summary; locale:4951, 428668)",
  "Collect balloons for a balloon bundle for Quills in Sanctuary (locale:428078)",
  "Gather food ingredients for Helga (article 1300 summary)",
  "Fight Cakenstein and cakelings with fireworks (locale:428098, 428096, 428063, 428042/428043)",
  "Collect the eight area-themed birthday cakes (locale:14419)",
  "Log in during Birthday Bash 2012 for the cake hat (locale:707 / article 2580)"
 ],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350", "currency": "station_cash", "source": "locale:692 ('Get it now for only 1350 Station Cash. That's a 250 Station Cash savings!'); name in locale:691"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:14419 ('Collect all eight area-themed birthday cakes and get the Boss Birthday Cake FREE!'); item name locale:30109"},
  {"name": "Birthday Invitation", "price": null, "currency": null, "source": "locale:4951 ('Birthday Invitation', plural 'Birthday Invitations')"},
  {"name": "Box of Birthday Invitations", "price": null, "currency": null, "source": "locale:428668"},
  {"name": "Birthday Bash Wall Sconce", "price": null, "currency": null, "source": "locale:666 (same Bash furniture set as the bundle; set membership not quoted)"},
  {"name": "Birthday Bash Floor Lamp", "price": null, "currency": null, "source": "locale:437014 (same Bash furniture set; set membership not quoted)"},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "article 2580 / locale:707 (free login reward during Birthday Bash 2012; wording not re-verified in this pass)"},
  {"name": "Zone birthday cakes (8)", "price": null, "currency": "station_cash", "source": "wiki 'Cake' (sold on SC Marketplace during the Bash; not re-verified)"}
 ],
 "rewards": [
  "Boss Birthday Cake (free for collecting all eight area-themed birthday cakes; locale:14419)",
  "Birthday Cake Hat (2012 login; article 2580)",
  "Birthday Bash furniture (Dining Table, Bed, Chair, Sofa per earlier pack, locale:436980-436983; plus Wall Sconce locale:666 and Floor Lamp locale:437014)"
 ],
 "evidence": [
  {"claim": "The Birthday Bash is the anniversary party; the 2010 cake contest was run by Camellia with Sacred Grove chefs, and the player sponsors one chef.", "source": "http://www.freerealms.com/article/detail.action?articleId=1300 (fact:event)"},
  {"claim": "The 2010 party ended May 10, 2010.", "source": "http://www.freerealms.com/article/detail.action?articleId=1330 (fact: 'se termineront le [10] [mai] [2010]')"},
  {"claim": "The 2011 party ran from the posting date until May 18, with the anniversary on April 28.", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (summary)"},
  {"claim": "The 2012 third-anniversary Birthday Bash ran through May 24, 2012; it had a cake bake-off storyline led by Queen Valerian and a Cakenstein monster.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (fact:event and summary)"},
  {"claim": "The 2012 Bash marks Free Realms turning three, and Sanctuary's cake competition starts with Camellia; Cakenstein and cakelings threaten it.", "source": "locale:707 ('Sanctuary Free Realms Turns Three!')"},
  {"claim": "Collecting all eight area-themed birthday cakes gives a free Boss Birthday Cake.", "source": "locale:14419"},
  {"claim": "Birthday Bash Furniture Bundle costs 1350 Station Cash, saving 250.", "source": "locale:692"},
  {"claim": "Birthday Invitation and Box of Birthday Invitations are Bash items.", "source": "locale:4951; locale:428668; locale:4952 ('Invite someone to the birthday bash!')"},
  {"claim": "A balloon-bundle quest for the big birthday bash is in Sanctuary.", "source": "locale:428078"},
  {"claim": "Cakenstein quests use fireworks and cakelings.", "source": "locale:428098 (Downing Cakenstein); locale:428096 (Cakey Madness); locale:428063 (Cakenstein's Last Stand)"},
  {"claim": "Undated client quotes say Glerga will compete in next year's cake bake-off and Sal Monella enters the bake-off for the Birthday Bash. These show the bake-off recurring but do not fix years.", "source": "locale:428071; locale:428708; locale:428710"},
  {"claim": "The 2011 party held events in eight zones.", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (summary: 'eight zone..', list truncated)"},
  {"claim": "The 2013 4th-birthday event (April 29, 2013) had only a Birthday Bash dancing area in Sanctuary.", "source": "http://www.freerealms.com/article/detail.action?articleId=2924 (summary; not re-verified in this pass)"}
 ],
 "confidence": 0.6,
 "open": [
  "Event identity: the pack's name 'Birthday cake competition' is a sub-activity of the Birthday Bash, not a separate event. The client's bake-off quests say 'the Birthday Bash' itself. Keep one event with the cake contest as an activity.",
  "live set to 'no': the Bash ran in the original game 2010-2013 (late April to late May). No source shows a current run. The scheduler should confirm this.",
  "2011 year is inferred from the 1st and 3rd anniversary numbering; no source states the 2011 year directly.",
  "Anniversary date conflict: the wiki and article 2924 say April 29 (2013); articles 2107 and 2580 say April 28. This answer uses April 28 for the anniversary and lists April 29 as the discrepancy.",
  "Posting/start dates for 2010 and 2012 are not stated. Article 1330 was not found in the lookup index; the 2010 end date rests on the quote in the pack.",
  "2013: article 2924 was not matched in the lookup index; the 2013 occurrence rests on the pack summary only and is not counted toward recurrence.",
  "Eight zones: the full zone list is not quoted in any source. Locale:6707-6713 (Cakenstein zones, not re-checked here) name seven; Sanctuary would be the eighth by inference. Do not wire the zone list without checking.",
  "Birthday Cake Hat: the free-login wording comes from the pack's article 2580 and locale:707 note; the locale:707 hit I saw did not show the hat line, so the exact wording needs checking.",
  "Birthday T-shirts (Briarwood, Wugachug, Sanctuary, Snowhill, Blackspore Swamp): the wiki pages are named but no quote ties them to the Bash. Left out of items.",
  "Zone cake prices and currency: 'station_cash' comes from a wiki statement only. Boss Birthday Cake price is not stated; the source for its acquisition is locale:14419, not a Marketplace listing.",
  "Birthday Bash! (locale:29341) and the ability 'Birthday Bash' (locale:428377) are undated; their content is unconfirmed.",
  "Quest titles: the five quest titles come from the earlier pack and were not re-verified against locale in this pass. The balloon-bundle quest (locale:428078) has no title in the pack.",
  "Commandant Kagoul, Glerga, Helga, Papillonnette and Plumette come from article 1300's summary only, not from client or wiki text.",
  "Not included (no source ties them to the Bash): Birthday Cake (427853), Big Birthday Cake (428028), Large Birthday Cake (428031), Birthday Cake Samples (9391), Birthday Party Crate (video C3fysVLxrMg), Cakenstein Attacks! (locale:4917)."
 ]
}
```
