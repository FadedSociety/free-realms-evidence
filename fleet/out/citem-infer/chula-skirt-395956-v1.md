<!-- fleet job=citem-infer id=chula-skirt-395956-v1 status=done turns=7 usd=0.0029 tokens(read,write,in,out)=[35001, 8915, 16, 2887] model=claude-haiku-5-5 -->
# Hula Skirt

{"item": {"name": "Hula Skirt", "locale_id": 395956, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Sold only as a component of the [Hula] [Outfit] (Boys) bundle, which includes [Hula] Skirt, Lei Necklace, [Hula] Shirt, [Hula] Anklets, Lei Headdress and [Hula] Bracelets", "where": "Station Cash Marketplace", "price": "Bundle price not captured (wiki price text is blank in our extract); members get a 10% discount on the bundle", "currency": "station_cash", "source": "wiki page 'Hula Outfit (Boys)' (categories: SC Marketplace, Seasonal, Summer); article http://www.freerealms.com:80/article/detail.action?articleId=137"},
  {"type": "event", "detail": "Seaside Summer Splash celebration, when the Hula Outfit was added to the Marketplace", "where": "Seaside / summer event", "price": null, "currency": null, "source": "article http://www.freerealms.com:80/article/detail.action?articleId=137; wiki category 'Summer'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Hula Skirt' (locale 395956) with description 'Hula-mazing!' (locale 397008)", "source": "locale:395956; locale:397008"},
  {"claim": "Hula Skirt is one of six pieces of the Hula Outfit (Boys) bundle, an All-jobs male-exclusive Summer bundle sold in the Station Cash Marketplace", "source": "wiki page 'Hula Outfit (Boys)'"},
  {"claim": "The Hula Outfit was added to the Marketplace for the Seaside Summer Splash celebration", "source": "http://www.freerealms.com:80/article/detail.action?articleId=137"},
  {"claim": "In-game video shows [Hula] [Outfit] <Boys> and <Girls> variants at a sandy beach with tiki torches (Adventurer 20)", "source": "video:yBwnL7jnweI/00058.jpg, video:yBwnL7jnweI/00060.jpg"},
  {"claim": "Client row for the 270 coin price could not be tied to this item: no stores.json entry references definition 15714 or 57136-57146; coin price 270 appears on many unrelated items", "source": "repo:prototype/osfr-tools/data/content/stores.json (searched)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 270-coin store price in the client definition is unverified: no stores.json row maps to this item's definition ids, and 270 coins is shared by many other items. Treat as not a coin vendor sale until a matching item_id is found.",
  "Marketplace price for the Boys bundle and the single skirt is blank in the wiki extract (only 'at the price of , and to Members at the 10% discount price of .'). Need the raw wiki page to fill station_cash amounts.",
  "Whether the skirt is also sold individually, or in a Girls bundle (video shows a Girls variant), is not confirmed; the wiki page covered is the Boys bundle only.",
  "Retirement status not stated by any source; the Summer event and Marketplace listing suggest it has left sale but no source says so.",
  "The 36 client definitions (race/gender variants) are not mapped to bundle sales individually."
 ]}
