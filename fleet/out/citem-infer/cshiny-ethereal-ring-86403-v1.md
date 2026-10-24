<!-- fleet job=citem-infer id=cshiny-ethereal-ring-86403-v1 status=nothing_found turns=5 usd=0.0043 tokens(read,write,in,out)=[40437, 20188, 12, 2775] model=claude-haiku-5-5 -->
# Shiny Ethereal Ring

{"item": {"name": "Shiny Ethereal Ring", "locale_id": 86403, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: Id 22412, NameId 86403, Type 1, Class 50, Slot 8 (ring), CategoryId 108, MinProfileRank 16, PowerRating 5, MemberDiscount 10, TintAlias dyetint, DescriptionId 1114 (empty text), MaxStackSize -1.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:464379-464396"},
  {"claim": "Client has a 'Cost': 1780 field on this definition, but this is the client's item cost field, not a coin store price. No store entry for item 22412 exists in our repo data, so no coin vendor sale is evidenced.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:464387; repo search for 22412 found no store rows"},
  {"claim": "Name 'Shiny Ethereal Ring' is locale 86403; it sits in a cluster of sibling rings: Shiny Spectral/Mystical/Phantasmal/Eternal/Celestial Ring (86398-86402, ids 22407-22411) and Ruffian Dreadful/Fateful/Infernal/Spectral/Mystical Ring (86404-86408, ids 22413+). Same cost, slot and rank.", "source": "locale:86398 to locale:86408; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:464283-464400"},
  {"claim": "Locale string table lists Shiny Ethereal Ring only as an item name; no description line or related quest/event text was found next to it.", "source": "locale:86403; locale description 1114 has no matching text"},
  {"claim": "No wiki page, wiki category, article, or video frame names this item or its sibling Shiny/Ruffian ring set.", "source": "lookup wiki/articles/video for 'Shiny Ethereal Ring' and set terms: no matches"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found: no vendor, quest, drop, event, prize wheel, crafting, collection, or promotion evidence. Left empty rather than guessed.",
  "The first-pass tag said source 'collection' and live 'yes'; neither is supported by any evidence in the pack or the repo, so both are unverified.",
  "Shiny/Ruffian ring cluster has no wiki or video coverage; the set's acquisition path (likely a tiered drop, event, or promotion set) needs a source from a player or a video.",
  "Client 'Cost' 1780 is not a store price and should not be read as a coin price.",
  "Retired status unknown; no source says it was retired or still obtainable.",
  "Description text id 1114 is empty for this item, so no in-game description is available."
 ]}
