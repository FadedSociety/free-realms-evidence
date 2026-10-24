<!-- fleet job=event-infer id=vwikia-giveaway-v5 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[7075, 7333, 6, 2960] model=claude-haiku-5-5 -->
# Wikia giveaway

**Result: the pack's single event is four fan-site giveaways merged under one name. Split into four entries. None is wireable.**

A lookup for the Wikia, Sunstone Valley and contest terms in articles and wiki returned no matches, so I could not re-read the article or the wiki Category:Fansite page myself. The claims below rest on the pack's article summary and quotes for articleId 2779, plus the critique's check of those quotes. They are not independently re-verified.

```json
[
 {"event": {"name": "Wikia Giveaway @ Twitter (Free Realms fan-site giveaway, 2012)", "aliases": ["Wikia giveaway", "Wikia Giveaway @ Twitter"]},
  "kind": "contest", "live": "unsure",
  "occurrences": [{"year": 2012, "when": "Announcement captured 2012-09-24, posted '3 days, 19 hours ago', so about 2012-09-20 (estimate; year inferred from capture date; no exact date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}],
  "recurring": null, "zones": [], "npcs": [], "quests": [],
  "activities": ["Enter the Wikia giveaway through Twitter, per the rules on the Wikia site"],
  "items": [], "rewards": ["Prize not stated in the sources"],
  "evidence": [
    {"claim": "freerealms.com highlighted a giveaway from Wikia, entered via Twitter ('Wikia Giveaway @ Twitter').", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}
  ],
  "confidence": 0.3,
  "open": ["No exact post date, end date or winner post found.", "Helmet/Glasses items and the @WikiaGames code schedule come only from an undated user blog ('User blog:JAlbor/Free Realms Gear Giveaway'). Excluded: no official tie."]},

 {"event": {"name": "FR.Zam Sunstone Valley Screenshot Contest (2012)", "aliases": ["FR.Zam Sunstone Valley Screenshot Contest", "fan site giveaways"]},
  "kind": "contest", "live": "unsure",
  "occurrences": [{"year": 2012, "when": "About 2012-09-20 (estimate from capture 2012-09-24 and 'posted 3 days, 19 hours ago')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}],
  "recurring": null, "zones": ["Sunstone Valley (named in the contest title only)"], "npcs": [], "quests": [],
  "activities": ["Enter the FR.Zam Sunstone Valley screenshot contest"],
  "items": [], "rewards": ["Prize not stated; the post says prizes include new Sunstone Valley items, unnamed"],
  "evidence": [
    {"claim": "The post highlights giveaways from FR.Zam, Wikia, Mystic Mayhem and Free Realms Insider.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"},
    {"claim": "FR.Zam ran a Sunstone Valley screenshot contest.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}
  ],
  "confidence": 0.3,
  "open": ["No item names, dates or winner post. Entry is not wireable."]},

 {"event": {"name": "Mystic Mayhem Sunstone Valley Contest - $10 SC Code (2012)", "aliases": ["Mystic Mayhem Sunstone Valley Contest", "Sunstone Valley Contest - Cool Prizes! $10 SC Code"]},
  "kind": "contest", "live": "unsure",
  "occurrences": [{"year": 2012, "when": "About 2012-09-20 (estimate from capture date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}],
  "recurring": null, "zones": ["Sunstone Valley (named in the contest title only)"], "npcs": [], "quests": [],
  "activities": ["Enter the Mystic Mayhem Sunstone Valley contest"],
  "items": [], "rewards": ["$10 SC (Sony Cash) code, per the contest title"],
  "evidence": [
    {"claim": "Mystic Mayhem's contest title reads 'Sunstone Valley Contest - Cool Prizes! $10 SC Code'.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"},
    {"claim": "Mystic Mayhem is listed as a Free Realms fansite.", "source": "wiki page Category:Fansite"}
  ],
  "confidence": 0.3,
  "open": ["Wiki claim comes from the pack's summary; I could not re-open the Category:Fansite page.", "No dates or winner post."]},

 {"event": {"name": "Free Realms Insider Weekly Contest - $15 SC Card (2012)", "aliases": ["Free Realms Insider Weekly Contest", "Weekly Contest for $15 SC Card"]},
  "kind": "contest", "live": "unsure",
  "occurrences": [{"year": 2012, "when": "About 2012-09-20 (estimate from capture date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}],
  "recurring": null, "zones": [], "npcs": [], "quests": [],
  "activities": ["Enter the Free Realms Insider weekly contest"],
  "items": [], "rewards": ["$15 SC (Sony Cash) card, per the contest title"],
  "evidence": [
    {"claim": "Free Realms Insider's contest title reads 'Weekly Contest for $15 SC Card'.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2779"}
  ],
  "confidence": 0.3,
  "open": ["'Weekly' appears once, in the title. Not treated as a confirmed schedule, so recurring is null.", "Wiki Fansite claim is from the pack summary, not re-checked."]}
]
```

**Cross-cutting notes**
- Excluded: the in-game "Celebrity Giveaway" (locale:395331/395332) is a Snowhill kart-ticket reward, not a fan-site giveaway.
- Excluded: Ten Ton Hammer "Free Realms Beta [Giveaway]" (April 2009). Different pre-launch event, and its node was not confirmed.
- Sunstone Valley's location (articleId 2781) is a general zone fact and is not evidence that these contests were held there.
- Aliases: the pack's name, "Wikia giveaway", and the four contest titles. No other alias found.
- Items: none named, so the items fields are empty. The client was not searched for Sunstone Valley prize items.
- Do not wire any of these. Each needs an exact post date or a winner post, plus a named item, before it can go on the calendar.
- confidence 0.3 for all four.
