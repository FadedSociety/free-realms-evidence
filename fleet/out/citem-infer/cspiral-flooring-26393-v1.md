<!-- fleet job=citem-infer id=cspiral-flooring-26393-v1 status=nothing_found turns=10 usd=0.0085 tokens(read,write,in,out)=[168023, 34175, 22, 5032] model=claude-haiku-5-5 -->
# Spiral Flooring

{"item": {"name": "Spiral Flooring", "locale_id": 26393, "kind": "furniture"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 27964: name locale 26393 'Spiral Flooring', description locale 26394 'A spiral pattern for your floor.', Type 17, Class 1, CategoryId 51, IsTintable true, Cost 5, ResellValue 1, MemberDiscount 10, TintAlias dyetint, TextureAlias customization. One definition, no models, no coin store price.", "source": "Sanctuary/src/Resources/ClientItemDefinitions.json:575876-575896"},
  {"claim": "Sibling flooring set in the client text: Polkadot, Small Polkadot, Rainbow, Spiral, Star, Tiger Flooring (locale 26387-26398), all housing floor textures.", "source": "locale:26388, locale:26393, locale:26394, locale:26395, locale:26397 (client lookup)"},
  {"claim": "Rainbow Flooring (game item 5176, marketing item 27963, name locale 26391) is a 2011-12-15 store bundle entry: CurrencyType 1, Price 1, CategoryGroupId 141, Status 1, expires 2040. Its client definition is a different id from Spiral.", "source": "Sanctuary/src/Resources/StoreBundles.json:23597-23625"},
  {"claim": "Other 2011 floor bundles (Fast Food 5170, Fruity 5171, Pirate 5172, Wilds Cobblestone 5173, Seaside Sand 5169-range) exist in the same file. No bundle entry names Spiral, Star, Tiger or Polkadot Flooring, and game item 5174 is absent from the file.", "source": "Sanctuary/src/Resources/StoreBundles.json:23443-23600 (search for NameId 26393/26395/26397 and GameItemId 5174 returns no bundle)"},
  {"claim": "The wiki Items page lists Rainbow [Flooring] among the Floors but does not list Spiral Flooring.", "source": "wiki page Items (lookup, Floors section)"},
  {"claim": "No wiki page, video frame, article fact, vendor stock or quest/drop answer names Spiral Flooring.", "source": "lookup over client, wiki, articles, video; search over repo and refs"}
 ],
 "confidence": 0.25,
 "open": [
  "No source for how Spiral Flooring is obtained. The only store-data hit is Rainbow Flooring's 2011 bundle (CurrencyType 1, Price 1, currency unit not stated in the file); Spiral has no bundle entry, so no marketplace or Coin Shop source can be cited for it.",
  "The client's 'Cost 5' and 'ResellValue 1' are item-definition fields, not a coin store price; they are not used as a source.",
  "Whether Spiral was sold in the Station Cash Marketplace, given as a promotion, or was never obtainable is unknown. Wiki category 'SC Marketplace' or a wiki page for the set would settle it.",
  "The first-pass tag (live yes, source unknown) is a hint only; live status is left unsure.",
  "Locale 26390 is a duplicate-text Small Polkadot entry with the Polkadot description and is not Spiral's."
 ]}
