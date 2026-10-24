<!-- fleet job=citem-infer id=ccallahan-s-infernal-necklace-86710-v2 status=nothing_found turns=4 usd=0.0033 tokens(read,write,in,out)=[30039, 14047, 10, 2409] model=claude-haiku-5-5 -->
# Callahan's Infernal Necklace

{"item": {"name": "Callahan's Infernal Necklace", "locale_id": 86710, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name exists: locale:86710 \"Callahan's Infernal Necklace\" (definition 22719, slot 9, class 43, no coin store price, no model files, no description).", "source": "locale:86710; client_definition in evidence pack"},
  {"claim": "The name is one of a large generic 'X Infernal Necklace' series (e.g. Dull, Rascal, Intern, Sneak, Grunt, Sage Infernal Necklace at locale 86524-86569; Hardwood, Granite, Metallic, Jeweled Infernal Necklace at locale 69679-69707). The Callahan's group is wider than the pack listed: locale 86709-86718 also includes Callahan's Ethereal, Unearthly and Cosmic Necklace. No source text ties the series to a promotion, vendor, quest, or drop.", "source": "lookup client 'Infernal Necklace' and 'Callahan necklace'; locale:86524-86569, 69679-69707, 86709-86718"},
  {"claim": "Callahan's Cutter is a weapon with a wiki URL (not a necklace), and Doctor Callahan / Beth Callahan are Medic NPCs in Seaside and Queensfields. No client or repo line links either to this necklace.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:10277-10278; repo:notes/Build Guides/Content/Jobs/Medic.md:50-51"},
  {"claim": "Repo-wide search for 'Infernal' and definition id 22719 in JSON stores finds no vendor, quest, crafting, or drop entry for this item.", "source": "search repo *.json 'Infernal|22719'"},
  {"claim": "Corrected: the previous answer's citation locale:322885120 does not exist and has been dropped.", "source": "critique evidence[2]; locale lookup"},
  {"claim": "The lookup tool errors on any query containing an apostrophe, so wiki, article, and video absence could not be confirmed directly; the search used no quoted apostrophe name.", "source": "lookup error: fts5 syntax error near \"'\""}
 ],
 "confidence": 0.1,
 "open": [
  "No source found: no wiki page, image, article fact, video frame, coin store price, vendor stock, quest reward, enemy drop, or event names this item. Sources list is empty.",
  "Live status and retirement unknown. The 'X Infernal Necklace' series is large and unexplained; its acquisition method (drop, crafting, promotion, or non-obtainable variant) is not documented in the pack or the repo.",
  "Wiki and video searches were not confirmed because the apostrophe in the name breaks the FTS query; retry with the apostrophe removed (e.g. 'Callahans Infernal Necklace') or check the wiki page 'Callahan's_Infernal_Necklace' directly.",
  "The first-pass tag (live yes, source drop) is a cheap-model hint and is not used as evidence."
 ]}
