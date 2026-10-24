<!-- fleet job=citem-infer id=cnether-enchanted-wand-19566-v1 status=done turns=5 usd=0.0043 tokens(read,write,in,out)=[34902, 17627, 12, 3487] model=claude-haiku-5-5 -->
# Nether Enchanted Wand

{"item": {"name": "Nether Enchanted Wand", "locale_id": 19566, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 207 (tint variants; 1913 coins for item 38696 tint 1, 38700 tint 3, 38693/38694/38704/38710 family; 1780 coins for item 38698 tint 2)", "where": "Coin store (category 207; store name not resolved in repo)", "price": "1913 coins (member price 1721 coins, 10% member discount) for most variants; 1780 coins (member 1602) for variant 38698", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12404-12408 (item_id 38696, 38698, 38700); client definition coin_store_prices [1780, 1913]; repo:prototype/osfr-tools/data/reference/weapons.json lines 30974-31037 (client item ids 30540..38712 with cost 1913)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Item name is locale 19566 'Nether Enchanted Wand'", "source": "locale:19566"},
  {"claim": "Wiki: level 16 Wizard weapon, Green Text weapon, stated as 'can only be acquired through trade'", "source": "wiki page Nether Enchanted Wand"},
  {"claim": "Wiki page is in Category:Retired Weapons", "source": "wiki page Nether Enchanted Wand (categories)"},
  {"claim": "Wiki Green Text weapon list includes [Nether] [Enchanted] [Wand] marked yes (retired/green text list)", "source": "wiki page Green Text weapon"},
  {"claim": "Coin store data lists 10 client definitions of this wand with purchase prices 1913 and 1780 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12404-12408; repo:prototype/osfr-tools/data/reference/weapons.json lines 30974-31037"}
 ],
 "confidence": 0.5,
 "open": [
  "Wiki says the wand 'can only be acquired through trade' (player-to-player), which conflicts with the coin store price data; the store data is repo evidence of a coin vendor sale, but no wiki Coin Shop category or article names this wand, so the coin shop listing is unverified against live sources.",
  "Store category 207 is not named in the repo; confirm it maps to the Coin Shop (vs. another vendor) before publishing the vendor label.",
  "Price 1780 is listed for only one variant (item 38698, tint 2); the other 9 definitions are 1913 in the store data. Mapping of prices to individual tints/races is not fully confirmed.",
  "No retirement date or last-sale date found in any source; retired=true rests only on the wiki's Retired Weapons category.",
  "Member prices (1721 and 1602 coins) are derived from a 10% member discount in the store data, not a wiki-stated price.",
  "No wiki price, quest, drop, event, or prize-wheel source found for this wand."
 ]}</result>
