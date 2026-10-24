<!-- fleet job=citem-infer id=cchatty-t-shirt-2802-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5550, 7492, 6, 1455] model=claude-haiku-5-5 -->
# Chatty T-Shirt

{"item": {"name": "Chatty T-Shirt", "locale_id": 2802, "kind": "clothing"},
 "sources": [
  {"type": "promotion", "detail": "Redeemed with code F7KPG5A in the in-game redemption menu (freestyle jobs Chest clothing item)", "where": null, "price": null, "currency": null, "source": "wiki page 'Chatty T-Shirt' (https://freerealms.fandom.com/wiki/Chatty_T-Shirt); wiki file page 'Chatty t-shirt.jpg' ('[Chatty T-shirt] code item'); image:item_tooltip Chatty t-shirt.jpg"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item is a freestyle jobs Chest slot clothing item acquired by entering code F7KPG5A in the redemption menu; Cannot Sell, Cannot Trade", "source": "wiki page 'Chatty T-Shirt'"},
  {"claim": "Tooltip shows Required: Freestyle Jobs, Cannot Sell, Cannot Trade (resell value 27 shown, but tooltip also says Cannot Sell)", "source": "image:item_tooltip Chatty t-shirt.jpg"},
  {"claim": "Client name locale 2802 'Chatty T-Shirt'; locale 385538 'This is a Chatty T-Shirt.'", "source": "locale:2802, locale:385538"},
  {"claim": "Store data row for item 398 exists (category 103, purchase 270 coins, member 243, sell 27, no_sale false), but it names no vendor, zone or NPC and conflicts with the wiki's Cannot Sell; not used as a source", "source": "repo:prototype/osfr-tools/data/content/stores.json line 192"},
  {"claim": "Same category-103 coin price of 270 is shared by unrelated items (391, 394, 399 in the same file), so the price row does not identify a Chatty-specific vendor", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 190-193"},
  {"claim": "Chatty Baseball Cap cluster (locale 2804, 2806, 2807) is a name match only and is not used as evidence of a shared promotion", "source": "locale:2804, locale:2806, locale:2807"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor source removed: the only coin evidence is an unnamed stores.json row (item 398, 270 coins) with no vendor, zone or NPC, and its no_sale:false flag contradicts the wiki and tooltip 'Cannot Sell'. Verify in-game before listing any coin vendor.",
  "Whether code F7KPG5A is still redeemable, its start/end dates, and the promotion's name are not stated in any source; live status and retirement remain unknown.",
  "No article or forum source for the code's run was found in the pack."
 ]}
