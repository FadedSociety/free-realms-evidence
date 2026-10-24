<!-- fleet job=citem-infer id=csparkly-oil-flair-shard-386005-v1 status=done turns=4 usd=0.0056 tokens(read,write,in,out)=[38706, 27451, 10, 3490] model=claude-haiku-5-5 -->
# Sparkly Oil Flair Shard

{"item": {"name": "Sparkly Oil Flair Shard", "locale_id": 386005, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, definition 2694 (store category 124, flair shard row)", "where": "coin store (vendor not identified in our data)", "price": "300 coins (member price 270 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 2694 (line 724)"},
  {"type": "vendor", "detail": "Coin store sale, definition 55353 (second definition of the same name; no_sale flag set, so it cannot be sold back)", "where": "coin store (vendor not identified in our data)", "price": "270 coins (member price 243 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 55353 (line 13842)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 386005 is 'Sparkly Oil Flair Shard', description 'Covers your weapon or tool in sparkles.'; two definitions (2694, 55353), slot 13, class 69.", "source": "locale:386005; client definition pack"},
  {"claim": "Our store data lists definition 2694 at 300 coins, member price 270 coins, category 124, with source tags L1, L2, L4, R2, T633, R1.", "source": "repo:data/content/stores.json item 2694"},
  {"claim": "Our store data lists definition 55353 at 270 coins, member price 243 coins, no_sale true, category 124.", "source": "repo:data/content/stores.json item 55353"},
  {"claim": "Sibling flair shard Electric Oil Flair Shard (locale 386008) is a level 1 flair shard usable in any job, acquired by redeeming Free Realms Trading Card Game virtual reward card 1L19 Electric Weapon [Oil]. It duplicates the particle effect of Juiced Wand/Hammer/Scythe.", "source": "wiki page: Electric Oil Flair Shard (lookup result)"},
  {"claim": "The client has a 'Sparkly Weapon Oil' item (locale 909329336 / 3353817121) and the Sparkly Oil Flair Shard sits in the same Oil cluster (386001-386010) as the Icy, Fiery and Electric shards.", "source": "locale:909329336; locale:3353817121; client_cluster pack"}
 ],
 "confidence": 0.45,
 "open": [
  "Only the coin store is confirmed by our data. The first-pass guess 'vendor' is not checked further: no vendor NPC is named for store category 124 in the repo, so the specific vendor and zone are unknown.",
  "No wiki page, article or video names the Sparkly Oil Flair Shard. The wiki does name the sibling Electric Oil Flair Shard as a TCG virtual reward card (1L19). Whether the Sparkly shard also came from a TCG reward card (and which card code) is unverified.",
  "Why two definitions exist (2694 coin-store row at 300 coins and 55353 at 270 coins, no_sale) is not explained. The 55353 row may be a later re-price or a different store/tag, so the two prices may both be real or one may be stale.",
  "Retired status and the live status are unknown. The store tags suggest a coin sale, but no retirement date or live-check source was found.",
  "No wiki price was found for the item, so there is no sale-price cross-check. The member price (270/243) is the store's member discount, not a separate sale.",
  "Enemy drop, crafting, event, collection, prize-wheel and membership sources: none found in the pack or repo. Not checked further."
 ]}
