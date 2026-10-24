<!-- fleet job=citem-infer id=cspider-etched-gravestone-118878-v1 status=done turns=3 usd=0.0018 tokens(read,write,in,out)=[7792, 6181, 8, 1968] model=claude-haiku-5-5 -->
# Spider-Etched Gravestone

{"item": {"name": "Spider-Etched Gravestone", "locale_id": 118878, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (vendor not named in our data; stores.json lists it as a coin-priced store item, category 57, tint group 3)", "where": null, "price": "50 coins (member price 45 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 16839 (line 4210)"},
  {"type": "marketplace", "detail": "Station Cash store listing seen in a video frame, store page showing the gravestone with 'Add Station Cash' purchase flow", "where": "Station Cash store (store page not named in frame; likely the SC Marketplace)", "price": "135 Station Cash", "currency": "station_cash", "source": "video:g7pncDFzIrw/00230.jpg"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name locale 118878 is 'Spider-Etched Gravestone', definition 16839, one definition, model hsg_gravestone_04.adr, housing-style item (slot 0, class 0)", "source": "locale:118878"},
  {"claim": "Coin store price 50 for item 16839, member price 45, sell price 5", "source": "repo:prototype/osfr-tools/data/content/stores.json item 16839 (line 4210)"},
  {"claim": "Spider-Etched Gravestone appears in a housing video frame", "source": "video:mc1VU_zsfSs/00228.jpg"},
  {"claim": "Store frame shows Spider-Etched Gravestone at 135 station_cash with 'Add Station Cash' purchase option", "source": "video:g7pncDFzIrw/00230.jpg"},
  {"claim": "Sits in a cluster of Halloween/graveyard housing items (Snake-Etched Gravestone, Graveyard Fence, Hedge Urn, etc.) with consecutive locale ids 118873-118883", "source": "locale:118873 through locale:118883"}
 ],
 "confidence": 0.6,
 "open": [
  "No wiki page covers this item; the coin vendor that sells it (the stores.json entry has no vendor name) is not identified. Check the store category 57 vendor mapping.",
  "The 135 Station Cash price comes from a single video frame; the store section name (SC Marketplace vs. other) and date are not confirmed.",
  "Client description is empty, so no in-game text confirms the item's theme beyond the name and the video caption ('Click on the gravestone to see what crawls out').",
  "Retirement status unknown: no source states whether the coin or Station Cash listing was removed later.",
  "Neighbouring Snake-Etched Gravestone (locale 118877) and other cluster items share the same 50-coin pattern; the seasonal (Halloween) release tie is inferred from the cluster, not from a source."
 ]}
