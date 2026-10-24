<!-- fleet job=citem-infer id=cshared-energy-potion-2910-v2 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[30649, 13390, 10, 2356] model=claude-haiku-5-5 -->
# Shared Energy Potion

{"item": {"name": "Shared Energy Potion", "locale_id": 2910, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Five-pack 'Shared Energy Potion (5)' (bundle 2283, name locale:4484, description locale:4485), containing 5 x GameItemId 643 mapped to MarketingItemId 49998 (the single potion, client definition 49998). Wiki says the pack is bought from the SC Shop.", "where": "SC Shop (Station Cash Marketplace)", "price": "200 SC for five potions (wiki only; see open)", "currency": "station_cash", "source": "wiki page 'Shared Energy Potion' (categories SC Supplies, Supplies, Potions); repo-independent bundle: refs Sanctuary-main-20261019/src/Resources/StoreBundles.json lines 963-992 (bundle 2283, Price 1, AltCurrencyPrice 1, CurrencyType 1, Quantity 5, MarketingItemId 49998); locale:4484; locale:4485"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 49998 is 'Shared Energy Potion', NameId 2910, DescriptionId 2913, type 1, icon 772.", "source": "refs Sanctuary-main-20261019/src/Resources/ClientItemDefinitions.json lines 998818-998824; locale:2910; locale:2913"},
  {"claim": "A Station Cash bundle 'Shared Energy Potion (5)' (Id 2283) lists 5 units of MarketingItemId 49998, so the five-pack is sold as a store product.", "source": "refs Sanctuary-main-20261019/src/Resources/StoreBundles.json lines 963-992; locale:4484; locale:4485 ('This 5-pack of Shared Energy Potions ... More Energy means more special attacks!')"},
  {"claim": "Wiki: level 1 potion usable in any job, Cannot Sell / Cannot Trade; restores 16 energy/second for 3 seconds and instantly restores 2 energy; acquired from the SC Shop as a five-pack for 200 SC.", "source": "wiki page 'Shared Energy Potion'"},
  {"claim": "Newer client text: restores 50 energy to you and all group members over 5 seconds.", "source": "locale:422946; locale:422947"},
  {"claim": "Repo (our code/data) has no store or definition entry for 49998; the earlier 'no matches' note only covers our repo, not the Sanctuary reference.", "source": "repo search for '49998' and 'Shared Energy' (no matches)"},
  {"claim": "Sister potions Shared Health Potion (2909/2912) and Shared Replenishment Potion (2911/2914) share the same name block and set text.", "source": "locale:2909-2914 (client cluster)"}
 ],
 "confidence": 0.5,
 "open": [
  "The 200 SC price is wiki-only. The Sanctuary bundle 2283 records Price 1 and AltCurrencyPrice 1 with CurrencyType 1, which does not match 200; the currency-type code is not decoded here, so the price is unverified.",
  "Whether the bundle price applies to the five-pack or the single potion is not established; the wiki's 200 SC refers to the five-pack.",
  "Effect conflict: wiki says 16 energy/s for 3 s (plus 2 instant); newer client text locale:422947 says 50 energy to the group over 5 s. Confirm which build the rebuild targets.",
  "No live-date, retirement or delisting source found. The bundle has ExpireTime 2040-08-15 and status 1, but that is a store field, not proof of current sale. Retired and live status remain unconfirmed.",
  "No coin vendor, quest reward, enemy drop, event, or crafting source found in the pack or repo.",
  "Single-potion sale (apart from the five-pack) is not shown by any source."
 ]}
