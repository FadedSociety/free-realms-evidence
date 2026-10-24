<!-- fleet job=citem-infer id=ctank-wrecker-141870-v1 status=nothing_found turns=4 usd=0.0039 tokens(read,write,in,out)=[25529, 17383, 10, 2942] model=claude-haiku-5-5 -->
# Tank Wrecker

{"item": {"name": "Tank Wrecker", "locale_id": 141870, "kind": "mount"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Tank Wrecker is a Demolition Derby kart. Its name follows the derby-kart pattern (Wrecker/Crusher), and the client has per-kart part entries for it: Chassis (locale:114652 'The chassis for the Tank Wrecker.'), Engine (locale:403192), Turbo (locale:403193), Mod (locale:403194), Special Mod (locale:403195), plus Tank Wrecker Engine/Turbo/Steering Mod/Shock Absorbers names (locale:403137-403140, 114838).", "source": "notes/Build Guides/Content/Jobs/Demolition Derby Driver.md, 'Derby karts' section (client-derived; lists Tank Wrecker among 18 client-only names with no wiki page)"},
  {"claim": "The wiki's Derby Karts category covers only five karts (Barbed Crusher, Bear Wrecker, Crazy Crusher, Cutlass Wrecker, Sea Serpent Wrecker), all sold in the Station Cash Marketplace (Cutlass Wrecker 700 Station Cash, 630 for members). Tank Wrecker has no wiki page, and lookup of 'Tank Wrecker' and 'Derby Kart' returned no wiki or article hit for it.", "source": "wiki: Cutlass Wrecker; Bear Wrecker; Crazy Crusher; Sea Serpent Wrecker; Barbed Crusher; wiki Items page (Derby Karts list)"},
  {"claim": "Client description for the kart is 'Built tough and to turn fast' (locale:141871).", "source": "locale:141871"},
  {"claim": "No coin store price in the client definition (coin_store_prices empty), so no coin vendor sale is evidenced.", "source": "client definition, definition_ids 48315"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The wiki lists the Station Cash Marketplace as the sale source for five other derby karts, but Tank Wrecker is not on those pages. Whether it is sold in the SC Marketplace, a Coin Shop, or a derby vendor is unknown.",
  "No price evidence. Station Cash or coin prices are unknown.",
  "The first-pass tag (live: yes, source guess: unknown) is a hint only. Liveness is unconfirmed: it is client-defined but not on the wiki.",
  "Kind: 'mount' is a best fit for a rideable kart. The wiki files derby karts under Karts, not Mounts, so the kind may be 'other'.",
  "The client's Tank Wrecker part entries (chassis, engine, turbo, mods) imply a build of parts. Their sources are also unknown and are not part of this item's pack."
 ]}
