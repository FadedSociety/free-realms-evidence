<!-- fleet job=event-infer id=vaccount-and-station-cash-maintenance-v4 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5895, 6134, 6, 1734] model=claude-haiku-5-5 -->
# Account and Station Cash maintenance

```json
{
  "event": {
    "name": "Account and Station Cash maintenance",
    "aliases": ["Servicio de Cuentas y Mantenimiento de Comercio – jueves 8 de julio"]
  },
  "kind": "other",
  "live": "unsure",
  "occurrences": [
    {
      "year": 2010,
      "when": "Thursday 8 July 2010, 10:00 AM to 12:00 PM TP (about 2 hours), as announced",
      "source": "http://www.freerealms.com/article/detail.action?articleId=1613"
    }
  ],
  "recurring": null,
  "zones": [],
  "npcs": [],
  "quests": [],
  "activities": [],
  "items": [],
  "rewards": [],
  "evidence": [
    {
      "claim": "Notice 1613 (Spanish) announces that account services, all Station Cash services and the purchase catalog will be offline for about 2 hours on Thursday 8 July 2010, 10:00 AM to 12:00 PM TP. Quote: 'tendrá una duración aproximada de 2 horas este Jueves, 08 de julio del 2010, comenzando a las 10:00 AM hasta las 12:00 PM TP'. This is a pre-announcement; it does not confirm the window ran.",
      "source": "http://www.freerealms.com/article/detail.action?articleId=1613"
    },
    {
      "claim": "The article's own summary says it is a service notice with no quests, NPCs, zones, items, rewards or activities, and that the page does not name Free Realms in its body.",
      "source": "http://www.freerealms.com/article/detail.action?articleId=1613"
    },
    {
      "claim": "No wiki game-event page was found. Category:Site maintenance exists but holds wiki-administration pages, not game events.",
      "source": "wiki Category:Site maintenance"
    },
    {
      "claim": "A 28 July 2010 update (articleId 1711, servers offline after 9pm PDT for 2-4 hours) is a different event and is not merged here.",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=1711"
    }
  ],
  "confidence": 0.2,
  "open": [
    "Not a gameplay event. This is a service/maintenance notice. The schema has no maintenance kind, so 'other' is the nearest fit. Recommend a separate service/maintenance track, and do not schedule it as a game event (wireable: false).",
    "live is 'unsure': the only source is a scheduled pre-announcement. Its article date is null in the pack, and no archived source confirms the window ran as stated.",
    "Article 1614 was removed as a source. The pack holds no quote from it, and my lookup of its content returned nothing. It may be a second notice for the same window, but this is unverified. Retrieve its title and text from http://www.freerealms.com/article/detail.action?articleId=1614 before adding it.",
    "The forum and login slowdown warning was dropped. No quote in the pack supports it.",
    "My lookup for the 1613 text (Spanish maintenance and Station Cash, 8 July 2010) also returned no matches in the articles or wiki indexes. The 1613 claims therefore rest on the pack's quote alone and should be re-checked against the live article.",
    "The pack title may merge the account-services notice and the Station Cash notice. Treat 'Account and Station Cash maintenance' as a generic label, not a canonical event name.",
    "Wiki check was limited: Category:Site maintenance was seen, but its full member list was not read, and searches for 'Station Cash maintenance 2010' found no game-event pages.",
    "The 28 July 2010 update (articleId 1711) is a separate event and needs its own row."
  ]
}
```
