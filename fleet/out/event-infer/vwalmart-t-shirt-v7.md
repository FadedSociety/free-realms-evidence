<!-- fleet job=event-infer id=vwalmart-t-shirt-v7 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[12604, 7619, 8, 2872] model=claude-haiku-5-5 -->
# Walmart t-shirt

{"event": {"name": "Walmart T-Shirt promotion (October 2012)", "aliases": ["Walmart Shirt promotion", "Walmart T-Shirt", "Walmart Shirt", "Get Your Own Walmart Shirt"]},
"kind": "promotion",
"live": "yes",
"occurrences": [
 {"year": 2012, "when": "October 2012 (month only; no start or end day stated). Year is from the wiki page only; the article text has no year.", "source": "http://www.freerealms.com/article/detail.action?articleId=2789 (\"For the month of October...\"); wiki page: Walmart T-Shirt (October 2012); locale:9143 (\"only available through the month of October\")"},
 {"year": 2012, "when": "October 12-14, 2012 (double Station Cash offer; listed here because the article 2790 may be the same campaign, not confirmed)", "source": "http://www.freerealms.com/article/detail.action?articleId=2790 (\"redeem it between October 12 and October 14, 2012\"; article has no post date in the pack)"}
],
"recurring": null,
"zones": [],
"npcs": [],
"quests": [],
"activities": ["Buy a $10 Free Realms (Station Cash) card at Walmart", "Redeem the card in-game during October 2012 to receive the Walmart Shirt", "Buy an SOE Pre-Paid Card at US Walmart and redeem it October 12-14, 2012 for double Station Cash (separate offer, linkage unconfirmed)"],
"items": [
 {"name": "Walmart T-Shirt", "price": null, "currency": "reward", "source": "wiki page: Walmart T-Shirt (wiki describes it as a Freestyle Jobs chest-slot clothing item; not re-verified in this pass); locale:9132 (\"Walmart T-Shirt\"); locale:9142 (\"Walmart Shirt!\")"}
],
"rewards": ["Walmart T-Shirt (in-game shirt for the character)", "Double Station Cash (October 12-14, 2012 offer, per articleId=2790)"],
"evidence": [
 {"claim": "For the month of October, buying a $10 Station Cash card at Walmart and redeeming it during October gave the player a Walmart Shirt. No year in the article text.", "source": "http://www.freerealms.com/article/detail.action?articleId=2789"},
 {"claim": "A $10 Station Cash card bought at Walmart comes with an in-game Walmart t-shirt.", "source": "http://www.freerealms.com/article/detail.action?articleId=2790"},
 {"claim": "The 2012 year for the shirt comes from the wiki page only.", "source": "wiki page: Walmart T-Shirt"},
 {"claim": "Client offer text: buy a $10 Free Realms card at Walmart, redeem in-game for the shirt; only available through the month of October.", "source": "locale:9143"},
 {"claim": "Client item names: Walmart T-Shirt and Walmart Shirt!", "source": "locale:9132; locale:9142"},
 {"claim": "Article 2790 gives double Station Cash for an SOE Pre-Paid Card bought and redeemed at Walmart between October 12 and October 14, 2012.", "source": "http://www.freerealms.com/article/detail.action?articleId=2790"},
 {"claim": "Participating retailers for a separate promotion included Walmart among 7-Eleven, Best Buy, Blockbuster, CVS, Rite Aid, Speedway, Target and Toys R Us; this is a different, broader promotion and is not used for the dates here.", "source": "http://tentonhammer.com:80/node/74525"}
],
"confidence": 0.7,
"open": [
 "Same campaign or two: articleId=2790 (double Station Cash, Oct 12-14, 2012) and articleId=2789 (shirt, October) both tie to Walmart Station Cash in October 2012. The pack does not confirm one campaign. Kept as one row with two sub-windows; split them if the source shows separate events.",
 "Exact start and end days for the shirt offer are not stated in any source. The calendar uses October 2012 as the window.",
 "The 2012 year for the shirt is wiki-sourced only; neither article gives a year. Article post dates are missing from the pack for both 2789 and 2790.",
 "The Freestyle Jobs / chest-slot detail: the wiki page reportedly says it, but I did not re-verify it in this pass. Treat as unverified; not needed for the calendar.",
 "No price is stated for the shirt. It is a reward for redeeming a $10 card, so price is null.",
 "No zones, NPCs or quests are tied to this offer. The wiki category and quest-answer lists are empty.",
 "The TenTonHammer node (tentonhammer.com:80/node/74525) describes a different, multi-retailer promotion and is not used as evidence for the shirt.",
 "The Best Buy Double Station Cash promo (Aug 2013, wiki image Newbestbuy.jpg) is a different retail event and is excluded.",
 "Lookup queries with the words Shirt or 14 failed on FTS syntax in this pass; the findings above come from the 'Walmart Station Cash' search and the pack."
]}
