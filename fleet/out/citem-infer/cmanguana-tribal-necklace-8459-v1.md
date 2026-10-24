<!-- fleet job=citem-infer id=cmanguana-tribal-necklace-8459-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[3289, 11125, 6, 2301] model=claude-haiku-5-5 -->
# Manguana Tribal Necklace

{"item": {"name": "Manguana Tribal Necklace", "locale_id": 8459, "kind": "other"},
 "sources": [
  {"type": "drop", "detail": "Sandscale Scavenger (chance on defeat; listed in the wiki's Drops list, alongside Coins, Blast Spheres, Flabbergast Spheres, Cloth Wraps)", "where": "Sunstone Valley", "price": null, "currency": null, "source": "wiki:Sandscale Scavenger (cached wiki page, Drops section names Manguana Tribal Necklace; also locale:2200625134 'Manguana Tribal Necklace' ugdt line and locale:2200018944 'Sandscale Scavenger' in the same block)"},
  {"type": "drop", "detail": "Sandscale Magus (chance on defeat; Drops list shows [Manguana] [Tribal] [Necklace])", "where": "Sunstone Valley", "price": null, "currency": null, "source": "wiki:Sandscale Magus"},
  {"type": "drop", "detail": "Sandspear, boss (chance on defeat; Drops list shows [Manguana] [Tribal] [Necklace])", "where": "Sunstone Valley", "price": null, "currency": null, "source": "wiki:Sandspear"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is client text locale:8459 'Manguana Tribal Necklace'; the client has no model, no description and no coin store price for it (definition 18172, slot 0, class 0).", "source": "locale:8459 and client definition pack"},
  {"claim": "It is a quest-collection and crafting material, not a finished equipment piece: the Sunstone Valley Skullz quest asks you to collect Tin Ore and Manguana Tribal Necklaces in the Manguana Region.", "source": "locale:439866 (quest_dialog Sunstone Valley Skullz); locale:1062618949 'Collect Tin Ore, Manguana Tribal Necklaces and defeat Skullz Brawlers.'; locale:4090742671 'Collect Manguana Tribal Necklaces from the Manguana in Sunstone Valley.'"},
  {"claim": "It is a crafting ingredient for Motorsmith Boots (Sunstone Valley Red quest) and for the Manguana Statue furniture (10 needed).", "source": "locale:439717 (Sunstone Valley Red quest dialog); wiki:Manguana Statue"},
  {"claim": "Enemy drop chance from Manguana NPCs in Sunstone Valley; the Sandscale Scavenger wiki page lists it under Drops.", "source": "wiki:Sandscale Scavenger"},
  {"claim": "No vendor, coin shop, marketplace or prize-wheel source was found for this item.", "source": "vendor_stock empty in pack; no coin store price in client definition"}
 ],
 "confidence": 0.6,
 "open": [
  "Drop sources rest on wiki drop lists only. The pack's critique says no client drop table line was found; I did not find one in the repo either, so drop rates and whether the drops are live are unverified.",
  "The Sandscale Scavenger wiki text was cached in two forms; one lists the necklace as a bracketed link under Drops and the other names it. Treat the drop as wiki-sourced.",
  "No dates or retirement evidence: the live status is unsure, and retired is unknown.",
  "Item kind is 'other' (quest/crafting material), not clothing, despite slot 0 and class 0 in the client definition.",
  "Drop chance percentages were not given by any source."
 ]}
