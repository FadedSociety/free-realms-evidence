<!-- fleet job=citem-infer id=csavage-sting-hoodie-625-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[19970, 9428, 10, 2789] model=claude-haiku-5-5 -->
# Savage Sting Hoodie

{"item": {"name": "Savage Sting Hoodie", "locale_id": 625, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin vendor sale, price 715 coins (store item 1282, tint group 3, member price 643 coins). Vendor NPC not identified from repo data.", "where": null, "price": "715", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:5758 (item_id 1282)"},
  {"type": "vendor", "detail": "Coin vendor sale, price 9453 coins (store item 1340, tint group 2, member price 8507 coins). Vendor NPC not identified; likely the same or a higher-tier vendor line for another tint. Wiki price for this set not found.", "where": null, "price": "9453", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:5764 (item_id 1340)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Savage Sting Hoodie' is locale:625, item class 16, slot 3 (chest), 15 definitions, 12 listed definition ids, model archer_<race>_<gender>_chest_oneslvhoodie.adr.", "source": "client definition (locale:625)"},
  {"claim": "Store entries exist for definition-linked item ids 1282 (715 coins), 1340 (9453 coins), and 11122 (715 coins, tint group 1), all with no_sale true and sell price null.", "source": "repo:prototype/osfr-tools/data/content/stores.json:5758, 5764, 6519"},
  {"claim": "Same-named Archer set pieces Savage Sting Boots (locale:630), Gloves (locale:635), Leggings (locale:640), Quiver (locale:645), and the Savage Sting Bow (locale:102188) are client items, and an Elite Black Savage Sting Hoodie variant exists (locale:25039). These are siblings of the same set.", "source": "locale:630, locale:635, locale:640, locale:645, locale:102188, locale:25039"},
  {"claim": "Savage Sting Bow is a wiki-covered level 12 Archer weapon, and a Blacksmith recipe exists (Forging: Savage Sting Bow, locale:386114). This shows the set's wiki coverage is weak but the set is real in-game.", "source": "wiki page 'Savage Sting Bow'; locale:386114"},
  {"claim": "Storm Strike Hoodie (locale:623) and Storm Strike Boots (locale:628) sit next to it in the client text; no source ties this set to a Treasure War booster reward, so that link is unproven.", "source": "locale:623, locale:628"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor NPC and zone for the 715-coin and 9453-coin sales are not resolved: the repo's stores.json gives item ids and prices but no vendor mapping was found in vendors.json for these ids.",
  "The 'source_tags' in stores.json (L1, L2, L4, R2, L3, R1, T633) were not decoded, so the store location and era cannot be confirmed.",
  "No wiki page, article, or video covers the Savage Sting Hoodie. The first-pass tag 'vendor' is consistent with the store data but is only a hint.",
  "The 'Treasure War' locale:629 (flagged not_live) sits in the cluster, but no evidence ties the hoodie to a Treasure War reward. Not used as a source.",
  "Retirement status is unknown. Store entries have no_sale true, which may mean the item is no longer sold to players, but this is not confirmed by any source.",
  "Prices 715 and 9453 likely belong to different tints or tiers of the 15 definitions. The mapping from definition to price was not verified."
 ]}
