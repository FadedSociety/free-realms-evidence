<!-- fleet job=event-infer id=vformat-v8 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5944, 6524, 6, 1637] model=claude-haiku-5-5 -->
# Community event format

```json
{
 "event": {
  "name": "Community Team Thursday events (weekly Community Event slot)",
  "aliases": []
 },
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2011,
   "when": "first community party of 2011 (day and month not stated in retrieved text)",
   "source": "http://www.freerealms.com/article/detail.action?articleId=1988"
  }
 ],
 "recurring": "Stated rule: the Community Team holds these events every Thursday at a different location (articles 1987, 1988). No end date in the sources checked; the weekly run is not confirmed as a dated calendar beyond early 2011.",
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Community Team gathers at a different location each Thursday (articles 1987, 1988)",
  "Players invited to bring favorite outfits and boomboxes (article 1988)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {
   "claim": "Community events are held every Thursday by the Community Team at a different location (Spanish quote: 'Cada jueves el Equipo Comunitario se congrega en un lugar diferente para festejar')",
   "source": "http://www.freerealms.com/article/detail.action?articleId=1987 ; http://www.freerealms.com/article/detail.action?articleId=1988 (re-checked via lookup fact:event rows)"
  },
  {
   "claim": "Article 1988 announces the first community party of 2011, held on a stage in Snowy Hill on Server 1 (from article summary; full text not retrieved)",
   "source": "http://www.freerealms.com/article/detail.action?articleId=1988"
  },
  {
   "claim": "Players were invited to bring favorite outfits and boomboxes",
   "source": "http://www.freerealms.com/article/detail.action?articleId=1988"
  },
  {
   "claim": "'Community Event' is the client UI label",
   "source": "locale:5230"
  }
 ],
 "confidence": 0.3,
 "open": [
  "Not wireable. No verified day, month, or time for the 2011 party; the article summary gives only the year and 'first party of 2011'. Time of day is unsourced; earlier 3pm Pacific / 4pm PST drafts conflict and are dropped.",
  "Article 1984 was cited in an earlier draft but was not re-retrieved here, so it is not used as a source.",
  "The Spanish title 'Evento Comunitario: Fiesta de Inicio al 2011' names one specific party, not the recurring slot. It is dropped as an alias. Only the sourced Spanish quote is kept.",
  "Dated Thursday sessions (Ambassador Haunt and Seek 14 Oct 2010, Demolition Derby Day 18 Nov 2010, Snow Days 9 Dec 2010, Jul/Sep 2010 and Jan-Mar 2011 sessions) are not verified as part of this slot and are excluded. They may be separate events, and the bare 'Community Event' label could merge them with this slot. Super Spooktacular Thursdays (articles 1849/1850) are a separate dated October event.",
  "No source shows the Thursday slot running after early 2011, so 'weekly' is a stated rule, not a verified running schedule. Live status unknown.",
  "No items, NPCs, quests or rewards are tied to this event by a source. Touring Seaside is not linked (it appears only as a quest answer mention with no sourced tie).",
  "Beach party and demolition derby examples (article 1214) are per-week examples, not the slot rule, and are not attributed here."
 ]
}
```
