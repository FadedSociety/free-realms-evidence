<!-- fleet job=citem-infer id=cdoggy-cardboard-bot-mask-9945-v2 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[6183, 13484, 6, 2035] model=claude-haiku-5-5 -->
# Doggy Cardboard Bot Mask

{"item": {"name": "Doggy Cardboard Bot Mask", "locale_id": 9945, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace bundle 'Doggy Cardboard Bot Mask' (bundle Id 2386, NameId 9945, grants GameItemId 869, StoreId 1, CurrencyType 1). Bundle is only a Comment-labelled entry; no real SC price recorded (Price field is a placeholder 1).", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/StoreBundles.json:2512-2535; refs:FreeRealms-Legacy/src/Resources/StoreBundles.json:2512 (Comment 'Doggy Cardboard Bot Mask'); currency type inferred from CurrencyType 1"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Doggy Cardboard Bot Mask' is locale 9945; description line locale 150245 'This is a Doggy Cardboard Bot Mask item.'; locale 150595 'The mask for the doggy cardboard bot costume.'", "source": "locale:9945; locale:150245; locale:150595"},
  {"claim": "Client definition: head slot 1, class 31, 35 variants over 12 definition ids (10154-10165), pet head model pet_dog_<descriptor>_head_cardboardbot.adr", "source": "client definition in pack; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1063047-1063468 (Comment 'Doggy Cardboard Bot Mask' on the variant entries)"},
  {"claim": "A Marketplace bundle named for this mask exists (Id 2386, GameItemId 869), with a placeholder price and a 2040 expiry", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/StoreBundles.json:2512-2535"},
  {"claim": "The 270-coin store price could not be linked to definition ids 10154-10165. stores.json 270-coin entries (e.g. 5869, 8690-8699, 8869) and item 12386 do not match these ids.", "source": "repo:prototype/osfr-tools/data/content/stores.json:1445, 2333-2342, 2512, 3457"},
  {"claim": "Peccadillo promo and the 'In the Marketplace: Bionic Pet Outfits' article name the Doggy Cardboard Bot Outfit (locale 72303), not this mask; they are dropped as sources for the mask", "source": "refs:articles/facts.json:63478-63491; refs:articles/facts.json:32874-32886; locale:3675"}
 ],
 "confidence": 0.4,
 "open": [
  "Marketplace SC price for bundle 2386 is unknown; the Price field is a placeholder, so no price is given.",
  "The 270-coin store price in the client definition is not verified. No stores.json entry maps to definition ids 10154-10165, so no coin vendor source is listed.",
  "Peccadillo promo source removed: the cited article and locale 3675 name only the Doggy Cardboard Bot Outfit, not this mask.",
  "The Marketplace source is supported only by the bundle data. The earlier 'sold alongside the Outfit' claim is removed, because the article does not mention the mask.",
  "No wiki page, category, image, video or vendor stock covers this mask. Current availability and retirement are unknown; the 2040 expiry is a placeholder.",
  "Kind is 'clothing' rather than the first-pass 'pet': it is a head-slot costume worn by a dog pet."
 ]}
