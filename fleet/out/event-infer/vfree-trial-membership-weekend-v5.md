<!-- fleet job=event-infer id=vfree-trial-membership-weekend-v5 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6089, 6668, 6, 1988] model=claude-haiku-5-5 -->
# Free Trial Membership weekend

{
 "event": {
  "name": "Free Trial Membership weekend",
  "aliases": ["Fourth of July weekend free trial (article summary wording only; the quote says only 'all weekend long')"]
 },
 "kind": "promotion",
 "live": "no",
 "occurrences": [
  {"year": null, "when": "A free-trial weekend, described as the Fourth of July weekend in the article summary; exact days not stated; article date not in the pack", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Non-members used membership content during the free trial weekend (quote: 'All non-member players will have access to the membership content', articleId=1590)",
  "After the weekend, a membership had to be bought for member-only items to stay useful (fact 'membership', articleId=1590)",
  "Buying a membership before the trial weekend ends would end free access to membership content early (fact 'membership', articleId=1590; this is in the article fact text, not the quote)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "A free trial membership was offered all weekend; non-members had access to membership content (quoted text).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Buying a membership before the trial weekend ends would end free access; a membership must be purchased for member-only items to remain useful after the weekend (fact 'membership', articles/facts.json:49441). Earlier critique found no source for the early-end sentence; the lookup shows it in this fact, so it is kept with that citation.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Members could keep status by choosing a multi-month payment option. Single-source: fact 'statement' (articles/facts.json:9168), not in the quoted text.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Fourth of July timing comes from the article summary wording, not the quote.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1590"},
  {"claim": "Ten Ton Hammer mentions 'the upcoming Fourth of July holiday' with no details of this promotion. Context only.", "source": "http://tentonhammer.com/node/86237"}
 ],
 "confidence": 0.3,
 "open": [
  "Live is 'no': the only source is past-tense news ('was offered all weekend'). This is a historical occurrence, not a schedulable window.",
  "Year unknown: article 1590 has date null in the pack. The 'captured July 2010' summary note is a capture date, not an article date. Find the article's own date before setting a year.",
  "Promotion days are not stated. 'Fourth of July weekend' is summary wording only.",
  "Merge risk, resolved in this record: article 1590's title ('Double Station Cash and Free Trial Membership Weekend') joins two promotions. The double Station Cash card redemption (prepaid retail cards redeemed in the window return double Station Cash) is removed from this record and needs its own promotion record. It is not an activity or alias here, and its dates are unknown.",
  "Multi-month payment option is single-source (fact 'statement', articles/facts.json:9168), not in the quoted text.",
  "Excluded name-matched events: Best Buy double SC Aug 16-18 2013 (locale 510210); CVS double SC Jan 20-22 2012 (locale 465, not_live); Spring Celebration double SC Mar 29-31 (articleId 2893); December double SC ending Dec 19 (articleId 1970); Europe double SC Oct 7-10 2011 (articleId 2294); PSN-outage compensation (tentonhammer node 97967); articleIds 1186 and 346; Soccer Star job 'free trial' (tentonhammer node 75201).",
  "Wiki 'Uncle Sam Jacket' says it is available during the Fourth of July. It is not in the wiki category and no source ties it to this promotion, so it is not listed as an item.",
  "Summer Camp content in tentonhammer node 86237 has no details and is not linked to this event.",
  "No sourced zones, NPCs, quests, items, prices, or rewards. The wiki category and quest answers were empty in the pack."
 ]
}
