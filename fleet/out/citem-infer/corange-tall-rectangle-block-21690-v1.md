<!-- fleet job=citem-infer id=corange-tall-rectangle-block-21690-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3500, 4926, 6, 2006] model=claude-haiku-5-5 -->
# Orange Tall Rectangle Block

{"item": {"name": "Orange Tall Rectangle Block", "locale_id": 21690, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, definition 77068 (purchase 50 coins; member price 45 coins, 10% member discount; no_sale flag true)", "where": "coin vendor (category 147; store name not resolved)", "price": "50 coins (member 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77068 (line 16399)"},
  {"type": "vendor", "detail": "Coin store sale, definition 77148 (purchase 300 coins; member price 270 coins; sell_price 30 coins, no_sale false)", "where": "coin vendor (category 147; store name not resolved)", "price": "300 coins (member 270 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77148 (line 16479)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 21690 is 'Orange Tall Rectangle Block', description 'Great for stackability.', model hsg_block_03.adr, two definitions (77068, 77148), slot 0, class 0", "source": "locale:21690 and client definition pack"},
  {"claim": "Store data lists definition 77068 at purchase_price_coins 50 and definition 77148 at purchase_price_coins 300, both in category 147", "source": "repo:prototype/osfr-tools/data/content/stores.json items 77068 and 77148"},
  {"claim": "Sibling color blocks (Black, Blue, Green, Pink, Purple, Red, Teal, White Tall Rectangle Block, locale 21687-21695) share the same name pattern and cluster, so they are likely the same furniture family", "source": "locale:21687 through locale:21695"},
  {"claim": "No wiki page, image, article fact or video frame names this item; 'Tall Rectangle Block' wiki-era names (Basic, Cheese, Polkadot, Tiger, locale 8662-8695) are separate items", "source": "lookup of client and wiki indexes, no hits for wiki/articles/video"}
 ],
 "confidence": 0.5,
 "open": [
  "Two coin prices (50 and 300) belong to two different definition ids; the pack cannot tell whether they are different tints, sizes or sale periods. The 300-coin entry shows sell_price 30, which may be a resale value rather than a sale price; treat the 300 entry as unverified until a wiki or article source confirms it.",
  "Store category 147 is not named in the repo data, so the storefront (Coin Shop vs. a named coin vendor) and vendor location are unresolved.",
  "No wiki page, article, or video source names this block, so the sale window and whether it was retired are unknown. The 77068 entry has no_sale true, which may mean it was never resold or was removed from sale; confirm before marking it retired.",
  "The cluster entry locale:21686 (Sanctuary 'Find Fhred' shirt reward) and locale:21685 (Duelist Block) are not evidence for this item; they are not counted as sources.",
  "The client's 'Orange Tall Rectangle Block' was not found in any drop, quest, event, prize wheel or crafting answer in the pack."
 ]}
