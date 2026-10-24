<!-- fleet job=citem-infer id=cstar-sweeper-shin-guards-404840-v1 status=nothing_found turns=6 usd=0.0043 tokens(read,write,in,out)=[47088, 17579, 14, 3211] model=claude-haiku-5-5 -->
# Star Sweeper Shin Guards

{"item": {"name": "Star Sweeper Shin Guards", "locale_id": 404840, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Star Sweeper Shin Guards' is locale 404840; the Elite Pink and Elite Black variants are locale 404845 and 404846.", "source": "locale:404840; locale:404845; locale:404846"},
  {"claim": "The Star Sweeper set is a Soccer Star clothing set (base, Elite Black, Elite Pink), and the Shin Guards slot id for the base set is 2728943977; Elite Black 550136885; Elite Pink 149481519.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:208-210 (row 4-6, [client])"},
  {"claim": "A sibling Soccer Star shin guard, Monster Midfielder Shin Guards, is sold in the Station Cash Marketplace at 199 SC (179 SC for members). This is a different item and is not a source for Star Sweeper.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:243; wiki page 'Monster Midfielder Shin Guards' (Category:SC Marketplace)"},
  {"claim": "Repo store data does not tie the 750 and 1076 coin prices to these definitions. Every stores.json row at 750 coins has a different item_id (for example 4826, 4827, 16039, 61080). No row exists for the definition ids 62410-62423 at those prices. Ids 62415 and 62416 are in stores.json at 9453 coins, which is not a match for this set.", "source": "repo:prototype/osfr-tools/data/content/stores.json (item_id search for 62410-62423 and purchase_price_coins 750/1076)"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor, Coin Shop, Station Cash Marketplace, quest, drop, event, or prize-wheel source is evidenced for Star Sweeper Shin Guards. No wiki page, article fact, or video frame names it.",
  "The client-definition coin prices (750 and 1076) do not match any stores.json row for definition ids 62410-62423. The stores.json rows at 750 belong to other items. Resolve whether the pack's price came from a mismatched id before using it as a vendor source.",
  "Definition ids 62410-62423 (34 definitions in total) have no mapping in the repo to the 404840/404845/404846 names, so the Shin Guards tints/races are not separated.",
  "The Soccer Star notes list this set as client-only ([client]). Its live status and any retirement date are unknown.",
  "Elite Black and Elite Pink variants have the same unknowns: no source, no price evidence."
 ]}
