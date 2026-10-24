<!-- fleet job=event-infer id=vninja-brawl-bagarre-de-ninja-v5 status=done turns=1 usd=0.0029 tokens(read,write,in,out)=[0, 8191, 4, 3708] model=claude-haiku-5-5 -->
# Ninja Brawl (Bagarre de Ninja)

The pack covers two separate events under one name. Article 311 calls its 2009 run "[Ninja] [Brawl] 2", and article 2029 calls its 2011 run "the first [Ninja] [Brawl] session". A numbered series cannot start its first run in 2011 after run 2 in 2009. So I split the record. Record A is the 2011 run, which is the primary record. Record B is the 2009 run. Neither is confirmed as one series.

**Record A: Ninja Brawl (2011)**

```json
{"event": {"name": "Ninja Brawl", "aliases": ["[Ninja] [Brawl] (article 2029 wording)", "Bagarre de Ninja (French, article 2041)", "Community Event: Ninja Brawl (locale:9104)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
   {"year": 2011, "when": "Thursday 17 February 2011, 3pm Pacific (Americas and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2029"},
   {"year": 2011, "when": "Friday 18 February 2011, 9:00am Pacific (UK and Europe), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2029"}
 ],
 "recurring": null,
 "zones": ["Shrouded Glade"],
 "npcs": [],
 "quests": [],
 "activities": ["Arrive at the scheduled time and place", "Send duel invitations to other players", "Accept duel invitations received"],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "The first session was on Thursday 17 February 2011 at 3pm Pacific, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2029"},
   {"claim": "A second session was on Friday 18 February 2011 at 9:00am Pacific Time, Server 1, for UK and Europe. The article also prints '(4:00pm GMT)', which conflicts with its own Pacific time.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2029"},
   {"claim": "The event takes place in Shrouded Glade.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2029 (fact:location)"},
   {"claim": "Duelling is the activity: players send and accept duel invitations.", "source": "http://www.freerealms.com/article/detail.action?articleId=2041&request_locale=en_US (fact:event, French: 'Envoi des invitations de duel aux autres joueurs et accepte toutes les invitations reçues')"},
   {"claim": "The French post gives the same 17 and 18 Feb 2011 sessions (Jeudi 17 février 2011 3h Pacific; Vendredi 18 février 2011 18h CET / 4h00 GMT). Its publish date is not in the pack, and its tense is past ('was on'), so it is treated as corroboration of the dates, not as a plan.", "source": "http://www.freerealms.com/article/detail.action?articleId=2041&request_locale=en_US"},
   {"claim": "The name appears in the client as 'Community Event: Ninja Brawl'. This confirms the name only, not the duelling or the dates.", "source": "locale:9104"},
   {"claim": "Client locale 9105 describes Shrouded Glade duelling ('Ninjas often sneak to Shrouded Glade to find out who is the best. Bring your ninja and prepare to duel!'). It is consistent with the articles and is not independent proof of the same event.", "source": "locale:9105"}
 ],
 "confidence": 0.6,
 "open": [
   "Identity: this record is 2011 only. The 2009 run (Record B) is not merged here. Series status is unresolved.",
   "Article 2029 prints '9:00am Pacific Time (4:00pm GMT)'. 9:00am Pacific is 17:00 GMT and 18:00 CET, which matches the 2041 CET figure. The 4:00pm GMT figure is a typo in the source. The 17:00 GMT value is computed and appears in no article, so it is not listed as an occurrence.",
   "Article 2041 has no publish date in the pack ('posted 3 months, 2 weeks ago'). Its 2011 dates match article 2029, but the year is inferred from those dates, not stated by 2041 itself. Its Americas time '3h' has no am/pm; 15h is assumed from article 2029.",
   "Article 1391 announces a Ninja Brawl on Thursday 13 May 2010, 3pm Pacific, Server 1 ('was scheduled'). It also lists a second UK/Europe session for 'Friday April 14th, 2010' at 9:00am Pacific / 6:00pm GMT. That conflicts with its own May 13 date and weekday. Both 2010 items are announcements with no confirmed run, so they are excluded from occurrences.",
   "Recurring is null. No article states a cadence or says the event recurs, and the two 2011 days are one session pair.",
   "No items, prices, currency, quests, NPCs or rewards are tied to this event in the pack, the client or the wiki. The wiki Tavern Cellar hits ('brawl club rules', Archer Prize Wheel) and the Ninja achievement text are not tied to this event, so they are excluded. Ty at Lakeside is a separate Ninja job NPC from article 2041, truncated and unverified, not linked to this event.",
   "The wiki category is empty and there are no quest answers, so the activity detail beyond duelling is unsourced.",
   "Wireable: false for a calendar. The only dated runs are past, with no future or recurring schedule, and the identity is unresolved. It could be entered as one-off historical sessions once the series question is settled."
 ]}
```

**Record B: Ninja Brawl 2 (2009)**

```json
{"event": {"name": "Ninja Brawl 2", "aliases": ["[Ninja] [Brawl] 2 (article 311 title)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
   {"year": 2009, "when": "Friday 11 September 2009, 12pm-2pm Pacific, Server 1, Shrouded Glade", "source": "http://www.freerealms.com:80/article/detail.action?articleId=311"}
 ],
 "recurring": null,
 "zones": ["Shrouded Glade"],
 "npcs": [],
 "quests": [],
 "activities": ["Send duel requests to other players", "Accept incoming duel requests"],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "A session titled '[Ninja] [Brawl] 2' was held on Friday 11 September 2009, 12pm-2pm Pacific, Server 1, Shrouded Glade (past tense 'was held').", "source": "http://www.freerealms.com:80/article/detail.action?articleId=311"},
   {"claim": "Duel rules: participants send duel requests and accept incoming ones. The brawl ends the gathering until the next one is announced.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=311"}
 ],
 "confidence": 0.6,
 "open": [
   "The series link to Record A (2011) is unresolved. The article 311 title numbers this run '2', but Record A's source calls its 2011 run 'the first'. Keep them separate until the source numbering is checked.",
   "Only one 2009 run is in the pack. Recurrence cannot be established from one run.",
   "No items, rewards, NPCs or quests are sourced for this run."
 ]}
```

Summary of the fixes: the single merged record is replaced by two records. The 2041 post is cited for its past-tense session dates, not described as a plan. The 2010 April 14 and May 13 listings are recorded in open as announcements only. Locale 9105 is described as consistent, not independent.
