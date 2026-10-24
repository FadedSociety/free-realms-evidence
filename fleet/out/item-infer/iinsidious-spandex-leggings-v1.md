<!-- fleet job=item-infer id=iinsidious-spandex-leggings-v1 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[3016, 3908, 6, 1988] model=claude-haiku-5-5 -->
# Insidious Spandex Leggings

{"item": {"name": "Insidious Spandex Leggings", "locale_id": 5103086, "kind": "clothing"},
 "sources": [{"type": "marketplace", "detail": "Station Cash Marketplace, sold during HeroRealms Month (Hero vs. Villain event, Jan 2014) to everyone at the regular price", "where": "Station Cash Marketplace", "price": "75 Station Cash (regular price; the wiki text's price field is blank, value taken from the wiki station_cash field)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Insidious_Spandex_Leggings ; wiki categories SC Marketplace, SC Marketplace Clothing, HeroRealms Month"},
  {"type": "marketplace", "detail": "Station Cash Marketplace, Members price during HeroRealms Month (10% member discount)", "where": "Station Cash Marketplace", "price": "67 Station Cash (member sale price; 10% off 75 rounds to 67)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Insidious_Spandex_Leggings (text: 'to Members at the 10% discount price'; station_cash values 75, 67)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [{"claim": "Item is an Any Job clothing item available during HeroRealms Month via the Station Cash Marketplace, introduced in-game January 14, 2014 as part of HeroRealms Month", "source": "https://freerealms.fandom.com/wiki/Insidious_Spandex_Leggings"},
  {"claim": "Client name string for the item is 'Insidious Spandex Leggings'", "source": "locale:5103086"},
  {"claim": "HeroRealms Month page lists [Insidious] set pieces including [Spandex] Leggings alongside Boots, Gloves, Mask and [Spandex] Chestpiece (locale:5103082 is the Chestpiece)", "source": "https://freerealms.fandom.com/wiki/HeroRealms_Month"},
  {"claim": "Wiki categories: All Jobs, Clothing, Legs, HeroRealms Month, Marketplace Items, SC Marketplace, SC Marketplace Clothing", "source": "https://freerealms.fandom.com/wiki/Insidious_Spandex_Leggings"}],
 "confidence": 0.6,
 "open": ["Conflict: the wiki body says 'head slot', but the name, the 'Legs' category and the HeroRealms set context say leggings (legs slot). Treated as legs; the 'head slot' wording looks like an error, to verify in client data.",
  "The wiki body's price fields are blank ('at the regular price of , and ... 10% discount price of .'). The 75/67 figures come from the station_cash field, not the text; the 67 is the member price and is a sale price, not a second regular price.",
  "No retirement date is given. The item is described as available only during HeroRealms Month, which suggests it is time-limited, but the wiki does not say it was retired or when it left the Marketplace. Whether it is still purchasable on a live server is unknown.",
  "The HeroRealms Month page has a 'Coin Shop HeroRealms gear sets' section; the snippet returned was cut off before the Insidious set. Check whether Insidious pieces were also sold in the Coin Shop, which would add a coin_shop source. No coin price is in the pack.",
  "No drop, quest, crafting or vendor source is in the pack, and none was found."]}
