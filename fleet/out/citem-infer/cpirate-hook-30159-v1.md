<!-- fleet job=citem-infer id=cpirate-hook-30159-v1 status=done turns=6 usd=0.0052 tokens(read,write,in,out)=[57476, 23831, 14, 3336] model=claude-haiku-5-5 -->
# Pirate Hook

{"item": {"name": "Pirate Hook", "locale_id": 30159, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store vendor sale (vendor not identified; store row is Legacy-derived reference pricing with no vendor binding in our data). Four definitions: 8153 and 8159 (category 102, tint group 1) and 8163 and 8167 (category 102, tint group 2, flagged no_sale for selling back to vendors).", "where": null, "price": "1500", "currency": "coins", "source": "repo:data/content/stores.json item 8153; item 8159; item 8163; item 8167 (each purchase_price_coins 1500, member_price_coins 1350 with 10% member discount)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Pirate Hook' is locale 30159, description 'Beware of ticking crocodiles.' (locale 30173 'Kick butt with one leg.' is the flavor line for the same name); item has 4 definitions (8153, 8159, 8163, 8167), slot 2, class 1, models freestyle_<race>_f_hands_hookwglove.adr and freestyle_<race>_m_hands_hookandglove.adr.", "source": "client definition pack; locale:30159; locale:30173"},
  {"claim": "Coin store price 1500 is recorded for all four definition ids.", "source": "repo:data/content/stores.json item 8153, 8159, 8163, 8167"},
  {"claim": "Sibling pirate set items (Pirate Corset 30158, Pirate Hat 30160, Pirate Pegleg Pants 30161, Pirate Shirt 30164) sit in the same locale block, suggesting one pirate outfit set, but no source states the set's sale or availability.", "source": "locale:30158, 30160, 30161, 30164"},
  {"claim": "Client lines naming a pirate hook (locale 5215 'I seem to have misplaced my trusty pirate hook...', locale 5220) are marked QA/placeholder test text, so they are not evidence of a quest reward.", "source": "locale:5215; locale:5220"},
  {"claim": "No wiki page, article, video frame, quest, drop or event names the Pirate Hook.", "source": "lookup on client, wiki, articles, video returned no matches beyond client text"}
 ],
 "confidence": 0.35,
 "open": [
  "Which coin vendor (and zone) sells the 1500-coin pirate items is not bound in our data; stores.json rows carry no vendor id and their price provenance is 'reconstructed' from Legacy reference, so the vendor and the sale itself need a live-source check.",
  "Live status is unconfirmed: jev's first pass says live=yes, but the only evidence is reconstructed Legacy store pricing. No wiki page confirms sale, and no retirement source was found.",
  "Whether the item is part of a sold pirate outfit set (corset, hat, pegleg pants, shirt) or a standalone purchase is not stated by any source.",
  "Store category 102 is not mapped to a shop name in the repo, so 'where' is null.",
  "The four definitions likely differ by race/gender model (tint groups 1 and 2); whether tint group 2 (8163/8167) was ever sold separately is unknown; their no_sale flag only refers to selling back to vendors.",
  "The 'Beware of ticking crocodiles' description and locale 433603 pirate joke line are flavor text, not sources."
 ]}
