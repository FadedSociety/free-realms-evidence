<!-- fleet job=citem-infer id=cmine-lamp-147963-v1 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[15731, 8838, 10, 2142] model=claude-haiku-5-5 -->
# Mine Lamp

{"item": {"name": "Mine Lamp", "locale_id": 147963, "kind": "furniture"},
 "sources": [{"type": "vendor", "detail": "Unnamed coin vendor (coin store row only; no NPC or store name in our data)", "where": null, "price": "50 coins (member price 45 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 18134 (category_id 56, tint_group_id 2, purchase_price_coins 50, sell_price_coins 5)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name 'Mine Lamp' is locale 147963, item text with no description; definition 18134 uses model hsg_mine_lamp_01.adr, slot 0, class 0", "source": "locale:147963"},
  {"claim": "Store data lists item 18134 with a 50-coin purchase price, 45 for members, sell price 5 coins, not marked no_sale, and source tags L1, L2, L4, R2, T633, R1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 18134"},
  {"claim": "The same model file appears as scenery NPC spawns in the Fabled Realms zone script (non-item world objects), which is not a purchase source", "source": "repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:70668 and :70690"},
  {"claim": "Neighboring cluster items (Jug Lamp, Mausoleums, Briarwood Hedges, Giant Toilet Bowl) are part of one decoration set; Giant Toilet Bowl and Basic Swimming Pool are SC Marketplace items, but that does not confirm the Mine Lamp's channel", "source": "repo:prototype/osfr-tools/data/content/stores.json items 18135, 18136"}],
 "confidence": 0.4,
 "open": ["No wiki page, article, image or video frame names the Mine Lamp, so the vendor is not identified. Need the NPC/store that sells store category 56 tint 2 coin items in the same batch (ids 18125-18134).",
  "Status is unclear: the store row exists and is not no_sale, but the Legacy source tags (L1, L2, L4, R2, T633, R1) are not decoded here, so retirement cannot be confirmed.",
  "Client description is empty, so the item's Sunstone/Fabled theme cannot be confirmed from text.",
  "The jev first-pass 'vendor' guess is consistent with the coin price but was not used as evidence.",
  "The video 'Sunstone Street [Lamp]' frame is a different item (resell 50, cannot trade) and was not matched to the Mine Lamp."]}
