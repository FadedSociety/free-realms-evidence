<!-- fleet job=citem-infer id=cpet-cat-shorthair-siamese-black-75189-v2 status=nothing_found turns=3 usd=0.0026 tokens(read,write,in,out)=[16227, 11450, 8, 2061] model=claude-haiku-5-5 -->
# Pet: Cat: Shorthair: siamese_black

{"item": {"name": "Pet: Cat: Shorthair: siamese_black", "locale_id": 75189, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name and description 'Pet: Cat: Shorthair: siamese_black', definition id 24039, model cat_shorthair.adr, one definition, slot 0, class 0", "source": "locale:75189; client definition in pack"},
  {"claim": "Store record for item 24039 carries purchase_price_coins 540, member price 486, sell 54, with no price_provenance block and no named vendor or category", "source": "repo:prototype/osfr-tools/data/content/stores.json:6916"},
  {"claim": "Neighbouring records 24013-24047 (e.g. 24018, 24019, 24020, 24023-24026, 24028-24031, 24033-24040, 24042, 24043) use the identical 540/486/54 template with the same source_tags, so the 540 value is a shared template default, not a per-variant sale price", "source": "repo:prototype/osfr-tools/data/content/stores.json:6895-6920"},
  {"claim": "Items with wiki-backed prices (24021 Mojo, 24022 Mittens, 24027 Pooky, 24032 Zinx, 24041 Gizmo) have their coin cost cleared to null because no coin vendor stocks them; 24039 has no such clearing and no wiki price", "source": "repo:prototype/osfr-tools/data/content/stores.json:6898-6918"},
  {"claim": "The claim that the wiki Cats page says 'Cats are only available to be purchased with Station Cash' could not be re-verified: lookup on the Cats page returned no match and repo search for that quote returned no match", "source": "lookup (wiki) and search (repo), this run"},
  {"claim": "Sibling cat client lines 75184-75194 are a cluster with no separate wiki page, price, or source naming a vendor", "source": "client_cluster in pack"}
 ],
 "wireable": false,
 "confidence": 0.1,
 "open": [
  "No evidenced source for how this cat is obtained. The 540-coin vendor entry was removed: it is a shared template default on stores.json (lines 6895-6920) with no provenance and no named vendor, so it cannot be cited as this cat's price.",
  "The Station Cash marketplace entry was removed as unverified: the only support is a category-level wiki statement about Cats that the prior answer quoted from quest-lines/item-packs.json:9162, which could not be re-found in the repo or on the wiki lookup this run. If that statement is confirmed, it supports a category-level SC source with no variant name and no price; the SC venue would still be inferred.",
  "The 'vendor' tag from the first-pass model is a hint only and is not supported by any vendor record.",
  "Live status and retirement are unverified. The store source tags (L1, L2, L4, R2, T633, R1) are not decoded in the pack and were not used.",
  "Next step: check the wiki Cats page directly for a per-variant listing or SC price, and decode the store source tags T633 and R1 to see whether they map to a coin vendor, before setting any price."
 ]}
