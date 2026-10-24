<!-- fleet job=item-infer id=ithe-handyman-s-shelf-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5614, 8986, 6, 1840] model=claude-haiku-5-5 -->
# The Handyman's Shelf

{"item": {"name": "The Handyman's Shelf", "locale_id": 5102677, "kind": "furniture"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, Player Studio item designed by Andy Barth. 99 SC for everyone; members get the 10% discount price of 89 SC on this same listing (one offer, not two sources)", "where": "Station Cash Marketplace (SC Marketplace)", "price": "99 Station Cash (members: 89 Station Cash)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/The_Handyman's_Shelf (rev 43249; station_cash field [99, 89]; page text 'regular price ... and to members at the 10% discount price'; categories SC Marketplace, Marketplace Items, Player Studio). Wikitext per critique: {{SC|99}} and {{SC|89}}, rev 43249 line 4."}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Furniture Housing item designed by Andy Barth for the SOE Player Studio program; wiki gives introduction in game on October 22, 2013", "source": "https://freerealms.fandom.com/wiki/The_Handyman's_Shelf; Game Update 116 Overview 10/22/2013 on Free Realms Forums (forum post 418069, cited on the wiki page)"},
  {"claim": "Available to everyone on the Station Cash Marketplace at 99 SC; members get 89 SC at a 10% discount on the same offer", "source": "https://freerealms.fandom.com/wiki/The_Handyman's_Shelf (station_cash [99, 89]; categories SC Marketplace, Marketplace Items)"},
  {"claim": "In-game description: 'Be careful with hammers. Hammers are serious tools.' Created by Andy Barth for Player Studio", "source": "https://freerealms.fandom.com/wiki/The_Handyman's_Shelf (igd field)"},
  {"claim": "Item name matches the client text table entry", "source": "locale:5102677"},
  {"claim": "Page carries a {{Sunset Sale}} template (rev 43249, line 13); the Sunset Sale template describes permanent Station Cash pricing for March 18-31, 2014, so 99/89 may be pre-sunset pricing", "source": "freerealms-wiki wikitext rev 43249 line 13 (per critique; not re-checked in this pass)"},
  {"claim": "Sanctuary StoreBundles row 'The Handyman's Shelf' (Id 51095, NameId 5102677, CurrencyType 1, Status 1, ExpireTime 2040-08-15, LaunchTime 2013-10-15) suggests the row was still active in the store data", "source": "Sanctuary StoreBundles (per critiques; not re-checked in this pass)"}
 ],
 "confidence": 0.7,
 "open": [
  "Retirement unknown: no delisting evidence found. Status 1 and expiry 2040 in StoreBundles suggest it was still listed, but the wiki's Sunset Sale template means the 99/89 price should be checked against the marketplace as it stood at the 2014 sunset.",
  "Date conflict: wiki introduction date 10/22/2013 (Game Update 116) vs StoreBundles LaunchTime 2013-10-15. Unresolved.",
  "The 99 and 89 SC figures are confirmed by the station_cash field and the page's price sentence; the wikitext SC templates were cited in critiques but not re-read here.",
  "No coin vendor, quest reward, drop, crafting, or event source found in the pack; none listed.",
  "Locale 5102677 was matched via the locale tool; a direct grep of the locale data files for the id was inconclusive in this pass."
 ]}
