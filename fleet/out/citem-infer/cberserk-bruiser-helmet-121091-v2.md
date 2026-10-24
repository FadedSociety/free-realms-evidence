<!-- fleet job=citem-infer id=cberserk-bruiser-helmet-121091-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[11367, 9232, 8, 2087] model=claude-haiku-5-5 -->
# Berserk Bruiser Helmet

{"item": {"name": "Berserk Bruiser Helmet", "locale_id": 121091, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Unconfirmed: coin store rows with item_id 41092 (tint group 1) and 41097 / 41102 (tint groups 2 and 3), matched by definition id only. No store row names the helmet.", "where": "coin store, category_id 101 (category name not found in the data; 'Coin Shop' is not verified)", "price": "41092: 1027 coins (member 924, 10% off); 41097 and 41102: 9453 coins each (member 8507)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12562, :12564, :12566 (verified in this check)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Berserk Bruiser Helmet' is locale 121091, one of the five Berserk Bruiser set pieces (Shirt 121088, Boots 121089, Gloves 121090, Pants 121092).", "source": "locale:121091; locale:121088-121092"},
  {"claim": "Store rows 41092, 41097 and 41102 exist with the prices above; they are the only store rows for ids in the helmet's definition list.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12562-12566"},
  {"claim": "Searching the repo store data for item_ids 41107, 41112, 41117, 41122, 41127, 41132, 41137, 41142 and 41147 finds no rows. The earlier claim that these ids match store rows is wrong.", "source": "repo search of stores.json (no matches)"},
  {"claim": "Price 1027 is shared by unrelated store rows (for example 41093, 41155, 41156), so the price does not identify the helmet.", "source": "pack critique; repo stores.json"},
  {"claim": "Lookup of the name in client, wiki, articles and video returns only the locale entry. No wiki page, article fact, or video frame names the helmet or gives a source.", "source": "lookup 'Berserk Bruiser Helmet' (client, wiki, articles, video)"}
 ],
 "confidence": 0.3,
 "open": [
  "The coin store link is an id match only. Nothing in the store row, wiki, article or video names the helmet, so the Coin Shop source is unconfirmed and should not be wired as fact.",
  "Store category 101 has hundreds of unrelated rows. Its name is not found in the data, so the 'Coin Shop' label is not verified.",
  "Name id collision: collection_catalogue.json line 9195 uses name_id 41092 for a different sanctuary item (item_definition_id 3876). Not evidence for this helmet.",
  "Definition ids 41107-41147 have no store rows, so their sources are unknown. The pack's 16 definitions vs 12 listed ids is not resolved.",
  "No quest reward, enemy drop, event, prize-wheel, vendor or crafting source found. Vendor stock and mention lists are empty.",
  "Retirement and current availability unknown; store rows carry tags L1, L2, L4, R2, T633, R1 but no dates. Green Text / trade-only status unverified."
 ]}
