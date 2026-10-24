<!-- fleet job=citem-infer id=cfrightening-finisher-cleats-6256-v1 status=done turns=11 usd=0.0110 tokens(read,write,in,out)=[266314, 43868, 24, 5715] model=claude-haiku-5-5 -->
# Frightening Finisher Cleats

{"item": {"name": "Frightening Finisher Cleats", "locale_id": 6256, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fred Futbol, the 'Soccer Star Gear' vendor (stock is Soccer Star gear as a category; this exact cleat is not confirmed in his stock)", "where": "Snowhill, Snowhill Soccer Field (next to the Left Side Soccer Gate)", "price": null, "currency": null, "source": "video X35ewgMjcAM/00036 (title 'Soccer Star Gear'); video WjpJl2U5OK0/00016; repo:notes/Build Guides/Content/Jobs/Soccer Star.md lines 42 and 220 (Frightening Finisher base set, cleats name id 182613075); repo:prototype/osfr-tools/data/content/npcs/snowhill.json:16192-16228 (npc 9000000092, vendor_stock 'Soccer Star gear.')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Name 'Frightening Finisher Cleats' is locale 6256; the same set has base cleats name id 182613075 and Elite Black / Elite Pink cleats ids 1040149241 and 594499849, all in the Soccer Star clothing family (Frightening Finisher set #16-18).", "source": "locale:6256; repo:notes/Build Guides/Content/Jobs/Soccer Star.md:220-222"},
  {"claim": "The set belongs to the Soccer Star job's clothing line (eight set families, three tiers each); the client cluster 6251-6261 is the same Soccer Star gear batch (Star Sweeper Bandana, Wild Winger Jersey, Silent Screen Shin Guards, Durable Defender Shorts, Kitty Island Lei, Derby Wheeler decals).", "source": "repo:notes/Build Guides/Content/Jobs/Soccer Star.md:199-228; locale:6251-6261"},
  {"claim": "Fred Futbol is the Soccer Star Gear vendor at Snowhill Soccer Field, seen in video; stock and prices were not read in the video.", "source": "video X35ewgMjcAM/00036; repo:notes/Build Guides/Content/Jobs/Soccer Star.md:42"},
  {"claim": "The Soccer Star Gear vendor's item-level stock is unresolved in our data (no item-level stock evidence).", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:305-330"},
  {"claim": "Coin store prices 750 and 1076 are in the client definition, but I could not link them to any cleat item in repo stores.json: item ids 2196 and 61500-61512 are not present as store item_ids (only 61505 and 61506, priced 9453, appear, and the 1076 rows are other item ids in category 101-106).", "source": "repo:prototype/osfr-tools/data/content/stores.json (searched item_id 2196, 61500-61512)"},
  {"claim": "No wiki page, article, or video frame names this item directly; the wiki has no Soccer Star gear list.", "source": "lookup client/wiki/articles/video: only client locale 403935/403936 (Elite Pink/Black variants) returned; repo:notes/Build Guides/Content/Jobs/Soccer Star.md:17"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin store prices 750 and 1076 from the client definition are not tied to a store row. The stores.json search found no row for definition ids 2196 or 61500-61512. Confirm which store lists these and at what price; the pack's 1076 may be the Snowhill Stopper/other set price, not this one.",
  "Price at Fred Futbol is unknown; no video or wiki frame shows the cleat price or stock list.",
  "The pack's claim that this is a plain vendor sale is a first-pass guess only; the vendor link rests on the set family and the 'Soccer Star Gear' vendor title, not on a seen listing for these cleats.",
  "The Elite Black and Elite Pink versions have their own names (1040149241, 594499849) and may have different sources or prices; not checked separately.",
  "Whether this set is still obtainable on the live game, or was retired with the Soccer Star content, is not documented in any source here. Also the Soccer Star 'Frightening Finisher' set sold via the Soccer Star quest line or as a member reward is unverified.",
  "Quest or membership sources for the set: none found. The Soccer Star quest rewards are unknown (repo:notes/Build Guides/Content/Jobs/Soccer Star.md line 32).",
  "Definitions count 35 and includes tints/race variants (definition ids 2196, 61500-61512 are only a sample from the pack); the full list was not verified."
 ]}
