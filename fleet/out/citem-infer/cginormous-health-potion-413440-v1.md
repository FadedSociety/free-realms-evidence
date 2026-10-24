<!-- fleet job=citem-infer id=cginormous-health-potion-413440-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[3679, 9898, 6, 1776] model=claude-haiku-5-5 -->
# Ginormous Health Potion

{"item": {"name": "Ginormous Health Potion", "locale_id": 413440, "kind": "consumable"},
 "sources": [
  {"type": "promotion", "detail": "Shattered Past! TCG virtual reward card 2L15 (Ginormous Health Potion); the card's redemption is the only documented route to the item", "where": null, "price": null, "currency": null, "source": "wiki page 'Ginormous Health Potion' (\"It is acquired from the Shattered Past! virtual reward card 2L15 Ginormous Health Potion\"; categories Virtual Rewards, TCG Supplies)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is client locale 413440 'Ginormous Health Potion'; description locale 413441 'A huge potion that heals lots of health.'", "source": "locale:413440; locale:413441"},
  {"claim": "Client definition id 3995, class 9, slot 0; no coin store price in stores data (no vendor sale in the coin store)", "source": "client definition in evidence pack; repo search for 3995 found no store entry for this item"},
  {"claim": "Acquired from Shattered Past! TCG virtual reward card 2L15; usable by any job at level 1; heals 25% health/second for 3 seconds; cannot sell or trade", "source": "wiki page 'Ginormous Health Potion'"},
  {"claim": "Wiki categories: Supplies, TCG Supplies, Potions, Virtual Rewards", "source": "wiki page 'Ginormous Health Potion'"},
  {"claim": "The client text next to the name (locale 413436) is a Unicorn Forest quest line about a 'countering potion' tested for Xeydia; this is a different quest-side use, not a confirmed source for this item", "source": "locale:413436"}
 ],
 "confidence": 0.6,
 "open": [
  "Only one source (the wiki page) names the TCG virtual reward card. Not checked against a live card list or article, so the card's current availability and whether it is still redeemable are unknown; retired status is unconfirmed.",
  "Live status is 'unsure': the first-pass tag said live/vendor, but no vendor stocks it (vendor_stock empty, no coin store price), so the vendor guess is not supported and was not used as a source.",
  "The Unicorn Forest quest text (locale 413436) mentions a potion but does not name this item; it was not used as a quest-reward source. Needs a quest check before adding a quest_reward source.",
  "No price is documented: the item is not sold for coins or Station Cash per the evidence; the card's own price (if any) is not in the pack.",
  "Wiki page is a stub with the TCG card image only; no images or video confirm the card art or redemption flow."
 ]}
