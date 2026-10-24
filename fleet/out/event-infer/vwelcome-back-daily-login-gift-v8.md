<!-- fleet job=event-infer id=vwelcome-back-daily-login-gift-v8 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6311, 7476, 6, 2413] model=claude-haiku-5-5 -->
# Welcome Back daily login gift

{
 "event": {
  "name": "Welcome Back seven-day daily login gift",
  "aliases": ["Welcome Back daily login gift", "welcome-back login gift series", "Free login rewards (seven days)"]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Log in on each of the seven days to receive that day's free item (articleId=2127: one given out upon login each day for seven days; articleId=2129: 'Logging in on each of the next seven days')",
  "Logging in before the last day was needed to collect all seven items (articleId=2127; articleId=2131)"
 ],
 "items": [],
 "rewards": [
  "One free item per login day, seven days (items not named in any retrieved source text)"
 ],
 "evidence": [
  {"claim": "Seven-day login gift: one free item per login day for seven days; logging in before the last day was needed to collect all seven.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (English article text)"},
  {"claim": "Free login rewards: one item per day for seven days, provided the player logged in before the last day.", "source": "http://www.freerealms.com/article/detail.action?articleId=2131 (article text)"},
  {"claim": "German announcement: logging in on each of the next seven days gave a free item per day.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2129 (quote: 'Meldet euch täglich für die nächsten sieben Tage an')"},
  {"claim": "The series is part of a 'Welcome Back' returning-player post announcing a seven-day free login gift; the post is dated only relatively (roughly May 2011).", "source": "http://www.freerealms.com/article/detail.action?articleId=2138 (summary: 'Posted 2 weeks, 3 days ago')"},
  {"claim": "Parent program (not the series itself): 43 or 45 member days, depending on the article, plus 20,000 coins for lifetime members. Eligibility cutoff is early May 2011 (2 May 2011 per 2138 summary). Conflict: 43 days (2131 summary) vs 45 days (2127, 2129 summaries).", "source": "http://www.freerealms.com/article/detail.action?articleId=2131 (summary); http://www.freerealms.com:80/article/detail.action?articleId=2127 (summary); http://www.freerealms.com:80/article/detail.action?articleId=2129 (summary)"},
  {"claim": "Capture dates: 2127 summary says 'about May 2011' from a relative '2 months ago'; 2129 capture is 2011-05-21 with the post about six days earlier.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (summary); http://www.freerealms.com:80/article/detail.action?articleId=2129 (summary)"}
 ],
 "confidence": 0.3,
 "open": [
  "DATE: No dated source for the seven-day login series. Estimate only: circa mid-May 2011, inferred from 2138's relative 'Posted 2 weeks, 3 days ago' and 2129's 2011-05-21 capture. Not stored as an occurrence; do not schedule.",
  "PARENT: 'Welcome Back' returning-player program is a separate calendar entry (articles 2127, 2129, 2130, 2131, 2138, 2139, 2142, 2143, 2145), not an alias of this series. Build it first. Its 43-vs-45 day conflict and early-May 2011 cutoff belong there.",
  "LIFETIME BONUS: 20,000 coins for lifetime members is a parent-program reward, not a login-series reward. The lifetime bonus lot named in the 2129 summary is unidentified.",
  "ITEMS: No per-day item names appear in retrieved source text. Earlier item lists were unsourced and dropped. Day 6 conflicts across articles (Large Launch Pad in 2127/2130; large jump pad in 2129; Grand trampoline in 2138). Need full article bodies of 2127 and 2129 to list items.",
  "LIVE: 'unsure'. Articles use future wording ('will be given out'); no dated article confirms the series ran.",
  "PRICES: none found; all null.",
  "RECURRENCE: at most one occurrence; nothing says it recurs.",
  "CLIENT: no client quest, NPC or zone tied to this event was found in the locale table. The earlier locale:2139 citation is removed because that id does not exist.",
  "CALENDAR: not wireable. Exact date, live status and item list are unresolved."
 ]
}
