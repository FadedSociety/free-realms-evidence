<!-- fleet job=citem-infer id=cbrittle-eternal-triangle-shard-69779-v1 status=done turns=6 usd=0.0048 tokens(read,write,in,out)=[56405, 19049, 14, 3611] model=claude-haiku-5-5 -->
# Brittle Eternal Triangle Shard

{"item": {"name": "Brittle Eternal Triangle Shard", "locale_id": 69779, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for item 22877 (category 121, sell price 81 coins). The store row lists no named vendor; the row is in the same block as item ids 22856-22879, which share the same price and tags.", "where": null, "price": "811 coins (member price 729 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22877 (line 6732)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 69779 'Brittle Eternal Triangle Shard', item definition 22877, class 50.", "source": "locale:69779"},
  {"claim": "Our coin store data lists definition 22877 at 811 coins purchase, 729 coins member price, 81 coins sell price.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22877 (line 6732)"},
  {"claim": "The same 811-coin price and tags are shared by neighbouring item ids 22856-22879 in the same store block, so this block is a batch of shard listings.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6711-6734"},
  {"claim": "Sibling client names (Brittle Infernal, Spectral, Mystical, Ethereal, Celestial, Phantasmal, Fateful, Dreadful Triangle Shard) sit in the same locale block 69774-69784.", "source": "locale:69774 to locale:69784"},
  {"claim": "No wiki page, article fact, video frame, vendor stock line, or other answer names this shard. Searches for 'Brittle', 'Eternal Triangle' and the definition id 22877 found no other source.", "source": "lookup (client, wiki, articles, video) and repo search"}
 ],
 "confidence": 0.35,
 "open": [
  "The store row for 22877 names no vendor. Repo vendor data (vendors.json) does not reference 22877, so the vendor that sells it is unknown. The 'coin_shop' type is an inference from the store row, not a confirmed wiki category.",
  "Store category 121 covers many unrelated items in the repo, so the row alone does not show what this shard is used for or whether it is a Coin Shop item, a vendor item, or a crafting input.",
  "The client definition lists slot 12, but the Items and Inventory note maps slots 11-16 to Triangle, Square, Diamond... in order, which would make slot 11 the Triangle slot. The name says Triangle, so slot 12 looks mismatched and needs checking.",
  "No wiki page or article covers the 'Brittle' shard series. Whether it was retired or is still sold is unknown. The 'retired' value is null.",
  "The 'Brittle' prefix and the 'Eternal' tier name do not match the Jobs-tier shard names in the repo (Amateur, Pro, All-Star, Fisher's, Angler's). The source of the 'Brittle' series is unconfirmed."
 ]}
