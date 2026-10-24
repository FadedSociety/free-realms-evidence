<!-- fleet job=event-infer id=vformat-v4 status=done turns=3 usd=0.0040 tokens(read,write,in,out)=[18403, 12447, 8, 4529] model=claude-haiku-5-5 -->
# Community event format

```json
{
 "event": {
  "name": "Community Team Thursday events (weekly community slot)",
  "aliases": ["Community Event", "Community Events", "Evento Comunitario", "Equipo Comunitario events", "Community Team party", "Community party"]
 },
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "Thursday 8 July 2010, 3pm Pacific, Server 1 (US and Latin America), community soccer event", "source": "http://www.freerealms.com/article/detail.action?articleId=1621"},
  {"year": 2010, "when": "Thursday 9 September 2010, 3pm Pacific, Server 1 (US and Latin America), community party in Singing Crystal Mines", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1800"},
  {"year": 2010, "when": "Thursday 30 September 2010, 3pm Pacific, Server 1 (US and Latin America session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1830"},
  {"year": 2010, "when": "Thursday 18 November 2010, 3pm Pacific, Server 1 (US/Latin America session), Demolition Derby Day community event", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1910"},
  {"year": 2010, "when": "Thursday 9 December 2010, 3pm Pacific, Server 1 (US/Latin America session), Snow Days community party, Wintery Basin fishing area", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1953"},
  {"year": 2011, "when": "Thursday 6 January 2011, 3pm Pacific, Server 1 (US and Latin America), 2011 kick-off party, Snowy Hill", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984"},
  {"year": 2011, "when": "Thursday 20 January 2011, 3pm Pacific, Server 1 (US and Latin America), pool party at Memorial Caverns", "source": "http://www.freerealms.com/article/detail.action?articleId=2007&request_locale=en_US"},
  {"year": 2011, "when": "Thursday 3 February 2011, 3pm Pacific, Server 1 (US and Latin America)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"}
 ],
 "recurring": "Weekly on Thursdays per the Community Team wording (articles 1988, 1984, 1854): the team holds an event each Thursday at a different location. Dated Thursday 3pm Pacific sessions appear in 2010-2011. No end date is stated.",
 "zones": ["Snowy Hill (Server 1), 6 January 2011 kick-off party only", "Other weeks: a different location each Thursday, not named in the weekly-rule sources"],
 "npcs": [],
 "quests": [],
 "activities": [
  "Community Team gathers at a different place each Thursday to hang out and party (articles 1984, 1988)",
  "Players invited to bring favorite outfits and boomboxes (article 1988)",
  "Friday 9am Pacific Community Team session (article 1854 only; see open)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "The Community Team holds these events each Thursday at a different location; players invited to bring favorite outfits and boomboxes", "source": "http://www.freerealms.com/article/detail.action?articleId=1988"},
  {"claim": "Every Thursday the Community Team gathers in a different place to hang out and party as a Community Event; the 6 Jan 2011 session was 3pm Pacific on Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984"},
  {"claim": "Community Events every Thursday at 4pm PST and Friday at 9am PST, reachable via teleport from the in-game guide", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "Community Team Thursday event (beach party or demolition derby examples)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1214"},
  {"claim": "Thursday February 3rd, 2011 at 3pm Pacific for U.S. and Latin America, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"},
  {"claim": "Thursday 3 February 2011 3pm Pacific first event session (US and Latin America), Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2027&request_locale=en_US"},
  {"claim": "Thursday 9 December 2010 3pm Pacific, Snow Days community party, Wintery Basin fishing area, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1953"},
  {"claim": "Thursday 18 November 2010 3pm Pacific, Demolition Derby Day community event, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1910"},
  {"claim": "Thursday 9 September 2010 3pm Pacific, community party in Singing Crystal Mines, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1800"},
  {"claim": "Thursday 8 July 2010 3pm Pacific, community soccer event, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=1621"},
  {"claim": "Thursday 30 September 2010 3pm Pacific, Server 1 (US and Latin America session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1830"},
  {"claim": "Thursday 20 January 2011 3pm Pacific, pool party, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2007&request_locale=en_US"}
 ],
 "confidence": 0.3,
 "open": [
  "Scope/merge problem: the Thursday 3pm sessions are each a different named Community Team event (Stampede 1191, Demolition Derby 1910, Launch Pad 1888, Turkey Dance 1918, Robgoblin Rave 1993, Ninja Duel 2031/2032, Playazul party 1893/1894, kart race 2048, soccer 1621, Snow Days 1953). Only the weekly wording ties them to one format. Named one-offs should be scheduled as separate events. The weekly slot is a series of different events, not one repeated event.",
  "Dated sessions 1534 (17 Jun 2010), 1668 (22 Jul 2010), 1700 (29 Jul 2010), 1851 (14 Oct 2010) and 2027 (3 Feb 2011) come from the pack and were not re-confirmed in this run. Article 2020 does confirm 3 Feb 2011, and 2027 is cited as a second source for that date.",
  "Time conflict, unresolved: weekly-rule articles say 4pm Pacific (1854 says 4pm PST; 1861 and 1860 say 16:00 Pacific per the pack), while the dated Thursday sessions say 3pm Pacific on Server 1. Do not schedule one time until a source reconciles them.",
  "Friday 9am Pacific Community Team session: only article 1854 was checked and it confirms 'Friday at 9am PST'. Articles 1861 and 1860 were not re-confirmed (locale 1860 does not exist). Article 1988's Friday 9am session is for UK and Europe, not this slot.",
  "Friday 7 January 2011 date comes from article 1988 only; no time is stated there.",
  "Live status unsure: the weekly slot is described in 2010-2011 (1854 future tense, 1860 past tense per the pack). No source gives an end date or any Community Team Thursday event after 3 Feb 2011 in this pack. Article 2013/2011/2015 (27 Jan 2011, Thursday 3pm/15:00 Pacific, US and Latin America, Server 1) and 2048 (10 Mar 2011 kart race) show Thursday sessions continued into 2011, but their titles do not say Community Team.",
  "Pack's 'Touring Seaside (final, live yes)' is dropped: no source ties it to this event, so no live confirmation is taken from it.",
  "Items, NPCs, quests and rewards: none tied to this format by a source. Ballet Boombox (wiki, unreleased) has no tie to a named occurrence and no price. Client locale 1988 'Humongous Energy Potion' is a duplicate and not tied. Locale 1854 'Sunstone Mystery Boots' is a placeholder and not tied. Ambassador and Referee staff appear only in general wiki text. Client locale 9102, 9104, 9106, 6536 and 31362 are named one-off events, not this format.",
  "Pack's 'Community Event is the client's UI label (locale 5230)' was not re-verified and is not used.",
  "Wireable: false. The time is unresolved and the live end date is unknown. The 6 January 2011 kick-off party (articles 1984 and 1988, Snowy Hill, Server 1) can be scheduled on its own as a one-off."
 ]
}
```
