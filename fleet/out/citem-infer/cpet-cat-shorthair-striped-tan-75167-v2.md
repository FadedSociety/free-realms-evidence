<!-- fleet job=citem-infer id=cpet-cat-shorthair-striped-tan-75167-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5401, 11257, 6, 2092] model=claude-haiku-5-5 -->
# Pet: Cat: Shorthair: striped_tan

{"item": {"name": "Pet: Cat: Shorthair: striped_tan", "locale_id": 75167, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor (store id and NPC not mapped; the store row has no vendor id). Not wireable until mapped.", "where": null, "price": "540 coins (legacy purchase price; member price 486; sell price 54). Unverified: no provenance note on this row, and the same legacy 540 was cleared as unstocked on sibling rows 24009, 24021 and 24022.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24017 (line 6894); client definition coin_store_prices 540"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 24017 is named 'Pet: Cat: Shorthair: striped_tan' (locale 75167), one definition, model cat_shorthair.adr", "source": "locale:75167; client definition in pack (name and existence only; model and tint not checked in client files)"},
  {"claim": "Store row 24017 carries legacy coin cost 540, member 486, sell 54, not no_sale, tint_group 1, with legacy source tags L1, L2, L4, R2, T633, R1 and no price_provenance note", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24017 (line 6894)"},
  {"claim": "Sibling rows 24009, 24021 and 24022 carry the same legacy 540 but have provenance saying no coin vendor stocks them; they were re-priced at 400, 225 and 225 Station Cash on the SC Marketplace (wiki Mr. Kitty, Mojo, Mittens). Row 24017 has no such note, so its 540 is unverified.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6886, 6898, 6899"},
  {"claim": "Sister cat pets 24003 to 24025 with the same 540 row share the legacy tags; no wiki page, article fact, video frame, quest, drop or event names item 24017 or any Shorthair cat tint", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6880-6902; lookup (wiki, articles, client) returned only locale:75158-75167 names"},
  {"claim": "Client name cluster locale:75158-75172 lists plain and striped and tuxedo Shorthair cat variants, so 24017 is one tint of a multi-variant pet set", "source": "locale:75158 to locale:75172"}
 ],
 "confidence": 0.25,
 "open": [
  "Vendor not identified: the stores.json store row has no vendor id, and no NPC vendor file was matched. The vendor source is therefore not wireable; a builder cannot place it until the store id is mapped to an NPC.",
  "The 540-coin price is a legacy store value with no provenance note. Sibling rows with the same value were shown to have no coin vendor, so 540 for 24017 may be a legacy cost, not a live price. Verify against a player source or wiki price before use.",
  "Live status is unsure. The row is not marked no_sale, but nothing confirms current sale. Retirement is unknown.",
  "Holiday, promotion, membership, quest, drop, or prize-wheel source: none evidenced in the pack; legacy tags do not say.",
  "The client definition's coin_store_prices value of 540 is cited as the coin price, but it matches the legacy store row and is not independent confirmation of a vendor sale.",
  "Critique accepted: the previous answer's 'live coin store entry' claim did not follow from the row, so it is withdrawn and live is set to unsure. The model and tint claims were not checked in client files."
 ]
}
