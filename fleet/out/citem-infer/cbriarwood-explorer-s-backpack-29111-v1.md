<!-- fleet job=citem-infer id=cbriarwood-explorer-s-backpack-29111-v1 status=done turns=8 usd=0.0055 tokens(read,write,in,out)=[90796, 22348, 18, 3683] model=claude-haiku-5-5 -->
# Briarwood Explorer's Backpack

{"item": {"name": "Briarwood Explorer's Backpack", "locale_id": 29111, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, coin vendor not identified in the repo data (store row only; no vendor link for item 15280)", "where": "Coin store (stores.json category 106)", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15280 (line 3944: purchase_price_coins 270, member_price_coins 243, category_id 106, source_tags L1,L2,L4,R2,T633,R1)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines Briarwood Explorer's Backpack, locale 29111, definition 15280, slot 6 (shoulders/backpack model), one definition, no tints", "source": "locale:29111; client definition supplied in the pack"},
  {"claim": "Coin store row for item 15280 exists at 270 coins, member price 243 coins, sell price 27 coins, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15280 (line 3944)"},
  {"claim": "Sibling explorer backpacks (Seaside, Snowhill, Blackspore, Briarwood) sit together in the client text and the same store category; the Briarwood one appears in inventory frames", "source": "video:MzxfUBdIIGU/00032.jpg; locale:29103, 29085, 29108, 29164"},
  {"claim": "Blackspore Explorer's Backpack is obtained from a Blackspore Treasure Chest, which suggests the plain explorer backpacks come from area treasure chests as well; not confirmed for the Briarwood version", "source": "video:SdVAc6iTuK4/00000.jpg (Blackspore sibling only)"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor that sells item 15280 is not named in the repo (no vendor row or NPC link found); the store row alone is the price evidence.",
  "No wiki article covers this item; the wiki 'Briarwood [Explorer]' page is a collection (rewards: Adventurer Exp.), not this backpack, so it is not a source.",
  "Possible Briarwood Treasure Chest drop/reward by analogy with the Blackspore backpack; no Briarwood-specific evidence was found, so it is not listed as a source.",
  "Retired status not found in any source; the store row's live tags (L1, L2, L4, R2) suggest it was sold, but whether it is still sold is unverified.",
  "Elite Explorer Backpack of Briarwood (locale 419890) is a different item and was not covered here.",
  "The client description is empty, so no in-game description text is available."
 ]}
