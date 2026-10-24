<!-- fleet job=item-infer id=icross-wind-archer-quiver-v3 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[5518, 14388, 6, 2507] model=claude-haiku-5-5 -->
# Cross Wind Archer Quiver

{"item": {"name": "Cross Wind Archer Quiver", "locale_id": 132769, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Wiki Coin Shop: members-only level 10 Archer clothing, Misc slot. Item page says it is acquired from the Coin Shop 'where it sells at {{Coin|568}}' (wikitext rev 31025; the rendered body drops the price, so the figure is wikitext-only).", "where": "Coin Shop", "price": "568 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Cross_Wind_Archer_Quiver (rev 31025, freerealms-wiki/wikitext/10577-31025-1f10b176794d.wiki; categories Coin Shop, Coin Shop Clothing)"},
  {"type": "vendor", "detail": "Kimi, pixie Archer merchant; the quiver is in her Sells list. The wiki gives no price for Kimi.", "where": "Near the Lakeshore Cooking Table (wiki placement)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Kimi (Sells list); repo notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md row 77"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item is members-only level 10 Archer clothing, Misc slot, acquired from the Coin Shop at 568 coins (wikitext {{Coin|568}})", "source": "https://freerealms.fandom.com/wiki/Cross_Wind_Archer_Quiver (rev 31025)"},
  {"claim": "Item page categories include Coin Shop, Coin Shop Clothing, Archer Clothes, Level 10 Clothes, Marketplace Items, Misc", "source": "https://freerealms.fandom.com/wiki/Cross_Wind_Archer_Quiver"},
  {"claim": "Kimi, a pixie NPC merchant near the Lakeshore Cooking Table who sells exclusively Archer job items, lists Cross Wind Archer Quiver in her Sells list with no price", "source": "https://freerealms.fandom.com/wiki/Kimi"},
  {"claim": "Client name text is locale:132769 'Cross Wind Archer Quiver'", "source": "locale:132769"},
  {"claim": "Deep Mines wiki page lists Cross Wind Archer Quiver beside Battle Item Mystery Pack and an '80 Coins' figure, but the figure's row attachment is ambiguous, so it is not used as a source", "source": "https://freerealms.fandom.com/wiki/Deep_Mines; repo notes/Build Guides/Content/Dungeons/Deep Mines.md:68"}
 ],
 "confidence": 0.6,
 "open": [
  "Kimi's price for the quiver is not stated anywhere in the evidence. The 568-coin figure is the Coin Shop price on the item page, not Kimi's price. Verify in game whether Kimi sells it and at what price.",
  "Conflicting price: the Deep Mines wiki page shows '80 Coins' next to the quiver row, and the layout does not show whether it belongs to the quiver or to the Battle Item Mystery Pack. Reconcile in game or with the wiki source before fixing a price.",
  "Members-only is stated on the wiki, but no membership-pack source is evidenced, so no membership source is listed.",
  "Marketplace Items category hints at possible Station Cash marketplace history, but no SC price or SC Marketplace category is evidenced, so no marketplace source is listed.",
  "Live status is unknown: neither the item page nor the Kimi page carries a retirement note, and the repo's vendor data has no price or stock row for the quiver (repo search found the name only in the Kimi notes and the Deep Mines data)."
 ]}
