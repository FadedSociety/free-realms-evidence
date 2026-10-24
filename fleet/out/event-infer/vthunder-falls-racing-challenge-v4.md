<!-- fleet job=event-infer id=vthunder-falls-racing-challenge-v4 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7422, 8565, 6, 2390] model=claude-haiku-5-5 -->
# Community Event: Thunder Falls Racing Challenge

{
 "event": {"name": "Community Event: Thunder Falls Racing Challenge", "aliases": []},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": 2011, "when": "Thursday January 27, 2011, 3pm Pacific (U.S. and Latin America), Server 1 (scheduled run)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"year": 2011, "when": "Friday January 28, 2011, 9:00am Pacific (UK and Europe), Server 1 (scheduled run). Article also states '4:00pm GMT', which conflicts with 9:00am Pacific (9:00am PST = 17:00 GMT, a derived conversion, not the article's wording)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"}
 ],
 "recurring": null,
 "zones": ["Thunder Falls Speedway (zone not verified; Lakeshore claim unsourced and dropped)"],
 "npcs": [],
 "quests": [],
 "activities": ["Player-versus-player kart race at Thunder Falls Speedway with AI turned off, joined through the lobby or created by a player"],
 "items": [],
 "rewards": ["Winner-takes-all outcome (no prize item sourced)"],
 "evidence": [
  {"claim": "Event name 'Community Event: Thunder Falls Racing Challenge' appears as client text (identical duplicates at two ids, no date or context)", "source": "locale:2786; locale:31486"},
  {"claim": "Client line tying the Community Team to a fast-paced, bumper-to-bumper race at Thunder Falls Speedway on SERVER 1. This is an unattributed client string, not article text, and carries no date", "source": "locale:2787"},
  {"claim": "Article 2009 verbatim quote is future tense: 'This week's Community Event will be a fast-paced, bumper-to-bumper, winner-takes-all race at Thunder Falls Speedway.' The pack's extracted fact reads 'was', which contradicts the quote; the quote is treated as authoritative. It is an announcement, not a recap", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"claim": "Article 2009 summary: PvP kart race at Thunder Falls Speedway on Server 1, dated January 27, 2011 (U.S./Latin America) and January 28, 2011 (UK/Europe); explains joining or creating a race lobby and PvP race with AI off", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (summary)"},
  {"claim": "Article 2009 post date is not given in the pack; the summary's '1 month, 1 week before capture' is relative and is not used as a date", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (summary)"}
 ],
 "confidence": 0.3,
 "open": [
  "Live status unconfirmed: article 2009 is an announcement of two scheduled runs (Jan 27 and Jan 28, 2011). No recap or results article was found, so it is not confirmed that the runs happened. Needs a dated recap or results article.",
  "Recurrence not established. The 'weekly' wording ('This week's Community Event') is from one article; the undated Spanish articles 2011 and 2013 are unverified candidates for further occurrences. recurring is null.",
  "Article 2009 post date is unknown; the 2011 year comes only from the schedule text.",
  "Time conflict in article 2009: 9:00am Pacific and 4:00pm GMT for the UK/Europe run do not agree. The '4:00pm GMT' figure is not in the pack's quote or summary and is unverified here. Which figure was meant is unresolved.",
  "Alias collision: the bare title 'Thunder Falls Racing Challenge' is the exact title of quest 7036 (locale:7036), a housing feature. No bare alias is recorded; quest 7036 is not attached to this event.",
  "NPC lead only: locale:31494 ('Do you wanna go fast? Head to Thunder Falls and drive against the best! SERVER 1') is tagged with this event's context, but the speaker is unidentified. npcs is empty.",
  "No items or sourced rewards. The winner-takes-all outcome is not a prize item.",
  "Other events kept separate by judgement, not verified text: Thunder Falls Sprint Challenge (locale:3339), Thunder Falls Endurance Challenge (locale:3340), 'Kart Racing at Thunder Falls!' (locale:3244), Thunder Falls Demolition Derby (locale:6678, article 1910). Their text was not re-checked in this pass. 'Racing Challenge' also names Wildwood Racing Challenge (article 2045, locale:7142) and Snow Day: Frost Ridge Racing (locale:31310); not merged.",
  "Pack's fact:event for article 2009 says 'ran' while the verbatim quote says 'will be'; the pack may be merging an announcement with a recap. Not resolved."
 ]
}
