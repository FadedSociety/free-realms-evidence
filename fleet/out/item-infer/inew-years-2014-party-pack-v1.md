<!-- fleet job=item-infer id=inew-years-2014-party-pack-v1 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[3211, 4449, 6, 2011] model=claude-haiku-5-5 -->
# New Years 2014 Party Pack

{"item": {"name": "New Years 2014 Party Pack", "locale_id": 5103011, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace bundle, regular price for non-members (available Dec 31 2013 and Jan 1 2014 only)", "where": "Station Cash Marketplace (SC Marketplace)", "price": "99", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack; image text 'Only 99sc for Non-Members!'"},
  {"type": "marketplace", "detail": "Station Cash Marketplace bundle, member price (10% discount), same Dec 31 2013 to Jan 1 2014 window", "where": "Station Cash Marketplace (SC Marketplace)", "price": "89", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack (station_cash field 99, 89; text says members get 10% discount price; 89 is the sale/member price)"},
  {"type": "membership", "detail": "Free to members who logged in between Dec 31 2013 and Jan 1 2014", "where": null, "price": "free", "currency": null, "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack; locale:5103012 ('Become a Member and get this FREE! (Available Dec 31st & Jan 1st ONLY.)')"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Item is a Consumable marketplace bundle sold on the Station Cash Marketplace, available Dec 31 2013 and Jan 1 2014", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack"},
  {"claim": "Non-member Station Cash price is 99sc", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack (station_cash 99; image 'Only 99sc for Non-Members!')"},
  {"claim": "Member price is 89sc, a 10% discount", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack (station_cash 89; page text 'members at the 10% discount price')"},
  {"claim": "Members logging in Dec 31 2013 to Jan 1 2014 received one free", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack; locale:5103012"},
  {"claim": "Bundle contents: Purple, Golden Fountain, Red, Blue, Gold, Green Pinwheel/Fountain Fireworks (2 each) plus 2014 Party Glasses and 2014 Party Hat (1 each)", "source": "https://freerealms.fandom.com/wiki/New_Years_2014_Party_Pack; corroborated by individual firework wiki pages (e.g. Gold Pinwheel Firework, Blue Pinwheel Firework) that cite the 2014 Party Pack bundle"},
  {"claim": "Name is client locale 5103011", "source": "locale:5103011"}
 ],
 "confidence": 0.8,
 "open": [
  "Retired status is inferred from the time-limited sale window (Dec 31 2013 and Jan 1 2014 only); no wiki 'Retired' category or explicit retirement statement was in the pack.",
  "The wiki page text dropped the price numbers ('regular price of , ... discount price of .'); 99 and 89 come from the station_cash field and the image text, so the 89 figure is the wiki's member price but was not stated in running text.",
  "No coin vendor stock or prize wheel/drop source found; none listed."
 ]}
