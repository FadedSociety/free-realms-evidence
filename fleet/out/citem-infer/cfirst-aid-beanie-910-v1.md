<!-- fleet job=citem-infer id=cfirst-aid-beanie-910-v1 status=done turns=8 usd=0.0075 tokens(read,write,in,out)=[126445, 29877, 18, 4990] model=claude-haiku-5-5 -->
# First Aid Beanie

{"item": {"name": "First Aid Beanie", "locale_id": 910, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Legacy coin store row for definition 2242 (First Aid Beanie, tint group 1, category 101 clothing); the same price is on definition 18770 (tint group 2). The store row names no vendor, so the specific vendor or shop is not identified.", "where": "coin store (category 101, clothing)", "price": "291 coins (member price 261 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2242 (line 651) and item 18770 (line 4591); client definition Cost 291 at repo/FreeRealms-Legacy ClientItemDefinitions.json line 42725 (Comment 'First Aid Beanie', Id 2242, NameId 910)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'First Aid Beanie' is locale 910, item class 7, slot 1, model military_<race>_<gender>_head_beanie.adr, and it has 14 definitions (12 listed ids plus 2 unlisted).", "source": "locale:910; client definition pack"},
  {"claim": "Definition 2242 has Cost 291 and a 10% member discount; the Legacy coin store carries it at 291 coins (member 261), sell-back 29 coins.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2242 (line 651)"},
  {"claim": "Definition 18770 (tint group 2) is also sold at 291 coins in the same category.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 18770 (line 4591)"},
  {"claim": "The 10-coin price in coin_store_prices does not belong to this beanie's listed ids; stores.json rows at 10 coins are items 404 and 2192 (category 101), which are not in the 12 listed ids. Their names are not confirmed in the pack.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 195 and 636"},
  {"claim": "The client's Medic-set names sit together: First Aid Gloves/Pants/Beanie, Elite Pink First Aid Beanie (912), Elite Black First Aid Beanie (32521), Grief Relief Beanie (908), Grief Relief Pants (913).", "source": "locale:905-915; locale 32521 via lookup"},
  {"claim": "The wiki's Medic job vendor Shephard (Medic Job Center, Sanctuary) sells only Medic job items, but the sells list shown names Stable Condition Medic items, not First Aid Beanie.", "source": "wiki page 'Shephard'"},
  {"claim": "The Medic job's Grief Relief set is a level-3 Medic reward per the Medic wiki page. The Grief Relief Hammer wiki page says it can only be acquired through trade. That is a different set from First Aid.", "source": "wiki pages 'Medic' and 'Grief Relief Hammer'"}
 ],
 "confidence": 0.4,
 "open": [
  "No vendor, wiki page or video names the First Aid Beanie. The coin store row is the only source, and it does not say which vendor or shop sells it. The 'Coin Shop' or a Medic job vendor is plausible but unconfirmed.",
  "Whether the 291-coin price was live or only a Legacy store row is unknown. No retirement date was found, so retired is null and live is unsure.",
  "The first-pass tag's source_guess 'vendor' is not confirmed. Its price evidence supports a coin-store sale, not a named vendor.",
  "The 10-coin coin_store_prices value does not match any listed id; the two unlisted definitions (and items 404, 2192) should be checked.",
  "The item's name is also used on Elite Pink and Elite Black versions. Those variants' sources were not checked and may differ."
 ]}
