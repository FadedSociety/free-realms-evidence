<!-- fleet job=citem-infer id=ckitty-turban-6151-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5403, 8639, 6, 1674] model=claude-haiku-5-5 -->
# Kitty Turban

{"item": {"name": "Kitty Turban", "locale_id": 6151, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 6 (category name not given in the repo). Vendor/NPC not identified; the Brent (Sanctuary Pet Adoption Center) link from the prior answer is dropped because his stock list does not name this item.", "where": null, "price": "50 coins (member price 45 coins, 10% member discount; sell price 5 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2167 (line 630)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 2167 is named Kitty Turban (locale 6151), slot 1, class 61, model pet_cat_<descriptor>_head_turban.adr, one definition", "source": "locale:6151; client definition in pack"},
  {"claim": "Coin store record for item 2167: category_id 6, tint_group 1, purchase 50 coins, member price 45, sell 5, no_sale false, source tags L1/L2/L4/R2/T633/R1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2167 (line 630), re-read and confirmed"},
  {"claim": "Sibling items 2163 to 2170 share store category 6 at the same 50-coin price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 626-633"},
  {"claim": "Kitty and Doggy costume set (Turban, Alligator Headress, Octopus Hat, Traffic Cone) sits together in client text 6147 to 6154; the cluster has no acquisition line", "source": "locale:6147-6154"},
  {"claim": "Brent (Sanctuary) is recorded as a pet clothing merchant, but his stock list does not name the Kitty Turban, so he is not a confirmed source", "source": "repo:prototype/osfr-tools/data/content/npcs/sanctuary.json (Brent entry); notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md line 86"},
  {"claim": "Wiki, articles and video lookups for 'Kitty Turban' returned no matches", "source": "lookup: wiki, articles, video"}
 ],
 "confidence": 0.45,
 "open": [
  "Vendor not identified: no source ties store category 6 to a named NPC or shop. The coin store record is the only evidenced source; the 'where' field is left null.",
  "Brent's stock list does not include this turban; the prior Sanctuary Pet Adoption Center attribution is unsupported and was removed.",
  "Pet Supplies vendor Bowawow (Highroad Junction) is marked 'No longer in-game' on the wiki with no stock list; not confirmed as a source.",
  "live is 'unsure': the store record exists with no_sale false, but no wiki, article or video confirms current sale. Retirement status unknown.",
  "No holiday, event or drop line for the Kitty/Doggy costume set in the client text; not checked for the sibling Doggy and Kitty alligator, octopus and traffic cone items."
 ]}
