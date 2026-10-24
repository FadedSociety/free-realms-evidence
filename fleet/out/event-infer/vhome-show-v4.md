<!-- fleet job=event-infer id=vhome-show-v4 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[7504, 10632, 6, 2785] model=claude-haiku-5-5 -->
# Home Show

{
 "event": {
  "name": "Community Event: House Party Tuesday",
  "aliases": ["House Party Tuesday", "House Party", "Every Tuesday is our House Party!"]
 },
 "kind": "weekly",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Tuesday March 23, 2010, 4pm Pacific Time (U.S. and Latin America), Server 1 (first House Party)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
  {"year": 2010, "when": "Tuesday April 20, 2010 (article post date only; the session line is not quoted, so treat as unconfirmed as a session date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263"},
  {"year": 2012, "when": "Tuesday January 31, 2012: special Wilds Condo edition, Sanctuary, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2492; http://www.freerealms.com:80/article/detail.action?articleId=2493; http://www.freerealms.com/article/detail.action?articleId=2494"},
  {"year": null, "when": "Tuesday October 3 (year not stated in the sources, likely 2011 or 2012; unverified)", "source": "http://www.freerealms.com/article/detail.action?articleId=2286"}
 ],
 "recurring": "weekly on Tuesdays (articles state 'every Tuesday' and 'run every Tuesday'); the wiki says a weekly event ran 'most Tuesdays', so some weeks may have been skipped",
 "zones": ["Sanctuary (Server 1)"],
 "npcs": ["House Party (Community Team character who teleports to featured player houses)"],
 "quests": [],
 "activities": ["Meet in Sanctuary with the Community Team", "Follow the House Party character to visit decorated player homes", "Wilds Condo edition: tour about 8 player-decorated Wilds Condos (articleId=2493)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Weekly Tuesday community event meeting in Sanctuary to visit decorated player homes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1214; articleId=1452; articleId=1536; articleId=1168"},
  {"claim": "First House Party was Tuesday March 23, 2010, 4pm Pacific (U.S. and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
  {"claim": "Special Wilds Condo edition held Tuesday January 31, 2012 in Sanctuary, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2492; articleId=2493; articleId=2494"},
  {"claim": "Wilds Condo Tuesday is a special edition of the House Party (not a separate event)", "source": "wiki: Community Events"},
  {"claim": "Client UI title 'Community Event: House Party Tuesday' with body 'Join the Community Team on a tour of homes and lots!'", "source": "locale:428314; locale:428315"},
  {"claim": "Home Show is a separate player-submitted housing spotlight, not an alias of this event. Article 2493 invites photos to homeshow@soe.sony.com as a related feature.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1827; articleId=2493"},
  {"claim": "Featured Home Show houses are highlighted during House Party visits when possible (a link between the two features, not an alias)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209; articleId=1452"}
 ],
 "confidence": 0.75,
 "open": [
  "PACK MISLABEL: the input pack is titled 'Home Show' and its names_seen says 'Home Show', but its facts, summaries and critiques are all about House Party Tuesday. I rebuilt the answer around House Party Tuesday. Home Show is a separate housing feature and is not listed as an alias.",
  "Do not merge with other events: 'Community Event: New Year House Party' (locale 31364) and 'New Year House Party' (locale 426815); 'Community Event: Pirate House Party' (locale 436162); 'Community Event: Snow Days House Party' (locale 436455; 436459 is a duplicate FLAG); 'Treehouse Party' (locale 430483). Festival of Hearts (locale 3545) is flavor text only.",
  "The 3pm Pacific first session on April 6, 2010 (article 1209 summary) is not used. Its post date is null and the quote is not checked. The first session I can source is March 23, 2010 at 4pm (article 1168).",
  "Article 1263 gives session times for two regions. The pack does not name the regions or quote the times, so they are not recorded.",
  "The October 3 session (article 2286) has no year in the sources, so its year is unverified.",
  "Futuristic Bicycle: the wiki Futuristic Bicycle page says it was received by touring the House Party homes, but that page is not in the wiki event category. It is left out until a source ties it to the event.",
  "Zones: only Sanctuary is sourced. The 'Seaside' string appears only as a locale key prefix (428314, 428315), not as a zone.",
  "Quests: none found tied to House Party Tuesday. Rewards: none sourced. Item prices: none sourced.",
  "The wiki's 'most Tuesdays' wording conflicts a little with the article 'every Tuesday' wording. The weekly pattern is kept on the article quotes; skipped weeks are not documented."
 ]
}
