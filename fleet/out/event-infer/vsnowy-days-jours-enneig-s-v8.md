<!-- fleet job=event-infer id=vsnowy-days-jours-enneig-s-v8 status=done turns=1 usd=0.0037 tokens(read,write,in,out)=[0, 9886, 4, 4988] model=claude-haiku-5-5 -->
# Snowy Days (Jours Enneigés)

```json
{
  "event": {
    "name": "Snow Days",
    "aliases": ["Snowy Days", "Snow Days!", "Snow Days Are Back!", "Jours Enneigés"]
  },
  "kind": "holiday",
  "live": "yes",
  "occurrences": [
    {"year": 2010, "when": "December 2010: Wintery Basin Snow Days party, Server 1 (US/Latin America Thu Dec 9, 2010 15:00 Pacific; UK/Europe Fri Dec 10, 2010 9:00am Pacific / 4pm GMT)", "source": "http://www.freerealms.com/article/detail.action?articleId=1953 ; http://www.freerealms.com/article/detail.action?articleId=1959"},
    {"year": 2011, "when": "December 2011: Snow Days 2011 live; webcast held December 8, 2011", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
    {"year": 2013, "when": "December 10, 2013: Snow Days 2013 in-game and Station Cash Marketplace (Game Update 123, dated 12/10/2013)", "source": "wiki:2013 Snow Days Toy Collector Pack ; wiki:Template:News (Game Update 123) ; wiki:Snow Days (Week #2 - 12/10/2013). Wiki-only, no dated article in the pack."}
  ],
  "recurring": "Yearly in December: dated articles for 2010 and 2011 show two December runs; the 2013 run is wiki-sourced. Article 892 (Jan 26, 2010 patch notes) says Snow Days ended and would return the following year.",
  "zones": ["Snowhill", "Wintery Basin"],
  "npcs": [],
  "quests": ["A gift from the Gifting Tree", "Guarding the Gifting Tree", "Snowmen Disassembly", "Silversnow's Sapling"],
  "activities": [
    "Defend the Gifting Tree from the Abominable Snowman and his snowmen with snowballs (article 1955, French, undated)",
    "Take the daily gift from under the Gifting Tree (article 1956; locale:433669)",
    "Spin the Snow Days wheel for bonus prizes (locale:426649)",
    "Attend the Wintery Basin Snow Days party, Dec 2010 (articles 1953, 1959; locale:15043, 15048)",
    "Eat Snow Days cookies from quest and battle rewards (locale:441144)",
    "Fight Robgoblins for Snow Days clothing (articles 2429, 2808 from earlier pack; not re-fetched)"
  ],
  "items": [
    {"name": "Snow Days outfits", "price": null, "currency": null, "source": "article 809 (limited-time Catalog outfits); article 828 (sold in the Marketplace for a limited time). Currency unverified."},
    {"name": "Subarctic Winterwear Jacket", "price": null, "currency": "reward", "source": "wiki:Subarctic Winterwear Jacket (Snow Days quest Snowmen Disassembly)"},
    {"name": "Subarctic Winterwear Gloves", "price": null, "currency": "reward", "source": "wiki:Subarctic Winterwear Gloves (Snow Days quest Silversnow's Sapling)"},
    {"name": "Subarctic Winterwear Boots", "price": null, "currency": "reward", "source": "wiki:Subarctic Winterwear Boots (Snow Days quest Guarding the Gifting Tree)"},
    {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729"},
    {"name": "Bert & Ernie, Ice Troll Scout, Ice Troll Guardian, Yeti Pounder", "price": null, "currency": "station_cash", "source": "wiki:Snow Days (Week #2 - 12/10/2013) ; wiki:Template:News (Game Update 123)"},
    {"name": "2013 Snow Days Toy Collector Pack", "price": null, "currency": "station_cash", "source": "wiki:2013 Snow Days Toy Collector Pack (Marketplace, Dec 10, 2013)"},
    {"name": "Snow Days Toy [2013 Edition] (Bruce)", "price": null, "currency": "reward", "source": "wiki:Bruce (free with the 2013 Toy Collector Pack)"}
  ],
  "rewards": [
    "Subarctic Winterwear Jacket, Gloves and Boots (Snow Days quests)",
    "Snow Days Present (Gifting Tree gift)",
    "Snow Days wheel bonus prizes (locale:426649)",
    "Snow Days outfits (Catalog, limited time)",
    "2013 Toy Collector Pack with Bruce toy (Station Cash Marketplace, wiki-sourced)"
  ],
  "evidence": [
    {"claim": "Snow Days returned to Snowhill with gifts under the Gifting Tree, and the Abominable Snowman attacks are defended with snowballs. Article is undated, so no year.", "source": "http://www.freerealms.com/article/detail.action?articleId=1955"},
    {"claim": "Dec 2010 Wintery Basin Snow Days party: US/Latin America Dec 9, 2010 15:00 Pacific; UK/Europe Dec 10, 2010 9:00am Pacific / 4pm GMT, Server 1.", "source": "http://www.freerealms.com/article/detail.action?articleId=1953 ; http://www.freerealms.com/article/detail.action?articleId=1959"},
    {"claim": "Snow Days 2011 was live, with a webcast held Dec 8, 2011.", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
    {"claim": "Snow Days 2013 introduced in-game Dec 10, 2013 with the Toy Collector Pack.", "source": "wiki:2013 Snow Days Toy Collector Pack ; wiki:Template:News"},
    {"claim": "Snow Days ended in the Jan 26, 2010 patch notes ('the end of Snow Days').", "source": "article 892 (patch notes, Jan 26, 2010)"},
    {"claim": "Client names: Snow Days Present, Snow Days Are Back!, Community Event: Wintery Basin Snow Days Party.", "source": "locale:1729 ; locale:1653 ; locale:15043"}
  ],
  "confidence": 0.6,
  "open": [
    "2012: no dated Snow Days article. The wiki's 12 Days of Presents 2012 pages (Builders Pack, Unicorn Sweater, Snowflake Glasses, Snowglobe Helmet, Figgy Pudding Critter) call that series Snow Days, but article 2827 and 2813 describe it as the '12 Days of Holidays' (daily challenges Dec 13-24, presents Dec 25). Treated as a separate event series and excluded. 2012 Snow Days is unknown.",
    "12 Days of Presents / 12 Days of Holidays 2013 items (Icy Snowflake Glasses, wiki image 12days2013.png, locale:441181 '12 Days 2013 - Day 9: Snow Days Soccer') are also excluded from this event. Needs its own record; the locale:441181 name suggests overlap, unresolved.",
    "2009 season: article 892 implies a prior run that ended in Jan 2010, but no dated source is in the pack. Not listed as an occurrence.",
    "Article 828 ('Snow Days Beginning To Thaw') is undated and marks an end-of-season post; it is not placed on the calendar.",
    "Article 1955 is undated; the French title gives the alias 'Jours Enneigés' only.",
    "Article 1967 (Dec 2010 Special Member Reward) is a membership promotion, not an occurrence; excluded.",
    "Conflict: wiki Community Events calls the Wintery Basin party 'the first party of 2011'; articles 1953 and 1959 date it to Dec 2010. Dec 2010 kept.",
    "NPCs: no source ties any NPC name to this event in the pack. Candi Ivy, Alana Yedra, Calvin Coldcastle and Trina Turtledove are unverified and omitted. Article 1955 mentions an unnamed NPC giving a daily gift.",
    "Aliases dropped: 'Días de Nieve (Spanish)' (unsourced) and 'Colina Nevada' (a place name, not an event alias). 'Les Jours de Neige' is sourced only to the membership post.",
    "Quest titles: 'Guarding the Gifting Tree' vs 'Guard the Gifting Tree' unresolved (locale:420280 and 420481 not checked). 'A gift from the Gifting Tree' and 'Snowmen Disassembly' are taken from wiki item pages and article 1956; exact client strings not confirmed.",
    "Snow Days outfits currency: Station Cash claimed from article 809 but not confirmed in the cited text; currency left null.",
    "Locale 829 ('Snow Days Housing Update!') suggests a possible 2011 housing tie-in; unverified, not included.",
    "Holiday Gifting Tree (SC Marketplace 2011) and Toy Maker Ears (Dec 15, 2011) could not be re-verified; excluded. Mini Holiday Tree is tied to an achievement, not a year; excluded.",
    "Prices: no item price found in any source; all null.",
    "The Gifting Tree wiki page says Sacred Grove; article 1955 and Snowhill pages say Snowhill town center. Snowhill kept.",
    "No Snow Days source after 2013 in the pack; 2014 and later unknown. 'Live: yes' rests on the 2010 and 2011 articles; 2013 is wiki-only."
  ]
}
```
