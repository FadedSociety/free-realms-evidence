<!-- fleet job=item-infer id=iarcher-s-flair-shard-of-smoldering-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[4826, 11658, 6, 2424] model=claude-haiku-5-5 -->
# Archer's Flair Shard of Smoldering

{"item": {"name": "Archer's Flair Shard of Smoldering", "locale_id": 130973, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase; wiki lists it as a level 1 Archer Flair Shard in the Coin Flair / Coin Shop categories", "where": "Coin Shop", "price": "750 (unverified: wiki's structured coin field shows 750, but the page's prose price is blank; repo value only)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Flair_Shard_of_Smoldering (rev 32666, categories Coin Shop, Coin Flair, Flair Shard, Marketplace Items)"},
  {"type": "vendor", "detail": "Gilbert, Sells section, listed as Archer's Flair Shard of Smoldering (stock listing only; not directly re-checked in this pass)", "where": null, "price": "750 (unverified: repo reference price from stores.json, vendors.json:16057, price_basis says no captured NPC quote)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Gilbert (section Sells, rev 2025-05-31, as cited in repo:prototype/osfr-tools/data/content/vendors.json:16068-16076)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client text, locale 130973", "source": "locale:130973"},
  {"claim": "Wiki page classifies the item as a level 1 Archer flair shard and places it in the Coin Shop category; no retired category is present", "source": "https://freerealms.fandom.com/wiki/Archer's_Flair_Shard_of_Smoldering"},
  {"claim": "The wiki prose price is blank ('sells for .'), so the wiki page text does not state 750 coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Flair_Shard_of_Smoldering"},
  {"claim": "Gilbert's Sells list is recorded as stocking this item (stock_source wiki page Gilbert, section Sells); the 750/675/375 figures are repo reference values, with price_basis stating no captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:16053-16092"}
 ],
 "confidence": 0.45,
 "open": [
  "Coin Shop price of 750 is not confirmed by a quote: the wiki prose price is blank, and the 750 comes from the wiki's structured coin field and the repo's stores.json reference. Verify against a live Coin Shop listing.",
  "Gilbert vendor stock is cited only through the repo's stock_source pointing at the wiki Gilbert page; the Gilbert page text was not retrievable in refs, so the vendor source is unverified. Gilbert's zone is unknown.",
  "The 750 figure in both sources is one shared reference value, not two independent confirmations.",
  "Member price 675 and sell price 375 are repo reference values with no wiki or in-game citation; excluded.",
  "No Station Cash price or SC Marketplace source is evidenced, despite the 'Marketplace Items' category.",
  "The wiki page has broken file links and no images, so the icon is unverified.",
  "Retirement or later removal from the Coin Shop is not documented; retired is null and live is 'unsure'."
 ]}
