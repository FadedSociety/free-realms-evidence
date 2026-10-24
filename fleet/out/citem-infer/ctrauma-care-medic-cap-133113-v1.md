<!-- fleet job=citem-infer id=ctrauma-care-medic-cap-133113-v1 status=done turns=6 usd=0.0052 tokens(read,write,in,out)=[75238, 24241, 14, 2739] model=claude-haiku-5-5 -->
# Trauma Care Medic Cap

{"item": {"name": "Trauma Care Medic Cap", "locale_id": 133113, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Kimble (Medic gear merchant, NPC id 9500000791; 'sells exclusively [Medic] Job items')", "where": "Stillwater Crossing (near the warpstone)", "price": "627 coins (member price 564 coins, 10% member discount; sell-back 62 coins). Reference price from stores.json, not a captured NPC quote", "currency": "coins", "source": "wiki:Kimble (Sells section: 'Trauma Care Medic Cap'); repo:prototype/osfr-tools/data/content/stores.json item 76105 (purchase_price_coins 627); repo:prototype/osfr-tools/data/content/vendors.json Kimble item_ids includes 76105; repo:notes/Build Guides/Content/NPCs/NPCs - Stillwater Crossing.md row 66"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Trauma Care Medic Cap' is locale 133113, item name in the same Trauma Care Medic set as locale 133108-133115.", "source": "locale:133113"},
  {"claim": "Kimble's wiki Sells list includes Trauma Care Medic Cap (wiki page revision 2023-11-18), next to the rest of the Trauma Care Medic set (Backpack, Fatigues, Gloves, Boots, Shirt).", "source": "wiki:Kimble"},
  {"claim": "Store data gives item 76105 a coin purchase price of 627 (member 564, sell 62).", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76105"},
  {"claim": "Kimble's merchant listing was introduced 27 August 2013 (Stillwater Crossing merchants, Aug-Oct 2013 wave).", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Stillwater Crossing.md row 66 (cites wiki Kimble, Merchants)"},
  {"claim": "Client definition: slot 1, item class 7, one definition (76105), one model file military_<race>_<gender>_head_baseball.adr, no tint variants listed.", "source": "client definition in pack; locale:133113"}
 ],
 "confidence": 0.7,
 "open": [
  "The 627-coin price is a stores.json reference price, not a captured Kimble quote; the wiki page gives no price in the lookup text. Confirm against a live NPC quote if one exists.",
  "No wiki page exists for the cap itself; the Kimble wiki Sells list is the only named source. Kimble's wiki listing was last revised 2023-11-18; that suggests it was still sold then, but no retirement notice was found.",
  "No quest reward, drop, prize wheel, event or promotion source was found for this cap in the pack or repo.",
  "Client description is empty, so the item's own description text gives no extra detail.",
  "Sell price 62 coins is the store's sell-back value, not a second purchase price."
 ]}
