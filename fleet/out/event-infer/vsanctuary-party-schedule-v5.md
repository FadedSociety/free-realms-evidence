<!-- fleet job=event-infer id=vsanctuary-party-schedule-v5 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7567, 8337, 6, 2939] model=claude-haiku-5-5 -->
# Sanctuary party schedule

{"event": {"name": "Sanctuary Trick or Treat party (2nd Annual Super Spooktacular)", "aliases": ["Trick or Treat in Sanctuary", "Fiesta de Truco o Trato en Santuario"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Thursday 21 October 2010, 15:00 Pacific Time (US and Latin America), Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=1870; http://www.freerealms.com:80/article/detail.action?articleId=1864"},
  {"year": 2010, "when": "Friday 22 October 2010, 09:00 Pacific Time / 16:00 GMT (UK and Europe), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864; http://www.freerealms.com/article/detail.action?articleId=1870"}
 ],
 "recurring": null,
 "zones": ["Sanctuary"],
 "npcs": ["Halloween Harry (location contested: Sanctuary per wiki and client objectives; Pixiewood per articles 1854/1860/1861 and locale:416800)"],
 "quests": ["Trick or Treat in Sanctuary", "Trick-or-Treat around Sanctuary"],
 "activities": ["Attend the community party in Sanctuary, collect candy and show off costumes near the Sanctuary Warpstone", "Complete daily Trick or Treat quests for candy from shop owners and Halloween Harry"],
 "items": [],
 "rewards": ["Candy from daily Trick or Treat quests"],
 "evidence": [
  {"claim": "Article 1864 (English) says a community Trick or Treat party 'was held' in Sanctuary as part of the 2nd Annual Super Spooktacular, with daily Trick or Treat quests and candy handed out by shop owners and Halloween Harry. Past tense supports live = yes.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864"},
  {"claim": "Article 1864 gives Friday October 22nd, 2010 9:00am Pacific Time / 4:00pm GMT (UK and Europe), Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864"},
  {"claim": "Article 1870 (Spanish) gives Jueves 21 de octubre del 2010 15 hrs Pacific (US and Latin America), Server 1, and Viernes 22 de octubre del 2010 09:00 hrs Pacific / 16:00 European (UK and Europe), Server 1. It announces the party as celebrating the second anniversary of the Super Spooktacular.", "source": "http://www.freerealms.com/article/detail.action?articleId=1870"},
  {"claim": "The client names the party quest 'Trick or Treat in Sanctuary' (locale:14563); its objective (locale:14567) says to collect candy and show off costumes at a party near the Sanctuary Warpstone.", "source": "locale:14563; locale:14567"},
  {"claim": "'Trick-or-Treat around Sanctuary' (locale:415821, objective locale:415370) is a daily candy quest in Sanctuary. Article 1864 ties daily Trick or Treat quests to this party, but the client text does not name the party itself, so the tie is article-based plus zone.", "source": "locale:415821; locale:415370; http://www.freerealms.com:80/article/detail.action?articleId=1864"},
  {"claim": "Halloween Harry is placed at Sanctuary by the wiki Sanctuary and Halloween Harry pages and client objectives locale:416853 and locale:415943. Articles 1854, 1860, 1861 and locale:416800 place him at Pixiewood. Unresolved.", "source": "wiki: Sanctuary; wiki: Halloween Harry; locale:416853; locale:415943; locale:416800; http://www.freerealms.com/article/detail.action?articleId=1854"}
 ],
 "confidence": 0.6,
 "open": [
  "Pack title 'Sanctuary party schedule' merges several events. Excluded: the weekly House Party Tuesday articles, Birthday, Luau, Pet, Postal, Winter, Seaside Beach, New Year's Eve Ball, the Referee Heliotrope party, and the Ghostly Pet Party (Blackspore, 7-8 Oct 2010; articles 1845, 1849, 1850), which is a separate community event.",
  "The Super Spooktacular parent event is larger. Its items (Parachute, 2009 Member Pack, Necrowart Wrist Wraps, Chatty Costume, and the 899 and 89 station_cash prices from undated video frames) belong to the parent, so items is empty.",
  "Halloween Harry location conflict (Sanctuary vs Pixiewood) is unresolved.",
  "Article 1870's Pixiewood decorating line and the Chiller Boomboxes/cassette radio props (article 1864 and 1870) were not re-verified in this pass; they are not included as claims.",
  "Article 1870's 'daily candy from shop owners and Halloween Harry' wording was not re-found; the daily-candy claim rests on article 1864.",
  "Article posting dates for 1864 and 1870 are null; year 2010 comes from the quoted dates.",
  "Recurring is null: no 2011+ Sanctuary party occurrence was found and no article says it recurs.",
  "The 2009 first-run dates (TenTonHammer node 75739) and the 2013 fourth-annual claim (article 2949) are unverified and excluded.",
  "Halloween Harry wiki quests (Bag Snatchers, Candy Gram, A Formal Report, Halloween Fanatic, Delicious Goo'd Candy) are not tied to this party and are excluded.",
  "Confidence 0.6: the live flag rests on article 1864's past tense ('was held'), which was re-confirmed."
 ],
 "critique_fixes": "Quests now include locale:415821 (article-tied, not client-named). Evidence for 2nd-annual wording and daily candy now cites 1864, which was re-verified. Unverified 1870 wording is noted in open."}
