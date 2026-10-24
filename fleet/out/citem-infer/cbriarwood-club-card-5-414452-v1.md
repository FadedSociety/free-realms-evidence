<!-- fleet job=citem-infer id=cbriarwood-club-card-5-414452-v1 status=done turns=8 usd=0.0083 tokens(read,write,in,out)=[143990, 36303, 18, 4565] model=claude-haiku-5-5 -->
# Briarwood Club Card 5

{"item": {"name": "Briarwood Club Card 5", "locale_id": 414452, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Briarwood Club Cards set (one of eight cards, 414448-414455). Found by searching around Sir Wellington in Briarwood; the quest text says doing so 'to find all of the Briarwood Club Cards' earns a prize. The prize itself is not named in any source.", "where": "Briarwood (beyond the hedge maze, around Sir Wellington)", "price": null, "currency": null, "source": "locale:414425 (quest_objective 'Search around Sir Wellington in Briarwood to find all of the Briarwood Club Cards and receive your prize!'); locale:414426 ('Briarwood Club Cards'); locale:132508 ('This item can be added to the Briarwood Club Cards Collection'); locale:37554 (Sir Wellington is in Briarwood beyond the hedge maze)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 68904, NameId 414452 'Briarwood Club Card 5', type 1, CategoryId 19, Cost 1, MinProfileRank 1, MemberDiscount 10, no coin store price (coin_store_prices empty), no models.", "source": "refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 1172594-1172600; locale:414452"},
  {"claim": "The card is a member of a set of eight: Briarwood Club Card 1-8 (ids 68900-68907 range, names locale 414448-414455), all sharing description locale:132508 and the same Briarwood Club Cards collection.", "source": "refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 1172529-1172642; locale:414448-414455"},
  {"claim": "Sir Wellington's Briarwood location is tied to the Card Duelist storyline (Wellington's Game Face, Cardie Partay), but no quest in the sources gives Club Cards directly.", "source": "locale:413767, locale:413811, locale:413768; prototype/osfr-tools/data/content/npcs_unresolved.json (Card Duelist Part 2 Briarwood)"},
  {"claim": "No coin vendor, Station Cash Marketplace, Coin Shop, or wiki page lists this card. Not in the wiki Items list or any article.", "source": "lookup 'Club Card' and 'Briarwood Club Card' across client, wiki, articles and video returned only client lines"},
  {"claim": "The cluster's 'Gardener's Gummyfruit Gumbo' (locale:414457) is a quest title and unrelated to the cards; 'Pile of Cards' (locale:414456) has no source text in the pack.", "source": "locale:414457; locale:414456"}
 ],
 "confidence": 0.35,
 "open": [
  "The actual prize for completing the eight-card set is not identified in any source; the card's own sources are only the hidden-find collection mechanic. Verify the prize and whether it is a drop, quest reward or event item.",
  "The first-pass tag 'drop' is not supported: no enemy drop or quest reward text names these cards. Treated as collection only.",
  "No wiki page, article or video frame covers the Briarwood Club Cards. Dates of the event and whether the search is still active are unknown, so 'live' stays unsure.",
  "The 'Pile of Cards' (locale 414456) may be the container or pickup for these cards; its description and source are not in the pack. Check it before finalising.",
  "Coin price: none. The definition has Cost 1 and MemberDiscount 10 but no store price, so no coin vendor sale is shown."
 ]}
