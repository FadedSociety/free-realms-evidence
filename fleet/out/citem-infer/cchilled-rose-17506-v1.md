<!-- fleet job=citem-infer id=cchilled-rose-17506-v1 status=nothing_found turns=5 usd=0.0027 tokens(read,write,in,out)=[33479, 11068, 12, 1955] model=claude-haiku-5-5 -->
# Chilled Rose

{"item": {"name": "Chilled Rose", "locale_id": 17506, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 17506 is the name 'Chilled Rose'; its only client line is the name itself. The client definition (definition 9138) has no models, no coin store price, and class 0 / slot 0.", "source": "locale:17506; client definition 9138"},
  {"claim": "The description text 'This item can be added to the Snowhill Roses Collection' (ui locale:132492) shows it is a collection-piece item for the Snowhill Roses collection, not a sold item.", "source": "locale:132492"},
  {"claim": "The wiki 'List of Collections' page lists a '[Snowhill] [Roses]' collection, so the collection exists on the wiki.", "source": "wiki page: List of Collections"},
  {"claim": "Sibling items 17501-17507 (Wintery, Snowy, Frosty, Frozen, Frostbitten, Chilled, Glacial Rose) and 17508-17511 (Icy/Wintery/Snowy/Frosty Daisy) form a cluster of collection pieces; 17573 'Snowhill Roses' and 17583 ('These special roses are able to survive even the harshest cold weather conditions.') name the set.", "source": "locale:17501-17511, locale:17573, locale:17583"}
 ],
 "confidence": 0.2,
 "open": [
  "No wiki article, video, article fact, vendor stock or quest/drop answer names Chilled Rose or its sibling roses, so no source for how a player obtains it was found. Do not treat the collection as a live source without evidence.",
  "The 'Snowhill Roses' collection appears in the wiki List of Collections, but no wiki page for its contents was retrieved; the wiki page for the collection should be checked for the rose list and acquisition method (quest, drop, or other).",
  "No coin store price in the client definition (coin_store_prices empty) and no repo store entry for definition 9138, so no coin vendor or Coin Shop sale is evidenced.",
  "Live status is unconfirmed: the first-pass 'live: yes' is a hint only. The rose may be a sub-piece of a collection that was retired; no retirement source found.",
  "Set membership: the Snowhill Roses collection's rose list is unverified; Chilled Rose may or may not belong to it, though the description text says it can be added to it."
 ]}
