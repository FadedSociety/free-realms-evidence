<!-- fleet job=citem-infer id=ckitty-fairy-collar-81202-v1 status=done turns=6 usd=0.0043 tokens(read,write,in,out)=[45578, 17966, 14, 3280] model=claude-haiku-5-5 -->
# Kitty Fairy Collar

{"item": {"name": "Kitty Fairy Collar", "locale_id": 81202, "kind": "clothing"},
 "sources": [
  {"type": "promotion", "detail": "Valentine's Special: Kiri pet promo. Buying Kiri gave the Kitty Fairy Outfit free; the collar is one of the four pieces of that costume (wings, shoes, antennae, collar). Whether the collar was in the free bundle or sold separately is not confirmed.", "where": null, "price": null, "currency": null, "source": "locale:140224774 (\"Valentine's Special! Buy Kiri and get the Kitty Fairy Outfit free!\"); locale:150660 (\"The collar for the kitty fairy costume.\"); articles/facts.json Kiri fact (article-2521, http://www.freerealms.com/article/detail.action?articleId=2521: \"Kiri's promo pet outfit was the Kitty Fairy Outfit.\")"},
  {"type": "coin_shop", "detail": "Sold individually for coins (client-side store price, not checked against a wiki page)", "where": "Coin Shop", "price": "270 coins (member price 243 coins if the usual 10% member discount applies)", "currency": "coins", "source": "repo:data/content/stores.json item 270 (price value from the client definition; the item_id to this collar link was not verified, since stores.json rows are keyed by numeric item_id and the pack gave no id)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Kitty Fairy Collar' is locale 81202, with the description line locale 150305 'This is a Kitty Fairy Collar item.'", "source": "locale:81202; locale:150305"},
  {"claim": "The collar is part of the Kitty Fairy costume with wings, shoes and antennae, all tagged to the same promo", "source": "locale:150619, locale:150633, locale:150641, locale:150660; locale:140224774"},
  {"claim": "Kiri's promo pet outfit was the Kitty Fairy Outfit (live era)", "source": "articles/facts.json fact for pet Kiri, article-2521 (freerealms.com)"},
  {"claim": "Client store price of 270 coins is recorded for this item", "source": "client definition coin_store_prices [270]; repo:data/content/stores.json has 270-coin rows (e.g. item_id 76, 82, 106)"}
 ],
 "confidence": 0.4,
 "open": [
  "No wiki article covers the Kitty Fairy Collar. The Valentine's promo and the coin price are from the client text, the article fact and the pack, not from a wiki page.",
  "The 270-coin price is not tied to this item in the repo: stores.json is keyed by item_id and the pack gave no id, so the link is unverified. Confirm by matching the collar's definition ids (26414-26425) to a stores.json item_id.",
  "Whether the collar was in the free Kiri bundle or only sold separately is unconfirmed. The article only names the 'Kitty Fairy Outfit'.",
  "Promo dates (Valentine's window) and any retirement date were not found in the sources, so retired is null and live is unsure.",
  "The first-pass tag (live yes, coin_shop) is a hint only; the promotion source comes from the client text and the article fact, and the coin_shop source depends on the unverified price link."
 ]}
