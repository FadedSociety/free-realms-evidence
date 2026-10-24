<!-- fleet job=item-infer id=iarcher-s-flair-shard-of-smoldering-v3 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[21886, 9122, 10, 1992] model=claude-haiku-5-5 -->
# Archer's Flair Shard of Smoldering

{"item": {"name": "Archer's Flair Shard of Smoldering", "locale_id": 130973, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase (Archer flair shard, level 1 Archer)", "where": "Coin Shop", "price": "750 (wiki structured coin field only; the wiki prose price is blank: 'sells for .')", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Flair_Shard_of_Smoldering (rev 32666; categories Coin Shop, Coin Flair, Flair Shard, Marketplace Items)"},
  {"type": "vendor", "detail": "Gilbert, Pixie NPC merchant near the Greenwood Forest warpstone; 'Sells' section lists Archer's Flair Shard of Smoldering", "where": "Greenwood Forest", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Gilbert (Sells section; also Merchants page: 'Gilbert found near the Greenwood Forest Warpstone'); repo:prototype/osfr-tools/data/content/vendors.json:16068-16076"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client text, locale 130973", "source": "locale:130973"},
  {"claim": "Wiki page classifies the item as a level 1 Archer flair shard and places it in the Coin Shop category; the prose says it is acquired from the Coin Shop but the price field is blank", "source": "https://freerealms.fandom.com/wiki/Archer's_Flair_Shard_of_Smoldering"},
  {"claim": "Gilbert wiki page (retrieved in this pass) lists Archer's Flair Shard of Smoldering under Sells; Gilbert is a pixie merchant near the Greenwood Forest warpstone and sells exclusively Archer job items", "source": "https://freerealms.fandom.com/wiki/Gilbert"},
  {"claim": "Repo reference values 750 / member 675 / sell 375 come from stores.json with 'no captured retail NPC quote'; they are not wiki or in-game prices and are not used as evidence of the price", "source": "repo:prototype/osfr-tools/data/content/vendors.json:16054-16061"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin Shop price 750 is unverified: it appears only in the wiki's structured coin field (rev 32666); the prose price is blank and no live Coin Shop quote was captured. Confirm against a live listing.",
  "Gilbert's sell price for this item is not stated on the wiki page; no price is given for the vendor source.",
  "The 750 figure in the repo reference is the same value as the wiki structured field, so it is not an independent confirmation.",
  "Gilbert's stock listing is confirmed from the wiki Sells section but the item's current availability at Gilbert is not dated beyond the repo's 2025-05-31 revision.",
  "No Station Cash or SC Marketplace source is evidenced despite the 'Marketplace Items' category.",
  "The wiki page has broken file links and no images, so the icon is unverified.",
  "No retirement or removal from the Coin Shop is documented; retired is null and live is 'unsure'."
 ]}
