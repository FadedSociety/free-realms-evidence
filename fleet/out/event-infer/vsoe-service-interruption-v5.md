<!-- fleet job=event-infer id=vsoe-service-interruption-v5 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6439, 7376, 6, 2306] model=claude-haiku-5-5 -->
# SOE service interruption

{"event": {"name": "Double Station Cash day (compensation after the April 2011 service interruption)", "aliases": ["Station Cash em Dobro", "Double Station Cash day, Saturday April 30"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [{"year": 2011, "when": "Saturday April 30; window 4 AM Sat Apr 30 to 3:59 AM Sun May 1 Brasilia time (8 AM to 7:59 AM Portugal time)", "source": "http://www.freerealms.com/article/detail.action?articleId=2125 (fact line; Portuguese-language post); http://www.freerealms.com/article/detail.action?articleId=2119 (Spanish-language, roughly late April 2011); http://www.freerealms.com/article/detail.action?articleId=2118 (Spanish-language, capture date 2011-06-04)"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Double Station Cash day (mechanics not stated in sources; articleId=2118, 2119, 2125)"],
 "items": [],
 "rewards": ["Double Station Cash for the day (the window was a double Station Cash day across SOE's games; articleId=2119, 2125)"],
 "evidence": [
  {"claim": "SOE announced a one-day double Station Cash day across its games on Saturday April 30, as an apology after a recent service interruption.", "source": "http://www.freerealms.com/article/detail.action?articleId=2119; http://www.freerealms.com/article/detail.action?articleId=2118"},
  {"claim": "The window ran 4 AM Saturday April 30 to 3:59 AM Sunday May 1, Brasilia time (8 AM to 7:59 AM Portugal time).", "source": "http://www.freerealms.com/article/detail.action?articleId=2125"},
  {"claim": "The 2125 post describes the double day as a thank-you after the service interruption; the 2125 summary calls it an apology. Both describe the same compensation.", "source": "http://www.freerealms.com/article/detail.action?articleId=2125"},
  {"claim": "The service interruption (April 21, 2011, external intrusion) is a separate outage record, not this event.", "source": "http://www.tentonhammer.com:80/node/97837 (dated 2011-04-25)"},
  {"claim": "Ten Ton Hammer reports SOE offered a Double Station Cash event on a Saturday for Free Realms players as compensation for the PlayStation Network-related interruption. The EverQuest/EverQuest II scope is not verified and is dropped.", "source": "http://tentonhammer.com/node/97967"}
 ],
 "confidence": 0.6,
 "open": [
  "Pack merges three things: (a) the April 21, 2011 outage (node/97837), not a schedulable event; (b) this Double Station Cash day; (c) the PS3 / PSN repair plan (articleId=2118, 2119), which has no dates or details in these sources and needs its own record.",
  "Year 2011 is inferred: the articles give month and day (Saturday April 30) and the outage was April 2011; no quoted article line states the year explicitly. Confirm against article records before scheduling.",
  "articleId=2112 (pre-launch plan) was not retrieved; it is not used as evidence here.",
  "Scope: articleId=2118 and 2119 say 'across SOE's games'. Specific games are not verified. node/97967 names Free Realms players only in the fact line; its EverQuest scope is unverified.",
  "Activities and item purchases/redemptions are not stated in any source; left empty. Do not infer earning or spending.",
  "Price, currency and item lists: none; Station Cash is the promotion currency, not an item.",
  "Do not match generically on 'Double Station Cash': unrelated promotions include Europe card redemption (articleId=2294, Oct 7-10, 2011), Walmart card (articleId=2790, Oct 12-14, 2012), 7-Eleven card (articleId=2806), Spring Celebration (articleId=2893, Mar 29-31; SMS exclusion does not apply here), Sept 18-20, 2009 card redemption (node/74525), and December 2011 weekend (articleId=1970).",
  "Zones, NPCs, quests: no source ties any to this event. Locale hits for 'intrusion' and 'interrupt' are unrelated dialogue.",
  "Recurring: null. One occurrence; no source says it recurs.",
  "The pack title 'SOE service interruption' is not the event name; the name comes from articleId=2119, 2125 and node/97967.",
  "Critique fixes applied: removed the claim that 2125 was confirmed by lookup text earlier (it is now confirmed by a fact line on this lookup, Portuguese post); corrected purpose to apology/thank-you per source; removed earning/spending activity guess; dropped the unverified EverQuest scope; marked 2119 as undated/late April 2011 and 2118 date as capture date; dropped the unverifiable 2112 claim."
 ]}
