<!-- fleet job=item-infer id=istupendous-gloves-v1 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3084, 3817, 6, 1437] model=claude-haiku-5-5 -->
# Stupendous Gloves

{"item": {"name": "Stupendous Gloves", "locale_id": 5103047, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop purchase during HeroRealms Month (January 2014), open to everyone; part of the Coin Shop HeroRealms gear set (Stupendous: Boots, Gloves, Mask, and others)", "where": "Coin Shop", "price": "40 coins (regular price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Stupendous_Gloves (rev 36480; categories Coin Shop, Coin Shop Clothing); lookup of wiki page 'HeroRealms Month' lists Stupendous gear as Coin Shop HeroRealms gear set"},
  {"type": "membership", "detail": "Members' 10% discount purchase of the Coin Shop item during HeroRealms Month", "where": "Coin Shop", "price": "36 coins (Members, 10% discount; the sale price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Stupendous_Gloves (coin prices 40 and 36 in page data)"}],
 "retired": true, "live": "no",
 "evidence": [{"claim": "Stupendous Gloves are an Any Job hands-slot clothing item sold in the Coin Shop during HeroRealms Month, introduced January 14, 2014", "source": "https://freerealms.fandom.com/wiki/Stupendous_Gloves"},
  {"claim": "Regular price 40 coins; Members price 36 coins at 10% discount", "source": "https://freerealms.fandom.com/wiki/Stupendous_Gloves (coins field [40, 36])"},
  {"claim": "Client name string for the item is locale 5103047, category HeroRealms Gear", "source": "locale:5103047"},
  {"claim": "Gloves are part of the Stupendous HeroRealms Coin Shop gear set alongside Boots, Mask, Spandex Chestpiece and Spandex Leggings", "source": "https://freerealms.fandom.com/wiki/HeroRealms_Month"},
  {"claim": "Item is in the Coin Shop Clothing and HeroRealms Month categories", "source": "https://freerealms.fandom.com/wiki/Stupendous_Gloves (categories)"}],
 "confidence": 0.8,
 "open": ["Retirement: the pack gives no end date; 'HeroRealms Month' is a one-month event, so it is treated as retired, but no wiki source states it was removed. Verify.",
  "Wiki prices are stripped of currency symbols in the page text; the coins field gives 40/36, and the 'Coin Shop' category implies coins, not Station Cash.",
  "No vendor stock or quest/drop data in the pack; none assumed.",
  "Wiki page's 'Marketplace Items' category is not treated as a separate SC Marketplace source because no wiki price in Station Cash appears."]}
