<!-- fleet job=citem-infer id=chaunted-headstone-16638-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5700, 8122, 6, 1894] model=claude-haiku-5-5 -->
# Haunted Headstone

{"item": {"name": "Haunted Headstone", "locale_id": 16638, "kind": "furniture"},
 "sources": [
  {"type": "event", "detail": "Halloween activate-able housing item, listed with Jack-O-Lantern and Easy Bake Cauldron. The article does not say how it was issued or sold.", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304 (Halloween Activate-able Items article; fact:housing via lookup articles)"},
  {"type": "marketplace", "detail": "Included free in a bundle of two Quest Packs. The bundle string does not name the two packs, so the bundle is unidentified. The headstone was not sold on its own in this text.", "where": "Station Cash Marketplace", "price": "1,200 SC for the two Quest Packs plus the headstone (advertised as a 400 SC value; the 400 SC is marketing, not a per-item price)", "currency": "station_cash", "source": "locale:156856 (ui, Quest Packs; text confirmed by lookup and locale)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Haunted Headstone' is locale 16638; its description (locale 16651) says to place it on the ground and click it to turn into a skeleton.", "source": "locale:16638, locale:16651"},
  {"claim": "Halloween activate-able housing items include Jack-O-Lantern, Easy Bake Cauldron and Haunted Headstone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Bundle text: buy the two Quest Packs together and get the Haunted Headstone included, all for 1,200 SC, a 400 SC value.", "source": "locale:156856"},
  {"claim": "Client definition 69820 has no coin store price, and no repo store, vendor or drop entry for it was found.", "source": "client definition pack; repo search for 69820 and 'Haunted Headstone' returned no store entry"},
  {"claim": "Sibling Halloween item names sit at locale 16634-16643 (Scaredy Cake through Super Spooky Flair Shard). Locale 16633 is a dev-note asset name and is not used as evidence.", "source": "locale:16634-16643"},
  {"claim": "No wiki page for the Haunted Headstone turned up in lookup.", "source": "lookup wiki search, 'Haunted Headstone'"}
 ],
 "confidence": 0.4,
 "open": [
  "The bundle's two Quest Packs are not named in locale:156856. Locale 112 ('Pumpkin Costume Quest Pack') and 114 ('Chiller Boombox Quest Pack') exist, but nothing ties them to this bundle, so they are not used as a source.",
  "The bundle's name, dates and whether it is still sold are unknown. The bundle is the only purchase evidence.",
  "The article gives no Halloween event dates, sale method, or standalone price. The 2009 'Super Spooktacular' link from the earlier answer is not confirmed for this item and is dropped.",
  "live is unsure and retired is unknown. No source states the headstone was retired or is still obtainable.",
  "The earlier critique flagged 'sold/issued alongside' as unsupported; it is removed. The 400 SC figure is advertised value, not a sale price for the headstone."
 ]}
