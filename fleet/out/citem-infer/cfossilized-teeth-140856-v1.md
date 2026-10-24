<!-- fleet job=citem-infer id=cfossilized-teeth-140856-v1 status=done turns=7 usd=0.0043 tokens(read,write,in,out)=[54250, 16605, 16, 3385] model=claude-haiku-5-5 -->
# Fossilized Teeth

{"item": {"name": "Fossilized Teeth", "locale_id": 140856, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 48284 'Fossilized Teeth' (locale 140856) exists with no description, slot 0, class 0, no models, and no coin store price.", "source": "client definition in evidence pack; locale:140856"},
  {"claim": "Client UI text 'This item can be added to the Shark Teeth Fossils Collection' exists, so a Shark Teeth Fossils collection set is a live client concept.", "source": "locale:132362"},
  {"claim": "Shark Teeth Fossils is a live collection set of fossilized shark teeth ('Gather the largest set of chompers you will ever see, from sharks as large as the Great White').", "source": "https://freerealms.com:80/collections.vm (articles/facts.json, page-collections-vm, era live); wiki page 'Collections' and 'List of Collections' (lists [Shark] [Teeth] [Fossils])"},
  {"claim": "The wiki lists Shark Teeth Fossils in List of Collections, Rare/Statues-type category, with no per-item acquisition data.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (revision 27852, 2013-07-13)"},
  {"claim": "Repo collection record 'Shark Teeth Fossils' (wiki:7:215, client_id 1073742039, name_id 7754) has an empty entries list and no reward/spawn/area data.", "source": "prototype/osfr-tools/data/content/collections.json:11047-11072"},
  {"claim": "Fossilized Teeth is the item the Shark Teeth Fossils collection most plausibly takes (name match only).", "source": "name match between locale:140856 and the Shark Teeth Fossils collection; not confirmed by any answer that names the item"}
 ],
 "confidence": 0.35,
 "open": [
  "No acquisition source found for Fossilized Teeth: no coin vendor stock, no coin store price, no wiki page, no quest reward, no enemy drop, and no event entry names it.",
  "Its link to the Shark Teeth Fossils collection rests on the name match and the collection's wiki description; no source ties definition 48284 to collection 1073742039 (name_id 7754).",
  "The client cluster (locale 140851-140861: Flat Soccerball, Frozen Pinecone, Yeti Plushie, Star Fossil, Rusty Spring, Single Glove, Torn Card, Empty Gift Box, Broken Stick, Old Doll) reads like a set of junk or trash items, but no source confirms how they are obtained.",
  "The sharks in the collection blurb suggest a fishing or shark-enemy drop (repo fishing.json lists Tangletooth Shark and Purplenosed Shark), but no source ties Fossilized Teeth to either. Do not record this as a source without evidence.",
  "Live status is inferred from the 2013 wiki list and the live collections article, not from a dated sale or removal record. Retired status is unknown."
 ]}
