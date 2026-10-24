<!-- fleet job=event-infer id=vcomunitario-carreras-en-la-pista-de-hojasilvestre-kart-races-v5 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[7731, 9158, 6, 3351] model=claude-haiku-5-5 -->
# Comunitario: Carreras en la Pista de Hojasilvestre (Community Event: Kart Races at Hojasilvestre Race Track)

```json
{
 "event": {
  "name": "Wildwood Racing Challenge",
  "aliases": [
   "Comunitario: Carreras en la Pista de Hojasilvestre (Spanish notice, article 2048; article-only alias)",
   "Course de karts au Circuit du Bois Sauvage (French notice, article 2049; article-only alias)",
   "Summer Camp Racing Week is NOT an alias (separate event, article 1700, July 2010)"
  ]
 },
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": 2011, "when": "Thursday 10 March 2011, 3pm Pacific Time (U.S. and Latin America), Server 1 (announced session)", "source": "http://www.freerealms.com/article/detail.action?articleId=2049 (quote: \"jeudi 10 mars 2011 3pm Pacific Time (U.S. et l'Amérique Latine) Serveur 1\"); also http://www.freerealms.com:80/article/detail.action?articleId=2045 (pack quote for Thursday March 10, 2011 3pm Pacific)"},
  {"year": 2011, "when": "Friday 11 March 2011, 18:00 CET (Paris) / 4pm GMT label as printed (UK and Europe), Server 1 (announced session); 09:00 Pacific is derived arithmetic (CET = UTC+1, PST = UTC-8)", "source": "http://www.freerealms.com/article/detail.action?articleId=2049 (quote: \"vendredi 11 mars 2011 18:00am CET (Heure de paris)/ 4:00pm GMT (UK et l'Europe) Serveur 1\"); Spanish notice 2048 Friday session per pack summary"}
 ],
 "recurring": null,
 "zones": ["Wildwood Speedway (client/wiki name; source: articles 2045 and wiki Speedways)"],
 "npcs": [],
 "quests": [],
 "activities": [
  "Kart race on the speedway course, south of the Crossroads Warpstone (articles 2045, 2048, 2049)",
  "Players were asked to wear a helmet for the race (article 2049)",
  "Off-track party beside the course for non-racers (articles 2045, 2049)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 2045 (English) announces the Wildwood Racing Challenge, a kart race run by the Community Team Ambassadors at the Wildwood Speedway, just south of the Crossroads Warpstone, with a party just outside the course.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2045"},
  {"claim": "Article 2049 (French) gives the Thursday session as 10 March 2011 3pm Pacific (Americas) and the Friday session as 11 March 2011 18:00 CET (UK/Europe), both Server 1, on the Bois Sauvage circuit.", "source": "http://www.freerealms.com/article/detail.action?articleId=2049"},
  {"claim": "Article 2049 says the race is at the Bois Sauvage circuit and that non-racers could join an off-track party beside the race; players were told to wear a helmet.", "source": "http://www.freerealms.com/article/detail.action?articleId=2049"},
  {"claim": "Article 2048 (Spanish) invites players to the kart race at the Pista de Carreras de Hojasilvestre, south of the Crossroads teleport stone.", "source": "http://www.freerealms.com/article/detail.action?articleId=2048"},
  {"claim": "The three notices (2045, 2048, 2049) are merged as one event by inference only: same track, format, party and March 2011 session dates. No article text states the merge; the Spanish and French names are article-only aliases.", "source": "articles 2045, 2048, 2049"},
  {"claim": "Summer Camp Racing Week (article 1700, July 2010) and the Torrentrueno weekly kart challenge (articles 2011, 2013) are separate events and are not merged.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1700; http://www.freerealms.com/article/detail.action?articleId=2011"},
  {"claim": "Article 889 does not support a weekly kart race, so no recurrence is claimed.", "source": "http://www.freerealms.com/article/detail.action?articleId=889"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status unconfirmed: all notices are future-tense invitations, article post dates are not in the pack, and no post-event confirmation was found. Treat the sessions as announced, not confirmed as run.",
  "Article 2049 labels 18:00 CET as '4:00pm GMT'; that is inconsistent (18:00 CET = 17:00 GMT). The CET figure is used. The 09:00 Pacific Friday time comes from article 2048/2045 per the earlier draft and is not re-quoted here; it equals 18:00 CET by arithmetic.",
  "Article 2045's 'Friday 9:00am Pacific / 4:00pm GMT' combination is internally inconsistent (9am PT = 17:00 GMT). Not used as a source quote.",
  "Thursday 10 March session in 2048 (Spanish) is unverified: the Spanish date text was not retrieved. Friday session in 2048 is per the pack summary only.",
  "Merge of 2045/2048/2049 is an inference; confirm by reading all three in full. If session facts differ, split into separate events.",
  "Track naming: 'Wildwood Speedway' (client/wiki, article 2045) vs 'Hojasilvestre' (2048) and 'Bois Sauvage' (2049). A client-text lookup for 'Hojasilvestre' returned no match, so the same-track link rests on the articles only.",
  "Not merged: '[Wildwood] Demolition Day' (wiki community event, demolition derby on the same speedway), the March 2011 luau (articles 2064, 2065), Summer Camp Racing Week (1700), Torrentrueno weekly kart challenge (2011, 2013).",
  "No quests, NPCs, items, prices or rewards are tied to this event by any source. Wiki kart items (Race Away Jacket, Buccaneer Racer, Arrow Runner, Wicked Racer, Splash Zipper, USA Racer) and Johnny Thunder are not attached.",
  "ID checks: locale:2048 does not exist; locale:2045 is unrelated UI text; locale:2049 is a FLAGGED placeholder. None is event evidence.",
  "Critique fixes applied: removed the unverified 2045 Pacific-Friday and 2048 clock-time claims; labelled sessions as announced; kept the merge inferred; kept the track aliases article-only; removed off-track party from unverified claims (now supported by 2049 text)."
 ]
}
```
