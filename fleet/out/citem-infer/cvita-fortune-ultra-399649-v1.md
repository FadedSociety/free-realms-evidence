<!-- fleet job=citem-infer id=cvita-fortune-ultra-399649-v1 status=nothing_found turns=4 usd=0.0033 tokens(read,write,in,out)=[24556, 15180, 10, 2330] model=claude-haiku-5-5 -->
# Vita-Fortune Ultra

{"item": {"name": "Vita-Fortune Ultra", "locale_id": 399649, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 59787 exists: slot 206, class 73, description 'These pet vitamins greatly improve your pet's chances of finding treasure.' (locale:399652), no models, no coin store price.", "source": "evidence pack; locale:399649; locale:399652"},
  {"claim": "Same item family: Vita-Fortune Basic (locale:399647, def 59785, 'slightly improve') and Vita-Fortune Plus (locale:399648, 'moderately improve') share the same structure. Tiers are Basic < Plus < Ultra by potency.", "source": "locale:399647; locale:399648; locale:399650; locale:399651; repo:quest-lines/citem-packs.json:412610-412655"},
  {"claim": "Item name appears in the locale tables and the Legacy and Lxzxrus ClientItemDefinitions.json as a comment only (no source, price or drop data).", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1108511; Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:1108511"},
  {"claim": "No repo store, vendor, quest, or recipe entry references definition 59787 or the name 'Vita-Fortune Ultra'. No wiki page, article, or video frame names it. Locale 17767 'Pet Vitamins' and 426703 'Pet vitamins' (spin food) are different text and do not establish a source for this item.", "source": "repo search for 59787 / 399649 / Vita-Fortune: no matches; lookup wiki/articles/video: no matches"},
  {"claim": "The first-pass guess 'marketplace' is not supported by any evidence found; it is a hint only.", "source": "evidence pack jev_first_pass"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. No coin vendor, Station Cash Marketplace, Coin Shop, quest, drop, event, prize wheel, crafting, or promotion evidence names Vita-Fortune Ultra.",
  "Price unknown: client definition has no coin store price and no wiki price exists.",
  "Live status unknown: the first pass says live, but nothing in the sources confirms it. The item is a client definition with a Seaside-zone text cluster, which suggests a Seaside-era pet item, possibly retired, but this is unverified.",
  "Next step: check the wiki for pet consumables (for example a 'Pet Vitamins' or Seaside pet supplies page) and the Basic/Plus siblings for any shared source, then check the Station Cash and Coin Shop lists by definition id 59787 and its siblings 59785 and the Plus definition."
 ]}
