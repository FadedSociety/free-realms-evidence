<!-- fleet job=citem-infer id=cstar-sweeper-jersey-403720-v2 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[12034, 6917, 8, 1905] model=claude-haiku-5-5 -->
# Star Sweeper Jersey

{"item": {"name": "Star Sweeper Jersey", "locale_id": 403720, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fred Futbol (Soccer coin merchant); probable, not confirmed per item. Wiki news says he was converted to a coin merchant 'for all Soccer items'; no per-item stock row names him for this jersey", "where": "Snowhill soccer area (Soccer Star Gear)", "price": "750 coins (member price 675 coins, 10% member discount); price is for stores.json item 61290 (tint group 1) only, mapping to base locale 403720 unverified; Elite variants (403725, 403726) not priced here", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8451 (item 61290, category 103, tint_group 1, purchase 750, member 675, sell 75, no_sale false); wiki Template:News ('Fred Futbol and Tommy Crackletoe have been converted to coin merchants for all Soccer items'); locale:410136 = 'Fred Futbol'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Star Sweeper Jersey' is locale 403720; cluster includes Elite Pink (403725) and Elite Black (403726) variants", "source": "locale:403720, locale:403725, locale:403726"},
  {"claim": "Coin store row for item 61290 (tint group 1) at 750 coins, member price 675, sell price 75, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8451"},
  {"claim": "Fred Futbol was converted to a coin merchant for all Soccer items (general, not item-specific)", "source": "wiki Template:News"},
  {"claim": "Fred Futbol is a named NPC in the client text", "source": "locale:410136"},
  {"claim": "Soccer Star clothing set families include a jersey slot item in each set (base, Elite Black, Elite Pink)", "source": "repo:notes/Build Guides/Content/Jobs/Soccer Star.md lines 199-210"}
 ],
 "confidence": 0.45,
 "open": [
  "Vendor link is probable only: the Template:News line covers Soccer items generally; no stock row ties Star Sweeper Jersey (403720) to Fred Futbol.",
  "The 750-coin row is item 61290 (one of 12 ids in the 61290-61303 tint group set). Which tint is base 403720 vs Elite Black/Pink is unverified; Elite prices may differ.",
  "Article 424 (http://www.freerealms.com:80/article/detail.action?articleId=424) says six soccer outfits were added. It does not name this jersey, so it is not cited as acquisition evidence.",
  "Retirement not established. The store row has no_sale false, which suggests it was listed at capture time, but there is no dated source for current availability; live is therefore 'unsure' rather than confirmed.",
  "No quest reward, enemy drop, prize-wheel or event source found. No wiki article, images or video frames name this item.",
  "Critique note: the earlier claim that locale:410136 did not resolve was incorrect; it resolves to 'Fred Futbol'."
 ]}
