<!-- fleet job=event-infer id=vwalmart-t-shirt-v6 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5811, 6668, 6, 1881] model=claude-haiku-5-5 -->
# Walmart t-shirt

{"event": {"name": "Walmart T-Shirt promotion (October 2012)", "aliases": ["Walmart Shirt promotion", "Walmart T-Shirt", "Walmart Shirt", "Get Your Own Walmart Shirt"]},
"kind": "promotion",
"live": "yes",
"occurrences": [{"year": 2012, "when": "October 2012 (month only; no start or end day stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=2789 (\"For the month of October...\", no year in text); wiki page: Walmart T-Shirt (gives October 2012); locale:9143 (\"only available through the month of October\")"}],
"recurring": null,
"zones": [],
"npcs": [],
"quests": [],
"activities": ["Buy a $10 Free Realms (Station Cash) card at Walmart", "Redeem the card in-game during October 2012 to receive the Walmart shirt"],
"items": [{"name": "Walmart T-Shirt", "price": null, "currency": "reward", "source": "wiki page: Walmart T-Shirt; locale:9132 (\"Walmart T-Shirt\"); locale:9142 (\"Walmart Shirt!\")"}],
"rewards": ["Walmart T-Shirt (in-game shirt for the character)"],
"evidence": [
{"claim": "For the month of October, buying a $10 Station Cash card at Walmart and redeeming it during October gave the player a Walmart Shirt. No year in the article text.", "source": "http://www.freerealms.com/article/detail.action?articleId=2789"},
{"claim": "The 2012 year comes from the wiki page: the shirt was acquired by buying a $10 card at Walmart and redeeming it during October 2012.", "source": "wiki page: Walmart T-Shirt"},
{"claim": "Client offer text: buy a $10 Free Realms card at Walmart, redeem in-game for the shirt; 'only available through the month of October'. Month-granular window only.", "source": "locale:9143"},
{"claim": "Client item names: 'Walmart T-Shirt' and 'Walmart Shirt!'.", "source": "locale:9132; locale:9142"},
{"claim": "Wiki ad image text: 'Buy a $10 Card at Walmart. Redeem In-game in October! Get Your Own Walmart Shirt!'", "source": "wiki image: Whats new walmart50 ad.jpg"},
{"claim": "Article 2790 says a $10 Station Cash card bought at Walmart comes with an in-game Walmart t-shirt. The article has no post date in the pack. Its October 12-14, 2012 window applies to the separate double Station Cash offer, not to the shirt.", "source": "http://www.freerealms.com/article/detail.action?articleId=2790"}
],
"confidence": 0.75,
"open": [
"Possible same campaign: articleId=2790 (titled 'Double Station Cash Exclusive with Walmart!') ties the shirt to the Walmart Station Cash tie-in. The pack does not confirm one campaign or two. This row keeps the shirt offer separate. A separate calendar row is needed for 'Double Station Cash with Walmart' (SOE Pre-Paid Game Cards bought and redeemed at US Walmart stores October 12-14, 2012; source articleId=2790; post date not in pack). If the two are one campaign, merge them with sub-windows: shirt = October 2012 (month-granular), double SC = October 12-14, 2012.",
"Exact start and end days for the shirt offer are not stated in any source. The calendar uses October 2012 as the window.",
"No price is stated for the shirt. It is a reward for redeeming a $10 card, so price is null.",
"The Freestyle Jobs / chest-slot detail was removed: no source in the pack supports it.",
"No zones, NPCs or quests are tied to this offer. The pack's wiki category and quest-answer lists are empty.",
"The TenTonHammer node (tentonhammer.com:80/node/74525) is not tied to this shirt offer and is not used as evidence.",
"The Best Buy Double Station Cash promo (Aug 2013, wiki image Newbestbuy.jpg) is a different retail event and is excluded.",
"Alias 'Walmart t-shirt' removed as a case-only duplicate of 'Walmart T-Shirt'."
]}
