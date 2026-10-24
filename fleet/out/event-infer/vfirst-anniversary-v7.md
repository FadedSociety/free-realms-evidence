<!-- fleet job=event-infer id=vfirst-anniversary-v7 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[20172, 11130, 8, 4215] model=claude-haiku-5-5 -->
# First anniversary celebration

```json
{
 "event": {
  "name": "Free Realms anniversary celebration (Birthday Bash series)",
  "aliases": [
   "First anniversary celebration (2010 instance, pack title)",
   "1st birthday party (2010)",
   "Second birthday party / Geburtstagsparty (2011)",
   "Birthday Bash (2012 onward)",
   "Free Realms turns Four! (2013 wiki slide only, unverified)"
  ]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "First anniversary; party ran into May 2010, ending 10 May 2010 (start date 29 April per article 1267 vs 28 April per later posts; unresolved)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 ; http://www.freerealms.com:80/article/detail.action?articleId=1268 ; http://www.freerealms.com/article/detail.action?articleId=1331 (corroborates all-day anniversary events held after an anniversary update)"},
  {"year": 2011, "when": "Second anniversary; anniversary 28 April 2011, party runs from the post date until 18 May 2011", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (German post, 'endet am 18. Mai' / 'until May 18'); http://www.freerealms.com:80/article/detail.action?articleId=2106 (per pack; not re-fetched)"},
  {"year": 2012, "when": "Third anniversary Birthday Bash; ran through 24 May 2012 (anniversary 28 April)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "recurring": "Observed in 2010, 2011 and 2012, each year around the 28 April launch anniversary and running into May. The wiki Balloon Bow page calls it the 'annual Birthday Bash'. The window moves each year, so it is not a fixed date rule.",
 "zones": [
  "Sanctuary (cake bake-off start with Camellia near the great tree; article 2580 Queen Valerian storyline)",
  "Sacred Grove (cake competition setting; locale 707)",
  "Party locations across towns (article 2099)"
 ],
 "npcs": [
  "Camellia (starts the bake-off; locale 707, article 1300)",
  "Queen Valerian (2012 bake-off storyline; article 2580)",
  "Papillonnette (party invitations; article 1300)",
  "Plumette (balloons; article 1300)",
  "Helga (food ingredients; article 1300)",
  "Cakenstein / Gâtostein / Kuchenstein (party boss; locales 4918, 4949; articles 1300, 2099, 2580)"
 ],
 "quests": [],
 "activities": [
  "Daily party-prep quests, repeatable each day (articles 1300, 2107, 2580; exact reset rules not stated)",
  "Help Camellia with the cake bake-off (article 1300; locale 707)",
  "Deliver party invitations for Papillonnette (article 1300)",
  "Collect balloons for Plumette (article 1300)",
  "Gather food ingredients for Helga (article 1300)",
  "Fight the Gâtostein / Cakenstein cake monsters and cakelings (articles 1300, 2099; locale 707)",
  "Cakenstein Attacks! encounter with a prize wheel (wiki Balloon Bow page)"
 ],
 "items": [
  {"name": "Balloon Bow", "price": null, "currency": null, "source": "wiki: Balloon Bow (prize wheel on the Cakenstein Attacks! encounter during the annual Birthday Bash; also tradeable); locale:6792 (purchase requires owning the Balloon Bow from that encounter)"},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "locale:694 (name only; 2012 login grant unverified, article 2578 not retrieved)"},
  {"name": "Birthday Party Crate", "price": null, "currency": null, "source": "locale:5664 (name and 'Place this crate on the ground to get the party started'); Station Cash currency wiki-only, unverified"},
  {"name": "Anniversary Firework", "price": null, "currency": null, "source": "locale:14571 (name only; no reward link confirmed)"}
 ],
 "rewards": [
  "Birthday Cake Hat (name in client; acquisition unverified)",
  "Balloon Bow via the Cakenstein Attacks! prize wheel (wiki)"
 ],
 "evidence": [
  {"claim": "2012 third-anniversary Birthday Bash ran through May 24, 2012; Queen Valerian bake-off in Sanctuary; daily party-prep quests; Cakenstein", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "2011 second-anniversary party ran from the post date until May 18; anniversary April 28; party quests, items, Kuchenstein boss", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099"},
  {"claim": "2010 guide: Camellia cake contest, Papillonnette invitations, Plumette balloons, Helga ingredients, Gâtostein fights; daily repeatable quests", "source": "http://www.freerealms.com/article/detail.action?articleId=1300"},
  {"claim": "Anniversary celebrated with an update and all-day events after the game's first year (new producer post)", "source": "http://www.freerealms.com/article/detail.action?articleId=1331"},
  {"claim": "Camellia starts the cake competition in Sanctuary", "source": "locale:707"},
  {"claim": "Cakenstein is a boss in the client", "source": "locale:4918 ; locale:4949"},
  {"claim": "Balloon Bow is tied to the Cakenstein Attacks! encounter during the annual Birthday Bash", "source": "wiki: Balloon Bow"},
  {"claim": "Birthday Cake Hat, Birthday Party Crate, Anniversary Firework exist as client item names", "source": "locale:694 ; locale:5664 ; locale:14571"}
 ],
 "confidence": 0.6,
 "open": [
  "Pack title 'First anniversary celebration' is the 2010 instance. The earlier answer merged 2010-2012 (and the 2013 wiki slide) under one 'Birthday Bash' name; the merge is an editorial choice, not one source. Treat the per-year entries as separate occurrences.",
  "2010 start date conflicts: article 1267 says 29 April 2010; 2099/2106 put the anniversary at 28 April. The 10 May 2010 end is sourced to article 1268, which I could not re-fetch in this pass.",
  "Article 1293 (Chef Jarvie, Robgoblin Camp, seven defeats, fireworks) was not retrievable; those details are excluded.",
  "Article 2578 (28 April 2012 free Birthday Cake Hat login, tripled Station Cash) was not retrievable; the login grant and Station Cash claims are unverified.",
  "Quest titles are unconfirmed by any source; the quests list is empty. Quest givers and tasks are listed under activities from article 1300.",
  "No prices are sourced for any item. Birthday Party Crate currency (station_cash) is wiki-only and unverified.",
  "Birthday Bash furniture (wall sconce, chair, lamp, table, bed) appears only in the wiki Template:News/Archive for the 24 April 2012 Marketplace update. It is a marketplace release sharing the name, not a confirmed event item, so it is excluded.",
  "Excluded as different events: Mystic Mayhem 'third anniversary' (guild, 1 Nov 2013), Waldo 25th Anniversary (locale 9144), Walmart 50th shirt, Anniversary Ring (locale 66913), April Member Rewards Pack (locale 156945), Orange/Blue anniversary silly string (locales 14574, 14575, 14581).",
  "Article 1331's summer-content preview (new pets, mounts, housing decor, summer-camp events) is a plan, not a live event, and is not part of this calendar.",
  "2013 'Turns Four' and 'April 29, 2013' come only from a wiki image and an unfetched article; no 2013 occurrence is counted.",
  "Launch-date conflict (April 28 2009 per TTH 67397 vs April 29 in wiki) is unresolved; Ten Ton Hammer node 83041 not verified."
 ]
}
```
