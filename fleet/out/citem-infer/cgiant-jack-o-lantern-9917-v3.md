<!-- fleet job=citem-infer id=cgiant-jack-o-lantern-9917-v3 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[19140, 14039, 8, 2699] model=claude-haiku-5-5 -->
# Giant Jack-O-Lantern

{"item": {"name": "Giant Jack-O-Lantern", "locale_id": 9917, "kind": "furniture"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing, seen in one store frame beside Parachutes, Broomstick and Giant Candy Corn. No event name or date is shown in the frame.", "where": "Station Cash Marketplace", "price": "630 station_cash (single unverified frame)", "currency": "station_cash", "source": "video:g7pncDFzIrw/00036.jpg; repo:data/content/stores.json item 79441 (no coin price; no_sale true; sc_price 349 reconstructed from wiki 'Jack-O-Lantern Ride', ride_id 13570, stores.json:17513)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Giant Jack-O-Lantern' is locale 9917, description locale 9918 'It makes for a spooktacular hut.', definition id 79441, class 172, slot 0, model ball_m_jackolantern.adr. It is a housing item.", "source": "locale:9917; locale:9918; notes/Autopilot/T452.md:123"},
  {"claim": "A store frame lists Giant Jack-O-Lantern at 630 station_cash in the Station Cash Marketplace, sorted by Default with no filters. The frame shows no event tie or date.", "source": "video:g7pncDFzIrw/00036.jpg"},
  {"claim": "Sanctuary StoreBundles entry for Id 79441 (Comment 'Giant Jack-O-Lantern', NameId 9917, DescriptionId 9918) has Price 500, CurrencyType 1, AltCurrencyPrice 1, StoreId 1, Status 1, LaunchTime 2011-04-06, ExpireTime 2090-01-01. CurrencyType 1 is not decoded, so the 500 figure is not confirmed as Station Cash. The 2090 expiry is a placeholder-style date and gives no end of sale.", "source": "refs: Sanctuary-main-20261019/src/Resources/StoreBundles.json:31893-31922"},
  {"claim": "Our store data gives item 79441 no coin price, no_sale true, and sc_price 349. That 349 is reconstructed from the wiki page 'Jack-O-Lantern Ride' (ride_id 13570), so it is tied to a ride, not this housing item. It conflicts with the housing class 172 and with the frame's 630 figure.", "source": "repo:data/content/stores.json:17513"},
  {"claim": "Big Jack-O-Lantern is a Members Only Coin Shop housing item from Super Spooktacular events. Coin Shop frames show Small 2250 coins and Big 4500 coins. Giant Jack-O-Lantern is not in those frames, so it is a different item.", "source": "wiki 'Big Jack-O-Lantern' (Category:Coin Shop, Category:Super Spooktacular); video:1TNyzyI62nc/00268.jpg; video:1TNyzyI62nc/00276.jpg"},
  {"claim": "Big and Small Jack-O-Lantern are Archer Prize Wheel rewards on the wiki pages for Werewolf Dance Practice and Vampire Dance Practice. Giant Jack-O-Lantern is not named on either list.", "source": "wiki 'Werewolf Dance Practice'; wiki 'Vampire Dance Practice'"},
  {"claim": "The Super Spooktacular event tie from the previous answer is removed. The wiki page does not name this item in its Marketplace week lists.", "source": "critique of previous answer"}
 ],
 "confidence": 0.3,
 "open": [
  "Price conflict: frame 630 station_cash (video:g7pncDFzIrw/00036.jpg), StoreBundles Price 500 with CurrencyType 1 and StoreId 1 (undecoded), and stores.json sc_price 349 (ride-based reconstruction, ride_id 13570). The correct price is unresolved.",
  "Identity check: stores.json maps 79441 to a Jack-O-Lantern Ride (ride_id 13570), while the client definition is housing class 172. Confirm that the Marketplace row is the housing item and not the ride.",
  "stores.json marks 79441 no_sale true, which conflicts with the Marketplace frame. Either the listing ended or the flag is stale.",
  "Retired status is unknown. The StoreBundles ExpireTime 2090-01-01 is a placeholder and gives no end date. Nothing in the pack dates the Marketplace listing.",
  "No vendor, quest, drop, crafting, or prize wheel source was found for this item. The Super Spooktacular link is unverified.",
  "Only one store frame supports the Marketplace sale. Confirm with a second frame or a dated listing."
 ]}
