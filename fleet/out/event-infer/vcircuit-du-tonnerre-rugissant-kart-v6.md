<!-- fleet job=event-infer id=vcircuit-du-tonnerre-rugissant-kart-v6 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[7501, 8052, 6, 2689] model=claude-haiku-5-5 -->
# Circuit du Tonnerre Rugissant community kart event

{
 "event": {
  "name": "Community Event: Thunder Falls Racing Challenge",
  "aliases": [
   "Circuit du Tonnerre Rugissant community kart event (source title of French article 2015, posted 2011-01-27; same 27-28 Jan 2011 sessions on Server 1; link inferred from matching dates, server and Kart Race Lobby access)",
   "Thunder Falls Speedway community kart race (article 2009 wording)"
  ]
 },
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2011,
   "when": "Thursday 27 January 2011, US/Latin America session, Server 1. Time unresolved: article 2015 says '3h (heure du Pacifique)'; the 3:00pm Pacific figure in the earlier draft is not verified because article 2009 was not re-read in full.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (date and Server 1 confirmed by its summary); http://www.freerealms.com/article/detail.action?articleId=2015&request_locale=en_US (quote 'Jeudi 27 janvier 2011 3h (heure du Pacifique)')"
  },
  {
   "year": 2011,
   "when": "Friday 28 January 2011, UK/Europe session, Server 1. Time unresolved between sources: article 2015 gives '18h (Heure de Paris) / 4h:00 GMT' (internally inconsistent; 18:00 Paris = 17:00 GMT). The earlier 9:00am Pacific figure (= 17:00 GMT = 18:00 Paris) matches the Paris time but is not verified as quoted text.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009 (date and Server 1 confirmed by its summary); http://www.freerealms.com/article/detail.action?articleId=2015&request_locale=en_US (quote 'Vendredi 28 janvier 2011 18h (Heure de Paris)/ 4h:00 GMT')"
  }
 ],
 "recurring": null,
 "zones": ["Thunder Falls Speedway (kart track near Lakeshore; article 169 says it was added by the Speedway Thunder update, no exact date)"],
 "npcs": [],
 "quests": [],
 "activities": [
  "Teleport to Thunder Falls Speedway and click the Kart Racing Lobby icon (article 2009)",
  "Join a race about to begin, or start one (article 2009)",
  "Player-versus-player kart race, winner takes the whole race (article 2009)",
  "Select Thunder Falls as the track when creating a race (article 2009)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Client names the event 'Community Event: Thunder Falls Racing Challenge'", "source": "locale:2786; locale:31486"},
  {"claim": "Client description: join the Community Team for a fast-paced race at Thunder Falls Speedway, Ambassador Events, SERVER 1", "source": "locale:2787"},
  {"claim": "Article 2009 announces a player-versus-player kart race at Thunder Falls Speedway on Server 1, on January 27, 2011 (U.S./Latin America) and January 28, 2011 (UK/Europe)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"claim": "Article 2009 says a weekly Community Event was a winner-takes-all kart race at Thunder Falls Speedway (past tense, text only)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
  {"claim": "Article 2015 (French) announces a kart community event at the Circuit du Tonnerre Rugissant on Server 1 with the same two dated sessions; capture 2011-06-04, posting date relative only", "source": "http://www.freerealms.com/article/detail.action?articleId=2015&request_locale=en_US"},
  {"claim": "Players joined a race via the Kart Racing Lobby icon at Thunder Falls Speedway", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status unsure: the sources announce two dated sessions (27-28 Jan 2011) and one past-tense 'was' line. No source confirms they ran. Not wireable until confirmed.",
  "Recurrence: 'weekly' rests on a single phrase in article 2009. Only two dated sessions exist, so recurring is null; no schedule is set.",
  "Session times conflict and are unresolved: Thursday 3h Pacific (article 2015) vs 3pm Pacific (earlier draft, unverified). Friday 18h Paris / 4h GMT (article 2015, internally inconsistent) vs 9am Pacific (earlier draft, unverified; equals 17:00 GMT = 18:00 Paris) vs 16:00 European time (earlier draft's article 2011, not in the pack). Re-read article 2009 and 2015 in full to settle.",
  "Name link: the French title is the same event by inference (same dates, Server 1, Kart Race Lobby). Client names are canonical.",
  "Spanish name 'Torrentrueno' is not an alias; it is not confirmed as the same track or event.",
  "Quest candidates unconfirmed: locale 7036 (quest_title 'Thunder Falls Racing Challenge') and locale 31494 (NPC dialog). No source ties them to the sessions, so quests is empty.",
  "NPCs (Laurin, Chase Wheeler, Ace O'Mally, Linx Redline) are Thunder Falls residents in the client; no source ties them to this event.",
  "No items, prices, currency or rewards are tied to this event in the pack.",
  "Excluded: article 2048 (Hojasilvestre track, 10 March 2011) and video frames video:kNZtSg_Qrsw/00120.jpg and 00122.jpg (different track or undated).",
  "Wireable: false. Two dated sessions and a zone are not enough to schedule a live event; live status and times must be confirmed first."
 ]
}
