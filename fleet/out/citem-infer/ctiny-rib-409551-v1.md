<!-- fleet job=citem-infer id=ctiny-rib-409551-v1 status=done turns=9 usd=0.0072 tokens(read,write,in,out)=[143755, 29015, 20, 4252] model=claude-haiku-5-5 -->
# Tiny Rib

{"item": {"name": "Tiny Rib", "locale_id": 409551, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin Shop, Fishing Lures (supplies category), per the wiki Fisherman page. The wiki lists Tiny Rib among the lures; no per-item Coin Shop price is given in the evidence.", "where": "Coin Shop", "price": null, "currency": null, "source": "wiki page Fisherman (Lures section: 'lures are bought from the Coin Shop under the supplies item category'; Tiny Rib text: 'This lure gives a 10% chance of catching Spineless Stickleback, Calico Catfish and Purplenosed Shark'); locale:641677831"},
  {"type": "vendor", "detail": "Guppie, lure vendor in Sacred Grove Shallows (Stillwater Crossing area). The client says he sells the basic fishing lures. Whether Tiny Rib is in his stock is not confirmed.", "where": "Sacred Grove Shallows", "price": null, "currency": null, "source": "locale:641677831 ('You can buy a lure from Guppie. He carries all the basic supplies a fisherman might need.'); locale:408632 ('Buy a lure from Guppie'); locale:408633; notes/Build Guides/Content/Jobs/Fisherman.md line 37 (stock and prices not seen)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item name 'Tiny Rib' is client locale 409551, item class 142, slot 0; description says the lure gives a 10% better chance of catching Spineless Stickleback, Calico Catfish and Purplenosed Shark.", "source": "locale:409551; locale:412943 ('Tiny Rib - Lure' description); client definition 68163"},
  {"claim": "Lures are bought from the Coin Shop under the supplies category, and the wiki Fisherman page lists Tiny Rib among them.", "source": "wiki page Fisherman (Lures section)"},
  {"claim": "Guppie in Sacred Grove Shallows sells lures; the beginner quest 'So A-Luring' sends the player to buy one from him.", "source": "locale:408623, locale:408632, locale:408645, locale:641677831"},
  {"claim": "Tiny Rib's three fish are the Spineless Stickleback, Calico Catfish and Purplenosed Shark, and the fish pages name the Tiny Rib lure for them (fish tables: Rainbow Lake, Lagoon, Banks, Basin).", "source": "notes/Build Guides/Content/Jobs/Fisherman.md lines 210, 233, 236, 277; locale:29749, locale:29762, locale:29780, locale:3275375471, locale:471495023"},
  {"claim": "No coin store price for item 68163 in our store data. No quest reward, enemy drop, event or prize-wheel source found for Tiny Rib.", "source": "client definition (coin_store_prices empty); search of repo and refs for 'Tiny Rib' and 68163"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop price for Tiny Rib is not recorded in any source. The wiki gives the lure section but not the per-lure price. Need the wiki price or a Coin Shop capture (repo data/content/stores.json has no entry for 68163).",
  "Guppie's stock list is not confirmed, so it is unknown whether he sells Tiny Rib or only the basic lures.",
  "Retired status is unknown. No source says whether Tiny Rib left the Coin Shop.",
  "Data bug: prototype/osfr-tools/data/content/fishing.json lines 1505-1515 map 'tiny_rib' to Blubracuda, Baconfish and Changed Salmon. Those are the fish of a different lure (locale:409555). The correct fish, per the Tiny Rib client text, are Spineless Stickleback, Calico Catfish and Purplenosed Shark. Fix this in the fishing data.",
  "The 'live' answer rests on the wiki Fisherman page listing and the Coin Shop lure category. No dated wiki or article fact confirms it."
 ]}
