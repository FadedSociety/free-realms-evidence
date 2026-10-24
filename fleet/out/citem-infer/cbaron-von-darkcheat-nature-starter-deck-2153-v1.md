<!-- fleet job=citem-infer id=cbaron-von-darkcheat-nature-starter-deck-2153-v1 status=done turns=11 usd=0.0081 tokens(read,write,in,out)=[204572, 28509, 24, 4953] model=claude-haiku-5-5 -->
# Baron von Darkcheat Nature Starter Deck

{"item": {"name": "Baron von Darkcheat Nature Starter Deck", "locale_id": 2153, "kind": "card"},
 "sources": [{"type": "marketplace", "detail": "Station Cash Marketplace sale of the 40-card Baron von Darkcheat Nature starter deck (Trading Card Game Series 3 product, sphere Nature). Store bundle Id 5025, MarketingItemId 17768, grants GameItemId 5105 x1, NameId 2153, DescriptionId 2162, StoreId 1 (the single Marketplace store), launch 2011-11-09.", "where": "Station Cash Marketplace (Trading Card Game section)", "price": "539 station_cash", "currency": "station_cash", "source": "wiki: Items page, Trading Card Game section, 'Baron Cone Nature Starter Deck - {{SC|539}}' (freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:523); store bundle row refs FreeRealms-Legacy/src/Resources/StoreBundles.json:23192-23215"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name and description: 'Baron von Darkcheat Nature Starter Deck', a 40-card starter deck from the third Free Realms TCG set, based on the Nature sphere, with a Snowhill card player.", "source": "locale:2153; locale:2162"},
  {"claim": "Store bundle for this deck exists in the Marketplace store (StoreId 1), with MarketingItemId 17768 (the definition id) and GameItemId 5105, launch 2011-11-09, expire 2040.", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:23192-23215"},
  {"claim": "Wiki lists the deck in the Trading Card Game section at 539 SC (Station Cash).", "source": "wiki: Items page, freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:523"},
  {"claim": "Sister Shattered Past Nature Starter Deck is also listed at 539 station_cash in a Station Cash Marketplace screenshot, showing the same price tier for the Marketplace starter decks.", "source": "video:UFsVcZ3X5iA/00052 (frame text; Shattered Past product, not this item)"},
  {"claim": "No coin store price in client definition or repo coin stores; vendor_stock is empty, so the cheap first-pass 'vendor' guess is not supported.", "source": "pack client_definition.coin_store_prices = []; pack vendor_stock = []"},
  {"claim": "Four Baron starter decks (Chaos, Machine, Nature, Order) appear together in the wiki Trading Card Game list, all at 539 SC.", "source": "wiki: Items page, freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:521-524"}
 ],
 "confidence": 0.6,
 "open": [
  "The 539 SC price is from the wiki list; no video frame or store screenshot showing the Baron Nature deck with its price was found. The video frame that showed 539 is the Shattered Past Nature deck.",
  "Live status and retirement not confirmed: the wiki list has no retired marker, and the store row expire date (2040) is a placeholder-style date, so the deck may have left the store later. Need a dated source.",
  "Store bundle Price field is 1 with CurrencyType 1 in every StoreBundles row, so the field does not decide the price; the 539 figure rests on the wiki.",
  "No quest reward, drop, event or prize-wheel source for this deck was found. The four event answers in the pack only cite locale:2153 and name the expansion, so they are not sources for this item.",
  "The pack's 'vendor' first-pass guess is unsupported: no coin vendor stocks it and it has no coin price."
 ]}
