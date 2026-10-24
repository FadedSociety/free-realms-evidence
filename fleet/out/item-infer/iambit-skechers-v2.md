<!-- fleet job=item-infer id=iambit-skechers-v2 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5164, 6119, 6, 1467] model=claude-haiku-5-5 -->
# Ambit Skechers

{"item": {"name": "Ambit Skechers", "locale_id": 14107, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing for all players at the regular price; Members get a 10% discount tier (269 Station Cash) on the same listing", "where": "SC Marketplace", "price": "299 Station Cash (regular); 269 Station Cash (Members, 10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Ambit_Skechers (rev 36805; wiki text: 'available to everyone for purchase through the Station Cash Marketplace at the regular price ... and to Members at the 10% discount price'; station_cash field [299, 269]; the rendered sentence lost the figures, so the numbers come from the station_cash field)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Ambit Skechers is an All Jobs, feet-slot clothing item sold through the Station Cash Marketplace.", "source": "https://freerealms.fandom.com/wiki/Ambit_Skechers"},
  {"claim": "Regular price 299 Station Cash and Members 10%-discount price 269 Station Cash; both are one SC Marketplace listing, not two sources. The figures come from the wiki station_cash field, not the visible sentence.", "source": "https://freerealms.fandom.com/wiki/Ambit_Skechers (station_cash [299, 269])"},
  {"claim": "Client name text for the item is locale:14107 'Ambit Skechers'; locale:14108 is the Skechers trademark line.", "source": "locale:14107; locale:14108"},
  {"claim": "Wiki categories are All Jobs, Clothing, Feet, Marketplace Items, SC Marketplace, SC Marketplace Clothing; no Retired or event category.", "source": "https://freerealms.fandom.com/wiki/Ambit_Skechers"},
  {"claim": "Appearance is based on the Boys Luminators: Ambit shoes by Skechers (licensed, trademark of SKECHERS USA, Inc.).", "source": "https://freerealms.fandom.com/wiki/Ambit_Skechers"}
 ],
 "confidence": 0.6,
 "open": [
  "Retired and live status unconfirmed: no retirement note, no date of introduction, and no repo listing data (repo search found no Ambit/14107 marketplace data). Category absence of Retired is weak evidence.",
  "The 299 and 269 prices rest on the wiki station_cash field; the visible page text omits them. No second source confirms them.",
  "Critique fix applied: the Members 269 price is a tier on the same listing, so it is one source, not two.",
  "No coin vendor, quest, drop, crafting, or event source found in the pack or repo; none recorded."
 ]}
