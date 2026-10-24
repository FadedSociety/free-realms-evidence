<!-- fleet job=event-infer id=vwalmart-t-shirt-v5 status=no_submit turns=2 usd=0.0021 tokens(read,write,in,out)=[6357, 7580, 6, 2172] model=claude-haiku-5-5 -->
# Walmart t-shirt

```json
{
 "event": {
  "name": "Walmart T-Shirt promotion (October 2012)",
  "aliases": ["Walmart Shirt promotion", "Walmart T-Shirt", "Walmart Shirt", "Walmart t-shirt", "Get Your Own Walmart Shirt"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {
   "year": 2012,
   "when": "October 2012 (month only; no start or end day stated)",
   "source": "http://www.freerealms.com/article/detail.action?articleId=2789 (\"For the month of October...\"); locale:9143 (\"only available through the month of October\"); wiki page: Walmart T-Shirt (\"during the month of October, 2012\")"
  }
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Buy a $10 Free Realms (Station Cash) card at Walmart",
  "Redeem the card in-game during October 2012 to receive the Walmart shirt"
 ],
 "items": [
  {
   "name": "Walmart T-Shirt",
   "price": null,
   "currency": "reward",
   "source": "wiki page: Walmart T-Shirt; locale:9132 (\"Walmart T-Shirt\"); locale:9142 (\"Walmart Shirt!\")"
  }
 ],
 "rewards": ["Walmart T-Shirt (Freestyle Jobs, chest slot clothing)"],
 "evidence": [
  {
   "claim": "For the month of October, buying a $10 Station Cash card at Walmart and redeeming it during October gave the player a Walmart Shirt. The article text gives no year.",
   "source": "http://www.freerealms.com/article/detail.action?articleId=2789"
  },
  {
   "claim": "The 2012 year comes from the wiki page: the shirt was acquired by buying a $10 card at Walmart and redeeming it during the month of October, 2012.",
   "source": "wiki page: Walmart T-Shirt"
  },
  {
   "claim": "Client offer text: buy a $$10 Free Realms card at Walmart, redeem in-game for the shirt; 'only available through the month of October'. Month-granular window only.",
   "source": "locale:9143"
  },
  {
   "claim": "Client item names: 'Walmart T-Shirt' and 'Walmart Shirt!'.",
   "source": "locale:9132; locale:9142"
  },
  {
   "claim": "Wiki ad image text: 'Buy a $10 Card at Walmart. Redeem In-game in October! Get Your Own Walmart Shirt!'",
   "source": "wiki image: Whats new walmart50 ad.jpg"
  },
  {
   "claim": "Article 2790 also says a $10 Station Cash card bought at Walmart comes with an in-game Walmart t-shirt. It has no post date in the pack, but its promo window is stated as October 12-14, 2012.",
   "source": "http://www.freerealms.com/article/detail.action?articleId=2790"
  }
 ],
 "confidence": 0.8,
 "open": [
  "Separate event, not merged here: 'Double Station Cash with Walmart' (kind: promotion). Article 2790 says SOE Pre-Paid Game Cards bought and redeemed at US Walmart stores between October 12 and October 14, 2012 gave double Station Cash. Source: http://www.freerealms.com/article/detail.action?articleId=2790 (post date not in pack). It needs its own calendar row; this object covers only the shirt offer.",
  "Exact start and end days for the shirt offer are not stated anywhere. The calendar should use the month of October 2012 as the window, not a sourced range.",
  "No price is stated for the shirt. It is a reward for redeeming a $10 card, so price is null.",
  "No zones, NPCs or quests are tied to this offer. The pack's wiki category and quest-answer lists are empty.",
  "The TenTonHammer node (tentonhammer.com:80/node/74525) lists nine retailers for an unnamed promotion. It is not tied to this shirt offer and is not used as evidence.",
  "The Best Buy Double Station Cash promo (Aug 2013, wiki image Newbestbuy.jpg) is a different retail event and is excluded.",
  "Critique fix applied: the 2012 year is now cited to the wiki page, not to articleId=2789, which gives no year. Article 2790's October 12-14, 2012 dates corroborate the same month and store chain but are for the other promo.",
  "Critique fix applied: the locale name is recorded as 'Walmart Shirt!' (locale:9142). 'Get Your Own Walmart Shirt' comes from the wiki ad image text, which I re-checked and found in the lookup output."
 ]
}
```
