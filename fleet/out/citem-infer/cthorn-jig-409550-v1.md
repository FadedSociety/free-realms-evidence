<!-- fleet job=citem-infer id=cthorn-jig-409550-v1 status=done turns=5 usd=0.0040 tokens(read,write,in,out)=[31381, 17623, 12, 2887] model=claude-haiku-5-5 -->
# Thorn Jig

{"item": {"name": "Thorn Jig", "locale_id": 409550, "kind": "consumable"},
 "sources": [
  {"type": "vendor", "detail": "Guppie, the fishing supply vendor (lure stock; item-specific stock not confirmed)", "where": "Sacred Grove Shallows", "price": null, "currency": null, "source": "locale:408632 'Buy a lure from Guppie'; locale:408645 'Did you buy that lure from Guppie yet?'; locale:408623 'He carries all the basic supplies a fisherman might need.'; notes/Build Guides/Content/Jobs/Fisherman.md:262 (wiki says lures are bought from the Coin Shop under supplies, Guppie sells lures in the Shallows)"},
  {"type": "coin_shop", "detail": "Coin Shop, supplies category (lure sold as a supply; item-specific listing not confirmed)", "where": "Coin Shop", "price": null, "currency": null, "source": "notes/Build Guides/Content/Jobs/Fisherman.md:262 citing wiki Fisherman page (wiki text: 'Thorn Jig - \"This [lure] gives a...\"' on page ns0 Fisherman)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item name 'Thorn Jig' is a client item (locale 409550); the item definition is 68162, class 142, slot 0, with no coin store price", "source": "client definition; locale:409550"},
  {"claim": "Lure text: gives a 10% better chance of catching Blue Thornfin, Chipsen Fish and Thorny Trout", "source": "client definition description; locale:29773, locale:29770, locale:29751 (NPC dialog 'likes the Thorn Jig')"},
  {"claim": "Fish-to-lure pairing Thorn Jig -> Blue Thornfin, Chipsen Fish, Thorny Trout", "source": "notes/Build Guides/Content/Jobs/Fisherman.md:207,214,239,276; prototype/osfr-tools/data/content/fishing.json:1495-1503"},
  {"claim": "Lures are bought from Guppie in Sacred Grove Shallows (general lure vendor, not Thorn Jig-specific)", "source": "locale:408632; locale:408645; locale:408623"},
  {"claim": "Wiki (Fisherman page) lists Thorn Jig with the lure text; wiki says lures come from the Coin Shop under supplies", "source": "wiki page Fisherman (ns0) via lookup; notes/Build Guides/Content/Jobs/Fisherman.md:262"},
  {"claim": "Client-side item is live as a fishing lure; no not_live or placeholder flag on its text", "source": "locale:409550, locale:409555-409559 (sibling lures, unflagged)"}
 ],
 "confidence": 0.5,
 "open": [
  "No repo store entry: definition 68162 has no coin_store_prices and does not appear in data/content stores, so no coin price is evidenced.",
  "The Guppie and Coin Shop sources are generic to the lure line; no quote names Thorn Jig in a stock list or price. Price and stock for Thorn Jig are unknown.",
  "The Coin Shop claim rests on a repo note paraphrasing the wiki, not on a directly read wiki listing; verify on the wiki Fisherman page or Coin Shop category.",
  "Possible other sources (quest rewards, drops, prize wheel) are not evidenced for this item.",
  "Retirement status unknown: no source states it was retired or still sold at the end of the game.",
  "A second client name 'Thorn Jig - Lure' (locale 412940) exists; it may be a separate item string and was not tied to definition 68162.",
  "Pack critique: none carried in the pack; wiki_page and vendor_stock were empty, so the vendor link is inferred."
 ]}
