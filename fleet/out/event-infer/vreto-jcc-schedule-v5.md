<!-- fleet job=event-infer id=vreto-jcc-schedule-v5 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[7518, 8706, 6, 2684] model=claude-haiku-5-5 -->
# Reto JCC schedule

{
 "event": {"name": "Reto JCC (Spanish-language weekly JCC community event)", "aliases": ["Evento Comunitario: Reto JCC (pack-only title, unconfirmed by lookup)", "Juego de Cartas de Coleccion (JCC) community event"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": null, "when": "Friday 20 November, 15:00-17:00 Pacific Time (US and Latin America, Server 1)", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event: 'The [JCC] event session for US and Latin America was Friday 20 November, 15:00-17:00 Pacific time, on Server 1'; quote 'Viernes 20 de noviembre 1500 – 1700 Tiempo Pacifico')"},
  {"year": null, "when": "Friday 20 November, 09:00-11:00 Pacific Time (UK and Europe, Server 1), listed also as 18:00-20:00 local", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event: 'The [JCC] event session for UK and Europe was Friday 20 November, 09:00-11:00 Pacific time (18:00-20:00 local listed), on Server 1'; quote '0900 – 1100 Tiempo Pacifico / 1800 – 2000')"}
 ],
 "recurring": null,
 "zones": ["Crossroads (Encrucijada)", "JCC lobby (enterable from anywhere in the game)"],
 "npcs": [],
 "quests": [],
 "activities": ["Player-versus-player JCC (Juego de Cartas de Coleccion) matches: start games, join matches (per article 640 fact:event row)", "Gather at Crossroads/Encrucijada or enter the JCC lobby"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 640 and 641 describe a Spanish-language community event focused on the JCC card game, player versus player.", "source": "http://www.freerealms.com/article/detail.action?articleId=640 ; articleId=641 (fact:event rows)"},
  {"claim": "Article 640 describes players starting games and joining matches; trading cards and watching are stated in its fact:event row.", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event row)"},
  {"claim": "Article 640 and 641 call the event weekly ('weekly community event' / 'evento comunitario semanal'). The weekday is not named in any retrieved source.", "source": "http://www.freerealms.com/article/detail.action?articleId=640 ; articleId=641 (fact:event rows)"},
  {"claim": "Session on Friday 20 November, 15:00-17:00 Pacific, US and Latin America, Server 1 (no year stated).", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event row)"},
  {"claim": "Session on Friday 20 November, 09:00-11:00 Pacific, UK and Europe, Server 1, with 18:00-20:00 listed (time zone of the second figure not named).", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (fact:event row)"},
  {"claim": "Players were invited to meet at Crossroads (Encrucijada) or enter the JCC lobby from anywhere in the game.", "source": "http://www.freerealms.com/article/detail.action?articleId=640 (summary); articleId=641 (summary)"},
  {"claim": "New players were directed to NPC Mar Mita in Pixiewood to start the JCC. Carried from the prior pack's fact:npc rows; not re-found in this pass.", "source": "http://www.freerealms.com/article/detail.action?articleId=641 (summary, prior pack)"}
 ],
 "confidence": 0.4,
 "open": [
  "Name: 'Reto JCC' is a pack name; no article title line confirmed it in this pass. The alias 'Evento Comunitario: Reto JCC' is pack-only.",
  "Year: no article states a year and article dates are null. Friday 20 November matches 2009 by weekday only (inference, not claimed). Needs an article date.",
  "Live status: the articles use past tense for the sessions; no end date. 'unsure' until dated.",
  "Recurrence conflict: articles 640/641 say 'weekly'. Articles 1592, 1593, 1601, 1627 reportedly say JCC events were expected daily (carried from the prior pack; not re-verified here). Recurrence left null until the conflict is settled.",
  "Possible merge: the Friday 09:00 Pacific UK/Europe block matches the general Friday 09:00 Pacific game-event slot in articles 1601/1627 (carried, not re-verified). The session may belong to that general schedule.",
  "Second session's time zone: 18:00-20:00 is unsourced; UK local is not claimed.",
  "Locale: no locale id ties to this event. locale:640 and locale:641 are unrelated; 641 is flagged not_live. Article ids are not locale ids; 1627 is not a locale reference.",
  "Items, rewards, quests: none tied to this event by any source. Kai and other JCC NPCs and TCG content (e.g. articles 1861, 709, 718, 771) are not tied to this event.",
  "Prior critique correction: article 640 does say 'weekly' in its fact:event row, and its fact row includes trade and watch. The earlier claim that it lacks 'weekly' was wrong.",
  "Wireable: false. One dated session with no year, unresolved recurrence, possible merge with the general Friday 09:00 slot, and an unsourced second-session zone."
 ]
}
