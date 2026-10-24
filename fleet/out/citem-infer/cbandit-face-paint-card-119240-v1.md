<!-- fleet job=citem-infer id=cbandit-face-paint-card-119240-v1 status=done turns=5 usd=0.0028 tokens(read,write,in,out)=[26410, 9252, 12, 2736] model=claude-haiku-5-5 -->
# Bandit Face Paint Card

{"item": {"name": "Bandit Face Paint Card", "locale_id": 119240, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, definition 69560 (purchase 180 coins; member price 162 coins with 10% member discount). Vendor NPC not identified in the repo data.", "where": null, "price": "180 coins (member price 162 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 69560 (category 145)"},
  {"type": "vendor", "detail": "Coin store sale, definition 17593 (purchase 2000 coins; member price 1800 coins with 10% member discount). Vendor NPC and whether this is a separate or higher-priced variant of the same card are not identified.", "where": null, "price": "2000 coins (member price 1800 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 17593 (category 145)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 119240 is 'Bandit Face Paint Card', description 'No one will ever see you coming.'", "source": "locale:119240"},
  {"claim": "Two client definitions (17593, 69560) share the name; both are slot 6, class 1, and both appear in the coin store table under category 145 with purchase prices 2000 and 180 coins.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 17593 and item 69560"},
  {"claim": "Wiki Super Spooktacular (Halloween-season event) lists sister face paint cards 'Troll [Face Paint] [Card]' and 'Phantom [Face Paint] [Card]' as available with the event; the Bandit card is not named on that page snippet.", "source": "wiki page: Super Spooktacular"},
  {"claim": "The client text cluster puts Bandit with Monster, Phantom, Troll, Sea Monster and Saber-toothed face paint cards and Halloween-style pails and spectacles, suggesting a shared Halloween/Spooktacular release group. This is a grouping inference, not a source for the Bandit card's sale.", "source": "locale:119235-119245"},
  {"claim": "Same-category sister cards in the coin store (e.g. 36003-36021 at 270 coins) show the store lists face paint style items under category 145.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 11735-11753"}
 ],
 "confidence": 0.45,
 "open": [
  "Which NPC/vendor sells definition 17593 (2000 coins) and definition 69560 (180 coins) is not in the repo or wiki evidence; the store table gives no vendor name. Mapping to a vendor needs a store-to-NPC lookup.",
  "Unknown whether 17593 and 69560 are both sold to players or one is a different race/tint variant of the same card; the pack says 2 definitions but names no variant.",
  "No wiki page or article names the Bandit Face Paint Card itself; the Super Spooktacular page names only Troll and Phantom cards, so an event source for Bandit is not confirmed.",
  "Retired/availability status not established: no source states whether the coin store still sells it or when it was removed.",
  "Jev's first-pass 'live: yes, source: vendor' is a hint only; the store rows support a coin sale but not live status.",
  "The 2000-coin price is the higher of the two prices and no second wiki price exists to say whether it is a sale price."
 ]}
