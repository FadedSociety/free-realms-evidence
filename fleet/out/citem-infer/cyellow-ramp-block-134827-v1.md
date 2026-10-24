<!-- fleet job=citem-infer id=cyellow-ramp-block-134827-v1 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[9141, 13534, 8, 2464] model=claude-haiku-5-5 -->
# Yellow Ramp Block

{"item": {"name": "Yellow Ramp Block", "locale_id": 134827, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, definition 77234 (store category 147), 50 coins; member price 45 coins (10% member discount); no_sale flag set, so it cannot be sold back to the vendor", "where": null, "price": "50 coins (45 coins for members)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77234 (line 16565)"},
  {"type": "vendor", "detail": "Coin store sale, definition 77282 (store category 147), 400 coins; member price 360 coins; sell-back price 40 coins", "where": null, "price": "400 coins (360 coins for members)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77282 (line 16613)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Yellow Ramp Block' is locale 134827, item text", "source": "locale:134827"},
  {"claim": "Client defines two item definitions (77234, 77282) under this name, model hsg_block_ramp_01.adr, slot 0, class 0", "source": "client definition in pack"},
  {"claim": "Both definitions have coin store purchase prices (50 and 400 coins) in the store data, category 147", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77234; item 77282"},
  {"claim": "Sibling color variants (Pink, Purple, Red, Teal, White Ramp Block) sit in the same client block 134822-134827, so this is part of a color-variant ramp-block set", "source": "locale:134822 to locale:134827"},
  {"claim": "Wiki has no article for Yellow Ramp Block; only generic 'Ramp Block' names in wiki building-block lists (Foreman pages) and no price or source there", "source": "lookup wiki: 'Ramp Block' (Foreman Hetfield, Foreman Moser, Foreman Redd pages list block items)"},
  {"claim": "The 'Ramp Block' family is a furniture building block, matching the description 'Great for stackability.' and the housing-style model", "source": "locale:134827 description in client definition"}
 ],
 "confidence": 0.5,
 "open": [
  "The store data names category 147 only by number; the vendor/store name (which coin vendor or shop page) was not resolved, so the vendor detail is generic.",
  "Which definition (77234 at 50 coins or 77282 at 400 coins) is the sold item versus a different variant/tint is not established; both are listed as coin store prices with no wiki page to confirm the split.",
  "No wiki page, image, article, or video frame names Yellow Ramp Block; the sale source is evidenced only by the repo store data, not by a player-facing source.",
  "Live status and retirement are not stated by any source; the store rows carry source tags but no retirement date. 77282 has a sell-back price while 77234 is no_sale; this does not settle whether either was later removed.",
  "The jev first pass (live, furniture, vendor) is a hint only; the vendor and furniture claims rest on the store rows and the description, not on the first pass.",
  "The client cluster shows the color-ramp family, but no source confirms whether the Pink/Purple/Red/Teal/White siblings share the same vendor or price."
 ]}</result>
