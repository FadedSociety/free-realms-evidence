<!-- fleet job=citem-infer id=cpet-cat-longhair-calico-grey-75214-v2 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[21240, 18957, 8, 2357] model=claude-haiku-5-5 -->
# Pet: Cat: Longhair: calico_grey

{"item": {"name": "Pet: Cat: Longhair: calico_grey", "locale_id": 75214, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop listing for the calico_grey longhair cat pet (item 24064, tint group 1). Unverified: the 540-coin price is the Legacy CoinStoreItems/ClientItemDefinitions Cost value carried into our store data, not a confirmed live transaction. No coin vendor NPC stocks it in our data.", "where": "Coin Shop", "price": "540 coins (member price 486 coins with 10% member discount; sell-back 54 coins under the reconstructed T633 rule)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24064 (line 6941); client definition coin_store_prices 540; notes/Research/Coin Shop.md lines 33-34 (Cost used as starting price, 'not checked against a real client transaction'); sell-back is the T633 reconstruction (Coin Shop.md lines 36-41)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for item 24064 is locale 75214 'Pet: Cat: Longhair: calico_grey', one of 11 longhair cat colour variants (locale 75209-75219); no separate description text", "source": "locale:75214; client definition in the pack"},
  {"claim": "Item 24064 has a Coin Shop row at 540 coins, member price 486, sell 54, tint_group_id 1, with source tags L1,L2,L4,R2,T633,R1 (not the reconstructed SC-price tags)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6941"},
  {"claim": "The 540 value is the Legacy catalogue Cost field used as a starting regular price; the research note says this mapping has not been checked against a real client transaction", "source": "notes/Research/Coin Shop.md lines 25-34"},
  {"claim": "The 54-coin sell-back is a reconstructed rule (max(1, Cost//10)), not a value read from the client", "source": "notes/Research/Coin Shop.md lines 36-41"},
  {"claim": "The sibling family claim is wrong: the 24021-24066 range is mixed. Several siblings (e.g. 24021 Mojo, 24022 Mittens, 24027 Pooky, 24032 Zinx, 24041 Gizmo, 24044 Bubba, 24062 Minnie) had their coin price cleared and were reconstructed as Station Cash items at 225 or 400 SC from wiki prices. Most other rows, including 24064, keep the 540-coin Cost. So the range does not establish a uniform coin listing for 24064.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6890-6944"},
  {"claim": "No wiki page, article, video, or client line names this calico_grey cat or any vendor, quest, or drop for it; the repo's only reference to 24064 is stores.json", "source": "lookup of wiki/articles/video for 'calico grey cat pet' returned no matches; repo and refs searches for 24064/calico/longhair"}
 ],
 "confidence": 0.3,
 "open": [
  "The only source is a Legacy-derived catalogue Cost (540 coins). It is not confirmed as ever sold live, and no sale window or price was verified against a real transaction or wiki page.",
  "No wiki page covers this pet; retirement status and whether it was ever stocked in the Coin Shop are unknown.",
  "Live status is unsure. Nothing in the evidence confirms it was on sale during the live era.",
  "Other sources (promotion, event, prize wheel, membership pack, quest reward) were not found in the pack and could not be checked.",
  "The first-pass 'vendor' tag is only a hint; no coin vendor NPC is linked to this item in the repo.",
  "The 54-coin sell-back value is a reconstructed rule, not a sourced fact about this item."
 ]}
