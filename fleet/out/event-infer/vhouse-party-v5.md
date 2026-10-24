<!-- fleet job=event-infer id=vhouse-party-v5 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[10515, 12329, 6, 3466] model=claude-haiku-5-5 -->
# House Party

```json
{
 "event": {"name": "House Party Tuesday", "aliases": ["House Party", "Community Event: House Party Tuesday"]},
 "kind": "weekly",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Tuesday, September 13 (4pm Pacific, U.S./LatAm, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2262"},
  {"year": 2011, "when": "Sunday, September 18, 3pm Pacific, Server 1 (special, not a Tuesday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2269"},
  {"year": 2011, "when": "Tuesday, September 20 (Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"},
  {"year": 2012, "when": "Tuesday, January 31 (Wilds Condo Tuesday edition, Server 1, Sanctuary)", "source": "http://www.freerealms.com/article/detail.action?articleId=2492 ; hosted per http://www.freerealms.com/article/detail.action?articleId=2493"}
 ],
 "recurring": "Weekly, every Tuesday (per articles and wiki). Year-by-year run dates beyond the listed sessions are not confirmed.",
 "zones": ["Sanctuary (meeting point)", "player housing (toured homes; Wilds Condo for the Jan 2012 edition, a housing location not a zone)"],
 "npcs": ["House Party (Community Team special character; teleports to featured houses)"],
 "quests": [],
 "activities": [
  "Meet in Sanctuary and tour decorated player homes",
  "Add the House Party character to Friends List during the event",
  "Teleport to House Party each time he moves to a new house",
  "Show off decorated or newly assigned homes (Wilds Condo edition)"
 ],
 "items": [
  {"name": "Futuristic Bicycle (membership-exclusive ride, via unique code)", "price": null, "currency": null, "source": "wiki 'Futuristic Bicycle' (ns0); wiki 'Community Events' (ns0): codes given to players whose home was toured, 'Not every event will have codes given out'"}
 ],
 "rewards": ["Futuristic Bicycle ride code (only at some sessions)"],
 "evidence": [
  {"claim": "House Party Tuesday is a weekly community event held every Tuesday in Sanctuary, where players meet and visit decorated homes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536; articleId=1452; articleId=1168 ('A weekly House Party Community Event was run every Tuesday'); articleId=1263; articleId=1241; articleId=1209; articleId=1556 (lookup text confirmed)"},
  {"claim": "Recurrence also stated on wiki 'Community Events': weekly event run most Tuesdays", "source": "wiki page 'Community Events'"},
  {"claim": "Special Community Team character 'House Party' teleports to featured houses; players add him to Friends List and teleport to him when he moves", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209 ('Add him to your Friends List during the event. He will teleport to the featured houses.'); articleId=2286 ('You can teleport to him each time he moves to a new house!')"},
  {"claim": "Sept 13 2011 session in Sanctuary on Server 1 (year from weekday; article gives no year)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2262"},
  {"claim": "Sept 18 2011 Sunday session, 3pm Pacific, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2269"},
  {"claim": "Sept 20 2011 Tuesday session, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"},
  {"claim": "Jan 31 2012 Wilds Condo Tuesday edition was hosted", "source": "http://www.freerealms.com/article/detail.action?articleId=2493 ('On Tuesday, January 31, 2012, the Community Team hosted a special Wilds Condo version...'); also articleId=2494"},
  {"claim": "Futuristic Bicycle ride was received by a unique code from touring a player's home in House Party; not every event gave codes", "source": "wiki 'Futuristic Bicycle' (ns0); wiki 'Community Events' (ns0)"},
  {"claim": "Client string names the event and tour line", "source": "locale:428314; locale:428315"}
 ],
 "confidence": 0.6,
 "open": [
  "Start time conflict: articleId=2492 gives '9:30 a.m. Pacific Time / 4:30pm GMT'. In January Pacific is UTC-8, so 9:30am Pacific is 17:30 GMT; the pair does not agree. UK/EU start is unresolved. Sept 2011 articles also disagree (2262: 4pm Pacific; 2270 pack value 16:30 GMT). Start time is not wired.",
  "2010 session: articleId=1209 summary gives 'Tuesday April 6, 2010, 3pm Pacific, Server 1' and articleId=1241 summary mentions an 'April 12, 2010 instance'. Only summaries; no quote and no verified post date. Left out of occurrences until the article text is read.",
  "Oct 3 'Tuesday, October 3rd' (articleId=2286) has no year and no Tuesday Oct 3 falls in 2009-2014 with that date; left out.",
  "articleId=1214 quote 'Every Tuesday is our House Party!' did not show in lookup; not cited. Recurrence rests on 1536, 1452, 1168, 1263, 1241, 1209, 1556 and the wiki.",
  "Quote 'Add him to your Friends List during the events' attributed to articleId=2270 did not appear in lookup; not cited. Blog 'User blog:SelenaStormybow/Futuristic Bike ride' not verified; not cited.",
  "Name variants possibly separate events, not merged: 'New Year House Party' (locale:31364, locale:426815), 'Pirate House Party' (locale:436162), 'Snow Days House Party' (locale:436455; locale:436459 is a flagged duplicate), 'Treehouse Party' (locale:430483). Each needs its own article check.",
  "Lookup hits locale:1452, locale:1263, locale:2270, locale:2494 matched article IDs, not item names; not tied to the event as items.",
  "No quest titles found for this event; quests empty.",
  "No prices or currency for the Futuristic Bicycle or any item are sourced.",
  "Whether the weekly event ran after January 2012 is not established; 'live: yes' rests on 2011-2012 articles only.",
  "Pack's date 2011-09-13 on articleId=2270 and the 'inferred' year on 2262/2269 are not verified post dates."
 ]
}
```
