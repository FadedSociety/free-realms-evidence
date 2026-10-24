<!-- fleet job=citem-infer id=cjuicy-apricot-hair-color-card-414077-v6 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6625, 11072, 6, 2009] model=claude-haiku-5-5 -->
# Juicy Apricot Hair Color Card

{"item": {"name": "Juicy Apricot Hair Color Card", "locale_id": 414077, "kind": "card"},
 "sources": [{"type": "coin_shop", "detail": "Unconfirmed candidate: Coin Shop store row item 35972 (category 142) is priced 180 coins list / 162 coins member, but the row is flagged no_sale=true and no row or frame names this card. The link to Juicy Apricot is inferred from the matching definition id 35972 only.", "where": "Coin Shop (store category 142; shop section not decoded)", "price": "180 coins list (store row and client coin_store_prices; not seen on this card's own listing); 162 coins member price (sibling colour cards in frames only)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7905; client definition coin_store_prices [180]; video:1xtVveaQ3XI/00112.jpg (sibling cards at 162 coins, card not in frame)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 414077 is 'Juicy Apricot Hair Color Card'; description says it changes hair colour; class 1, slot 3; definition ids 35972 and 68839.", "source": "locale:414077; client definition"},
  {"claim": "Store row 35972 is category 142, purchase 180 coins, member 162 coins (10% discount), sell price null, no_sale true. Rows 35957-35981 carry identical values, all no_sale true.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7890-7914"},
  {"claim": "Client coin_store_prices lists 180 for definition family 35972/68839.", "source": "client definition"},
  {"claim": "Oct 2013 Coin Shop frames list other hair colour cards (Gold Rush, Atomic Blast, Sun Kissed, Shock Wave) at 162 coins. Juicy Apricot is not in those frames.", "source": "video:1xtVveaQ3XI/00112.jpg; video:1xtVveaQ3XI/00116.jpg"},
  {"claim": "The wiki Super Spooktacular page (Oct 2013) says new Hair Color Style Cards were introduced (Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum). Juicy Apricot is not named.", "source": "wiki: Super Spooktacular"},
  {"claim": "Lookup for 'hair color card' and 'Juicy Apricot' found no wiki page, article, quest, drop, event, prize wheel, crafting, collection, membership or promotion naming this card.", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.3,
 "open": [
  "Coin Shop row 35972 is no_sale=true, so no active sale is confirmed. Do not wire as an active Coin Shop item from this row alone.",
  "The 35972 to Juicy Apricot link is inferred from matching definition id, not from a row naming the colour. Definition 68839 has no store row.",
  "Price is unresolved for this card: 180 is the list value from store row and client coin_store_prices; 162 is the member price shown for sibling cards in frames, not this card.",
  "Live status unsure and retirement unknown: no dated source says whether it is sold, retired or unobtainable.",
  "Store category 142 and source tags (L1, L2, L3, L4, R2) are not decoded, so the exact shop section is unknown.",
  "No quest, drop, event, prize wheel, crafting, collection, membership or promotion source found.",
  "Earlier answer's citation of locale:429663 was dropped: it is a flagged cosmetic-option fragment and is not evidence for this card."
 ]}
