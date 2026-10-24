<!-- fleet job=event-infer id=vfree-trial-membership-weekend-v6 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5912, 6269, 6, 1795] model=claude-haiku-5-5 -->
# Free Trial Membership weekend

{
 "event": {
  "name": "Free Trial Membership weekend",
  "aliases": ["Double Station Cash and Free Trial Membership Weekend (article 1590 title; the double Station Cash half is a sibling promotion, see open)", "Fourth of July weekend free trial (article summary wording only, not in the quote)"]
 },
 "kind": "promotion",
 "live": "no",
 "occurrences": [
  {"year": null, "when": "A free-trial weekend in the Fourth of July window, per the article summary; exact days and year not stated in the pack (article date null)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Non-members used member content during the free trial weekend (quote: 'All non-member players will have access to the membership content', articleId=1590)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "A free trial membership was offered all weekend long; non-member players had access to membership content (quoted text).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Article summary: a free trial membership weekend gives non-members access to member content, in a Fourth of July weekend promotion (summary wording, captured July 2010; not the article's own date).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Quote-backed post-trial rule: 'A membership must be purchased for any member-only items to continue to be useful after the weekend ends' (fact 'membership', articles/facts.json:49441).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"}
 ],
 "confidence": 0.3,
 "open": [
  "Live is 'no': the only source is past-tense news. Not a schedulable window.",
  "Year and exact days unknown: article 1590 has date null in the pack. 'Captured July 2010' is a capture date, not the article date. Find the article's own publication date before assigning a year. Lookup returned no further date.",
  "'Fourth of July weekend' is summary wording only, not in the quoted text.",
  "Early-end rule ('buying a membership before the trial weekend ends would end free access') is summary paraphrase from fact 'Membership purchase during trial' (articles/facts.json:49438); no quote supports it. Kept out of activities; treat as unverified rule.",
  "Multi-month payment option (members keep status) is single-source, in the fact statement only (articles/facts.json:9168), no quote. Left out of activities.",
  "Merge risk: article 1590 covers two promotions. The double Station Cash card redemption (prepaid retail cards redeemed in the window return double Station Cash) shares the same article and window per the summary, but the pack gives it no dates or record. It needs a sibling record citing articleId=1590; not built here.",
  "Excluded name-matched events: Best Buy double SC Aug 16-18 2013 (locale 510210); CVS double SC Jan 20-22 2012 (locale 465, not_live); Spring Celebration double SC Mar 29-31 (articleId 2893); December double SC ending Dec 19 (articleId 1970); Europe double SC Oct 7-10 2011 (articleId 2294); PSN-outage compensation (tentonhammer node 97967); articleIds 1186 and 346; Soccer Star 'free trial' job (tentonhammer node 75201).",
  "Wiki 'Uncle Sam Jacket' says it is available during the Fourth of July. It is not in the wiki category and no source ties it to this promotion, so it is not listed.",
  "Ten Ton Hammer node 86237 mentions 'the upcoming Fourth of July holiday' and Summer Camp with no details of this promotion. Context only.",
  "No sourced zones, NPCs, quests, items, prices, or rewards. Wiki category and quest answers were empty in the pack."
 ]
}
