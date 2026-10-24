<!-- fleet job=citem-infer id=cinferno-scorched-goggleguard-120691-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5232, 8657, 6, 1905] model=claude-haiku-5-5 -->
# Inferno Scorched Goggleguard

{"item": {"name": "Inferno Scorched Goggleguard", "locale_id": 120691, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin store, store category 101: tint group 1 variant (definition 40692) at 1027 coins; tint group 2 (definition 40697) and tint group 3 (definition 40702) at 9453 coins. The NPC/shop name is not in the store data.", "where": null, "price": "1027 coins (tint 1, member price 924 coins); 9453 coins (tints 2 and 3, member price 8507 coins). Member discount 10%.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12505 (item 40692), 12507 (item 40697), 12509 (item 40702)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:120691 'Inferno Scorched Goggleguard', part of the Inferno Scorched set (Shirt 120688, Boots 120689, Gloves 120690, Apron 120692).", "source": "locale:120691"},
  {"claim": "Store rows exist for definitions 40692 (cat 101, tint 1, 1027 coins), 40697 (cat 101, tint 2, 9453 coins) and 40702 (cat 101, tint 3, 9453 coins). No store rows were found for the other nine definitions (40707-40747), so their price is not evidenced.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12505, 12507, 12509"},
  {"claim": "The price split follows tint group across the whole store file: tint 1 rows are 1027 (or 618 for the lower tier), tint 2 and 3 rows are 9453 in the same tier. Examples: 40612 tint 1 618 (line 12493) vs 40617 tint 2 9453 (line 12495). This is a general pricing pattern, not a stale entry for this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12493-12515"},
  {"claim": "No wiki page, image, article fact, or video frame names this item; the only hit is the client locale line.", "source": "lookup wiki/articles/client for 'Inferno Scorched Goggleguard' (only locale:120691)"},
  {"claim": "Store rows carry source tags L1, L2, L4, R1, R2, T633, which suggest a live listing, but no wiki or article confirms it.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12505"}
 ],
 "confidence": 0.5,
 "open": [
  "Name the NPC vendor and zone for store category 101. The store file gives prices only.",
  "Confirm live status and any retirement date with a wiki page, article, or video. Only repo store rows and their tags support a sale.",
  "Price for definitions 40707-40747 (nine variants) is not evidenced; no store rows were found for them.",
  "Other set pieces (Shirt, Boots, Gloves, Apron) were not checked for the same vendor and category, so the set source is unconfirmed.",
  "No evidence for quest rewards, drops, events, prize wheel, crafting, or promotions."
 ]}
