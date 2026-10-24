<!-- fleet job=citem-infer id=cdoggy-dragon-amulet-64434-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6080, 10659, 6, 2419] model=claude-haiku-5-5 -->
# Doggy Dragon Amulet

{"item": {"name": "Doggy Dragon Amulet", "locale_id": 64434, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale in store category 6 (the vendor/NPC is not named in our data; price row only)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell price 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 8816 (line 2459, purchase_price_coins 270, no_sale false); item 8817 (line 2460) and 8818-8819 (lines 2461-2462) identical; 8820-8826 same price and no_sale false"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Doggy Dragon Amulet' (locale 64434); the item line reads 'This is a Doggy Dragon Amulet item.' (locale 150239).", "source": "locale:64434; locale:150239"},
  {"claim": "Set membership confirmed: 'The amulet for the doggy dragon costume.' (locale 150593), with sister pieces 'The shirt for the doggy dragon costume.' (150578), 'The claws for the doggy dragon costume.' (150582), 'The mask for the doggy dragon costume.' (150587). A set outfit 'Doggy Dragon Outfit' exists as locale 72306 (no store row checked).", "source": "locale:150593; locale:150578; locale:150582; locale:150587; locale:72306"},
  {"claim": "Store rows for item ids 8816 through 8826 are category 6, 270 coins purchase, 243 member price (10% member discount), 27 sell, no_sale false. Item 8827 is no_sale true with no sell price, so it is not a live sale row.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2459-2470"},
  {"claim": "The rows 8797-8815 (immediately before the amulet block) carry the same category and price, but nothing in the evidence ties those ids to the amulet; they are not counted as this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2440-2458"},
  {"claim": "Searching client, wiki, articles and video for 'doggy dragon' returned only client text lines; no wiki page, article, video frame, quest, drop, event or prize-wheel source names this item.", "source": "lookup over client, wiki, articles, video"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor not identified: category 6 store rows show a coin price but no NPC or store page. Do not wire a named NPC until one is found.",
  "Kind: the first-pass guess 'pet' is not supported; the client class is 31, slot 6, model pet_dog_<descriptor>_shoulders_necklacecoin, and the text calls it part of a costume. Recorded as clothing (worn costume piece); confirm before the rebuild relies on the kind field.",
  "Live status is unsure: the store row (no_sale false) is the only evidence; no wiki or video confirms the sale and no retirement evidence was found.",
  "Only ids 8816-8826 are confirmed as priced at 270 coins with no_sale false; 8827 is no_sale. The 36-definition block was not checked beyond these rows, and tint variants may differ.",
  "Store tags (L1, L2, L4, R2, T633, R1) are undecoded.",
  "Doggy Dragon Outfit (locale 72306) has no store row checked; whether the amulet is sold on its own or only with the outfit is unknown.",
  "No quest, drop, event, or prize-wheel source found."
 ]}
