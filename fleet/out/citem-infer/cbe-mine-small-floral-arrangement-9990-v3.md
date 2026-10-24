<!-- fleet job=citem-infer id=cbe-mine-small-floral-arrangement-9990-v3 status=no_submit turns=3 usd=0.0022 tokens(read,write,in,out)=[13576, 8139, 8, 2079] model=claude-haiku-5-5 -->
# Be-Mine Small Floral Arrangement

```json
{"item": {"name": "Be-Mine Small Floral Arrangement", "locale_id": 9990, "kind": "furniture"},
 "sources": [
  {"type": "other", "detail": "Random daily-click prize from the placed Gifting Basket housing item (2011 Festival of Hearts). The Gifting Basket page lists it with tints Amethyst, Bubblegum, Rubyburst, Stonesurf. The page snippet does not show the section heading, so 'Rewards' is taken from the earlier critique and not re-read.", "where": "Player housing lot (placed Gifting Basket)", "price": null, "currency": null, "source": "wiki: Gifting Basket (https://freerealms.fandom.com/wiki/Gifting_Basket), tint list; Cupid, Heart Critter and Lovasus pages say the basket gives random prizes"},
  {"type": "coin_shop", "detail": "Store row for item 76824, store category 54. The vendor and channel are not named in the data, so 'Coin Shop' is not confirmed. The row is undated.", "where": "store category 54 (vendor unnamed)", "price": "200 coins (member price 180 coins, 10% member discount; sell price 20 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16336 (item_id 76824)"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Be-Mine Small Floral Arrangement', description 'Great for giving to that special someone.', definition 76824, housing slot 0, model hsg_small_arrangement_01.adr", "source": "locale:9990; client definition in pack"},
  {"claim": "Store row for item 76824: category 54, purchase 200 coins, member 180, sell 20, no_sale false, tags L1,L2,L4,R2,T633,R1", "source": "repo:prototype/osfr-tools/data/content/stores.json:16336 (verified)"},
  {"claim": "Gifting Basket was sold through the SC Marketplace during 2011 Festival of Hearts and can no longer be acquired", "source": "wiki: Gifting Basket (verified)"},
  {"claim": "Gifting Basket page lists 'Be-Mine Small Floral Arrangement, available in Amethyst, Bubblegum, Rubyburst, Stonesurf' alongside the Large arrangement and Be-Mine Basket", "source": "wiki: Gifting Basket (verified via lookup snippet)"},
  {"claim": "Pet pals Cupid, Heart Critter and Lovasus are random prizes from the Gifting Basket", "source": "wiki: Cupid; wiki: Heart Critter; wiki: Lovasus (verified)"}
 ],
 "confidence": 0.4,
 "open": [
  "The wiki does not say the arrangement was sold inside the basket. The earlier 'marketplace' source was wrong and is removed. It is a basket prize, so no SC price is given for it.",
  "The 200-coin store row is real, but the channel is only 'store category 54'. 'Coin Shop' and any vendor name are not evidenced. The row is undated, so it is unknown whether it is a current sale.",
  "The row's tags (L1, L2, L4, R2, T633, R1) are unexplained and appear on many unrelated rows.",
  "Whether the arrangement is a 'Rewards' prize or a separate listing on the Gifting Basket page needs a direct re-read of the page's section heading.",
  "The basket is retired, and the arrangement is a basket prize, so it is probably retired too. Its own live status is unresolved because of the undated coin row."
 ]}
```
