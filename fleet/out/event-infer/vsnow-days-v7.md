<!-- fleet job=event-infer id=vsnow-days-v7 status=done turns=1 usd=0.0037 tokens(read,write,in,out)=[0, 12342, 4, 4248] model=claude-haiku-5-5 -->
# Community Events (Snow Days)

```json
{
  "event": {
    "name": "Snow Days",
    "aliases": ["Días de Nieve", "Les Jours de Neige", "Snow Days community events", "Colina Nevada (Snowhill, Spanish posts)", "Snow Days 2011 (webcast title only)"]
  },
  "kind": "holiday",
  "live": "yes",
  "occurrences": [
    {"year": 2009, "when": "Dec 18, 2009 through Jan 3, 2010, daily in-game community events at 3pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705 (Spanish repeat: articleId=709)"},
    {"year": 2010, "when": "Early-to-mid December 2010 run (return posts, undated; placed by the pack around early Dec 2010, approximate). Season party Dec 9 (US/Latam) and Dec 10 (UK/EU) per post, year not printed in the text. Member reward pack began Wed 15 Dec 2010, 21:00 CET, delivered over 2-3 days", "source": "Return posts: http://www.freerealms.com:80/article/detail.action?articleId=1950, http://www.freerealms.com/article/detail.action?articleId=1956 and 1957. Member reward: http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US (states 'mercredi 15 décembre 2010')"},
    {"year": 2011, "when": "Undated in text (webcast recap says Snow Days is HERE)", "source": "http://www.freerealms.com/article/detail.action?articleId=2428 (no month/day; unconfirmed as a dated occurrence)"}
  ],
  "recurring": "Yearly each winter, around December into early January. Inferred from the dated 2009-10 window and the 2010 December run, plus article 892 ('Snow Days is over until next year', date 2010-01-26 comes from the pack only). The 2011 and 2013 occurrences are not dated.",
  "zones": ["Snowhill (town centre, Gifting Tree)", "Wintery Basin (fishing area above Snowhill, season party, article 1953)"],
  "npcs": ["Candi Ivy"],
  "quests": ["The Gifting Tree"],
  "activities": [
    "Daily in-game community events at 3pm Pacific, a different event each day, including snowball battles and jump-platform games (articles 705, 770, 771)",
    "Talk to Candi Ivy each day to get a present from under the Gifting Tree (articles 828, 2808)",
    "Spin the Snow Days prize wheel (article 828)",
    "Repel Abominable Snowman attacks with snowballs and snow piles around the Gifting Tree (articles 1950, 1956, 1957, 2815)",
    "Snow Days season party in Wintery Basin: wear wintery outfits, bring boomboxes (article 1953)"
  ],
  "items": [
    {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729 (client names it with the event)"},
    {"name": "Snow Days Toys", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "Icy Snow Days Flair Shard", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "2013 Snow Days Toy Collector Pack", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
    {"name": "Radiocasetera de Días de Nieve (Snow Days radio cassette, Jingle Bell Boombox page)", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=820 (desktop wallpaper promo)"},
    {"name": "Snow Days outfits (Bah Humbug, Bow Wrapped Suit, Santa Claus, Penguin, Reindeer, Toy Soldier and other wiki-listed Snow Days outfits)", "price": null, "currency": null, "source": "articles 809, 1950, 1957 (outfits offered for limited time); wiki category 'Snow Days' for the named pieces"}
  ],
  "rewards": [
    "Snow Days present from under the Gifting Tree (daily, via Candi Ivy)",
    "Snow Days prize wheel prizes (article 828)",
    "Snow Days outfits, limited time (article 809)",
    "Snow Days member reward pack, tiered by membership, 2010 (articles 1966, 1967)"
  ],
  "evidence": [
    {"claim": "Snow Days ran daily from Dec 18, 2009 through Jan 3, 2010 with in-game community events", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
    {"claim": "Community events took place each day at 3pm PST", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
    {"claim": "Same 18 Dec 2009 to 3 Jan 2010 window in the Spanish post", "source": "http://www.freerealms.com/article/detail.action?articleId=709"},
    {"claim": "Different event each day at 15:00 Pacific; snowball battles and jump platforms", "source": "http://www.freerealms.com/article/detail.action?articleId=770"},
    {"claim": "Member reward pack began Wed 15 Dec 2010 at 21:00 CET, arriving in 2-3 days", "source": "http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US"},
    {"claim": "Snowhill is decorated and presents are under the Gifting Tree in the town centre", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950"},
    {"claim": "Talk to Candi Ivy every day for a present; spin the Snow Days prize wheel; the holiday was ending", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
    {"claim": "Abominable Snowman towered over players around the quest givers in Snowhill during Snow Days", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2815"},
    {"claim": "Snow Days is over until next year", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
    {"claim": "Snow Days is HERE at the 2011 community webcast (no date)", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"}
  ],
  "confidence": 0.6,
  "open": [
    "Article dates are null in the pack. The 2009-10 window is article-stated (705). The 2010 member reward is stated by the French post (1966). The 2010 return posts (1950, 1956, 1957) and season party (1953) are undated; their year is inferred from the pack's capture-date comparisons, not printed in the text.",
    "Article 892's 2010-01-26 date comes from the pack only, not the article text.",
    "Recurrence rests on two dated seasons (2009-10, 2010) plus 'over until next year'. Not confirmed against a third dated year. 2011 (article 2428) and 2013 (wiki Mini Holiday Tree, no month/day) are undated.",
    "NPC conflict: Spanish posts 1956 and 1957 name Alana Yedra as the daily Gifting Tree giver; English posts name Candi Ivy. Not resolved whether these are one NPC. Only Candi Ivy is listed. Everett (coal request, from a summary of article 1950 only) is not listed.",
    "Quest titles: 'The Gifting Tree' comes from article 2808 and the wiki category 'The Gifting Tree (quest)'; the exact client quest title is not confirmed. Quest-answer titles (Holiday Cheer, Present Problems, Silversnow's Sapling, Guarding the Gifting Tree, The Perfect Disguise, The Great Robgoblin Robbery Ring, Holiday Recital, Bye-Bye Supplies!, Snowmen Disassembly) have no source tie to Snow Days in this pass and are excluded. 'Snow Days Are Back!' (locale 1653) is a likely title for article 1950 but is not tied in the text, so it is excluded.",
    "Possible merged event: 12 Days of Presents (Dec 2012, articles 2813/2827, locale 441946) is separate. The client string '12 Days 2013 - Day 9: Snow Days Soccer' (locale 441181) shows Snow Days content inside 12 Days; overlap unresolved. The 2011 'SOE 12 Days of Holidays' promo is also separate. Excluded: locale 829 'Snow Days Housing Update!', the Snow Days Cheer Specialist (441047), and cookie/eggnog strings (441089-441176) tied to 12 Days.",
    "The wiki category has about 60 members. Only the Snow Days-named items and the client-named Snow Days Present are listed as items. The other category members (Candy Cane Hammer, Garnet, Mini Holiday Tree, etc.) are not tied to Snow Days in the sources here, so they are not listed. No prices or currencies were found.",
    "Activity and quest claims cite client locale numbers (15043, 15044, 436455, 436457, 426650, 1729) that were not re-checked in this pass. Video frames were not checked.",
    "Pre-launch check: none of the cited articles were identified as previews; all are written as live."
  ]
}
```
