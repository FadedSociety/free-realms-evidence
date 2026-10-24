<!-- fleet job=citem-infer id=cjunkyard-kart-hood-67411-v1 status=nothing_found turns=5 usd=0.0033 tokens(read,write,in,out)=[34045, 12515, 12, 2758] model=claude-haiku-5-5 -->
# Junkyard Kart Hood

{"item": {"name": "Junkyard Kart Hood", "locale_id": 67411, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 23798 is named 'Junkyard Kart Hood' (locale 67411) with description 'This item can be added to the Derby Junkyard Kart Parts Collection' (locale 132481 / 2972895795 in the ui table), one definition, no models, no coin store price.", "source": "locale:67411; locale:132481; repo:data search for 23798 returned no store rows"},
  {"claim": "The collection it feeds is 'Derby Junkyard Kart Parts' (ugdt 2889387358) with collection text 'A collection of junkyard kart parts. Anything to get back into the derby works for me.' (locale 67702).", "source": "locale:67702; en_us_data.dat ugdt 2889387358 (client locale table)"},
  {"claim": "Sibling items in the same client block (locale 67406-67415): 110 Crystal Fuel, 1000 Crystal Fuel, Junkyard Engine, Wheels, Shocks, Steering Wheel, Spoiler, Kart Door, Roll Cage. The block is the Derby Junkyard parts set; the cluster is client-only.", "source": "client_cluster in pack; locale:67406-67415"},
  {"claim": "Repo kart-part class data (ItemClasses rows 75/76, 'Demo Derby Kart' Type 10) has parts with Chassis, Engine, Steering categories and rank gate 1, but no row for this item id was matched to the Junkyard name.", "source": "repo:notes/Research/Pieces/041 Racer and derby progression.md:44-47"},
  {"claim": "Wiki, article and video lookups for 'Junkyard Kart' / 'Derby Junkyard Kart Parts' returned no pages, facts or frames. The only junk-yard wiki content is the Sunstone Valley quest 'Junk or Bust' (Scrap Yard Junk), which is a different item set.", "source": "lookup (wiki, articles, video, client) returned no matches; repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md:223"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source found. The client text only says the part can be added to the Derby Junkyard Kart Parts Collection; no wiki page, vendor stock, quest, drop, event or prize-wheel link names it.",
  "The collection's own reward or unlock (how a player completes 'Derby Junkyard Kart Parts', and whether parts are awarded individually) is unknown.",
  "No coin store price exists in the client definition or repo stores, so no vendor or coin-shop sale is evidenced.",
  "Live status is unverified. The pack's first-pass 'live: yes' is a hint only; the client still ships the definition, but no retirement note was found.",
  "Item kind: set to 'collection' per the pack; it is a physical kart part that feeds a collection, so 'other' would also fit.",
  "The Kart Driver vendor Clack (Briarwood) and Willow Slamdash (Wilds) stock kart parts but their stock and prices were not seen, so they are not linked here.",
  "Item definition 23798 does not appear in the repo data, so this item's stat/class row was not confirmed against server data."
 ]}
