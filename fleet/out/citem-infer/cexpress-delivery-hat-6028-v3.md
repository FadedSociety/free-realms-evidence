<!-- fleet job=citem-infer id=cexpress-delivery-hat-6028-v3 status=nothing_found turns=2 usd=0.0019 tokens(read,write,in,out)=[6070, 7456, 6, 1762] model=claude-haiku-5-5 -->
# Express Delivery Hat

{"item": {"name": "Express Delivery Hat", "locale_id": 6028, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Express Delivery Hat' is locale 6028 (item). It is the only client text hit for the name; no wiki, article or video hit names it.", "source": "locale:6028; lookup client/wiki/articles/video for \"Express Delivery Hat\" OR \"Hasty Trot\" OR courier ballcap"},
  {"claim": "Its client cluster is the courier/delivery-themed set Hasty Trot Hat (6024), All-Star Postman Hat (6029), Amateur Postman Hat (6030), Breakneck Mailing Hat (6031), Speedy Sprint Hat (6032). Sibling Hasty Trot pieces (Shoes 143, Gloves 6015, Shorts 6045, Skirt 5989, Shirt 6005) are also client-only in the lookup; no source names them as sold or dropped.", "source": "locale:6024, 6028, 6029, 6030, 6031, 6032, 143, 6015, 6045, 5989, 6005"},
  {"claim": "stores.json line 516 is item_id 1757, category_id 101, tint_group 1, purchase 464 coins, member 417, sell 46. The file does not name the item or the shop, so this row is an id-only match to this hat and is not evidence of its acquisition.", "source": "repo:prototype/osfr-tools/data/content/stores.json:516"},
  {"claim": "stores.json lines 517 and 3590 (items 1759 and 13055, category 101) list 9453 coins, but the same 9453 price is shared by many unrelated item ids, so it does not identify this hat.", "source": "repo:prototype/osfr-tools/data/content/stores.json:517, 3590"},
  {"claim": "The store row source tags (L1, L2, L4, R2, T633, R1) show the listing data's origin only; they do not date a sale or a removal.", "source": "repo:prototype/osfr-tools/data/content/stores.json:516"}
 ],
 "confidence": 0.2,
 "open": [
  "No source names this hat as sold, dropped, rewarded or given at an event. The wiki, images, articles, video and vendor stock lookups are empty for it.",
  "Provisional, unconfirmed: stores.json item 1757 (category 101, tint 1) at 464 coins (member 417, sell 46). Matched by definition id only; not cited as a source. Needs a store or shop name from repo data, or a vendor/quest citation that names the hat.",
  "The 9453-coin rows (1759, 13055) are shared by many unrelated items and are not attributed to this hat.",
  "Shop name for category 101 is not in repo data, so 'Coin Shop' is not confirmed.",
  "Retired status, removal date and live status are unknown; no source dates the listing.",
  "Quest reward, enemy drop, event, prize wheel, crafting, collection and promotion sources were not found in any source that names the hat.",
  "Earlier 'Express Postman Hat' (item 76006, Tipper, 902 coins) is a different item and is not a source for this one.",
  "Wireable: false until a source names the hat."
 ]}
