<!-- fleet job=event-infer id=vsoe-12-days-of-holidays-promotion-v6 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[8410, 14514, 6, 3523] model=claude-haiku-5-5 -->
# SOE 12 Days of Holidays promotion

{"event": {"name": "SOE 12 Days of Holidays promotion", "aliases": ["SOE 12 Days of Holidays", "12 Days of Holidays (SOE cross-game promotion, Free Realms news posts)"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Dec 13 to Dec 25, 2011 (promotion window, 09:01 CET Dec 13 to 08:59 CET Dec 25); day 8 = Dec 20, 2011, double Station Cash redeemable until 21 Dec 08:59 CET (year inferred, see open)", "source": "http://www.freerealms.com/article/detail.action?articleId=2457 (day-8 text, no year); window from articles/articles.json summary of the 'Die \"SOE 12 Days of Holidays\"-Promotion ist da!' post and the 'kommt bald!' post (dated 13 Dec 2011 09:01 CET to 25 Dec 2011 08:59 CET); Dec 17 2011 PST Triple Station Cash day per http://www.freerealms.com:80/article/detail.action?articleId=2455"},
  {"year": 2012, "when": "Dec 2012, Station Cash offer valid through Dec 21, 2012 11:59 PM PST (triple Station Cash)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2826 (summary; no year printed in the post, 2012 comes from the summary's stated date)"}
 ],
 "recurring": "yearly in December (two dated occurrences: 2011 and 2012 SOE 12 Days of Holidays promotions)",
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Log in during the promotion window and redeem or buy Station Cash to get the promotional bonus (double or triple Station Cash)", "Daily offers at participating SOE games during the 12 Days (per 2011 announcement summary)"],
 "items": [],
 "rewards": ["Double Station Cash on Station Cash redemptions on day 8 (article 2457)", "Triple Station Cash offers (article 2455 Dec 17 2011 PST; article 2826 valid through Dec 21 2012)"],
 "evidence": [
  {"claim": "On day 8 of the SOE 12 Days of Holidays promotion, Free Realms offered double Station Cash on redemptions until 21 December at 08:59 CET.", "source": "http://www.freerealms.com/article/detail.action?articleId=2457"},
  {"claim": "The SOE 12 Days of Holidays promotion ran 13 Dec 2011 09:01 CET to 25 Dec 2011 08:59 CET with daily offers at participating games.", "source": "articles/articles.json summary of 'Die \"SOE 12 Days of Holidays\"-Promotion ist da!' and 'Die \"SOE 12 Days of Holidays\"-Promotion kommt bald!' (freerealms.com pages; the text itself does not name Free Realms)"},
  {"claim": "A Triple Station Cash day for the 12 Days of Holidays ran on December 17, 2011 (PST).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2455"},
  {"claim": "A generic 12 Days of Holidays Station Cash offer (triple Station Cash) was valid through December 21, 2012 at 11:59 PM PST.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2826"}
 ],
 "confidence": 0.6,
 "open": [
  "Article 2457 has no year. 2011 is inferred: Day 8 of a Dec 13 start is Dec 20, and the ending 21 Dec 08:59 CET fits a one-day offer inside the Dec 13-25 2011 window. Not stated by the article itself.",
  "The 2012 occurrence rests on article 2826 summary (valid through Dec 21 2012 11:59 PM PST). That is a different Station Cash offer; it is not the same as the 2457 double-Station-Cash day.",
  "Previous answer conflated this promotion with the Free Realms '12 Days of Presents' Snowhill quest event (Dec 13-24 2012, articles 2813/2827, wiki). That is a separate event and is removed from this entry. The 12 Days of Presents calendar entry should be kept separate. The wiki (Snow Days, 12 Days of Presents) calls it 'a part of SOE's 12 Days of Holidays', so the two are related but distinct.",
  "The Free Realms-specific 12 Days of Presents items, NPC Trina Turtledove, and quests are not tied to this promotion by any source in this pack and are left out. Locale ids cited in the earlier draft (392128125, 2109814218, 2976893817) did not resolve and are not used.",
  "No station_cash prices or item rewards are sourced for this promotion; items list is empty.",
  "Article 2457 gives 'day 8' only. Whether a day 1-12 schedule of Station Cash bonuses existed for Free Realms is not established by this pack.",
  "Article 2826 is generic SOE (not Free Realms-specific) and its year rests on the summary's date; treat as moderate confidence.",
  "Live status: the articles are archived freerealms.com news posts, so the promotion ran; exact 2011 day-by-day schedule and whether the 2012 offer was Free Realms-hosted are not verified."
 ]}
