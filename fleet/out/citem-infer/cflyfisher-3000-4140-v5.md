<!-- fleet job=citem-infer id=cflyfisher-3000-4140-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6908, 10656, 6, 1894] model=claude-haiku-5-5 -->
# Flyfisher 3000

{"item": {"name": "Flyfisher 3000", "locale_id": 4140, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Flyfisher 3000' is locale 4140, item class 142, definition 68153, slot 0. Description (locale 4142): 10% better chance of catching Chilly Grouper, Butter Flyfish and Briar Nibbler.", "source": "locale:4140, locale:4142"},
  {"claim": "A second client name 'Flyfisher 3000 - Lure' (locale 412922) has a matching description (locale 412923) with the same three fish.", "source": "locale:412922, locale:412923"},
  {"claim": "Fish and angler dialog use the lure by name: 'The Briar Nibbler / Butter Flyfish / Chilly Grouper loves to find the Flyfisher 3000!', 'I've been using a Flyfisher 3000 to catch lots of those from the stream.', 'A Flyfisher 3000 would probably work too...'", "source": "locale:29759, locale:29767, locale:29772, locale:414049, locale:414051"},
  {"claim": "The wiki Fisherman page carries the Flyfisher 3000 description text (Chilly Grouper, Butter Flyfish, Briar Nibbler). It is a description citation only; it names no vendor, price, or date. The same page lists the 16oz Steak description (Winter Piranha, Toothy Tetra, Blind Swurglefish), so locale:4141 belongs to 16oz Steak, not to this item, even though the client tags it 'Flyfisher 3000'.", "source": "wiki page ns0 Fisherman; locale:4141"},
  {"claim": "Repo Fisherman notes list this lure with the same three fish (Fisherman.md:208-213, 267). The file lists client keys, not sources.", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:208-213, 267"},
  {"claim": "No coin store price: client definition coin_store_prices is empty and no repo store row exists for definition 68153.", "source": "client definition; repo search for 68153"},
  {"claim": "Guppie's generic 'Buy a lure from Guppie' line does not name this lure, so Guppie is not evidenced as a seller and is not listed as a source.", "source": "locale:408632, locale:408633"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced: no vendor stock row, coin or Station Cash price, quest reward, drop, prize wheel, crafting, collection, membership, or promotion source. Sources are left empty rather than guessed.",
  "Guppie (Sacred Grove Shallows) may sell lures, but locale:408633 names no lure and no stock row ties him to the Flyfisher 3000. Needs a stock row or a wiki page naming the item before it is listed.",
  "Retired status is unknown; no source says whether it was removed or is still sold, so live is 'unsure'.",
  "Repo conflict to fix: prototype/osfr-tools/data/content/fishing.json:1396-1402 pairs 'Flyfisher 3000 - Lure' with Plattypus, Lady Tetra, Roach Loach. The client text (locale:412923, locale:4142) gives Chilly Grouper, Butter Flyfish, Briar Nibbler. Correct the file before the rebuild.",
  "Withdrawn: the id 'locale:1920656359' is not a locale id (it is a dat-file hash key for the Guppie line) and is not cited anywhere in this answer.",
  "Repo Fisherman.md:267 ids 1244002952 and 2252922992 are client locale keys for the name and '- Lure' variant, not price or source data.",
  "Wiki Fisherman is cited for the description only; it does not source the item."
 ]}
