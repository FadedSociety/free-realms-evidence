<!-- fleet job=citem-infer id=cblacksmith-s-ring-of-talent-ii-132066-v1 status=done turns=5 usd=0.0035 tokens(read,write,in,out)=[37608, 14267, 12, 2669] model=claude-haiku-5-5 -->
# Blacksmith's Ring of Talent II

{"item": {"name": "Blacksmith's Ring of Talent II", "locale_id": 132066, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Seppa (human woman merchant, Blacksmith gear; wiki Seppa page, Sells section)", "where": "Dartmoor Quarry, Northern Wilds", "price": "806 coins (reference purchase price; 725 coins with member discount; 80 coins sell-back)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Seppa (Sells, revision 2025-05-31); repo:prototype/osfr-tools/data/content/vendors.json item 75620 (stock_source wiki Seppa); repo:data/content/stores.json item 75620 (purchase_price_coins 806)"},
  {"type": "vendor", "detail": "Same wiki Blacksmith vendor list also lists the sibling Blacksmith Power Shard of Talent II / Tongs of Talent II (not this item's source; context only)", "where": "Dartmoor Quarry, Northern Wilds", "price": null, "currency": null, "source": "notes/Build Guides/Content/Jobs/Blacksmith.md:190 (Seppa row, wiki)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name string for item 75620 is 'Blacksmith's Ring of Talent II' (locale 132066), in a tier cluster with Ring/Necklace of Talent and Timing I-IV", "source": "locale:132066"},
  {"claim": "Wiki Seppa page lists Blacksmith's Ring of Talent II in its Sells section; Seppa is at Dartmoor Quarry", "source": "https://freerealms.fandom.com/wiki/Seppa; notes/Build Guides/Content/NPCs/NPCs - Wilds.md:58"},
  {"claim": "Store reference price 806 coins, member price 725 coins, sell 80 coins for item 75620", "source": "repo:data/content/stores.json item 75620"},
  {"claim": "Blacksmith Ring of Talent II is a vendor item in the vendor data with item_name_id 132066 mapped by exact locale match", "source": "repo:prototype/osfr-tools/data/content/vendors.json (item 75620 entry)"}
 ],
 "confidence": 0.7,
 "open": [
  "The 806 / 725 / 80 coin prices are reconstructed from the Legacy reference Cost and MemberDiscount values, not a captured NPC quote (stores.json price_provenance kind 'reconstructed'; vendors.json price_basis says 'no captured retail NPC quote'). The wiki page gave no price in this pack. Treat the price as unverified.",
  "The wiki Seppa Sells list was not re-read directly in this pack; the vendor link relies on the repo's recorded wiki stock_source.",
  "No retirement date found. Whether Seppa still sells it in the live game is unconfirmed; the wiki revision is 2025.",
  "Kind is set to clothing from the first-pass guess and slot 8 / class 14; the client shows no model files and no description, so the exact item category (accessory vs. tool-enhancer) is unconfirmed.",
  "No quest, drop, event, crafting or collection source was found for this item in the pack.",
  "No critiques were carried in the pack."
 ]}
