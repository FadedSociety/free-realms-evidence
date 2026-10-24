<!-- fleet job=item-infer id=ivile-spandex-leggings-v1 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[3115, 4016, 6, 2034] model=claude-haiku-5-5 -->
# Vile Spandex Leggings

{"item": {"name": "Vile Spandex Leggings", "locale_id": 5103081, "kind": "clothing"},
 "sources": [{"type": "marketplace", "detail": "Station Cash Marketplace, HeroRealms Month item, regular price (non-members)", "where": "SC Marketplace", "price": "75", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings (station_cash list [75, 67]; prose price blank in extracted text)"},
  {"type": "marketplace", "detail": "Station Cash Marketplace, Members 10% discount price", "where": "SC Marketplace", "price": "67", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings (second wiki price, 10% member discount of 75 = 67.5, listed as 67)"},
  {"type": "event", "detail": "HeroRealms Month (Hero vs. Villain month-long event), introduced in-game January 14, 2014; item sold during the event", "where": "SC Marketplace", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings; https://freerealms.fandom.com/wiki/HeroRealms_Month (lists Vile set including Spandex Leggings)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [{"claim": "Item is an Any Job clothing item sold on the Station Cash Marketplace during HeroRealms Month to everyone at the regular price, and to Members at a 10% discount", "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings"},
  {"claim": "Introduced in-game January 14, 2014 as part of HeroRealms Month; announced by Producer Steve 'Shock' George on Twitter January 13, 2014", "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings"},
  {"claim": "Wiki categories: HeroRealms Month, Clothing, Legs, Marketplace Items, SC Marketplace, SC Marketplace Clothing, All Jobs", "source": "https://freerealms.fandom.com/wiki/Vile_Spandex_Leggings"},
  {"claim": "Client name string exists as item name", "source": "locale:5103081"},
  {"claim": "HeroRealms Month page lists the Vile gear set including Spandex Leggings", "source": "https://freerealms.fandom.com/wiki/HeroRealms_Month"}],
 "confidence": 0.7,
 "open": ["Prices: the extracted prose has blank price fields ('at the regular price of , ... of .'); the 75 / 67 values come only from the station_cash field. Confirm against the page's rendered text or a marketplace capture.",
  "Slot conflict: the wiki prose says 'head slot' but the categories say 'Legs' and the item name is leggings. Treat as legs clothing unless a client Resource says otherwise.",
  "The HeroRealms Month page has a 'Coin Shop HeroRealms gear sets' section; the Vile set may also have had Coin Shop pieces. The snippet was truncated, so a Coin Shop source for these leggings is unverified and left out.",
  "Retirement: no 'Retired' category and no end date on the page. Whether the Marketplace listing ended after HeroRealms Month (January 2014) is not confirmed, so retired is null and live is unsure.",
  "No quest, drop, crafting, or prize-wheel source found in the pack."]}
