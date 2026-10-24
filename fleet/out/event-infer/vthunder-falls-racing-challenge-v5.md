<!-- fleet job=event-infer id=vthunder-falls-racing-challenge-v5 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7238, 9753, 6, 2694] model=claude-haiku-5-5 -->
# Community Event: Thunder Falls Racing Challenge

{"event": {"name": "Community Event: Thunder Falls Racing Challenge", "aliases": ["Thunder Falls Racing Challenge (community event title only; NOT the housing quest of the same bare name, locale:7036)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": 2011, "when": "Thursday January 27, 2011, 3pm Pacific Time, U.S. and Latin America, Server 1 (one of two regional runs of the same event)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"year": 2011, "when": "Friday January 28, 2011, 9:00am Pacific Time for UK and Europe, Server 1. The same article's extracted text also says '4:00pm GMT'; that conflicts with 9:00am Pacific in January (PST = GMT-8, so 9:00am PST = 17:00 GMT). Unresolved.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"}
 ],
 "recurring": null,
 "zones": ["Thunder Falls Speedway"],
 "npcs": [],
 "quests": [],
 "activities": ["Player-versus-player kart race at Thunder Falls Speedway with AI turned off, joined through the race lobby or created by a player"],
 "items": [],
 "rewards": ["Winner-takes-all outcome (no prize item sourced)"],
 "evidence": [
  {"claim": "Event name 'Community Event: Thunder Falls Racing Challenge' is client text (duplicate ids, no date, server or format)", "source": "locale:2786; locale:31486"},
  {"claim": "Client line: 'Join the Community Team for a fast-paced, bumper-to-bumper race at Thunder Falls Speedway... SERVER 1'. Unattributed client string, no date; it supports Server 1 and the Speedway venue only", "source": "locale:2787"},
  {"claim": "Article 2009 verbatim quote is future tense: \"This week's Community Event will be a fast-paced, bumper-to-bumper, winner-takes-all race at Thunder Falls Speedway.\" This is an announcement wording. The pack's extracted line 'A weekly Community Event was a winner-takes-all kart race' conflicts with the quote on tense and is not used for recurrence.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"claim": "Article 2009 summary: PvP kart race at Thunder Falls Speedway on Server 1, held January 27, 2011 (U.S./Latin America) and January 28, 2011 (UK/Europe); explains joining or creating a race lobby and PvP race with AI off", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (summary)"},
  {"claim": "Article 2009 extracted event facts give the two run times: Jan 27, 2011 3pm Pacific (U.S./Latin America) and Jan 28, 2011 9:00am Pacific (UK/Europe), the latter also written as 4:00pm GMT", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (extracted facts)"},
  {"claim": "Article 2009 post date is not given. The summary's '1 month, 1 week before capture' is relative and is not used as a date", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (summary)"}
 ],
 "confidence": 0.35,
 "open": [
  "Live status unconfirmed. Article 2009 announces scheduled runs in future tense; the extracted fact 'The event ran on Server 1...' reads as past tense but no recap or results article was found in the pack. Needs a dated recap to mark live = yes.",
  "Time conflict within article 2009: 9:00am Pacific and 4:00pm GMT for the Jan 28 UK/Europe run cannot both hold in January (PST). Which figure was meant is unresolved; check the original article text.",
  "Article 2009 post date is unknown. The 2011 year comes only from the schedule text in the article summary.",
  "Recurrence not established. 'This week's Community Event' is one phrase in one article; the pack has no second dated occurrence. Undated Spanish articles from 2011 and 2013 are unverified candidates. recurring is null.",
  "Alias collision: the bare title 'Thunder Falls Racing Challenge' is the exact title of quest locale:7036, a housing feature (its neighbour locale:7015 describes building race tracks in a house). Not attached to this event.",
  "NPC lead only: locale:31494 ('Do you wanna go fast? Head to Thunder Falls and drive against the best! SERVER 1') is an npc_dialog line with no named speaker in the pack. Also locale:6906 has similar wording without Server 1. npcs stays empty.",
  "No items or sourced prizes. Winner-takes-all is an outcome, not an item.",
  "Separate events, by text only: locale:3339 'Thunder Falls Sprint Challenge', locale:3340 'Thunder Falls Endurance Challenge', locale:3244 'Kart Racing at Thunder Falls!' (these look like kart-racer titles), and locale:6678 Demolition Derby (its own article 1910 not re-read). None is dated in this pack, so the separation is a judgement from the text.",
  "The pack's previous answer listed the two regional runs as two separate occurrences. They are one scheduled community event split by region in one article; they are shown above as two dated runs of one event, not two events.",
  "Lakeshore location claim dropped: no source in the pack. Wiki 'Speedways' page not re-opened."
 ]
}
