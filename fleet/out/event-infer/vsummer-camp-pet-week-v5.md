<!-- fleet job=event-infer id=vsummer-camp-pet-week-v5 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6288, 7079, 6, 2397] model=claude-haiku-5-5 -->
# Summer Camp - Pet Week

## Result: two linked records (the pack merged them; split as the critiques asked)

### 1. Parent: Pet Week (2010 Summer Camp finale theme)
```json
{"event": {"name": "Summer Camp - Pet Week", "aliases": ["Pet Week (2010 Summer Camp finale theme)"]},
 "kind": "weekly",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Crossroads", "Sanctuary"],
 "npcs": [],
 "quests": [],
 "activities": ["Pet Parade, a child activity (see record 2)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Pet Week was announced as the final weekly theme of the 2010 Summer Camp community event season ('We are going to end the season with this week's theme... Pet Week!'). The article is a pre-launch announcement, so it does not prove the theme ran.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1775"},
  {"claim": "The article describes a pet parade from Crossroads to Sanctuary and an expected schedule of in-game and TCG events; it has a relative posting time only.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1775"},
  {"claim": "Summer Camp was a 13-week virtual themed event announced in June 2010.", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "Summer Camp was released on June 7, 2010.", "source": "http://tentonhammer.com/node/86237"}
 ],
 "confidence": 0.3,
 "open": [
  "Pet Week has no absolute date in any source, so it has no occurrence. Its only source (articleId 1775) is a preview.",
  "Removed from the earlier answer: 'pet showing and mount riding'. The article text in the pack does not contain it (only the fact statement did).",
  "The season end is not stated. The 13-week run is an inference and sets no end date.",
  "The expected in-game and TCG schedule named in articleId 1775 is not in the pack, so no items or quests are attached.",
  "Pet Parade names are shared with other parades (articleId 516, Oct 23 2009, Blackspore; articleId 877 Dress Up Your Pet Day; articleId 889 costume parade, Wugachug). These are separate events and are not included here. Locale 31294 conflicts with the 2010 route and is not used. Locale 424963/424964 carry a dev_note flag and are not used.",
  "Locale 31293 ('Pet Parade') is a name-only match and does not place Pet Week."
 ]}
```

### 2. Child: Pet Parade (Summer Camp 2010, Server 1)
```json
{"event": {"name": "Pet Parade (Summer Camp 2010)", "aliases": ["Pet Parade"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Sept 2, 2010 (Thursday), US/LatAm session, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"year": 2010, "when": "Sept 3, 2010 (Friday), UK/Europe session, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"}
 ],
 "recurring": null,
 "zones": ["Crossroads", "Sanctuary"],
 "npcs": [],
 "quests": [],
 "activities": ["Players brought pets from Crossroads and marched to the area near the Sanctuary warpstone."],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "The Pet Parade started in Crossroads, marched to the area near the Sanctuary warpstone, was held on Server 1 on September 2 and 3, 2010 (US/LatAm and UK/Europe times), and was the last Summer Camp event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"}
 ],
 "confidence": 0.6,
 "open": [
  "Session times were not confirmed, so none are given. The 'biggest yet' quote was not verified and is dropped.",
  "The article's publication date is not in the pack. The year 2010 and the September dates come from the event text, not a posting date.",
  "Whether this parade is the Pet Week theme's parade (articleId 1775 mentions a parade) is inferred from matching route and season. The link is not explicit in the sources."
 ]}
```
