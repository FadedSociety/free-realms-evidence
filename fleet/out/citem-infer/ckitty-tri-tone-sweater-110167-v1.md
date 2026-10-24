<!-- fleet job=citem-infer id=ckitty-tri-tone-sweater-110167-v1 status=nothing_found turns=5 usd=0.0041 tokens(read,write,in,out)=[39487, 18731, 12, 2735] model=claude-haiku-5-5 -->
# Kitty Tri-Tone Sweater

{"item": {"name": "Kitty Tri-Tone Sweater", "locale_id": 110167, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Kitty Tri-Tone Sweater' at locale:110167 (item, no description).", "source": "locale:110167"},
  {"claim": "Sibling client item 'Doggy Tri-Tone Sweater' exists at locale:110867, so the Kitty version is one of a pet-sweater pair sharing a plaid/tri-tone texture (TextureAlias casual-plaidtritone-L1 in the legacy definitions).", "source": "locale:110867; refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:579044-579247 (Comment 'Kitty Tri-Tone Sweater')"},
  {"claim": "Definition comments in the legacy/community item definitions carry the name 'Kitty Tri-Tone Sweater' across the 36 variants; slot 3 (chest), class 61, model pet_cat_<descriptor>_chest_sweater.adr. Matches the pack's client definition.", "source": "refs: TCG-Files/Emulator/Resources/ClientItemDefinitions.json:703049-703196 (ids 34358+)"},
  {"claim": "No wiki page, article fact, video frame, coin store price (stores.json), vendor stock, quest reward, or drop names this item. Searches of repo, refs, and lookup (client/wiki/articles/video) found only the name strings and item-definition comments.", "source": "search repo/refs for 'Tri-Tone' and '34358'; lookup 'Tri Tone sweater kitty' (no matches)"},
  {"claim": "Related but not evidence for this item: articles say Snow Days/holiday sweaters came from quests, presents, and the Marketplace; the Holiday Pass gave a free Argyle Sweater. Neither names the Tri-Tone sweater.", "source": "articles/facts.json (Snow Days entries); articles/articles.json:20634"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The first-pass 'vendor' guess has no evidence behind it (vendor_stock is empty and no store price exists), so it is not confirmed.",
  "Client text is 'ucdt' (item name) with an empty description; no lines sit next to it in the locale table to show a set or promotion.",
  "Lookup's FTS5 index fails on the hyphenated term 'Tri-Tone'; the wiki and video indexes were not searched by exact name. A manual wiki check for 'Kitty Tri-Tone' or 'Doggy Tri-Tone' pages (and the Holiday/Snow Days/pet-clothing category pages) is needed.",
  "Live status is unsure: the item exists in the client and in community definitions, but no source or retirement note was found.",
  "Check the stores.json and vendor data for the 36 definition_ids 34358-34369 and their sibling Doggy Tri-Tone ids (locale 110867 set) for any coin or Marketplace listing."
 ]}
