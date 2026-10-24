<!-- fleet job=citem-infer id=cninja-s-power-shard-of-the-armadillo-131162-v6 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[32908, 17931, 10, 3339] model=claude-haiku-5-5 -->
# Ninja's Power Shard of the Armadillo

{"item": {"name": "Ninja's Power Shard of the Armadillo", "locale_id": 131162, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale row for item 75418, seller not identified (row has no vendor id; category 121 is a shared price tier, not a vendor). Row block 75413-75418 carries the identical price, so the price is shared and the link to this shard rests on client definition 75418.", "where": null, "price": "2435 coins purchase; 2191 coins for members (10% discount); 243 coins resell", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15302 (item 75418, category 121); repo:prototype/osfr-tools/data/content/stores.json:15297-15301 (items 75413-75417, same price); client definition coin_store_prices [2435]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for this item is locale 131162, \"Ninja's Power Shard of the Armadillo\", in the Ninja Power Shard family (Vitality I-V, Precision, Second Wind, Entangling, the Vampire, and so on).", "source": "locale:131162; locale:131157-131167"},
  {"claim": "Store row for item 75418 reads purchase 2435, member 2191 (10% discount), resell 243, no_sale false. The same row values appear on items 75413-75417.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15297-15302"},
  {"claim": "A quoted wiki search for \"Power Shard of the Armadillo\" returns only the Archer variant page and its tooltip image. No page, tooltip, or video frame names the Ninja Armadillo shard.", "source": "wiki page:ns0 \"Archer's Power Shard of the Armadillo\"; wiki page:ns6 \"File:Archer's Power Shard of the Armadillo.jpg\""},
  {"claim": "The Archer Armadillo shard is Archer-only and comes from the Wraiths of Wrath! prize wheel. It shows resell 243, which matches the shared store block. This is sibling evidence only and does not identify the Ninja source.", "source": "wiki page:ns6 \"File:Archer's Power Shard of the Armadillo.jpg\"; image:item_tooltip Archer's Power Shard of the Armadillo.jpg"},
  {"claim": "Other Ninja shards appear on wiki pages: Ninja's Power Shard of Vitality III and V, Regeneration IV, V and II are listed as Coin Shop items (prices blank in the extract). Ninja's Power Shard of the Vampire and of Entangling appear in Ninja Prize Wheel lists (Mushroom Mania!, Mudshell). The Armadillo variant is not named on any of these pages.", "source": "wiki page:ns0 \"Ninja's Power Shard of Vitality III\", \"Ninja's Power Shard of Vitality V\", \"Ninja's Power Shard of Regeneration IV\"; wiki page:ns0 \"Mushroom Mania!\", \"Mudshell\""}
 ],
 "confidence": 0.3,
 "open": [
  "Wireable: false. The coin-store row (item 75418, category 121) has no vendor id, and the seller is not decoded. Do not wire a vendor or shelf from it until the vendor id or the meaning of category 121 is decoded.",
  "The price 2435/2191/243 is shared by items 75413-75418, so it is not specific to this shard. Only the client definition (definition_ids 75418, coin_store_prices [2435]) links it to the Ninja Armadillo name.",
  "Possible but unconfirmed source: the Ninja Prize Wheel. Sibling Ninja shards (Vampire, Entangling) are listed on Ninja Prize Wheel lists on wiki pages, but no wiki page names the Ninja Armadillo on any wheel. Check those wheel pages for the Armadillo entry.",
  "The earlier Wraiths of Wrath! prize-wheel source is the Archer variant only. It is not applied to the Ninja item.",
  "Coin Shop sale status is unconfirmed: the Ninja Vitality and Regeneration shards are on Coin Shop pages, but the Armadillo is not. Retirement status is unknown; no retirement evidence was found either way.",
  "No quest, drop, crafting, collection, or event source was found. Blackspore Swamp and Briarwood job-merchant rotations were not checked.",
  "The earlier 'no Ninja page' claim came from a search that errored. This pass re-ran the quoted search: the Ninja variant still has no page, but the search was not exhaustive across every Ninja Coin Shop and prize-wheel page."
 ]}
