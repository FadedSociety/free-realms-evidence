<!-- fleet job=citem-infer id=cvine-noodles-1225-v3 status=done turns=4 usd=0.0027 tokens(read,write,in,out)=[23917, 9846, 10, 2506] model=claude-haiku-5-5 -->
# Vine Noodles

{"item": {"name": "Vine Noodles", "locale_id": 1225, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash bundle 'Vine Noodles' (bundle Id 2267, NameId 1225, DescriptionId 3149), entry grants GameItemId 627 x3 with MarketingItemId 4066 (matches client definition 4066); CategoryGroupId 42, StoreId 1, SkuId 2, DiscountType 306", "where": "Station Cash marketplace (store 1)", "price": null, "currency": null, "source": "repo:Sanctuary-main-20261019/src/Resources/StoreBundles.json:873-902 (the file also exists under refs as Sanctuary-main-20261019; Sanctuary, Lxzxrus and Legacy copies carry the same MarketingItemId 4066 and NameId 1225 at lines 884/888)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 4066 is named 'Vine Noodles' (locale:1225); description: eating it turns the player into a vine golem wolf for thirty minutes", "source": "locale:1225; pack client_definition"},
  {"claim": "StoreBundles Id 2267 has Comment 'Vine Noodles', NameId 1225, Entries Quantity 3, GameItemId 627, MarketingItemId 4066, LaunchTime 2009-04-22, ExpireTime 2040-08-15, StoreId 1", "source": "repo:Sanctuary-main-20261019/src/Resources/StoreBundles.json:873-902"},
  {"claim": "Bundle MarketingItemId 4066 is a direct link to this item; GameItemId 627 is the granted item, not the sold item's identity. Nothing in the pack or the client shows item 627 as Vine Noodles", "source": "repo:Sanctuary-main-20261019/src/Resources/StoreBundles.json:884"},
  {"claim": "Bundle Price 1, AltCurrencyPrice 1, CurrencyType 1 are undecoded placeholders; no Station Cash price is verified", "source": "repo:Sanctuary-main-20261019/src/Resources/StoreBundles.json:891-893"},
  {"claim": "Wiki Items list includes '[Vine] [Noodles]' among food entries; it sits above the ' Members Only ' heading in the list, so it is not shown under that heading", "source": "wiki page:ns0 Items"},
  {"claim": "Repo coin store stores.json line 303 lists item_id 627 (category 104, purchase_price_coins 270). Whether this id is the same id space as the bundle GameItemId is unresolved, so it is not attributed to this item", "source": "repo:prototype/osfr-tools/data/content/stores.json:303"},
  {"claim": "No stores.json coin entry for item 4066; the client cost field is not a coin store price", "source": "repo:prototype/osfr-tools/data/content/stores.json; pack client_definition"}
 ],
 "confidence": 0.35,
 "open": [
  "Price and currency for the Station Cash bundle are unknown (Price 1 / CurrencyType 1 undecoded). Do not record a price or treat it as Station Cash-priced until decoded.",
  "Conflict: stores.json:303 item_id 627 at 270 coins vs bundle GameItemId 627. Confirm the id space before attributing any coin price; 270 is not this item's price.",
  "Client definition for item 627 was not found to carry NameId 1225, so the bundle's grant is not verified as Vine Noodles itself. The bundle's MarketingItemId 4066 is the stronger link.",
  "Membership status is unknown. The Items list order does not place Vine Noodles under 'Members Only'; do not assert a members-only sale.",
  "No coin vendor, quest reward, enemy drop, event, prize wheel, crafting or collection source found for 4066 or 'Vine Noodles'. The first-pass 'vendor' guess has no stock row.",
  "The 2040 ExpireTime is a data value, not proof of current availability. No retirement notice found; retired null, live unsure.",
  "No wiki article, images, article facts or video for this item; only the Items list entry."
 ],
 "wireable": false
}
