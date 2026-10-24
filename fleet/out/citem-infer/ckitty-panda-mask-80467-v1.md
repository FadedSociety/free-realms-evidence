<!-- fleet job=citem-infer id=ckitty-panda-mask-80467-v1 status=done turns=8 usd=0.0065 tokens(read,write,in,out)=[94566, 26446, 18, 4505] model=claude-haiku-5-5 -->
# Kitty Panda Mask

{"item": {"name": "Kitty Panda Mask", "locale_id": 80467, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. Store row for item 25574 (category 6, tint group 3) lists 270 coins, member price 243, resale 27. The row shows a coin store price but does not name the vendor, and no vendor stock list in the repo names this mask.", "where": null, "price": "270 coins (member 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14113 (item 25574); the client definition's coin_store_prices [270]"},
  {"type": "promotion", "detail": "Valentine's Special: buy the Gizmo cat pet and get the Kitty Panda Outfit free. The outfit is the costume set this mask belongs to (the mask is locale:150639, 'The mask for the kitty panda costume.'). The text says Gizmo does not color but the outfit does.", "where": null, "price": "free with Gizmo purchase", "currency": null, "source": "locale:873579200 (\"Valentine's Special! Buy Gizmo and get the Kitty Panda Outfit free!\"); articles fact http://www.freerealms.com/article/detail.action?articleId=2521 (\"Gizmo's promo pet outfit was the Kitty Panda Outfit.\")"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Kitty Panda Mask' is locale:80467 (item). Its description locale:150285 reads 'This is a Kitty Panda Mask item.'", "source": "locale:80467; locale:150285"},
  {"claim": "Mask is one piece of the Kitty Panda costume set: the suit, paws, collar and mask each have their own client line ('The mask for the kitty panda costume.').", "source": "locale:150639; locale:150601; locale:150621; locale:150657"},
  {"claim": "Kitty Panda Outfit was Gizmo's promo pet outfit, a Valentine's Special bundled with buying Gizmo.", "source": "articles/facts.json (fact for articleId=2521, http://www.freerealms.com/article/detail.action?articleId=2521); locale:873579200"},
  {"claim": "Coin store row for the mask's item id 25574 (category 6, tint group 3) is priced 270 coins, member 243, resale 27. The client definition carries the same 270 coin price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14113"},
  {"claim": "Gizmo's own acquisition: SC Marketplace 400 SC (member 360 SC), per the archived wiki page, which does not mention the outfit bundle.", "source": "repo:prototype/osfr-tools/data/content/pets.json:10302 (wiki 'Gizmo', archived 2023-08-05)"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin vendor for store item 25574 is not named. The repo's vendor stock lists (Brent at Sanctuary, Pet Adoption Center) do not include the Kitty Panda mask. Needs a vendor check.",
  "Whether the 270-coin store row is a live sale or only the Valentine's bundle price is unresolved. No wiki page covers the mask, and the Gizmo bundle text does not give a price for the outfit.",
  "Retired status is unknown. The Valentine's promotion is dated, but no source states it was retired or when it ended.",
  "The client definition lists 12 definition ids (25574-25585) against 35 total definitions. Only the 12 listed ids were checked against stores.json; the other tint variants were not checked.",
  "A second locale name entry 'Kitty Panda Mask' appears at ids 1838591440 (ucdt) and 2986280013 (ugdt). These are not the 80467 item; they are probably the same item's other name fields and were not traced further.",
  "No wiki page, image or video frame names this mask. The evidence is the client text plus one articles fact."
 ]}
