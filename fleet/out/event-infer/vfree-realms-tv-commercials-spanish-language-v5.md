<!-- fleet job=event-infer id=vfree-realms-tv-commercials-spanish-language-v5 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8560, 10270, 6, 3470] model=claude-haiku-5-5 -->
# Free Realms TV commercials (Spanish-language)

The pack's single name ("Free Realms TV commercials (Spanish-language)") merges separate commercials in English, Spanish, Portuguese and French. It is not one event. Per the calendar rules, each commercial is its own entry below. None has an absolute post date in the pack, so none can be scheduled and all have empty occurrences and recurring = null. Wireable: no.

```json
[
 {"event": {"name": "Tiger Ride [TV] Spot", "aliases": ["Tiger Ride TV Commercial"]},
  "kind": "promotion", "live": "unsure",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": [], "quests": [], "activities": ["Watch the TV spot on freerealms.com"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "freerealms.com posted a news item announcing a new TV commercial titled 'Tiger Ride [TV] Spot'. Only a relative timestamp ('Posted 2 days, 2 hours ago'); no absolute date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1747"}],
  "confidence": 0.3,
  "open": ["No absolute date. Relative age only."]},

 {"event": {"name": "Party Time [TV] Spot", "aliases": ["Temps de Faire la Fête! (French preview)"]},
  "kind": "promotion", "live": "no",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": [], "quests": [], "activities": ["Preview of the Party Time TV spot"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "PRE-LAUNCH PREVIEW: the official news page offered a 'sneak peek of our newest TV commercial: Party Time!' This is a plan, not a confirmed live run. The capture date (April 2010) is not a post date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1199"},
   {"claim": "French-language preview of the same spot, 'Temps de Faire la Fête!'.", "source": "http://www.freerealms.com/article/detail.action?articleId=1203"}],
  "confidence": 0.3,
  "open": ["Preview only. No evidence it aired; no date."]},

 {"event": {"name": "Second Free Realms TV commercial (Yeti)", "aliases": ["Yeti [TV] Spot"]},
  "kind": "promotion", "live": "unsure",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": ["Abominable Snowman (wiki appearance only)"], "quests": [], "activities": ["Watch the commercial on the site and share it"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "SOE posted that a second television commercial was available to watch on the site and encouraged sharing.", "source": "http://www.freerealms.com/article/detail.action?articleId=746"},
   {"claim": "Second commercial, featuring the Yeti (Spanish post; same spot).", "source": "http://www.freerealms.com/article/detail.action?articleId=757 ; http://www.freerealms.com/article/detail.action?articleId=756&request_locale=en_US"},
   {"claim": "Wiki appearance list includes 'Holiday [TV] Spot' and 'Yeti [TV] Spot'.", "source": "wiki: Abominable Snowman"}],
  "confidence": 0.35,
  "open": ["Undated. 746, 756 and 757 may be the same ad; 757 is the Yeti version. Wiki title only, not a date."]},

 {"event": {"name": "Third Free Realms TV commercial (housing)", "aliases": ["Viviendas commercial"]},
  "kind": "promotion", "live": "unsure",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": [], "quests": [], "activities": ["Watch the housing spot"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "Spanish news post announcing a third TV commercial about housing: 'Nuestro tercer comercial de televisión está aquí para que lo disfrutes.'", "source": "http://www.freerealms.com/article/detail.action?articleId=822&request_locale=en_US"},
   {"claim": "Same quote; likely a duplicate post under a second URL.", "source": "http://www.freerealms.com/article/detail.action?articleId=823&request_locale=en_US"}],
  "confidence": 0.35,
  "open": ["Undated. 822 and 823 may be one post."]},

 {"event": {"name": "Activities TV commercial (dragon flying, biking, housing, outfits, farming)", "aliases": ["New Adventures TV Commercial (Portuguese post 2151)"]},
  "kind": "promotion", "live": "unsure",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": [], "quests": [], "activities": ["Watch the activities spot on the site or on the YouTube channel"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "English post: new TV commercial viewable on the page and the Free Realms Online YouTube channel, showing dragon flying, bike riding, house building, outfit showing and farming.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2147"},
   {"claim": "Spanish posts with the same text.", "source": "http://www.freerealms.com/article/detail.action?articleId=2148 ; http://www.freerealms.com/article/detail.action?articleId=2149"},
   {"claim": "Portuguese post on the new-adventures commercial, viewable on YouTube.", "source": "http://www.freerealms.com/article/detail.action?articleId=2151"},
   {"claim": "Wiki page 'New Adventures TV Commercial' exists.", "source": "wiki: File:Free Realms New Adventures TV Commercial"}],
  "confidence": 0.3,
  "open": ["Undated. 2148 'June 2011' is a capture date, not a post date. Whether 2151 is the same spot as 2147 is not confirmed."]},

 {"event": {"name": "Halloween Super Spooktacular TV commercial", "aliases": ["Halloween [TV] Spot", "Spooktacular [Commercial]"]},
  "kind": "holiday", "live": "unsure",
  "occurrences": [],
  "recurring": null, "zones": [], "npcs": ["Pumpkin Prince (wiki appearance only)"], "quests": [], "activities": ["Watch the Halloween spot"],
  "items": [], "rewards": [],
  "evidence": [
   {"claim": "Spanish news post: 'Un Espacio en la TV - Halloween Super Spooktacular'; relative timestamp only ('7 months, 1 week ago').", "source": "http://www.freerealms.com/article/detail.action?articleId=1876"},
   {"claim": "Wiki appearance pages list 'Halloween [TV] Spot 2010' and 'Spooktacular [Commercial]'.", "source": "wiki: Pumpkin Prince"}],
  "confidence": 0.35,
  "open": ["Year not confirmed by an article. 2010 comes only from the wiki title 'Halloween [TV] Spot 2010'. Relative timestamp only."]}
]
```

**Dropped / not included**
- Article 752 (Spanish series post): promotes new TV commercials and a video, names no commercial, has no date. The alias "Un Espacio en la TV: Free Realms y las Festividades" is not in the captured text, so it is dropped.
- Ninja Prank [Commercial] (article 82) and Super Ego [Commercial] (article 95): wiki appearance pages only. No article text or date, so no entry.
- The merged series entry and its generic aliases ("Free Realms TV Spot", "Free Realms Commercial") are removed. They would collide across commercials.
- Locale-id checks are dropped. The locale table is separate from article ids and says nothing about articles.

**Open**
- No absolute post date exists in the pack for any commercial. Occurrences stay empty until dated sources are found.
- Possible duplicates: 746/756/757 (Yeti), 822/823 (housing), 2147/2148/2149 (activities).
- Whether 2151 (Portuguese, New Adventures) is the same spot as 2147 is not confirmed.
- Recommendation: do not log any of these as a live calendar event yet. Party Time (1199/1203) is a pre-launch preview, not a live run.

Confidence is low overall (about 0.3 to 0.35 per entry).
