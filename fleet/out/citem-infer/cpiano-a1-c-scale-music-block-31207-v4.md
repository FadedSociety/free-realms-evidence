<!-- fleet job=citem-infer id=cpiano-a1-c-scale-music-block-31207-v4 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[14126, 8436, 8, 2197] model=claude-haiku-5-5 -->
# Piano A1 C-Scale Music Block

{"item": {"name": "Piano A1 C-Scale Music Block", "locale_id": 31207, "kind": "furniture"},
 "sources": [
  {"type": "membership", "detail": "Monthly Member Pack: 5x Piano A1 C-Scale Music Block, listed with 5x Piano B1, C1 and C2 in the same pack row. The month is not confirmed; the page snippet shows April 2013 and May 2013 labels near the row.", "where": null, "price": null, "currency": null, "source": "wiki: Monthly Member Pack Items"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name, locale 31207, is 'Piano A1 C-Scale Music Block'; description 'Jumping on this block will play a sound!'; one definition, slot 0, class 163, model mkt_piano_block_c_major_a1.adr.", "source": "locale:31207"},
  {"claim": "The Piano C-Scale notes sit together at locales 31202-31209; Saxophono notes at 31210-31212.", "source": "locale:31202-31209; locale:31210-31212"},
  {"claim": "The Monthly Member Pack Items wiki page lists '5x [Piano A1] C-Scale Music Block' with 5x Piano B1, C1 and C2 (the same row). The row's month is not clear from the snippet.", "source": "wiki: Monthly Member Pack Items"},
  {"claim": "Sanctuary store bundle Id 5538, comment 'Piano A1 C-Scale Music Block', NameId 31207, grants Quantity 10 of GameItemId 5517 (MarketingItemId 38906); launch 2012-12-17, expire 2041-01-07. It is a store product record with no price or currency, so it is not used as a price source.", "source": "refs: Sanctuary/src/Resources/StoreBundles.json lines 29573-29590"},
  {"claim": "Coin store record for item 38906 is 400 purchase coins (member 360) but is marked no_sale: true, sell_price null, and names no vendor. Not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12419"},
  {"claim": "Station Cash Marketplace frames show the C1 and D1 C-Scale blocks at 45 station_cash. No frame shows A1 listed, so A1's Marketplace price is not verified and A1 is not listed as a Marketplace source.", "source": "video:ljDRabG8Akk/00072.jpg; video:4h2eVoje3Eg/00284.jpg; video:4h2eVoje3Eg/00286.jpg (as quoted in the pack)"}
 ],
 "confidence": 0.4,
 "open": [
  "Marketplace for A1 is unverified. The 45 station_cash price is evidenced only for the sibling C1 and D1 notes; a frame showing A1 listed is needed before adding a marketplace source.",
  "Monthly Member Pack month for A1 is not confirmed (April 2013 or May 2013 label region). Check the full wiki page to place the row. The pack has no price, so the membership source's price is null.",
  "Coin vendor price of 400 coins (member 360) in stores.json is marked no_sale and has no vendor; no coin vendor sale is verified.",
  "Sanctuary bundle 5538 grants 10 items with a 2012-12-17 launch; its real sale price and channel are unknown.",
  "Retirement and live status are unknown: no end date was found for the member pack row, the Marketplace listing, or the store bundle. Live is set to unsure.",
  "The earlier 180 Station Cash C-Scale bundle (locale:2990) was not re-verified and is not used."
 ],
 "wireable": false
}
