<!-- fleet job=citem-infer id=cninja-s-power-shard-of-the-armadillo-131162-v5 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[18574, 13486, 8, 2444] model=claude-haiku-5-5 -->
# Ninja's Power Shard of the Armadillo

{"item": {"name": "Ninja's Power Shard of the Armadillo", "locale_id": 131162, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin-store sale row (item_id 75418, category 121). No vendor id in the row and category 121 is not decoded, so the seller is unknown. Listed only because the client definition carries coin_store_prices [2435]; treat as an unconfirmed price record, not a confirmed vendor.", "where": null, "price": "2435 coins purchase; 2191 coins member price (10% member discount); 243 coins resell", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15302 (item_id 75418, category_id 121); identical block at stores.json:15297-15301 (items 75413-75417)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for this item is locale 131162, \"Ninja's Power Shard of the Armadillo\", in the Ninja Power Shard family (Vitality I-V, Precision, Second Wind, Entangling, the Vampire).", "source": "locale:131162; locale:131157-131167"},
  {"claim": "Store row for item 75418 reads purchase 2435, member 2191 (10% discount), resell 243, category 121, no vendor id, no_sale false. Source tags L1, L2, L4, R2, T633, R1 are undecoded and are the same on every row in the block, so they do not separate live from retired.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15302"},
  {"claim": "The row block 75413-75418 is shared; the rows do not name which definition is which shard, so the link from item 75418 to locale 131162 rests on the client definition (definition_ids 75418), not on the store row itself.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15297-15302; client definition 75418"},
  {"claim": "Wiki search finds no page or tooltip for the Ninja variant. The only Armadillo shard page is the Archer variant, which is acquired from the Wraiths of Wrath! prize wheel and is level 1, Archer-only. That is sibling evidence only and is not applied to the Ninja item.", "source": "wiki page:ns0 \"Archer's Power Shard of the Armadillo\"; wiki page:ns6 \"File:Archer's Power Shard of the Armadillo.jpg\""},
  {"claim": "Archer tooltip shows resell 243, matching the shared store block. This is a sibling match, not evidence for the Ninja shard.", "source": "image:item_tooltip Archer's Power Shard of the Armadillo.jpg"}
 ],
 "confidence": 0.25,
 "open": [
  "No wiki page, tooltip, article, or video frame names the Ninja-specific Armadillo shard. Its acquisition channel and live/retired status are unconfirmed.",
  "The vendor entry rests only on the unlabelled store row (item 75418, category 121, no vendor id). Do not wire it as an acquisition until the vendor id or the category 121 meaning is decoded. The price is confirmed as a store row, not as a named seller.",
  "Possible unverified source: the Wraiths of Wrath! prize wheel, the documented source for the Archer sibling. Not confirmed for the Ninja variant; the wiki search returned no Ninja entry for it. Check the wheel's contents directly.",
  "Coin-store sale status for the Ninja variant is not confirmed beyond the row; no retirement evidence was found either way.",
  "No quest, drop, crafting, or collection source found. Blackspore Swamp and Briarwood job-merchant rotations were not checked."
 ]}
