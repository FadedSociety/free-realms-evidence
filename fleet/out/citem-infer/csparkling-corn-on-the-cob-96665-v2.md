<!-- fleet job=citem-infer id=csparkling-corn-on-the-cob-96665-v2 status=nothing_found turns=2 usd=0.0020 tokens(read,write,in,out)=[5042, 9290, 6, 1595] model=claude-haiku-5-5 -->
# Sparkling Corn on the Cob

{"item": {"name": "Sparkling Corn on the Cob", "locale_id": 96665, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition_id 31259, item class 9 (food/consumable), slot 0. Description: 'Eating this food temporarily increases your talent as a Blacksmith, Chef, Miner, and Postman.' No coin store price in the client definition (coin_store_prices empty).", "source": "locale:96665; pack client_definition"},
  {"claim": "Re-check of the client text: the 'Sparkling' food series in the locale table is 96626 Sparkling Cherry Pie, 96627 Sparkling Pink Donut, 96629 Sparkling Crescent Roll, 96636 Sparkling Ham and Cheese, 96637 Sparkling Star Soup, 96639 Sparkling Fish, 96646 Sparkling Loaf, 96647 Sparkling Tomato Soup, 96649 Sparkling Pineapple Burger, 96662 Sparkling Banana, 96665 Sparkling Corn on the Cob, 96680 Sparkling Croissant Sandwich, 96681 Sparkling Gingerbread Cookie, 96689 Sparkling Grape, 96696 Sparkling Chocolate Cake, 96704 Sparkling Assorted Cookies, 96705 Sparkling Hot Dog, 100990 Sparkling Mushroom. Only the client name line exists for 96665 in the client lookup.", "source": "locale search 'Sparkling' (ids listed above)"},
  {"claim": "Client lookup for 'Sparkling Corn on the Cob' returns only the client line locale:96665. No wiki page, article, video frame, vendor stock, quest reward, drop or event entry names it.", "source": "lookup client/wiki/articles/video 'Sparkling Corn on the Cob'"},
  {"claim": "Repo search for 31259 and 'Sparkling Corn' finds no store, vendor, quest, recipe or drop entry for this item. Repo hits for 'Sparkling' are unrelated (flair shards, mushroom quest text, spawn-type notes).", "source": "search repo '31259|Sparkling Corn|Sparkling'"},
  {"claim": "Locale 96666 (Maker's Cake - DEPRECATED) is flagged not_live and is dropped from the cluster evidence per critique.", "source": "pack id_check"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source found anywhere in the repo, client text, wiki, articles or video. No coin store price, so no coin vendor sale is evidenced. The first-pass 'event' guess is unsupported and not adopted.",
  "Live status unverified. The first-pass 'live: yes' has no source. Whether this food was ever obtainable is unknown.",
  "The talent-buff link to Carrot Cheesecake and Cheesy Ritzy Bits rests on shared description wording and was not checked against each locale string here.",
  "Sibling 'Sparkling' foods have no source in the pack either; a shared event or cooking source for the series would need a wiki Items/cooking or holiday page check that was not found."
 ]}
