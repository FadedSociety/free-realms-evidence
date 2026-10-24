<!-- fleet job=citem-infer id=cn-bum-rush-brawler-shoulderpads-pl-bum-rush-brawler-shoulder-132878-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[35944, 16830, 12, 2645] model=claude-haiku-5-5 -->
# {n}Bum Rush Brawler Shoulderpads{pl="Bum Rush Brawler Shoulderpads"}

{"item": {"name": "Bum Rush Brawler Shoulderpads", "locale_id": 132878, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Fraz (pixie merchant; sells exclusively Brawler job items)", "where": "Wugachug", "price": null, "currency": null, "source": "wiki page Fraz (sells list includes Bum Rush Brawler Shoulderpads); wiki Merchants page 'Fraz found in Wugachug'"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132878 is 'Bum Rush Brawler Shoulderpads', item class 25, slot 6, one definition (id 75870).", "source": "locale:132878; client definition in pack"},
  {"claim": "Wiki Fraz page 'Sells' list includes [Bum] [Rush] [Brawler] Shoulderpads, alongside Pants, Beanie, Gloves, Boots, Shirt.", "source": "wiki page Fraz"},
  {"claim": "Fraz is a pixie merchant in Wugachug who sells exclusively Brawler Job items; introduced in-game August 6, 2013.", "source": "wiki page Fraz (wikitext 10132-48993-ec52c3832f5b.wiki)"},
  {"claim": "Wiki Merchants/location list places Fraz in Wugachug.", "source": "freerealms-wiki/wikitext/2651-44290-cff0fea2345a.wiki, Wugachug section"},
  {"claim": "Bum Rush Brawler set items (Shirt, Boots, Gloves, Beanie, Pants, Shoulderpads) sit together in client locale 132873-132878.", "source": "locale:132873-132878"},
  {"claim": "The pack's coin price 453 does NOT match this item: repo stores.json has no row for item_id 75870 (or 132878); 453 is the purchase price of other items (e.g. 75744, 75807).", "source": "repo:prototype/osfr-tools/data/content/stores.json (search for item_id 75870 returned nothing)"}
 ],
 "confidence": 0.6,
 "open": [
  "Price unknown: no wiki price for Fraz's items was found, and the client's 453 coin price is not attached to item 75870 in stores.json, so it cannot be cited as this item's price. Confirm the Fraz/Brawler price in-game or from a store dump.",
  "Currency not stated by the wiki for Fraz; assumed coin-vendor sale from the Fraz page, but not confirmed.",
  "Live status unsure: the repo's Wugachug build notes (notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:187) say Fraz and similar shops are 2013 updates that a launch-era rebuild would not have. No retirement date was found, so retired is null.",
  "Pack's critiques: none were carried in the pack. The repo's Fraz NPC record (quest-lines/npcs.json) also has open issues: its wiki location quote is loose, and the image File:Fraz.jpg shows an unnamed winged helmeted character, so the Fraz identity of that image is not confirmed.",
  "Drops, quest rewards, prize wheel, or other sources were not found in the pack or the wiki; none are listed."
 ]}
