<!-- fleet job=citem-infer id=cphysician-infernal-ring-86361-v1 status=nothing_found turns=4 usd=0.0027 tokens(read,write,in,out)=[18137, 10398, 10, 2445] model=claude-haiku-5-5 -->
# Physician Infernal Ring

{"item": {"name": "Physician Infernal Ring", "locale_id": 86361, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name text exists: 'Physician Infernal Ring', locale 86361, item class 43, slot 8, definition 22370, no coin store price, no model files, empty description.", "source": "locale:86361 (client definition pack)"},
  {"claim": "It is one member of an 11-ring tiered family in the client text table, all named '<Rank> <Element> Ring' and sitting in consecutive ids: Hoodlum Dreadful/Fateful/Infernal/Spectral/Mystical/Phantasmal/Eternal/Celestial/Ethereal (86350-86358), Physician Dreadful through Celestial (86359-86366), with the same element names reused across ranks (Dull, Rascal, Intern, Sneak, Grunt, Sage, Smooth, Prowler, Champion, Hardwood, Granite, Metallic, Jeweled).", "source": "locale:86350-86366; locale:69715, 69728, 69739, 69749; locale:86287-86377 (lookup, client)"},
  {"claim": "The family also includes other rank-prefixed Infernal rings (e.g. Intern, Sneak, Ruffian, Prowler, Faded, Polished, Dull, Hoodlum), so 'Physician' is one rank prefix within a larger generic ring series, not a unique item.", "source": "FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat (locale table, lines for 163294859, 4279 etc.)"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock, quest reward, drop or other answer names this ring or the family in the indexes searched.", "source": "lookup wiki/articles/video/client; search repo for '86361|22370|Physician|Hoodlum|Infernal'"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found for any acquisition method. The jev first-pass guess of 'drop' has no evidence behind it and is not used.",
  "Client definition has no coin store price, so no coin vendor sale is evidenced.",
  "Rank/element naming suggests a generic ring series (rank title plus element); the sources for the whole family (which ranks are drops, quest rewards, crafting or prize items) need one lookup, not one per ring.",
  "Live status is unverified: the 'yes' tag is a cheap-model hint only. The client has the item, which shows it existed in the shipped build, not that it was obtainable on the 2009-2014 server.",
  "Empty client description and no model files: this may be a placeholder or an unused variant. Check whether the definition is referenced by any shipped recipe, loot table or store row before treating it as live.",
  "Repo content stores have no entry for definition 22370 or locale 86361."
 ]}
