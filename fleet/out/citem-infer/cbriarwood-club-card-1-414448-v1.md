<!-- fleet job=citem-infer id=cbriarwood-club-card-1-414448-v1 status=done turns=7 usd=0.0067 tokens(read,write,in,out)=[103403, 31067, 16, 3500] model=claude-haiku-5-5 -->
# Briarwood Club Card 1

{"item": {"name": "Briarwood Club Card 1", "locale_id": 414448, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Briarwood Club Cards set: one of eight cards (Briarwood Club Card 1-8, locale 414448-414455) to find around Sir Wellington in Briarwood; finding the full set earns a prize (prize not named in the evidence). Card 1 is a set piece, not a purchasable item.", "where": "Briarwood (around Sir Wellington)", "price": null, "currency": null, "source": "locale:414425 (quest_objective: 'Search around Sir Wellington in Briarwood to find all of the Briarwood Club Cards and receive your prize!'); locale:414448; locale:414447 'Loot Cards'; quest-lines/citem-packs.json (cbriarwood-club-card-3-414450 and -4-414451 cluster, same 8-card set)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item 68900 is 'Briarwood Club Card 1', description 'This item can be added to the Briarwood Club Cards Collection' (locale:414448; description string locale:132508).", "source": "locale:414448; quest-lines/citem-packs.json cluster"},
  {"claim": "The set is found by searching around Sir Wellington in Briarwood, and finding all cards gives a prize.", "source": "locale:414425"},
  {"claim": "The 8 cards form one set, with the set name 'Briarwood Club Cards' (locale 1504688656 in the client dat).", "source": "locale:414448-414455; opening-journal-text-v2/locale/en_us_data.dat"},
  {"claim": "No coin store price, no vendor stock, no wiki page, no image, no article or video reference names this card. The first-pass source_guess 'drop' is not supported: nothing in the evidence shows an enemy drop.", "source": "client definition (coin_store_prices empty); lookup of client/wiki/articles/video returned only client text"},
  {"claim": "Sir Wellington is a Briarwood archaeologist and quest giver (Card Duelist opponent), so the set is tied to his NPC.", "source": "repo:prototype/osfr-tools/data/content/npcs/briarwood.json:60119-60140"}
 ],
 "confidence": 0.35,
 "open": [
  "The mechanic is not confirmed: 'search around' could mean hidden world pickups or a quest-driven pickup. No repo quest or spawn data for these cards was found.",
  "The prize for completing the Briarwood Club Cards set is not identified; no item name or reward source was found in the evidence.",
  "Dates, the event or promotion that ran the set, and whether it is still live are unknown. The jev first pass says live 'yes', but no source supports it, so live is marked unsure.",
  "No wiki article covers Briarwood Club Card 1 or the set. Verify on the wiki or in video before treating any card as a confirmed source.",
  "Kind is set to 'collection' from the description and the first pass; no model or icon was available to confirm."
 ]}
