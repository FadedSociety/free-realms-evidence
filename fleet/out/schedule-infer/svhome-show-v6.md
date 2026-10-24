<!-- fleet job=schedule-infer id=svhome-show-v6 status=no_submit turns=4 usd=0.0049 tokens(read,write,in,out)=[31789, 13980, 10, 5719] model=claude-haiku-5-5 -->
# Community Event: House Party Tuesday

```json
{"event": {"name": "Community Event: House Party Tuesday", "key": "house-party-tuesday"},
 "kind": "recurring_activity",
 "season": null,
 "slots": null,
 "weekly": {"days": ["tue"], "time_local": null, "source": "Cadence: 'every Tuesday' in articleId=1214, 1452, 1536, 1168, 1241, 1263 (lookup). Clock time NOT verified: the Pacific start times conflict across sessions. articleId=1168: Mar 23, 2010 at 4pm Pacific, Server 1. articleId=1209: Apr 6, 2010 at 3pm Pacific, first listed session. articleId=1241: Apr 12, 2010 at 3pm Pacific. articleId=1263: Apr 20, 2010 at 4pm Pacific. No single standing time, so time_local stays null."},
 "original_dates": [
  {"year": 2010, "start": "2010-03-23", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168 ('The first House Party was on Tuesday March 23, 2010 at 4pm Pacific Time ... on Server 1'; 'A weekly House Party Community Event was run every Tuesday' (past tense))"},
  {"year": 2010, "start": "2010-04-06", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209 ('The first listed session was Tuesday April 6, 2010 at 3pm Pacific ... Server 1'). Note: 1209 calls it the 'first listed session' while 1168 calls March 23 the first event."},
  {"year": 2010, "start": "2010-04-12", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1241 ('The April 12, 2010 House Party ran at 3pm Pacific ... Server 1'). (Flag: April 12, 2010 was a Monday, not a Tuesday, although 1241 says 'Tuesday April 12th'. The date is suspect and needs checking.)"},
  {"year": 2010, "start": "2010-04-20", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263 ('Tuesday April 20th, 2010 4pm Pacific Time (U.S. and Latin America) Server 1'). Body re-read via lookup this time."},
  {"year": 2010, "start": "2010-06-15", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536 ('Over the summer, House Party Tuesday visits houses matching a weekly theme; the theme for the June 15, 2010 event was Camping'). Summer 2010 themed run; the Tuesday was June 15, 2010."},
  {"year": 2011, "start": "2011-09-13", "end": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2262 ('Community House Party event held on Tuesday, September 13, meeting in Sanctuary'). Year is (R): the article gives no year. September 13 is a Tuesday in 2011 and not in 2010 or 2012, so 2011 is the only fit in the 2009-2014 window."},
  {"year": 2011, "start": "2011-09-20", "end": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270 ('On Tuesday, September 20th, we'll meet up in Sanctuary ... held on Server 1'). Year is (R): September 20 is a Tuesday in 2011 only within 2009-2014."}
 ],
 "zones": ["Sanctuary (Server 1)"],
 "runs": {
  "npcs": ["House Party (Community Team character who teleports to featured player houses)"],
  "props_or_areas": ["Player-decorated homes throughout Free Realms (visited, not a client area)"],
  "quests": [],
  "activities": ["Meet in Sanctuary with the Community Team", "Follow the House Party character to visit decorated player homes", "Summer 2010 weekly house theme (e.g., Camping on June 15, 2010, articleId=1536)"],
  "rewards": []
 },
 "announce": null,
 "revival": {"recurrence": "weekly", "why": "The weekly Tuesday cadence is sourced in several articles ('every Tuesday'). It is a weekly activity, not a daily slot, and the schema's weekly field fits it. It stays unwireable: time_local is null because the start time varies across sessions (3pm vs 4pm Pacific) and no standing time is sourced, and no run end is known. Staff-start it until the time is settled. The Jan 31, 2012 Wilds Condo special is a one-off and not part of this row."},
 "evidence": [
  {"claim": "Weekly community event held every Tuesday in Sanctuary (Server 1), visiting decorated player homes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1452; articleId=1536; articleId=1214"},
  {"claim": "The first House Party was Tuesday March 23, 2010 at 4pm Pacific on Server 1; the event 'was run every Tuesday' (past tense, bounded run)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
  {"claim": "Session Tuesday April 6, 2010 at 3pm Pacific, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209"},
  {"claim": "April 12, 2010 at 3pm Pacific, Server 1 (day-of-week conflict: April 12, 2010 was a Monday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1241"},
  {"claim": "Tuesday April 20, 2010 at 4pm Pacific, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263"},
  {"claim": "Summer 2010 weekly themed houses; June 15, 2010 theme was Camping", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536"},
  {"claim": "Sept 13 and Sept 20 sessions (year not stated in the articles; Tuesday in 2011)", "source": "http://www.freerealms.com/article/detail.action?articleId=2262; http://www.freerealms.com:80/article/detail.action?articleId=2270"},
  {"claim": "Jan 31, 2012 special Wilds Condo edition, Tuesday, Sanctuary, Server 1 (one-off)", "source": "http://www.freerealms.com/article/detail.action?articleId=2492; articleId=2493; articleId=2494"},
  {"claim": "Client title 'Community Event: House Party Tuesday'", "source": "locale:428314"},
  {"claim": "Wiki: 'Wilds Condo Tuesday' was a special edition of the House Party (not an alias)", "source": "wiki Community Events page"}
 ],
 "confidence": 0.5,
 "open": [
  "Clock time is unresolved. Sessions show 4pm Pacific (Mar 23, Apr 20, 2010) and 3pm Pacific (Apr 6, Apr 12, 2010) on Server 1. time_local stays null until a standing time is confirmed. The 2010 times may also have changed later.",
  "Run window: first sourced session is 2010-03-23 (1168). The last sourced session is 2011-09-20 (2270). The end date is unknown; the 1168 past tense and the summer 2010 mention suggest the run may have ended. Halloween and other seasons do not apply.",
  "articleId=1241: 'Tuesday April 12th, 2010' is a Monday. Either the date or the weekday is wrong; verify before using it as an occurrence.",
  "articleId=2286 (Oct 3, 'Tuesday') has no year. October 3 is a Tuesday only in 2006 and 2017, so it cannot be a 2009-2014 weekly session and is excluded.",
  "Skipped weeks: articles say 'every Tuesday', but the wiki says 'most Tuesdays'. Unresolved.",
  "The Sept 13 and Sept 20 2011 years are inferred from the weekday (R), since the articles give no year.",
  "Jan 31, 2012 Wilds Condo special (articleId 2492-2494) needs its own one_off row. It is not part of this weekly row, and 'Wilds Condo Tuesday' is not an alias.",
  "Home Show (articleId 1827) was in the pack title but is a separate player-house spotlight with no date or cadence. It is not part of this row.",
  "Do not merge with: New Year House Party (locale 31364 / 426815); Pirate House Party (436162); Snow Days House Party (436455; 436459 is a duplicate FLAG); Treehouse Party (430483); Festival of Hearts (3545, flavor text). Futuristic Bicycle is not in the Community Events category.",
  "No announcement text is sourced (locale 428315 body unverified, not cited). No quests, items or rewards are sourced."
 ]
}
```
