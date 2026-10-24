<!-- fleet job=citem-infer id=ccamouflage-sunglasses-398750-v2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6066, 10369, 6, 2005] model=claude-haiku-5-5 -->
# Camouflage Sunglasses

{"item": {"name": "Camouflage Sunglasses", "locale_id": 398750, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor. Legacy coin store sale, tint group 2 (item 2917; sibling 2923 has the same entry). No NPC is linked to this item in our data.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 763 (item 2917); client definition coin_store_prices 270"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Camouflage Sunglasses' (locale 398750), description 'You can see out, but they can't see in!' (locale 398931), flavor line 'Hide your eyes in plain sight.' (locale 398936).", "source": "locale:398750; locale:398931; locale:398936"},
  {"claim": "Stores.json carries a 270-coin purchase price (243 member) for item 2917 with no price_provenance note, so the coin price was not cleared the way the sibling sunglasses and Sailor Hat were.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 763"},
  {"claim": "Sibling entries Sailor Hat (2916), Polkadot Sunglasses (2922) and Tiger Sunglasses (2924) had their 270-coin Legacy price cleared and were re-listed at 49 or 99 Station Cash on the SC Marketplace, citing the fandom wiki prices. No such wiki-based re-listing exists for item 2917.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 762, 768, 770"},
  {"claim": "Wiki pages for Tiger Sunglasses and Polkadot Sunglasses say each was sold through the Station Cash Marketplace and through Cragara; neither page names a price for Cragara's sale.", "source": "wiki: Tiger_Sunglasses; Polkadot_Sunglasses"},
  {"claim": "No wiki page exists for Camouflage Sunglasses, and no wiki, article, quest, drop, event, prize-wheel or crafting source was found for it.", "source": "lookup wiki/client/articles for 'Camouflage Sunglasses' (no wiki page returned)"},
  {"claim": "Video frames show the item only in the inventory/collection screens next to other head items. They do not show a source.", "source": "video:p5sDafXSQtQ/00106.jpg; video:p5sDafXSQtQ/00108.jpg"}
 ],
 "confidence": 0.3,
 "open": [
  "The vendor that sold item 2917 for 270 coins is not named anywhere in the repo or wiki. Find the Legacy CoinStoreItems source or vendor catalogue entry before naming an NPC.",
  "Cragara is not confirmed for this item. The wiki ties her to Tiger and Polkadot Sunglasses only, and no wiki price is given for her sale. Do not treat her as the source.",
  "The late-2012 Cragara closure claim from the previous answer has no source in the pack and was dropped. Retirement status stays unknown.",
  "Item 2917 kept its 270-coin price while its siblings (2916, 2922, 2924) were cleared to SC Marketplace listings. Whether 2917 also belongs on the SC Marketplace (no SC price in our data) or is coin-only is unresolved.",
  "No drop, quest, event, prize-wheel, crafting, collection or membership source was found."
 ]}
