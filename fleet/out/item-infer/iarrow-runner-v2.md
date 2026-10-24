<!-- fleet job=item-infer id=iarrow-runner-v2 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5529, 6873, 6, 1439] model=claude-haiku-5-5 -->
# Arrow Runner

{"item": {"name": "Arrow Runner", "locale_id": 7160, "kind": "other"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing, sold to everyone at the regular price; Members get a 10% discount on the same listing (the 359 figure is that Member price, not a second source)", "where": "SC Marketplace", "price": "399 Station Cash (regular); 359 Station Cash (Member price, 10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Arrow_Runner (rev 36816; category SC Marketplace; station_cash values 399 and 359 in the pack; the price sentence itself is stripped in the pack text)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Arrow Runner is a Race Kart available to everyone in the Station Cash Marketplace at the regular price, and to Members at a 10% discount price.", "source": "https://freerealms.fandom.com/wiki/Arrow_Runner"},
  {"claim": "Wiki categories: Race Kart, Karts, SC Marketplace, Marketplace Items.", "source": "https://freerealms.fandom.com/wiki/Arrow_Runner"},
  {"claim": "Item name is client text locale:7160 'Arrow Runner'.", "source": "locale:7160"},
  {"claim": "Item description: 'One of the first closed cockpit race kart models.'", "source": "locale:7172"},
  {"claim": "Wiki Items index lists Arrow Runner under Race Karts with Wicked Racer, Splash Zipper, Slicing Racer, Speedy Runner, Slime Runner.", "source": "https://freerealms.fandom.com/wiki/Items"},
  {"claim": "Client has Arrow Runner part items (Chassis locale:7467, Engine locale:406490, Turbo locale:406502, Steering Column locale:406514, Tires locale:406526, Mod locale:406538), consistent with a kart vehicle.", "source": "locale:7467; locale:406490; locale:406502; locale:406514; locale:406526; locale:406538"}
 ],
 "confidence": 0.7,
 "open": [
  "The wiki price sentence is stripped in the pack; 399 and 359 come from the station_cash field plus the 10% Member wording. Verify both on the live wiki page or the Station Cash marketplace data.",
  "No retirement or removal date in the evidence; retired is unknown. The Items index still lists it under Race Karts, which does not confirm it is still sold.",
  "kind 'other' used because no source names a category for vehicles; 'mount' was dropped as unsupported. A 'kart' value may fit the schema better if one is allowed.",
  "No coin vendor, quest, drop, event, or prize wheel source found in the pack or client text."
 ]}
