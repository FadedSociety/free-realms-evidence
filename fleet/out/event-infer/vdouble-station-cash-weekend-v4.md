<!-- fleet job=event-infer id=vdouble-station-cash-weekend-v4 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[9472, 11243, 6, 2651] model=claude-haiku-5-5 -->
# Double Station Cash Weekend

{
 "event": {"name": "Double Station Cash Weekend", "aliases": ["Double Station Cash Weekend. Don't Miss Out!!"]},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy a pre-paid Free Realms Station Cash retail game card (not Starter Cards) and redeem it within the promotion window to receive double its value in Station Cash."],
 "items": [],
 "rewards": ["2x the card's face value in Station Cash (station_cash)"],
 "evidence": [
  {"claim": "Promotion: pre-paid Free Realms Station Cash retail game cards, redeemed in a set window, gave double value in Station Cash for players with accounts in good standing; Starter Cards excluded.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1186; http://www.freerealms.com/article/detail.action?articleId=346"},
  {"claim": "Article 346 and 1186 share the title 'Double Station Cash Weekend. Don't Miss Out!!' and the same offer wording. Their redemption windows are: Fri Sept 18 (after 7:00am PDT) to Sun Sept 20 (before 10:00pm PDT) [346, no year stated]; Fri April 2 (after 4:00pm PDT) to Sun April 4 (before 11:00pm PDT) [1186, no year stated].", "source": "http://www.freerealms.com/article/detail.action?articleId=346; http://www.freerealms.com:80/article/detail.action?articleId=1186"},
  {"claim": "Neither article states a year. The 2009 year for the September window comes only from a cross-game TenTonHammer post (node/74525, Free Realms/EQ/EQ2 double face value Sept 18-20 2009); the link to article 346 rests on the date match, not a title match. The April year (2010) is inferred from the capture date and is not stated by any source.", "source": "http://tentonhammer.com:80/node/74525; http://www.freerealms.com/article/detail.action?articleId=346; http://www.freerealms.com:80/article/detail.action?articleId=1186"},
  {"claim": "Not this event (separate promotions in the pack's merged set): articleId 2893 (Spring Celebration, Mar 29-31, purchases and cards); 1970 (purchase bonus, ran until Dec 19, no year); 2754 and 2763 (Labor Day weekend, Sept 1-3 2012); 2483 (CVS/pharmacy card weekend); 2806 (7-Eleven SOE Game Card); 2146 (Memorial Mania, triple); 2294 (Europe Oct 2011); tentonhammer node/97967 (PSN compensation); locale:465 (CVS Jan 2012, not_live); wiki image Newbestbuy.jpg (Best Buy exclusive card, separate retailer promotion).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2893; http://www.freerealms.com/article/detail.action?articleId=2754; http://www.freerealms.com/article/detail.action?articleId=2763; http://www.freerealms.com:80/article/detail.action?articleId=2483; http://www.freerealms.com/article/detail.action?articleId=2806; locale:465"},
  {"claim": "Unconfirmed candidates, not counted: articleId 1974 (same card-redeem wording, Dec 2010 capture, no window); articleId 1590 (Fourth of July weekend card double, captured July 2010, different title); tentonhammer node/78284 (Dec 23 2009 to Jan 3 2010, 100% bonus, not verified).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974; http://www.freerealms.com:80/article/detail.action?articleId=1590; http://tentonhammer.com/node/78284"},
  {"claim": "No zones, NPCs, quests, wiki category members or item prices are tied to this event in the sources. Retailers are not named in the article text.", "source": "event pack (wiki_category_members and quest_answers_mentioning_it empty); http://www.freerealms.com:80/article/detail.action?articleId=1186"}
 ],
 "confidence": 0.25,
 "open": [
  "Live status unsure: the articles describe a promotion that ran, but no article states a year. The September window's 2009 year rests on a cross-game TenTonHammer post (node/74525) matched by date only, so the occurrence is not schedulable from the article itself.",
  "Occurrences left empty on purpose. Dated candidates for the calendar, if the year is confirmed: Sept 18-20 (year 2009 per node/74525, title-unconfirmed); April 2-4 (year 2010 inferred from capture date only). Do not count as recurring: two same-title windows exist, but neither article gives a year, so no pattern is proven.",
  "Recurring is null. Two same-title windows (Sept and April) would suggest a pattern, but neither is dated by its own article.",
  "The pack's name merges several different promotions (Spring Celebration, Labor Day, CVS, 7-Eleven, Best Buy, Memorial Mania, Europe). Only articleIds 346 and 1186 share this title and wording; split the rest into their own records.",
  "Items: no price or SKU is tied to this event. The $5/$10/$15 card values in the client or wiki are not linked to this promotion's text, so price and items stay empty.",
  "Locale ids 465, 2790, 2806, 2807 are client strings (or flagged not_live); article ids 2806 and 2483 are retailer articles, not locale ids. Do not mix them up.",
  "Confidence is low (0.25): no year in either article, one cross-game year link, and an unverified 2010 inference."
 ]
}
