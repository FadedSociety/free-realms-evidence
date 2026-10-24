<!-- fleet job=citem-infer id=cclay-zipper-turbo-406509-v1 status=nothing_found turns=5 usd=0.0039 tokens(read,write,in,out)=[39462, 16865, 12, 2849] model=claude-haiku-5-5 -->
# Clay Zipper Turbo

{"item": {"name": "Clay Zipper Turbo", "locale_id": 406509, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Clay Zipper Turbo' is locale:406509; description 'The turbo for the Clay Zipper.' is locale:406569 (lookup client result). It is a Racing Kart part, not a vehicle.", "source": "locale:406509; locale:406569"},
  {"claim": "Item class 129 is the Turbo part category of the Racing Kart item class (ItemClasses.txt row 75, Turbo = category 130 per the research note; class 129 is Engine-category in that note, so the class-id mapping is unresolved).", "source": "notes/Research/Pieces/041 Racer and derby progression.md:44-47"},
  {"claim": "Sibling kart turbos (Speedy/Slime/Classic/Basphomie/Splash/Metallic/Neon/Battery/Vandy Zipper Turbo, locale 406504-406513) share the same cluster; no source text, store row, or wiki page for any of them was found.", "source": "client cluster in pack; lookup 'Zipper' (wiki returned only the Splash Zipper vehicle page)"},
  {"claim": "Clay Zipper (vehicle) appears only as client text (locale:7167); no wiki page for it exists in the lookup. The Splash Zipper vehicle is the only Zipper wiki page, sold on the SC Marketplace at 'the regular price of' (price text stripped) and 10% member discount.", "source": "wiki Splash Zipper (lookup ns0 page); locale:7167"},
  {"claim": "The client definition carries no coin_store_prices, and repo search finds no store row, vendor, quest, drop, or recipe for definition 61039 or the name.", "source": "repo search for 61039 / 406509 / 'Clay Zipper' / 'Zipper Turbo' (no hits in data or notes)"},
  {"claim": "Notes say Splash Zipper and other race karts were matched without a Station Cash store row, so store-row absence does not establish availability.", "source": "notes/Autopilot/T634.md:65"}
 ],
 "confidence": 0.15,
 "open": [
  "No source for how Clay Zipper Turbo is obtained: no wiki article, no store row, no vendor, no quest, no drop, no event, and no collection or prize-wheel mention was found.",
  "Price unknown: client definition has no coin store price and the wiki has no price for it.",
  "Retired status unknown. Live status is unsure: the first-pass tag was a guess and is not evidence.",
  "Likely a Station Cash bundle part of the Clay Zipper kart (the Splash Zipper vehicle is SC Marketplace), but that is inference from the sibling, not evidence for this turbo. Needs a wiki page or a store/marketplace listing check.",
  "Client definition slot/class mapping conflict: class 129 is listed as Engine in the research note while the item is a Turbo; verify class id mapping before using it."
 ]}
