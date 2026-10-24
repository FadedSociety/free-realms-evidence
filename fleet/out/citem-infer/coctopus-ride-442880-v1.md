<!-- fleet job=citem-infer id=coctopus-ride-442880-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[3681, 7964, 6, 2241] model=claude-haiku-5-5 -->
# Octopus Ride

{"item": {"name": "Octopus Ride", "locale_id": 442880, "kind": "mount"},
 "sources": [
  {"type": "membership", "detail": "July 2013 Monthly Membership Pack (members-only ride, the 'Octopus')", "where": null, "price": null, "currency": null, "source": "wiki: Octopus (page:ns0 'Octopus': 'a Membership exclusive ride that was distributed throughout the month of July in 2013 being apart of July's Monthly Membership Pack'); wiki: Rides (Octopus row: 'Received from July's Monthly Membership Pack'); wiki: Monthly Member Pack Items (Octopus listed under July 2013)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client item 79444 is named 'Octopus Ride' (locale 442880), description 'Travel the world and the seven seas on your Octopus Ride!' (locale 442881), model octopus_m_basic.adr, single definition, no variants", "source": "locale:442880; locale:442881; repo:prototype/osfr-tools/data/content/mounts.json (entry for ride 13573 / item 79444)"},
  {"claim": "Wiki page 'Octopus' calls it a members-only ride distributed in July 2013 via the Monthly Membership Pack, and places it in Category:Unobtainable", "source": "wiki page:ns0 'Octopus'"},
  {"claim": "Wiki 'Rides' table lists Octopus as an Exotic ride 'Received from July's Monthly Membership Pack' (Available/N/A column)", "source": "wiki page:ns0 'Rides'"},
  {"claim": "Monthly Member Pack Items page lists the Octopus ride in the July 2013 membership pack", "source": "wiki page:ns0 'Monthly Member Pack Items'"},
  {"claim": "Clocktopus (Clockwork Octopus ride) is a different item, earned from the Clockwork Mystery Chest with a member-only opportunity; it is not the Octopus Ride definition 79444 and is not counted as a source here", "source": "locale:944; article http://www.freerealms.com:80/article/detail.action?articleId=2721"},
  {"claim": "Store data has no coin price for item 79444 (purchase_price_coins null, no_sale true)", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79444"}
 ],
 "confidence": 0.8,
 "open": [
  "Membership pack price and exact pack price in coins or Station Cash not found in the sources; the stores.json row shows no coin price, and the T452 note mentions an unverified '449' figure that is not tied to this item.",
  "The first-pass tag 'live: yes, source marketplace' is rejected: the wiki says membership-pack only and unobtainable; no Station Cash Marketplace listing was found.",
  "The wiki's Monthly Member Pack table layout is ambiguous about which row Octopus sits in; the Octopus page's explicit 'July 2013' wording was used.",
  "Whether the ride could be re-obtained after July 2013 (for example a later pack or reward) is not documented in these sources.",
  "Client cluster lines (Legendary Seaside Coin, Rare Metal Vein, Terrifying mask, Robgoblin wizard item) are neighbouring items and were not used as evidence for this ride."
 ]}
