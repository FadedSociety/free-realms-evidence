<!-- fleet job=item-infer id=iluau-party-ticket-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[11648, 14954, 8, 2290] model=claude-haiku-5-5 -->
# Luau Party Ticket

{"item": {"name": "Luau Party Ticket", "locale_id": 5102398, "kind": "consumable"},
 "sources": [{"type": "vendor", "detail": "Tiger the Party Animal (client name id 2807361043); sells the ticket to everyone at the regular price, and to Members at a 10% discount", "where": "Blackspore Swamp, Sanctuary, Seaside (wiki also lists Snowhill among party zones in repo notes); only during Themed Community Event parties", "price": "200,000 coins regular; 180,000 coins for Members (10% discount, the second wiki price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Luau_Party_Ticket (rev 44838); wiki wikitext revision 10777-44838 (freerealms-wiki/wikitext/10777-44838-0a2d75af80e3.wiki line 2); wiki Tiger the Party Animal (Merchant as of August 27, 2013, sells Luau Party Tickets)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name exists in the client text table as a ticket item", "source": "locale:5102398 [item | Luau Party Ticket]; locale:5102399 'Purchasing this item will immediately begin a Luau Party for your current zone.'"},
  {"claim": "Tiger sells the ticket to everyone at the regular price of 200,000 coins and to Members at a 10% discount of 180,000 coins; Tiger is found in Blackspore Swamp, Sanctuary and Seaside", "source": "https://freerealms.fandom.com/wiki/Luau_Party_Ticket; freerealms-wiki/wikitext/10777-44838-0a2d75af80e3.wiki"},
  {"claim": "Tiger is a merchant as of August 27, 2013 and sells Luau Party Tickets", "source": "wiki Tiger the Party Animal (freerealms-wiki/wikitext/10677-49854-c7ae9e260318.wiki line 19)"},
  {"claim": "Luau is a summer community event lasting 20 minutes; purchasable Luaus also last 20 minutes", "source": "https://freerealms.fandom.com/wiki/Luau_Party_Ticket"},
  {"claim": "Repo's unresolved vendor list has Tiger's Luau Party Ticket stock claim with no matched item id or regional NPC key; the store frame in video has no seller or zone", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:72-93"},
  {"claim": "Repo notes say Tiger's Luau Party Ticket rows are poi_anchor and unspawned in the current build", "source": "repo:notes/Autopilot/F192.md:107-108"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status unsure: the wiki price and Tiger's merchant status date from August 2013; the repo notes say the Tiger rows are unspawned, so this is not confirmed live.",
  "Retired status not stated by the wiki; no retirement or unobtainable category was found in the pack.",
  "Tiger's vendor link is not resolved to an exact client item id or NPC id in the repo (vendors_unresolved.json:72-80), so the vendor source rests on wiki text and one video frame.",
  "The wiki price is in coins with no in-game currency label; the 200,000 / 180,000 pair is the wiki's own figures and was not checked against a client vendor record.",
  "Zone list: the wiki names Blackspore, Sanctuary and Seaside; repo notes also list Snowhill for Tiger, which the wiki page does not mention."
 ]}
