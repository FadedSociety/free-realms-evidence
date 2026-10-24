<!-- fleet job=item-infer id=irascal-v3 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[15358, 9769, 8, 2014] model=claude-haiku-5-5 -->
# Rascal

{"item": {"name": "Rascal", "locale_id": 100674, "kind": "pet"},
 "sources": [
  {"type": "marketplace", "detail": "Rascal excited small dog pet, sold to everyone at the SC Marketplace regular price. Members get a 10% discount tier on the same listing (about 202, derived from 225 x 0.9).", "where": "SC Marketplace", "price": "225 (station_cash metadata field; unverified against live page). Members about 202 (derived). Wiki image shows 250, conflicting.", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Rascal (category SC Marketplace; station_cash field [225, 202]; prose says 'regular price of , and to Members at the 10% discount price of .' with the numbers blank); repo:prototype/osfr-tools/data/content/pets.json:20660-20665 (adoption_source sc_marketplace price 225, member_price 202)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Rascal is a male small dog pet with the Excited trait, in Pets, Dogs, Small Dogs, Excited Pets, Males categories", "source": "https://freerealms.fandom.com/wiki/Rascal"},
  {"claim": "Rascal is sold through the SC Marketplace (category SC Marketplace, Marketplace Items)", "source": "https://freerealms.fandom.com/wiki/Rascal"},
  {"claim": "Pet description: 'Hi! I'm Rascal and I'm an excited dog! We should look for adventure!'", "source": "https://freerealms.fandom.com/wiki/Rascal"},
  {"claim": "Station cash field 225 regular and 202 member price", "source": "https://freerealms.fandom.com/wiki/Rascal (station_cash field); repo:prototype/osfr-tools/data/content/pets.json:20663-20664"},
  {"claim": "Vendor/shop image text lists Rascal at 250 alongside Nox, Pavel, Peccadillo and Roxie; this conflicts with the 225 field and is not resolved", "source": "wiki image text in pack (vendor_or_shop image)"},
  {"claim": "Name string 100674 is an NPC-name entry; repo lists other candidate name ids 557383365, 2308946111, 2632725147 for the pet name", "source": "locale:100674; repo:prototype/osfr-tools/data/content/pets.json:20648-20652"}
 ],
 "confidence": 0.45,
 "open": [
  "Treasure Trader prize source dropped: lookups of wiki, articles and client for 'Treasure Trader' with Rascal returned no matches, and the pack's own snippet did not show Rascal. Re-check the full Treasure Trader prize list on the wiki if it is to be restored; if it does name Rascal it would be a retired 2010 Facebook prize (application ran 8-28 Sept 2010).",
  "Price conflict: wiki image shows 250, station_cash field shows 225. Live Marketplace price not checked. The 202 Members figure is derived (10% off 225), not a listed price.",
  "Current availability on the SC Marketplace is not stated on the wiki page, so retired and live are left unresolved.",
  "Item-level client id is unresolved: repo notes no exact client item definition is bound to this pet; locale 100674 is an NPC-name string.",
  "The Members 10% figure is a discount tier on the same Marketplace listing, not a separate acquisition route, so it is not listed as its own source."
 ]}
