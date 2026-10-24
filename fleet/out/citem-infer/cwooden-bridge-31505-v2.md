<!-- fleet job=citem-infer id=cwooden-bridge-31505-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5759, 10951, 6, 2061] model=claude-haiku-5-5 -->
# Wooden Bridge

{"item": {"name": "Wooden Bridge", "locale_id": 31505, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for definition 16897 (category 56, tint group 1). Seller not named in the store data, so no vendor is identified. Candidate sale only; the definition-to-name link is unverified.", "where": null, "price": "1000 coins (member price 900 coins; sell-back 100 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:4260 (item 16897)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 31505 is 'Wooden Bridge', tagged 'place', description 'Bridge: It brings places together.'", "source": "locale:31505"},
  {"claim": "Store row for 16897 is 1000 coins, member 900, sell 100, no_sale false. The same 1000-coin tier is shared by many category 56 and other furniture rows (e.g. 16896, 16900, 16901, 16902), so it is a tier default, not proof of this item's price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4256-4270"},
  {"claim": "Definition 14302 (50 coins, no_sale true, no sell price) is not a sale source for this item and is excluded.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3784"},
  {"claim": "Wiki Items page lists '[Wooden] [Bridge]' and '[Wooden] Walkway' with no price. The wiki has no page titled plain 'Wooden Bridge'.", "source": "lookup wiki page Items"},
  {"claim": "Official site announced housing pieces '[Wooden] Suspension [bridge] and connecting walkway pieces'. These name a suspension bridge, not the plain Wooden Bridge; link is inferred.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1521"},
  {"claim": "Video frames show a wooden bridge in a sandy desert canyon in decorate mode ('Click to Decorate'), consistent with a placeable housing item.", "source": "video:yLjpOTxwUj8/00034.jpg; video:yLjpOTxwUj8/00048.jpg"},
  {"claim": "Sibling Storm Cloud Bridge (16892) has a reconstructed SC Marketplace price of 275 Station Cash from the fandom wiki, showing bridge housing items were sold via SC Marketplace rather than the coin vendor. Not evidence for Wooden Bridge's channel.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4255"}
 ],
 "confidence": 0.3,
 "open": [
  "The critique is correct that nothing ties definition 16897 or 14302 to locale 31505 by name; the link is unverified.",
  "No vendor names this item in vendor_stock; the store row has no seller, zone, or stock source. The 'vendor' type from the prior answer is replaced with coin_shop.",
  "Definition 14302 (50 coins, no_sale) is unexplained and excluded as a source.",
  "Whether the plain 'Wooden Bridge' is the same item as the wiki '[Wooden] [Bridge]' entry is inferred, not confirmed.",
  "Retirement status and current availability are unknown; no source found.",
  "The wiki Items page gives no price for [Wooden] [Bridge], so no SC Marketplace or Coin Shop category is confirmed for it.",
  "No quest reward, drop, event, or prize wheel source found."
 ]}
