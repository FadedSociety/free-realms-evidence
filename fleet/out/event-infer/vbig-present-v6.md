<!-- fleet job=event-infer id=vbig-present-v6 status=done turns=1 usd=0.0026 tokens(read,write,in,out)=[0, 8048, 4, 3160] model=claude-haiku-5-5 -->
# Big Present

```json
{
  "event": {
    "name": "12 Days of Presents",
    "aliases": ["Snow Days (wiki name for the 2012 edition only)", "12 Days 2013 (client quest-title name for a later edition; year not article-confirmed)"]
  },
  "kind": "holiday",
  "live": "yes",
  "occurrences": [
    {
      "year": 2012,
      "when": "Dec 13-24, 2012 (daily challenges, 12:01 am to 11:59 pm PST); presents opened Dec 25, 2012",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"
    }
  ],
  "recurring": null,
  "zones": ["Snowhill (article 2813, 2012)"],
  "npcs": [],
  "quests": ["Big Present 1", "Big Present 2", "Big Present 3 (locale:441944-441949; Big Present sub-mechanic, year not article-tied)"],
  "activities": [
    "Complete one daily holiday challenge per day, Dec 13-24, at Snowhill; a challenge completed on its first day gives a present with a bow (article 2813; rule restated in article 2827, undated)",
    "Open presents on December 25 (article 2813, 2012)",
    "Earn a bonus Big Present for every 4 daily presents opened (article 2813, 2012)",
    "Complete all 12 daily challenges for 12 bows and 15 presents in total (article 2813, 2012)"
  ],
  "items": [
    {"name": "Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Snowflake Glasses (labelled 2012 Snow Days series; no wiki category membership found, so tie is weak)"},
    {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki page Snow Days Unicorn Sweater (labelled 2012; weak tie as above)"},
    {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki page Snow Days Lot (labelled 2012, Day 11; weak tie as above)"},
    {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki page Snow Days Builders Pack (labelled 2012; weak tie as above)"}
  ],
  "rewards": [
    "A present with a bow for each daily challenge completed on its first day (article 2813; article 2827)",
    "Bonus Big Present for every 4 daily presents opened (article 2813, 2012)",
    "All 12 challenges: 12 bows and 15 presents in total (article 2813, 2012)"
  ],
  "evidence": [
    {"claim": "Event ran Dec 13-24, 2012 with a daily challenge giving a present with a bow, and presents opened Dec 25, 2012", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
    {"claim": "Big Present bonus: one per 4 daily presents opened; all 12 challenges give 12 bows and 15 presents", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
    {"claim": "Presents system rules (daily challenge, first-day present, Dec 25 opening, bows bought from Marketplace for missed days); undated, so it supports rules only, not a year", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
    {"claim": "Big Present is a bonus sub-mechanic inside this event, not a separate event; the pack's name 'Big Present' is a component name", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"}
  ],
  "confidence": 0.5,
  "open": [
    "The pack is named 'Big Present', but both articles describe it as a reward inside the 12 Days event. It is recorded here as a component of 12 Days of Presents, not as its own event.",
    "2013 edition: NOT article-confirmed. The only support is client quest titles '12 Days 2013 - Day 1' to 'Day 12' (locale:441125-441199), Trina Turtledove challenge-NPC strings (locale:441161, 441173, 441185, 441197), and a 'Dec 25 open' string (locale:441927). None gives a month, day or year. The 2013 dates Dec 13-24 are not sourced and are not listed as an occurrence. The wiki's 'annual' wording was not verified.",
    "Recurrence: 'annual' is not established. Only 2012 has a dated source, so recurring is null.",
    "Trina Turtledove is not listed as an NPC because her only support is 2013 client strings with no article tie.",
    "The 2012 Snowhill zone and the Dec 13-24 dates come from article 2813. Its posting date (2012-12-13) is inferred from a 'Posted 4 days, 9 hours ago' stamp against a 2012-12-18 capture; the event dates are stated in the article itself.",
    "The four 2012 'Snow Days' wiki items are tied only by wiki page labels; wiki category membership was empty in the pack, so these ties are weak. Prices are unsourced (null).",
    "The 2013 reward and item list (Figgy Pudding Critter, Icy Snowflake Glasses, Arctic Cat, Snow Days Gift Box - Cookies/Decorations, Holigoblin Mask) is wiki-only and not year-verified. It is excluded from this 2012 record and should not be wired as live content until a dated source is found.",
    "Per-day Big Present rewards (Day 8 St. Bernard pet, Day 9 Snowman Mask, Day 10 5,000 Coins, Day 12 Temporary Snowflake Parachute, Big Present Polar Bear Ride) were read only from a lookup excerpt and are excluded.",
    "Name collision: '12 Days of Holidays' is a separate 2011 SOE promotion (articles 2442, 2441, 2433, 2457; 13-25 Dec 2011) and is not an alias here.",
    "Excluded for no event tie: Snowglobe Helmet, Icy Snow Days Flair Shard, Winter Holiday Present (locale:132588), toy items (Fire Hawk, Hero Copter, Hover Ring, Blast Rover, Cyber Cycle), '12 Days of Sales' banners, 12 Days Present/Bow quest titles (locale:441513, 441525), and Candi Ivy / Alana Yedra (Gifting Tree NPCs, not confirmed for this event).",
    "Quest titles 'Day 2', 'Day 6', 'Day 8', 'Day 10' (2013) were not checked by id and are not listed."
  ]
}
```
