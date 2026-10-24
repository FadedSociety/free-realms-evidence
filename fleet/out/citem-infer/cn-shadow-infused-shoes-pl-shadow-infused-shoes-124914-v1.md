<!-- fleet job=citem-infer id=cn-shadow-infused-shoes-pl-shadow-infused-shoes-124914-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[28569, 15563, 10, 2581] model=claude-haiku-5-5 -->
# {n}Shadow Infused Shoes{pl="Shadow Infused Shoes"}

# Shadow Infused Shoes: source research

I could not confirm any real source for these shoes. The item is live in the client, but the pack gives no source evidence, so every source goes to `open`.

```json
{"item": {"name": "Shadow Infused Shoes", "locale_id": 124914, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 124914 'Shadow Infused Shoes'; it is a clothing item (slot 5, class 8) with 32 definitions and 2 model files (caster_<race>_f_feet_maryjanewstalking.adr, caster_<race>_m_feet_pointed.adr).", "source": "locale:124914; client definition in pack"},
  {"claim": "Its cluster is the Shadow Infused set: Long Cloak (124913), Fez (124916), Skirt (124917), Slacks (124918). The Shadow Infused Wand (locale 19546) is also in the same naming family.", "source": "locale:124913, locale:124916, locale:124917, locale:124918, locale:19546"},
  {"claim": "The Shadow Infused Wand wiki page says it is a Green Text weapon that can only be acquired through trade. Green Text weapons were retired as dungeon drops on 2009-12-14, and any that cannot be made by Blacksmiths are only obtainable by trade.", "source": "wiki page 'Shadow Infused Wand'; wiki Category:Green Text (ns14)"},
  {"claim": "The coin prices in the pack (828 and 9453) match purchase prices in the store data, but no store row references this item's definition ids (44915-44946). The price match is not a link to this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 65, 277, 542 (828) and 80-82 (9453); search for 44915 and related ids returned no store row"},
  {"claim": "The wiki's 'Memorial Caverns' page quotes the Gloam Council text, and the Game Update 128 news mentions [Gloam] achievement rewards. Neither names these shoes.", "source": "wiki page 'Memorial Caverns'; wiki Template:News (Game Update 128)"}
 ],
 "confidence": 0.2,
 "open": [
  "No wiki page, article, video frame or vendor row names Shadow Infused Shoes. Its real acquisition path is unknown.",
  "The 828 and 9453 coin prices are not confirmed for this item. Both values appear on many stores.json rows for other items, and no row links to definition ids 44915-44946. Do not assign these prices to the shoes without a row that carries one of those ids.",
  "The first-pass guess of 'vendor' is unsupported. The Shadow Infused Wand is documented as trade-only green text, so the shoes may be a trade or Green Text era item. That is only an inference from the shared name family.",
  "Check whether the Shadow Infused set (Long Cloak, Fez, Skirt, Slacks, Shoes) was a trade-only green-text set, or whether any of these pieces was a Gloam achievement, drop or event reward.",
  "Live status is unsure. Nothing in the pack shows it was retired, and the wand's Green Text retirement suggests the set may be unobtainable now, but this is unverified."
 ]}
```
