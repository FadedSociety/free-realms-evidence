<!-- fleet job=citem-infer id=ckitty-leather-collar-110517-v1 status=done turns=5 usd=0.0037 tokens(read,write,in,out)=[32966, 15558, 12, 2919] model=claude-haiku-5-5 -->
# Kitty Leather Collar

{"item": {"name": "Kitty Leather Collar", "locale_id": 110517, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Brent (NPC merchant, Sells section), sells pet clothing; listed as 'Kitty Leather Collar'. Variant not pinned to a single item id: the wiki name matches 37 catalogue definitions.", "where": "Sanctuary Pet Adoption Center (near the Sanctuary Warpstone)", "price": "270 coins (store data for ids 34708-34742 family)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brent (rev 2013-11-15); repo:prototype/osfr-tools/data/content/vendors_unresolved.json:4826-4879; repo:prototype/osfr-tools/data/content/stores.json:11278-11312 (category 6, purchase_price_coins 270, member price 243)"},
  {"type": "vendor", "detail": "Brent (NPC merchant), cheaper variant of the same name", "where": "Sanctuary Pet Adoption Center", "price": "150 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16357 item 77023 (category 6, purchase_price_coins 150, member price 135); candidate id 77023 listed in vendors_unresolved.json:4864"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Kitty Leather Collar' is locale 110517, item class 61, slot 6, model pet_cat_<descriptor>_shoulders_collarwtag.adr, 36 definitions", "source": "locale:110517; client definition supplied in pack"},
  {"claim": "Brent's wiki page lists 'Kitty Leather Collar' under Sells, at the Sanctuary Pet Adoption Center by the Sanctuary Warpstone", "source": "https://freerealms.fandom.com/wiki/Brent"},
  {"claim": "Store data prices item 34708 and its tint family 34709-34742 at 270 coins (member 243)", "source": "repo:prototype/osfr-tools/data/content/stores.json:11278"},
  {"claim": "Store data prices item 77023 at 150 coins (member 135)", "source": "repo:prototype/osfr-tools/data/content/stores.json:16357"},
  {"claim": "Wiki name match is ambiguous across 37 catalogue ids (34708-34742 plus 77023), so the wiki listing alone does not pin the variant", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:4826-4879 (status ambiguous_item_id)"},
  {"claim": "Brent's Sells list also includes Kitty Pirate Collar, Kitty Pirate Vest and Kitty Pirate Peg Leg, so this is one pet-clothing vendor stock group", "source": "https://freerealms.fandom.com/wiki/Brent; lookup wiki results"}
 ],
 "confidence": 0.7,
 "open": [
  "Which of the 37 candidate ids is the variant Brent sells, and whether the 150-coin (77023) and 270-coin (34708 family) prices are two separate vendor items or one item at two times. The wiki gives no price, so the price is store data only.",
  "No wiki price, date or retirement note found for Brent's Kitty Leather Collar; retired status is unknown. The Brent listing is from a 2013-11-15 revision.",
  "The pack's 'description' is empty and no quest, drop, event or promotion source was found in the supplied evidence.",
  "The client definitions count is 36 but the candidate id list has 37 entries; the 77023 id is outside the 34708-34742 range, which may be a separate catalogue entry."
 ]}
