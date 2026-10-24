<!-- fleet job=citem-infer id=cred-party-popper-407462-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[12154, 9949, 8, 2064] model=claude-haiku-5-5 -->
# Red Party Popper

{"item": {"name": "Red Party Popper", "locale_id": 407462, "kind": "consumable"},
 "sources": [{"type": "event", "detail": "5 Million Celebration event, 5M Party Wheel virtual rewards: 'Three Party Poppers' (article gives the generic 'Party Popper' only, not the red colour)", "where": null, "price": null, "currency": null, "source": "articles/facts.json (5M Party Wheel virtual rewards, quote 'One Party Crate * One Silly String can * Three Party Poppers * Grab Bag'); http://www.freerealms.com:80/article/detail.action?articleId=316; locale:407421 (placeholder 'Used for 5M item: Party Popper')"}],
 "retired": true, "live": "unsure",
 "evidence": [{"claim": "Client name and description are for the red colour variant of the party popper family (Green, Yellow, Red, Blue, Orange; generic Party Popper locale:407420 / 407422).", "source": "locale:407462; locale:407470; locale:407420; locale:407422"},
  {"claim": "The 5M celebration event (2009-09-16, limited time, login window Sept 16-23 2009) gave three Party Poppers as special virtual rewards.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=316 (via articles/facts.json '5M Party Wheel virtual rewards')"},
  {"claim": "Client text tags 'Used for 5M item: Party Popper' link the popper to the 5M item, but this is a placeholder-flagged string.", "source": "locale:407421"},
  {"claim": "No coin store price, vendor stock, wiki page, or video frame names the Red Party Popper; no coin vendor sale found.", "source": "repo search (no 62533 hit); refs search; lookup client/wiki/video"}],
 "confidence": 0.35,
 "open": ["The 5M article names only 'Party Poppers' with no colour, so it is not proven that the red variant was one of the three rewards; the colour variants may have been handed out differently or not at all.",
  "The 5M Party Wheel is the only evidence; it is not confirmed whether it was a prize-wheel spin or a direct event grant, so the source type is 'event' as the best fit.",
  "Retired status follows from the limited-time 5M event (Sept 2009); no source states that the red variant specifically was retired.",
  "Live status is 'unsure': the client definition exists (definition 62533, class 69), but no store or wiki record confirms the item was sold or granted live.",
  "Price: none in the client (no coin_store_prices) and no Station Cash listing found.",
  "Definition 62533 has no model files and no repo content record; check repo data stores for an item row before rebuild."]}
