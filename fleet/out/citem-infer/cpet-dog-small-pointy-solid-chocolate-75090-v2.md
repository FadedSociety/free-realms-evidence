<!-- fleet job=citem-infer id=cpet-dog-small-pointy-solid-chocolate-75090-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[12265, 8343, 8, 1877] model=claude-haiku-5-5 -->
# Pet: Dog: Small Pointy: solid-chocolate

{"item": {"name": "Pet: Dog: Small Pointy: solid-chocolate", "locale_id": 75090, "kind": "pet"},
 "sources": [
  {"type": "other", "detail": "Coin Shop catalogue entry only (stores.json row for item 23940). No NPC, merchant or zone is named in any source, so no vendor is confirmed.", "where": null, "price": "540 coins (buy, legacy Cost; client coin_store_prices agrees). Member price 486 and sell-back 54 are reconstructed, not observed.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23940 (line 6817, purchase_price_coins 540, no_sale false); client definition coin_store_prices [540]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item as locale:75090 'Pet: Dog: Small Pointy: solid-chocolate', definition id 23940, model dog_small_pointy.adr, one variant", "source": "locale:75090; client definition"},
  {"claim": "stores.json item 23940 has purchase_price_coins 540, member 486, sell 54, not no_sale. The row has no price_provenance block, so the 540 comes from the legacy Cost value, not from a sourced sale record.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6817"},
  {"claim": "Neighbouring row 23941 is no_sale with a reconstructed 400 Station Cash SC Marketplace price (Hurricane wiki rev 47881), and its note says no coin vendor stocks that item. So the 540 neighbour prices are not uniform proof of one shared vendor, and the row 23940 price may be a legacy value.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6818"},
  {"claim": "Dog model dog_small_pointy.adr is used by several NPC spawns, so the model alone does not identify a vendor.", "source": "repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:12334, 32599, 57248"},
  {"claim": "Client lookup returns only the locale lines for the cluster (75085-75094). No wiki page, article fact or video frame names this tint.", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor NPC or zone is identified. The earlier 'vendor' label was not supported, so the source is recorded as the Coin Shop catalogue only.",
  "The 540-coin price is a legacy Cost carried into the Coin Shop import. It has no price_provenance block and no live purchase has been observed.",
  "Retirement status is unknown. No source says whether it is still sold.",
  "Live status is unsure: the only support is the first-pass tag and the legacy store row.",
  "Cluster membership: the other solid and darkmark dog tints (75085-75095) were not checked row by row. Item 23941 shows that neighbouring rows can differ in provenance."
 ]}
