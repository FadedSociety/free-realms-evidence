<!-- fleet job=schedule-infer id=svwildwood-speedway-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5157, 6185, 6, 2220] model=claude-haiku-5-5 -->
# vwildwood-speedway

{"event": {"name": "Wildwood Racing Challenge", "key": "wildwood-racing-challenge"},
 "kind": "community",
 "season": null,
 "slots": null,
 "weekly": null,
 "original_dates": [
  {"year": 2011, "start": "2011-03-10", "end": "2011-03-10", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045 (Thursday March 10th, 2011, 3pm Pacific Time, U.S. and Latin America, Server 1); French article http://www.freerealms.com/article/detail.action?articleId=2049 gives the same date (jeudi 10 mars), Serveur 1"},
  {"year": 2011, "start": "2011-03-11", "end": "2011-03-11", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045 (Friday March 11th, 2011, 9:00am Pacific Time, UK and Europe, Server 1; the article's 4:00pm GMT is wrong, 9am PST = 17:00 GMT); French article 2049 gives vendredi 11 mars"}
 ],
 "zones": ["Sanctuary or Southern Wilds (unresolved: wiki pages disagree; the Wildwood Speedway is just south of the Crossroads teleport stone)"],
 "runs": {
  "npcs": [],
  "props_or_areas": ["Wildwood Speedway kart race course (Bois Sauvage circuit in the French article)", "off-track party beside the race course"],
  "quests": [],
  "activities": ["kart race (helmet required for racers; non-racers could join the off-track party)"],
  "rewards": []
 },
 "announce": null,
 "revival": {"recurrence": "admin_only", "why": "A one-off community race hosted by Community Team Ambassadors on two dated sessions in March 2011. No source shows a repeating cadence for this event, so it should be started by staff, not run on slots or a yearly season. The Wildwood track has other community kart events (Summer Camp Racing Week, article 1700; Demolition Derby, article 188) that are separate events."},
 "evidence": [
  {"claim": "Community Team Ambassadors held a kart racing community event called the Wildwood Racing Challenge at the Wildwood Speedway, with a party just outside the race course", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045 (confirmed by lookup of articles index)"},
  {"claim": "The event ran on Server 1 on Thursday March 10, 2011 at 3pm Pacific Time for U.S. and Latin America players", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045 (confirmed by lookup)"},
  {"claim": "A second session ran on Server 1 on Friday March 11, 2011 at 9:00am Pacific Time for UK and Europe players", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045 (confirmed by lookup)"},
  {"claim": "The French article gives the same two dates and a helmet rule for racers, with an off-track party for non-racers", "source": "http://www.freerealms.com/article/detail.action?articleId=2049 (from the event answer pack; not re-read)"},
  {"claim": "The GMT figures in both articles are one hour off for the Friday session; the Pacific times are used", "source": "Arithmetic on articleId=2045 times: 9:00am PST = 17:00 GMT (PST in effect until 13 March 2011)"},
  {"claim": "Halloween is the only season defined; this event does not match it and gets no season row", "source": "seasons_already_defined in the pack"}
 ],
 "confidence": 0.7,
 "open": [
  "Live status is not confirmed. The articles announce the sessions, but no source records that they ran or were cancelled.",
  "Zone is unresolved: the wiki places Wildwood Speedway in Sanctuary, and the Southern Wilds page lists it under Southern Wilds. Check before setting the zone.",
  "No season row: the event is not yearly, so Halloween-style yearly windows do not apply. Staff can start it again by hand.",
  "No announcement text: no locale id was found for the event announcement.",
  "Quest names with the track name (for example Wildwood Sprint Challenge, locale 3319/3497, and Kart Driver quests such as locale 3490) are not tied to this event by any source, so they are left out of runs.quests.",
  "Article 1700 (Summer Camp Racing Week) and the Demolition Derby of 7 Aug 2009 (article 188) are separate events and are not merged here."
 ]}
