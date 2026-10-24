<!-- fleet job=event-infer id=vformat-v5 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[8811, 10516, 6, 3139] model=claude-haiku-5-5 -->
# Community event format

```json
{
 "event": {
   "name": "Community Team Thursday events (weekly community slot)",
   "aliases": ["Evento Comunitario (Spanish title of article 1988)", "Community Event (client UI label, locale:5230)"]
 },
 "kind": "community",
 "live": "unsure",
 "occurrences": [
   {"year": 2011, "when": "Thursday 6 January 2011, 2011 kick-off party (first major community event of the year), Snowy Hill stage, Server 1. Friday 7 January 2011 is also named in the same article.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984 ; http://www.freerealms.com/article/detail.action?articleId=1988"}
 ],
 "recurring": "Stated as a weekly rule by the Community Team (\"Every Thursday the Community Team gathers in a different place\"; \"Cada jueves ... en un lugar diferente\"), per articles 1984, 1987 and 1988, and 1214 (\"Each Thursday the Community Team runs a different event\"). No end date is given. Only one dated session was confirmed in this run, so the schedule is not verified as running beyond what the sources state. Recurrence is a stated rule, not a verified calendar.",
 "zones": ["Snowy Hill (Server 1), 6 January 2011 only. Other weeks: 'a different place', not named in the sources checked here."],
 "npcs": [],
 "quests": [],
 "activities": [
   "Community Team gathers at a different place each Thursday to hang out and party (articles 1984, 1987, 1988)",
   "Players were invited to bring favorite outfits and boomboxes (article 1988)",
   "Each Thursday's event is a different activity, e.g. a beach party or demolition derby (article 1214)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "Every Thursday the Community Team gathers in a different place to hang out and party as a Community Event", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984"},
   {"claim": "Community events are held every Thursday by the Community Team at a different location (Spanish text)", "source": "http://www.freerealms.com/article/detail.action?articleId=1987"},
   {"claim": "The Community Team held a community party to start 2011, first major community event on Thursday 6 January 2011 and Friday 7 January 2011; stage in Snowy Hill, Server 1; players asked to bring outfits and boomboxes", "source": "http://www.freerealms.com/article/detail.action?articleId=1988"},
   {"claim": "Each Thursday the Community Team runs a different event, such as a beach party or demolition derby", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1214"},
   {"claim": "'Community Event' is the client UI label", "source": "locale:5230"}
 ],
 "confidence": 0.4,
 "open": [
   "Scope/merge: the Thursday sessions are different named one-offs, each with its own content. The weekly rule is one format; the dated sessions are separate events. Schedule them separately. Named client strings (e.g. locale 2776-2792, 6536-6541, 9102-9108, 15043-15049, 18240, 31291, 31293) name Community Event activities, but no source ties them to the Thursday slot here, so they are not listed as occurrences.",
   "Other dated Thursday sessions from the earlier draft (8 Jul 2010 article 1621; 9 Sep 2010 article 1800; 30 Sep 2010 article 1830; 18 Nov 2010 article 1910 Demolition Derby Day; 9 Dec 2010 article 1953 Snow Days, Wintery Basin; 20 Jan 2011 article 2007 pool party, Memorial Caverns; 3 Feb 2011 article 2020/2027) were NOT re-verified in this run. Treat them as 'source not checked' until their article text is read. Also unverified: 1534, 1668, 1700, 1851, and 27 Jan 2011 (2013/2011/2015) and 10 Mar 2011 (2048), whose titles do not say Community Team.",
   "Time conflict: 1854 and the Spanish weekly articles give 4pm / 16:00 Pacific (1854 states 4pm PST, 'Friday at 9am PST'), while dated Thursday sessions in the earlier draft say 3pm Pacific on Server 1. Not reconciled. Do not schedule a single time until a source reconciles them. The 6 Jan 2011 time (3pm Pacific) was taken from the earlier draft's reading of 1984 and was not re-read here.",
   "Friday 9am Pacific session: only article 1854 (not re-verified here) names it. Removed from this event's activities; treat as a separate question.",
   "Live status unsure: the weekly rule is described in 2010-2011 articles; no source in this run gives an end date or a Community Team Thursday event after Feb 2011. Range the sources cover is roughly July 2010 to Feb 2011 (unverified beyond 6 Jan 2011).",
   "Recurrence is single-source-weighted: 'weekly' rests on the Community Team's own wording in 1984, 1987, 1988 and 1214, which is a stated plan, not an observed calendar.",
   "Items, NPCs, quests and rewards: none tied to this format by a source. The earlier pack's Ballet Boombox (wiki, unreleased), Humongous Energy Potion (locale 1988), Sunstone Mystery Boots (locale 1854, placeholder) are not tied and are excluded. Ambassador and Referee appear only in general wiki text. Locale 9102/9104/9106/6536/31362 are named one-offs, not this format.",
   "Aliases: 'Community Event' is the UI label (locale:5230) and verified. 'Community party' and 'Community Events' are not used. 'Touring Seaside (final, live yes)' from the pack is dropped; no source ties it to this event.",
   "Wireable: false. The 6 Jan 2011 kick-off party (articles 1984/1988, Snowy Hill, Server 1) can be scheduled alone as a one-off once its time is confirmed."
 ]
}
```
