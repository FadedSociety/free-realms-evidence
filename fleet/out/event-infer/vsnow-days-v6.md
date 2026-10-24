<!-- fleet job=event-infer id=vsnow-days-v6 status=done turns=1 usd=0.0035 tokens(read,write,in,out)=[0, 12458, 4, 3816] model=claude-haiku-5-5 -->
# Community Events (Snow Days)

```json
{
  "event": {
    "name": "Snow Days",
    "aliases": ["Días de Nieve", "Les Jours de Neige", "Snow Days community events", "Snow Days 2011 (webcast title only)", "Colina Nevada (Snowhill, Spanish posts)"]
  },
  "kind": "holiday",
  "live": "yes",
  "occurrences": [
    {
      "year": 2009,
      "when": "Dec 18, 2009 through Jan 3, 2010 (daily in-game community events, 3pm Pacific)",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"
    },
    {
      "year": 2010,
      "when": "Member reward pack began Wed Dec 15, 2010 at 21:00 CET (French post); delivery over 2-3 days",
      "source": "http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US"
    }
  ],
  "recurring": "Yearly each winter (two dated occurrences, 2009 and 2010; article 892 says Snow Days 'is over until next year')",
  "zones": ["Snowhill", "Wintery Basin (fishing area above Snowhill, season party)"],
  "npcs": ["Candi Ivy"],
  "quests": ["The Gifting Tree"],
  "activities": [
    "Daily in-game community events at 3pm Pacific from Dec 18, 2009 to Jan 3, 2010, a different event each day, including snowball battles and jump-pad platforms (articles 705, 770, 771)",
    "Talk to Candi Ivy each day to get a present from under the Gifting Tree (articles 828, 2808)",
    "Spin the Snow Days prize wheel (article 828)",
    "Snowball fights against the Abominable Snowman, who attacked the Gifting Tree area (articles 1950, 1956, 1957, 2815)",
    "Wintery Basin Snow Days season party: ice fishing, wear Snow Days outfits, bring boomboxes (article 1953; client locale 15043, 15044)"
  ],
  "items": [
    {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729 (client names it with the event)"}
  ],
  "rewards": [
    "Snow Days present from under the Gifting Tree (daily)",
    "Snow Days outfits (limited time; article 809)",
    "Snow Days member reward pack (articles 1966, 1967)",
    "Snow Days prize wheel prizes (article 828)"
  ],
  "evidence": [
    {"claim": "Snow Days ran every day from December 18, 2009 through January 3, 2010 with in-game community events", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
    {"claim": "Community events took place each day at 3pm PST", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
    {"claim": "Same 18 Dec 2009 to 3 Jan 2010 window in Spanish post", "source": "http://www.freerealms.com/article/detail.action?articleId=709"},
    {"claim": "Different community event each day at 15:00 Pacific; snowball battles and jump-platforms", "source": "http://www.freerealms.com/article/detail.action?articleId=770"},
    {"claim": "Member reward pack started Wednesday 15 December 2010 at 21:00 CET, arriving in two to three days", "source": "http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US"},
    {"claim": "Snowhill decorated and presents under the Gifting Tree in the town centre", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950"},
    {"claim": "Talk to Candi Ivy every day for a present; spin the Snow Days prize wheel; outfits limited time", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
    {"claim": "Abominable Snowman towered over players around the quest givers in Snowhill during Snow Days", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2815"},
    {"claim": "Snow Days is over until next year (recurrence statement; article shows no year)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"}
  ],
  "confidence": 0.55,
  "open": [
    "Critique was truncated mid-sentence (evidence lens, item 7), so I could not see its full list of problems. Items below are the ones I found by re-reading the pack; any other critique point is unaddressed.",
    "Article 1953 (Wintery Basin party, Dec 9 US/Latam and Dec 10 UK/EU): the pack's own summary says the posting date is not shown, so the year 2010 is not stated in the article. Removed from occurrences. Needs the article date line to confirm year.",
    "Article 1967 (Spanish member rewards, 'Wednesday December 15'): the page gives no year; 2010 is inferred from the weekday. Used only the French article 1966, which states 'mercredi 15 décembre 2010'.",
    "Article 892 date 2010-01-26 comes from the pack only, not the article text. The 'over until next year' line is therefore not dated to a year.",
    "2011: webcast recap article 2428 says 'Snow Days is HERE!' with no month, day or year in the text. Not listed as a dated occurrence.",
    "2013: the wiki page Mini Holiday Tree says Snow Days 2013 introduced it, with no month or day. Wiki is not an article source, so no 2013 occurrence is listed.",
    "Dates for 2009 and 2010 windows are article-stated; the 'yearly each December' recurrence rests on only those two dated windows plus article 892. Not verified against a third dated year.",
    "Activity and quest claims cite client locale numbers (15043, 15044, 436455, 436457, 426650, 1729) that were not re-checked in this pass.",
    "NPC conflict: Spanish posts 1956 and 1957 name Alana Yedra as the daily Gifting Tree giver; English posts name Candi Ivy. Not resolved whether these are one NPC. Only Candi Ivy listed.",
    "Quest: 'The Gifting Tree' is taken from article 2808 and the wiki category 'The Gifting Tree (quest)'; the exact client quest title should be confirmed. 'Snow Days Are Back!' (locale 1653) is a likely title for article 1950 but is not tied in the text, so it is excluded.",
    "Quest titles from quest answers (Holiday Cheer, Present Problems, Silversnow's Sapling, Guarding the Gifting Tree, The Perfect Disguise, The Great Robgoblin Robbery Ring, Holiday Recital, Bye-Bye Supplies!, Snowmen Disassembly) have no source tie to Snow Days in this pass and are excluded.",
    "Items: the wiki category 'Snow Days' has about 60 members, most tied to 12 Days of Presents or not sourced to Snow Days here. Only the client-named Snow Days Present is listed. No prices or currencies were found, so price and currency are null.",
    "Merged-event risk: 12 Days of Presents (Dec 13-24, 2012, article 2813/2827, locale 441946) is a separate event. Client string '12 Days 2013 - Day 9: Snow Days Soccer' (locale 441181) shows Snow Days content inside 12 Days; the overlap is unresolved. The 2011 'SOE 12 Days of Holidays' promo is also separate.",
    "Excluded: locale 829 'Snow Days Housing Update!', the cross-game 12 Days promo articles, the Snow Days Cheer Specialist (441047) and cookie/eggnog strings (441089-441176) tied to 12 Days.",
    "Pre-launch check: none of the cited articles were identified as previews; all are written as live. Video frames were not checked.",
    "Everett's coal request appears only in a pack summary (article 1950) and is not listed as an NPC."
  ]
}
```
