<!-- fleet job=event-infer id=vsoe-12-days-of-holidays-promotion-v7 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6957, 8862, 6, 2952] model=claude-haiku-5-5 -->
# SOE 12 Days of Holidays promotion

{
 "event": {
  "name": "SOE 12 Days of Holidays",
  "aliases": ["12 Days of Holidays", "SOE 12 Days of Holidays promotion", "12 Days of Presents (Free Realms's part of the umbrella, wiki name)"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13 00:01 PST to Dec 24 23:59 PST, 2012 (Free Realms daily challenges, Days 1-12; Day 12 post)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813; http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"year": 2011, "when": "Dec 13 09:01 CET to Dec 25 08:59 CET, 2011 (SOE cross-game window; Free Realms not named in the body)", "source": "http://www.freerealms.com/article/detail.action?articleId=2433 and articleId=2442 (summaries); articleId=2431 (summary, Dec 13-24 2011 PST)"},
  {"year": null, "when": "Day 8 double Station Cash redemption window, ending 21 December 08:59 CET; year not printed (2011 is probable, not proven)", "source": "http://www.freerealms.com/article/detail.action?articleId=2457"}
 ],
 "recurring": "Yearly in December, per the wiki ('annual event', Dec 13-24). Two dated Dec windows (2011 cross-game, 2012 Free Realms). Treat the 2011 window as SOE-wide, not Free Realms-specific.",
 "zones": ["Snowhill"],
 "npcs": [],
 "quests": [],
 "activities": [
  "Log in each day of the window for the daily challenge and reward (Free Realms, 2012: article 2813 and 2827)",
  "Complete the daily holiday challenge at Snowhill, which awards a present (article 2813 summary)",
  "Open presents on the final day (wiki Snow Days: presents opened Dec 25, 2012)",
  "Buy or redeem Station Cash during the day-8 double window (article 2457)"
 ],
 "items": [],
 "rewards": [
  "Double Station Cash on Station Cash redemptions on day 8, until 21 Dec 08:59 CET (article 2457; year not printed)",
  "A present with a bow per daily challenge (article 2813 summary; 12 Days of Presents)"
 ],
 "evidence": [
  {"claim": "Free Realms ran the 12 Days of Holidays event Dec 13 2012 00:01 PST to Dec 24 2012 23:59 PST, with a daily challenge and reward plus daily offers.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Day 12 post for Free Realms' 12 Days of Holidays event explains one daily challenge per day, Dec 13-24, with a present per day.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"claim": "On day 8 of the SOE 12 Days of Holidays promotion, Free Realms offered double Station Cash on redemptions until 21 December 08:59 CET. No year printed.", "source": "http://www.freerealms.com/article/detail.action?articleId=2457"},
  {"claim": "The 2011 SOE 12 Days of Holidays window ran Dec 13 09:01 CET to Dec 25 08:59 CET with daily specials at participating games; the body does not name Free Realms.", "source": "http://www.freerealms.com/article/detail.action?articleId=2433 (summary); articleId=2442 (summary)"},
  {"claim": "The event is an annual December event running Dec 13-24.", "source": "wiki: Events / 12 Days of Presents (wiki page)"},
  {"claim": "Snowhill holiday challenge and presents are part of the 12 Days of Holidays.", "source": "articles summary articleId=2813; wiki: Snow Days"}
 ],
 "confidence": 0.55,
 "open": [
  "Year of article 2457 (day 8 double Station Cash) is not printed. The 2011 attribution is an inference from the window, not a source claim. Do not wire it as a dated 2011 occurrence without that flag.",
  "The 2011 window is SOE cross-game and never names Free Realms in the body. Only the 2012 occurrence (articles 2813, 2827) is clearly Free Realms-hosted. Whether Free Realms ran in 2011 is not established.",
  "Recurrence 'yearly' rests on the wiki's 'annual' wording plus two windows; no article states it recurs.",
  "The earlier answer's 2012 'triple Station Cash through 21 Dec 2012 11:59 PM PST' (articleId=2826) is generic SOE Station Cash, not a Free Realms event. It is dropped here.",
  "The earlier answer's Dec 17 2011 triple Station Cash day (articleId=2455) is a summary only and is not Free Realms-specific. Dropped.",
  "Quest titles, the Snowhill daily quests and the 12 Days of Presents items are not named in any source in this pack. The earlier NPC Trina Turtledove and the Calvin Coldcastle mention (wiki Snow Days) are not tied to a dated occurrence here. Left out; needs a quest-title pass.",
  "Items and prices: none sourced. Do not add station_cash prices.",
  "Locale ids 392128125, 2109814218, 2976893817 from the earlier draft did not resolve and are not used. Locale 831/832 (SOE 12 Days of Holidays is Here!) describe the cross-game daily specials and are not Free Realms-specific.",
  "Naming overlap: the wiki's '12 Days of Presents' is Free Realms' part of the SOE 12 Days of Holidays. Kept as an alias here, but the calendar may want it as a separate weekly/holiday entry."
 ]
}
