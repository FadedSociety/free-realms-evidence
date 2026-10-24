<!-- fleet job=event-infer id=vholiday-celebrations-v5 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[8311, 8943, 6, 1700] model=claude-haiku-5-5 -->
# Annual holiday celebrations

## Result: no single live event identified for "Annual holiday celebrations"

The pack names no event. Its only source is the 2011 anniversary post (http://www.freerealms.com:80/article/detail.action?articleId=2109, dated 2011-04-28). That post says Free Realms had "annual holiday celebrations that bring the gaming community together" and lists "annual holiday events" among the year's updates. It gives no event name, date, zone, NPC, item or price. A lookup of articles, wiki and client for the phrase returned only that article.

```json
{
  "event": {"name": "Annual holiday celebrations (unidentified umbrella, not an event)", "aliases": []},
  "kind": "other",
  "live": "unsure",
  "occurrences": [],
  "recurring": null,
  "zones": [], "npcs": [], "quests": [], "activities": [], "items": [], "rewards": [],
  "evidence": [
    {"claim": "Free Realms ran 'annual holiday events' (generic, no event named, no dates)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2109"}
  ],
  "confidence": 0.1,
  "open": [
    "The pack does not name an event, so no event record can be built from it. The earlier 'Snow Days' answer was not carried over: nothing in this pack ties Snow Days to the phrase 'annual holiday celebrations'. It can be a separate pack for Snow Days only.",
    "Candidate holiday events that need their own packs: Snow Days (Dec 2009-Jan 2010 dated by article 705; Dec 2010 party dated by article 1953; 2011 'Snow Days is HERE' in article 2428 with no month); Super Spooktacular Halloween (article 1854); Fall Harvest/Thanksgiving (wiki Raw Turkey, Nov 2012-2013); Black Friday 2013 (wiki Geek Outfit bundle); a Fourth of July holiday (TenTonHammer node/86237).",
    "Merge risk: the SOE '12 Days of Holidays' promotion (articles 2813, 2827, 2457, 2441, 2442, 2433, 2455; Dec 13-24, 2011 and 2012) is a different event from Snow Days. Do not merge them.",
    "Snow Days-specific conflicts still open for its own pack: article 1953 vs wiki Community Events on whether the Wintery Basin party was 2010 or 2011; 'Snowhill Snow Days' is a zone label, not a verified alias; 2012 run is wiki-only."
  ]
}
```

Next step: supply a pack for one named event (for example, Snow Days or Super Spooktacular Halloween) with its own article URLs, and this record can be rebuilt for that event.
