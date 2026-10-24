<!-- fleet job=citem-infer id=cicy-oil-flair-shard-386006-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5405, 7563, 6, 1525] model=claude-haiku-5-5 -->
# Icy Oil Flair Shard

{"item": {"name": "Icy Oil Flair Shard", "locale_id": 386006, "kind": "consumable"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale; selling vendor not identified. Store row item 2671 (category 124, sellable, no_sale false). Icy = 2671 is inferred from the client definition ids, not from a named store row.", "where": null, "price": "300 coins (member price 270 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 713 (item_id 2671); repo:prototype/osfr-tools/data/content/stores.json line 713 is the only sellable row for this item"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Icy Oil Flair Shard' is locale 386006, description 'Covers your weapon or tool in ice.', slot 13, class 69.", "source": "locale:386006"},
  {"claim": "Client definition ids 2671 and 55352 carry this name's data (per the client definition pack).", "source": "client definition pack, definition_ids [2671, 55352]"},
  {"claim": "Store row item 2671 is category 124 at 300 coins, member 270, no_sale false (sellable).", "source": "repo:prototype/osfr-tools/data/content/stores.json line 713"},
  {"claim": "Store row item 55352 is category 124 at 270 coins (member 243) but flagged no_sale:true, so it is not currently sold; it is not counted as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 13841 (per pack)"},
  {"claim": "No wiki page, image, article fact, video frame or vendor-stock entry names Icy Oil Flair Shard; lookup returns only the client text row locale:386006.", "source": "lookup client/wiki/articles/video, 'Icy Oil Flair Shard'"}
 ],
 "confidence": 0.4,
 "open": [
  "Store rows carry no item names. The name link to item 2671 rests on the client definition id list, not on a named row.",
  "The selling vendor (or the coin shop category 124 name) is not identified in the repo store data, and no wiki category cites Icy Oil.",
  "Item 55352 (no_sale row at 270 coins) is unexplained: it may be a retired or alternate version of the same item, but no source confirms that.",
  "TCG reward-card source removed. The only support was the sibling Electric Oil Flair Shard wiki page (card 1L19); nothing ties Icy Oil to a card, so it is not listed as a source.",
  "Current availability and any retirement date are not in the evidence, so retired is null and live is unsure.",
  "The first-pass 'vendor' guess was used only as a hint, not as evidence."
 ]}
