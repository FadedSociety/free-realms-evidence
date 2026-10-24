<!-- fleet job=item-infer id=ispook-sphere-v1 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[2967, 7632, 6, 1612] model=claude-haiku-5-5 -->
# Spook Sphere

{"item": {"name": "Spook Sphere", "locale_id": 2822, "kind": "consumable"},
 "sources": [{"type": "promotion", "detail": "Redeemable with promo code PXNH6HB in the in-game redemption menu", "where": "redemption menu (code entry)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Spook_Sphere (rev 46978: 'It is acquired by entering the code PXNH6HB in the redemption menu.'); freerealms-com/cdx-urls.json (archived freerealms.com URLs with ac=PXNH6HB, affid=candystand)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Spook Sphere is a consumable usable by any job, acquired by entering code PXNH6HB in the redemption menu", "source": "https://freerealms.fandom.com/wiki/Spook_Sphere"},
  {"claim": "Item tooltip: 'A magical orb that transforms the player into a frightful creature.' Required: Any Job, Power 5, Activatable effect Illusion: Mauthedog for 30 minutes, Cannot Sell, Cannot Trade; resell value 4", "source": "https://freerealms.fandom.com/wiki/Spook_Sphere (image: item_tooltip)"},
  {"claim": "Client name text 'Spook Sphere' is locale 2822", "source": "locale:2822"},
  {"claim": "Code PXNH6HB appears as an 'ac=' promo parameter on archived freerealms.com URLs (affid=candystand), consistent with a promotional redemption code", "source": "repo:freerealms-com/cdx-urls.json:587"},
  {"claim": "Wiki categories: Consumable, Supplies. No coin vendor, Station Cash, or Coin Shop price listed; no vendor stock or quest/drop mentions in the pack", "source": "https://freerealms.fandom.com/wiki/Spook_Sphere"}
 ],
 "confidence": 0.6,
 "open": [
  "No coin or Station Cash price: the wiki lists none, so the item has no purchasable price in the sources. Resell value 4 is a sell value, not a price.",
  "Redemption period and expiry of code PXNH6HB are not stated anywhere in the pack; retired status is unknown. Do not assume it is live.",
  "The wiki page has no retirement note, so 'retired' is null rather than true.",
  "Locale 2823 ('A magical orb that confuses the opponent.') is a neighbouring Spook-series item text, not this item; not used as evidence.",
  "Wiki revision 46978 is older than the revision that mentions the code in the 3362-47210 wikitext (line 89), which lists PXNH6HB beside Spook Sphere. This supports the source but was not checked in full."
 ]}
