<!-- fleet job=citem-infer id=clapping-leopard-helmet-106494-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[4916, 9259, 6, 1947] model=claude-haiku-5-5 -->
# Lapping Leopard Helmet

{"item": {"name": "Lapping Leopard Helmet", "locale_id": 106494, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase, helmet/head category 101; reference-derived listing for tint rows 33412 (tint 1), 33413 (tint 2), 33414 (tint 3). Ids 33415-33423 have no stores.json rows and are unverified.", "where": "Coin Shop, category 101", "price": "291 coins (member price 261 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 33412 (line 11116), item 33413 (line 11117), item 33414 (line 11118); reference-derived from CoinStoreItems.json, not checked against a live transaction (repo:notes/Research/Coin Shop.md lines 25-34)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Lapping Leopard Helmet' at locale 106494, item class 24, slot 1; 35 definitions share the name (ids 33412-33423 listed in the pack).", "source": "locale:106494; client definition in pack"},
  {"claim": "stores.json has rows for item 33412 (category 101, tint group 1), 33413 and 33414 only, each purchase 291, member 261, sell 29. Lines 11116-11118.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 11116-11118"},
  {"claim": "Searching stores.json for ids 33415-33423 returned no rows; the pack's claim that category 103 holds the same price on other rows is unsupported and is dropped.", "source": "repo search of prototype/osfr-tools/data/content/stores.json"},
  {"claim": "Sell-back 29 is not a sourced price. It is the reconstructed rule max(1, purchase // 10), i.e. 291 // 10 = 29.", "source": "repo:notes/Research/Coin Shop.md lines 36-41 (T633)"},
  {"claim": "The 291 price is also the client definition's coin store price (pack coin_store_prices), but the store data itself is reconstructed from Legacy CoinStoreItems.json and ClientItemDefinitions Cost fields, so it is not independent confirmation of a live sale.", "source": "repo:notes/Research/Coin Shop.md lines 25-34; pack client definition"},
  {"claim": "Lookup of the name returns only the client text entry locale:106494; no wiki page, article, image, or video frame names this helmet.", "source": "lookup 'Lapping Leopard Helmet' (client, wiki, articles, video)"}
 ],
 "confidence": 0.4,
 "open": [
  "The only source is a reference-derived Coin Shop row for 3 of 12 ids (33412-33414). Live availability is unconfirmed.",
  "Ids 33415-33423 (9 of 12 definitions, and their tints/races) have no stores.json rows and no verified source.",
  "Retirement status unknown; no source says whether the Coin Shop listing was removed.",
  "No vendor NPC, location, quest reward, drop, event, or crafting source found.",
  "The wiki 'Coin Shop' category was not confirmed against this item; no wiki page exists in lookup.",
  "The 29-coin sell-back is a reconstructed value, not a sourced price."
 ]}
