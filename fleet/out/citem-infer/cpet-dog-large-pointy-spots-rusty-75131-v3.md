<!-- fleet job=citem-infer id=cpet-dog-large-pointy-spots-rusty-75131-v3 status=nothing_found turns=2 usd=0.0026 tokens(read,write,in,out)=[6503, 12224, 6, 2096] model=claude-haiku-5-5 -->
# Pet: Dog: Large Pointy: spots-rusty

{"item": {"name": "Pet: Dog: Large Pointy: spots-rusty", "locale_id": 75131, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 75131 is 'Pet: Dog: Large Pointy: spots-rusty'; definition id 23981; model dog_large_pointy.adr; one of the 'Large Pointy' dog variants in locale 75126-75133.", "source": "locale:75131; client definition ids [23981]"},
  {"claim": "stores.json row for item 23981 (line 6858) carries purchase_price_coins 540, member 486, sell 54, no_sale false, category_id null, tint_group_id null, and no price_provenance or seller field. The client definition lists coin_store_prices [540].", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6858; client coin_store_prices [540]"},
  {"claim": "The 540/486/54 figures repeat across the 23973-23985 block. Rows 23973 and 23977 are no_sale true with no sell price, and row 23978 has its coin cost cleared because no coin vendor stocks it (its SC price is from the Bruno wiki page). So the 540 is a shared legacy value in the block, not per-item proof of a sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6850-6862"},
  {"claim": "No vendor row, quest, drop, event, prize wheel, crafting or promotion source names item 23981 or this pet. Searches of the repo for 23981 and the model name found only the stores row, pets.json entries for the different dog_large_pointyghost.adr (Shadow, id 55840), and NPC spawns that use the shared dog_large_pointy.adr model.", "source": "repo search for '23981|dog_large_pointy'"},
  {"claim": "Pet vendors named in notes (Jennifer at Cobblestone Village Pet Adoption Center; Gloria) are described only as 'pet vendors'. No record ties them to definition 23981. Florina sells pet supplies, not pets.", "source": "notes/Build Guides/Content/NPCs/NPCs - Cobblestone Village.md:68; notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:87"},
  {"claim": "Lookup for 'spots-rusty' and 'dog pointy' failed (FTS5 query error on the word 'rusty' treated as a column). A retry on the exact phrase is still needed, so this result is not a confirmed absence.", "source": "lookup client/wiki/articles/video, 'spots-rusty OR Large Pointy dog pet'"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source is evidenced. The earlier answer's 'Coin store pet sale' from vendor unknown is not supported: the 540 coin figure is a shared default in the stores block and no seller is named. Do not wire a vendor sale from this record.",
  "Seller not identified. Check the Cobblestone Village pet vendors (Jennifer, Gloria) against client vendor data for a row that sells definition 23981 before naming one.",
  "stores.json row 23981 carries source_tags [L1, L2, L4, R2, T633, R1] with no explanation in the pack. Tag meanings are not documented here; resolve them before treating the row as a source.",
  "Live status and retirement unknown. No wiki Pets page, article, or video names this variant. The first-pass 'live: yes' is a hint only.",
  "Lookup query for the name failed (FTS5 error), so the client, wiki, article and video absence is not confirmed. Re-run with the phrase quoted.",
  "No pets.json entry for definition 23981; the only pets.json dog entry is the Shadow variant (dog_large_pointyghost.adr, id 55840), so pet-data linkage is unverified.",
  "Critiques (evidence score 2, world score 2, both wireable false) are accepted. Sources were downgraded to none, and the record is not wireable."
 ]}
