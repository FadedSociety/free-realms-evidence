<!-- fleet job=citem-infer id=cwizard-s-ring-of-regeneration-v-131253-v1 status=done turns=5 usd=0.0035 tokens(read,write,in,out)=[28618, 12569, 12, 3257] model=claude-haiku-5-5 -->
# Wizard's Ring of Regeneration V

{"item": {"name": "Wizard's Ring of Regeneration V", "locale_id": 131253, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "[Wizard] Prize Wheel (Wizard class prize wheel; the ring appears in its item list alongside Battle Item Mystery Pack and Wizard Power Shard of Regeneration V)", "where": "Chugawump, Dark Spore Depths, Mudshell and other zone pages list the wheel", "price": null, "currency": null, "source": "wiki page 'Chugawump!' (item list under [Wizard] Prize Wheel); wiki page 'Dark Spore Depths'; wiki page 'Mudshell'"},
  {"type": "vendor", "detail": "Coin store sale listed in the client/store data at 2152 coins (member price 1936); no vendor NPC identified in the pack", "where": null, "price": "2152 coins (member price 1936 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75509 (line 17379). Caveat: price_provenance kind is 'reconstructed' from the Legacy reference (no captured retail NPC quote), so this price is unverified"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name is locale 131253 \"Wizard's Ring of Regeneration V\", part of the Regeneration ring set I-V (locale 131249-131253), next to Bark Skin necklaces", "source": "locale:131253 and locale:131249-131258"},
  {"claim": "Client definition 75509 has one definition, slot 8 and class 8; coin store price 2152 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75509"},
  {"claim": "Wiki prize-wheel item lists name the Wizard's Ring of [Regeneration] V under the [Wizard] Prize Wheel on several zone pages", "source": "wiki page 'Chugawump!', 'Dark Spore Depths', 'Mudshell'"},
  {"claim": "Lower-tier Wizard rings (II, III, IV) appear on the same [Wizard] Prize Wheel lists, so V is part of the same wheel set", "source": "wiki pages 'Fleetfoot Ninja!', 'Nettleseed Nibblers!', 'Moldy Shamblers!', 'Vale of the Ancients'"},
  {"claim": "Store-data sell price is 215 coins (one tenth of purchase), also reconstructed", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75509"}
 ],
 "confidence": 0.5,
 "open": [
  "The 2152-coin price is 'reconstructed' from the Legacy reference, not a captured retail quote. Treat as unverified until a real coin-vendor sale is found.",
  "No coin vendor NPC or store was identified for this item; the store row carries only source tags (R118, R2, T633, R1) without a vendor name.",
  "The wiki prize-wheel lists are not clearly tied to a specific wheel price or spin odds; the wheel is the only confirmed non-store source.",
  "Retirement status is unknown; no source says it was retired or unobtainable later.",
  "Kind is set to clothing because the item is an equippable accessory (slot 8, class 8); the pack gave no item-class detail beyond that.",
  "No article facts, video frames, or description text exist for this item; the client description is empty."
 ]}
