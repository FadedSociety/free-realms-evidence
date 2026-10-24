<!-- fleet job=citem-infer id=cstar-flow-jackhammer-384382-v1 status=nothing_found turns=5 usd=0.0036 tokens(read,write,in,out)=[38065, 14069, 12, 2892] model=claude-haiku-5-5 -->
# Star Flow Jackhammer

{"item": {"name": "Star Flow Jackhammer", "locale_id": 384382, "kind": "tool"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name and description: 'Star Flow Jackhammer', a miner tool that increases stars earned when equipped (definition 49602, slot 7, class 37, model tool_ar_ag_weapon_minijackhammer.adr).", "source": "locale:384382; locale:150380"},
  {"claim": "Client text for the name is flagged not_live: unused weapon variant with no quest context. It sits in a 10-item Coin Flow / Star Flow weapon cluster (locale:384377 to 384387) that has no quest or vendor context in the pack.", "source": "locale:384377-384387 (client lookup FLAG field)"},
  {"claim": "Store price 3522 is the value listed in the client definition, but repo:prototype/osfr-tools/data/content/stores.json has many entries at purchase_price_coins 3522 (e.g. item_id 4575, 4756, 6791) and none is linked to definition 49602 or to this item's name. Price match alone is not a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:857 and others (no item 49602 link found)"},
  {"claim": "Our notes say 'Star Flow Jackhammer' and 'Coin Flow Jackhammer' raise stars or coins earned (codes/IDs 2136155588, 2112534083), but give no vendor, price or source for it, and the Jackhammer wiki-based entry (Marketplace, 275 Station Cash, 247 for members) is for the plain Jackhammer, not this variant.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:305"},
  {"claim": "No wiki article, article fact, or video frame names Star Flow Jackhammer. The wiki index has only a 'Star Flow Saw' and 'Star Flow Megablade' title entry (hash-only correction records), and no 'Star Flow Jackhammer' title.", "source": "refs: freerealms-wiki/wikitext-newline-correction.json:12020; lookup (wiki, articles, video) returned no matches"},
  {"claim": "No coin vendor stocks it in the pack, and no quest reward, enemy drop, event, or crafting answer mentions it.", "source": "vendor_stock and mentioned_by_other_answers are empty in the evidence pack"}
 ],
 "confidence": 0.2,
 "open": [
  "No source for how players got Star Flow Jackhammer. The first-pass guess 'vendor' is a hint only and has no evidence behind it.",
  "The 3522 coin price in the client definition does not link to a stores.json entry for definition 49602. Check whether a store row uses this definition id (not found by search for 49602).",
  "The client flags the item not_live (unused weapon variant). Confirm with a live-era source (wiki page, screenshot, or store dump) before treating it as obtainable. The 'live' field is left unsure.",
  "Retirement status is unknown. No source gives a release or retirement date.",
  "Check whether the Miner.md claim about star-raising Jackhammers (codes 2136155588, 2112534083) refers to this item. It is unsourced in our notes, so it is not used as evidence here."
 ]}
