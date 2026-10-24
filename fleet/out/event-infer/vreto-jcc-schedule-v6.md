<!-- fleet job=event-infer id=vreto-jcc-schedule-v6 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[20319, 14005, 8, 2512] model=claude-haiku-5-5 -->
# Reto JCC schedule

{"event": {"name": "Reto JCC", "aliases": ["Evento Comunitario: Reto JCC (article title, articleId 640 and 641)", "JCC community event (Juego de Cartas de Coleccion)"]},
"kind": "community",
"live": "unsure",
"occurrences": [
 {"year": null, "when": "Friday 20 November, 15:00-17:00 Pacific Time, USA and Latin America, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event: 'The [JCC] event session for US and Latin America was Friday 20 November, 15:00-17:00 Pacific time, on Server 1'; quote 'Viernes 20 de noviembre 1500 – 1700 Tiempo Pacifico')"},
 {"year": null, "when": "Friday 20 November, 09:00-11:00 Pacific Time, UK and Europe, Server 1 (article also lists 18:00-20:00, time zone not named)", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event: 'The [JCC] event session for UK and Europe was Friday 20 November, 09:00-11:00 Pacific time (18:00-20:00 local listed), on Server 1'; quote '0900 – 1100 Tiempo Pacifico / 1800 – 2000')"}
],
"recurring": "weekly (articles 640 and 641 describe it as a 'weekly' / 'semanal' community event); weekday not named in any source",
"zones": ["Crossroads (Encrucijada)", "JCC lobby (enterable from anywhere in the game)", "Pixiewood (Mar Mita's location, per article 641 summary)"],
"npcs": ["Mar Mita"],
"quests": [],
"activities": ["Player-versus-player JCC card matches: start games, join matches, trade cards, watch (article 640 fact:event)", "Gather at Crossroads/Encrucijada or enter the JCC lobby", "New players start at NPC Mar Mita in Pixiewood"],
"items": [],
"rewards": [],
"evidence": [
 {"claim": "Article titled 'Evento Comunitario: Reto JCC' exists for both articleId 640 and 641; both are community events about the JCC card game, player versus player, described as weekly.", "source": "refs articles/articles.json:17507 and :17521; http://www.freerealms.com/article/detail.action?articleId=640 ; articleId=641 (fact:event rows)"},
 {"claim": "Players meet at Crossroads (Encrucijada) or enter the JCC lobby from anywhere; new players start with NPC Mar Mita (Pixiewood).", "source": "http://www.freerealms.com/article/detail.action?articleId=641 (summary); articleId=640 (summary)"},
 {"claim": "Sessions on Friday 20 November, 15:00-17:00 Pacific (US/LatAm) and 09:00-11:00 Pacific (UK/Europe), both Server 1.", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event rows; lookup confirmed)"},
 {"claim": "Article 641 summary says the event 'ran' on Friday 20 November in two time blocks, so the sessions are past, not a preview.", "source": "http://www.freerealms.com/article/detail.action?articleId=641 (summary)"}
],
"confidence": 0.45,
"open": [
 "Year not stated. Both article dates are null (articles.json:17509, :17523); article 640 was captured 2011-06-04, which is a capture date, not an event date. Friday 20 November matches 2009 and 2015 by weekday; no year is claimed.",
 "Live status: sessions are described in past tense, but there is no end date or year, so 'unsure'.",
 "Recurrence: 'weekly' is sourced from both articles. Earlier notes claim other articles (1592, 1593, 1601, 1627) say JCC events were daily; not verified here and left unresolved.",
 "Possible merge: the Friday 09:00 Pacific block may match a general Friday 09:00 game-event slot. Not verified; not claimed as a merge.",
 "Second session's 18:00-20:00 time zone is unsourced; UK local time is not claimed.",
 "No quests, wiki category members, or items tie to this event. No locale id ties to it (locale:641 is flagged not_live).",
 "Name: the title 'Reto JCC' is the short form; the full article title is 'Evento Comunitario: Reto JCC'."
]}
