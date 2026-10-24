<!-- fleet job=citem-infer id=cn-stalwart-protector-breeches-pl-stalwart-protector-breeches-135805-v3 status=nothing_found turns=3 usd=0.0029 tokens(read,write,in,out)=[18432, 12645, 8, 2334] model=claude-haiku-5-5 -->
# {n}Stalwart Protector Breeches{pl="Stalwart Protector Breeches"}

{"item": {"name": "Stalwart Protector Breeches", "locale_id": 135805, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name locale 135805 is '{n}Stalwart Protector Breeches{pl=\"Stalwart Protector Breeches\"}'; slot 4, class 15, 34 variants across definition ids 46805-46816, model warrior_<race>_<gender>_legs_kneepadpants.adr", "source": "locale:135805; client definition in pack"},
  {"claim": "Client holds sibling Stalwart Protector item names: Hightops (135175), Gauntlets (135490), Pauldrons (135910), Tunic (135000), Helm (135560). These show the set exists, not where the breeches come from.", "source": "locale:135175, locale:135490, locale:135910, locale:135000, locale:135560"},
  {"claim": "Client has a forging recipe string 'Forging: Stalwart Protector Hammer' (386101) and recipe text for the Hammer (1581, 1603). The Blacksmith guide lists the Stalwart Protector Hammer source as Unknown. No breeches recipe was found.", "source": "locale:386101; locale:1581; repo:notes/Build Guides/Content/Jobs/Blacksmith.md:261"},
  {"claim": "Searches of the repo data folder for definition ids 46805-46816 and for locale 135805 returned no store row, and no stores.json row with purchase_price_coins 715 was found by the exact-format search. The 715 coin_store_prices value in the client definition is therefore not tied to any identified vendor row.", "source": "repo:prototype/osfr-tools/data (search, no matches)"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock row, quest reward, drop or event names the breeches. A wiki search for the Level 15 Stalwart tier returned no match, so that tier claim is dropped.", "source": "lookup over client, wiki, articles, video"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source is evidenced. The client definition's coin_store_prices [715] (definition ids 46805-46816) suggests a coin store price exists, but no stores.json item id, vendor, or stock row ties it to this item, so no vendor source is recorded. Needs the store row keyed to these definition ids.",
  "The 643-coin member price was computed (715 x 0.9) and is not recorded by any source; dropped.",
  "The Level 15 Warrior tier on the wiki Warrior page was not verified; dropped.",
  "No breeches recipe found; only the Stalwart Protector Hammer recipe exists in the client and repo.",
  "Retirement status unknown. Nothing in the pack says it was sold, retired, or never sold; do not infer from the absence of a wiki page.",
  "The first-pass tag (live yes, vendor) is a hint only; live is set to unsure."
 ]}
