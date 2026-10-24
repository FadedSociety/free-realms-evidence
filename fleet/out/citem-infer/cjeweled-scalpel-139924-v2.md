<!-- fleet job=citem-infer id=cjeweled-scalpel-139924-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5453, 9358, 6, 1664] model=claude-haiku-5-5 -->
# Jeweled Scalpel

{"item": {"name": "Jeweled Scalpel", "locale_id": 139924, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin-store vendor (store category 207). The store row prices the item at 811 coins (member price 729). The stores.json record does not name the NPC. The wiki says the item was 'acquired only through trade', which contradicts a coin-vendor sale; treat this as unresolved.", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; sell price 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48174 (line 13224); verified in this pass. Wiki 'Jeweled Scalpel' page: 'can only be acquired through trade'"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Jeweled Scalpel is a level 5 Medic Blue Text weapon, Power 3, with Incision and Triage effects", "source": "wiki page: Jeweled Scalpel"},
  {"claim": "Wiki says the weapon 'can only be acquired through trade'", "source": "wiki page: Jeweled Scalpel (lookup, ns0)"},
  {"claim": "Wiki page is in Category:Retired Weapons", "source": "wiki page: Jeweled Scalpel (category list)"},
  {"claim": "Client name string for item 139924 is 'Jeweled Scalpel', in a set with Monarch and Jeweled/Gemstone weapons", "source": "locale:139924, locale:139919-139929"},
  {"claim": "Store record for item 48174: purchase 811 coins, member 729, sell 81; siblings 48172-48181 share the 811 price; 48160-48171 are 640", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13210-13230"},
  {"claim": "Wiki 'Blue Text weapon' and 'Medic' pages list Jeweled Scalpel / Jeweled [Scalpel] at Level 5", "source": "wiki pages: Blue Text weapon, Medic"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the stores.json coin price (811 coins) implies a coin-vendor sale, but the wiki says trade-only. Neither source names the vendor or zone. Until a coin-vendor page or player report confirms a sale, the vendor source is unverified.",
  "No retirement date is given. 'Retired' rests on the wiki's Retired Weapons category alone.",
  "No quest, drop, event, prize-wheel, or crafting source was found. No images or video frames name this item beyond the wiki file names.",
  "The 729-coin member price is from the store data, not a wiki sale price. No second wiki price was found.",
  "Live is set to 'no' from the Retired category, but the store row still exists in current data. The store row may be stale."
 ]}
