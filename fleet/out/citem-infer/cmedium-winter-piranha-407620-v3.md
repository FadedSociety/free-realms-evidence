<!-- fleet job=citem-infer id=cmedium-winter-piranha-407620-v3 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[16272, 10392, 8, 2281] model=claude-haiku-5-5 -->
# Medium Winter Piranha

{"item": {"name": "Medium Winter Piranha", "locale_id": 407620, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Fishing catch: Winter Piranha, Medium size tier (fish minimum level 1). The Medium tier is a size of the Winter Piranha catch, not a separately named fish; its share of catches is 31 of 100 in the size weights (the Small/Medium/Large/Extra Large split is 52/31/14/3, with the size order inferred).", "where": "Wintery Basin (Snowhill)", "price": null, "currency": null, "source": "locale:410546 (Basin fish list includes Winter piranha); locale:410083 (\"Winter piranha can be caught in the Wintery Basin.\"); repo:notes/Build Guides/Content/Jobs/Fisherman.md:193 (Winter Piranha 1 at Basin); repo:prototype/osfr-tools/data/content/fishing.json winter_piranha (minimum_level 1, size_weights [52,31,14,3]); repo:notes/Build Guides/Content/Jobs/Fisherman.md:242 (sizes S M)"},
  {"type": "other", "detail": "Fishing catch: Winter Piranha, Medium size tier (level 1). Reached by boat per the repo notes.", "where": "Frostbitten Banks (Snowhill)", "price": null, "currency": null, "source": "locale:410545 (Banks fish list includes Winter piranha); repo:notes/Build Guides/Content/Jobs/Fisherman.md:192 (Winter Piranha 1; boat); repo:notes/Build Guides/Gameplay/Fishing.md:133"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client defines Medium Winter Piranha as name locale 407620 with no coin store price", "source": "client definition in pack; locale:407620"},
  {"claim": "Winter Piranha is catchable at level 1 at Wintery Basin and Frostbitten Banks", "source": "repo:notes/Build Guides/Gameplay/Fishing.md:132-133; repo:notes/Build Guides/Content/Jobs/Fisherman.md:192-193; repo:prototype/osfr-tools/data/content/fishing.json winter_piranha"},
  {"claim": "Spot text names the species only, not a size", "source": "locale:410545; locale:410546; locale:410083"},
  {"claim": "Winter Piranha has S and M size tiers in the Fisherman table; the Medium tier has a size weight of 31 of 100", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:242; repo:prototype/osfr-tools/data/content/fishing.json winter_piranha size_weights"},
  {"claim": "Winter Piranha takes the 16oz Steak lure's 10% bonus; the text names the species, not a size", "source": "locale:29778"},
  {"claim": "No fish-to-collection mapping is known, so no collection source is attributed", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:195"}
 ],
 "confidence": 0.6,
 "open": [
  "The Medium tier is a size of the species; no source shows a separate Medium-only catch. Level 1 and both spots are for the species (plain Winter Piranha, locale 99942).",
  "The size order (Small, Medium, Large, Extra Large) behind the four size weights is inferred, not read from a source.",
  "Per-size catch rates beyond the repo size weight are not confirmed by any in-game or wiki source.",
  "No collection source is attributed.",
  "Wiki page text for Wintery Basin and Frostbitten Banks was not retrievable in this pass; the spot evidence is client locale text and repo notes.",
  "Locale 410082 is Small-size text only and is not used as spot evidence. The Frostbitten Banks boat detail comes from the repo note only.",
  "Live status not checked; no retirement evidence found."
 ]}
