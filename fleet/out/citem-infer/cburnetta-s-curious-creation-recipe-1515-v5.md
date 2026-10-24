<!-- fleet job=citem-infer id=cburnetta-s-curious-creation-recipe-1515-v5 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6749, 8481, 6, 1819] model=claude-haiku-5-5 -->
# Burnetta's Curious Creation Recipe

{"item": {"name": "Burnetta's Curious Creation Recipe", "locale_id": 1515, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Mae Farnum (Farnum Farmstead NPC, npc_id 9000000396). Client text says the recipe can be bought from her; no captured NPC price or stock screen.", "where": "Farnum Farmstead", "price": "unknown", "currency": null, "source": "locale:421052; repo:prototype/osfr-tools/data/content/vendors.json:305-326 (item_id 848; price_basis says reference only, no captured retail quote)"},
  {"type": "other", "detail": "Bordon Cloo (Sanctuary). Client-text mention only, unverified. Locale 389647 uses the same 'buy it from ... in Sanctuary' wording for another recipe, so the line may be generic template text. Not a confirmed vendor.", "where": "Sanctuary", "price": null, "currency": null, "source": "locale:421061; locale:414285"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item 848 is Burnetta's Curious Creation Recipe, name locale 1515, description 'This recipe teaches you how to create Burnetta's Curious Creation.'", "source": "locale:1515; locale:1542"},
  {"claim": "Client text says the recipe is bought from Mae Farnum in Farnum Farmstead", "source": "locale:421052"},
  {"claim": "vendors.json lists Mae Farnum stocking item 848, with the stock list and prices noted as not in any source", "source": "repo:prototype/osfr-tools/data/content/vendors.json:305-326"},
  {"claim": "Client text says Bordon Cloo in Sanctuary sells the recipe (text only)", "source": "locale:421061; locale:414285"},
  {"claim": "Quest objective 'Get the Burnetta's Curious Creation recipe' exists; owning quest not identified", "source": "locale:414286"},
  {"claim": "The recipe is used in the Downey Curious Gift Baskets holiday quest line (cook and hand over to Downey); this quest consumes the item and is not a source of it", "source": "locale:421000; locale:421002; locale:421050; locale:73402"},
  {"claim": "The 540/486 coin figures are reconstructed reference defaults shared by a category of recipe rows, not a captured sale price. Client coin_store_prices [540] carries the same reconstructed value.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:317-321; repo:prototype/osfr-tools/data/content/stores.json:17267"}
 ],
 "confidence": 0.4,
 "open": [
  "Mae Farnum price unknown: no captured NPC quote. 540/486 are reconstructed reference values, not evidence of a sale price.",
  "Bordon Cloo sale is text-only and may be template wording (see locale:389647). Not a confirmed vendor.",
  "Owning quest of locale:414286 ('Get the Burnetta's Curious Creation recipe') not identified; check whether it grants the recipe.",
  "retired/live status unknown. No source says it was retired; the wiki lookup errored on this query, so no wiki page was checked.",
  "Removed earlier citations locale:829103903 and locale:1275934548: these ids do not exist and are not used here.",
  "No Coin Shop, SC Marketplace, prize wheel, enemy drop, or event source found.",
  "Not wireable: no evidenced price and no evidenced granting quest, drop, or event."
 ]}
