<!-- fleet job=item-infer id=ituxedo-t-shirt-v1 status=done turns=3 usd=0.0015 tokens(read,write,in,out)=[6333, 4193, 8, 1741] model=claude-haiku-5-5 -->
# Tuxedo T-Shirt

{"item": {"name": "Tuxedo T-Shirt", "locale_id": 9140, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, regular price for everyone", "where": "Station Cash Marketplace (SC Marketplace Clothing)", "price": "299 Station Cash", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Tuxedo_T-Shirt (rev 37222; categories SC Marketplace, SC Marketplace Clothing; infobox station_cash value 299)"},
  {"type": "membership", "detail": "Monthly Membership Pack item (January 2013), member 10% discount price on Marketplace", "where": "Station Cash Marketplace (members)", "price": "269 Station Cash (member sale price, 10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Tuxedo_T-Shirt (page text: introduced in January 2013's Monthly Membership Pack; members get 10% discount; second price 269 in station_cash field)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Tuxedo T-Shirt', locale id 9140 (distinct from Doggy Tuxedo T-Shirt 81766 and Kitty Tuxedo T-Shirt 88568)", "source": "locale:9140"},
  {"claim": "Item is an All Jobs, chest slot clothing item introduced in January 2013's Monthly Membership Pack; currently sold to everyone in the Station Cash Marketplace at the regular price, members get 10% off", "source": "https://freerealms.fandom.com/wiki/Tuxedo_T-Shirt"},
  {"claim": "Wiki categories: All Jobs, Chest, Clothing, Marketplace Items, SC Marketplace, SC Marketplace Clothing", "source": "https://freerealms.fandom.com/wiki/Tuxedo_T-Shirt"},
  {"claim": "Monthly Membership Packs were granted to members each month (e.g. January 2012 pack noted in news archive), supporting the membership-pack origin", "source": "Template:News/Archive (wiki, 'Update of January 19, 2012' Monthly Membership Pack entry); Monthly Member Pack Items page"}
 ],
 "confidence": 0.6,
 "open": ["The page's price sentences have blank numbers in the text; 299 and 269 come from the station_cash field only. 269 = 299 less 10%, consistent with the stated discount, but the text itself does not state the figures.",
  "The Monthly Member Pack Items page excerpt I saw did not show the January 2013 row, so the membership-pack origin rests on the Tuxedo page alone. Verify the January 2013 pack contents.",
  "Current availability (still sold on Marketplace today) is not confirmed; the page says 'currently' but its revision date is unknown. Live status set to unsure.",
  "No coin vendor stock, quest reward, drop, or crafting source found in the pack; none listed.",
  "Critiques: none were carried in the pack."]}
