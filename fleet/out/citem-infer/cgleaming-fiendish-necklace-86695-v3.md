<!-- fleet job=citem-infer id=cgleaming-fiendish-necklace-86695-v3 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[6036, 7727, 6, 2057] model=claude-haiku-5-5 -->
# Gleaming Fiendish Necklace

{"item": {"name": "Gleaming Fiendish Necklace", "locale_id": 86695, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Gleaming Fiendish Necklace' exists (definition_id 22704, slot 8, class 50, no coin store price in repo stores.json). Description: menacing necklace of haunted silver that increases Health regeneration for any Combat Job.", "source": "locale:86695; client_definition in pack"},
  {"claim": "The Gleaming <Adjective> Necklace family (86684-86696) includes Fiendish at 86695, alongside Dreadful, Fateful, Infernal, Spectral, Mystical, Phantasmal, Eternal, Celestial, Ethereal, Unearthly, Cosmic and Corporeal.", "source": "locale:86684-86696"},
  {"claim": "The Chaz set has twelve necklaces, not four. Locale 86697-86708 holds Chaz's Fateful, Infernal, Spectral, Mystical, Phantasmal, Eternal, Celestial, Ethereal, Unearthly, Cosmic, Fiendish (86707) and Corporeal. The earlier claim that Chaz had only four variants is wrong and is removed.", "source": "locale:86697-86708"},
  {"claim": "Fiendish variants also exist for other NPC-named necklaces and rings: Gleaming Fiendish Ring (86460), Chaz's Fiendish Ring (86472), Callahan's (86484 ring, 86719 necklace), Kai's (86496, 86731), Fastvi's (86508, 86743), Nova's (86520, 86755), Bullseye's (87548 ring, 87783 necklace). These are client names only, not sources for this item.", "source": "locale:86460-86520, 86719-86755, 87548, 87783"},
  {"claim": "A text search of the client, wiki, articles and video for 'Gleaming Fiendish Necklace' and 'Chaz's Fiendish Necklace' returned no hits (the lookup query failed on quoting, so this is weaker than a clean run). A repo search for Fiendish, Chaz's and 22704 found only Chaz quest/NPC notes (Brawler.md, Mugwort's Hollow.md, NPCs - Lakeshore.md), none naming this necklace or a Fiendish item.", "source": "lookup (client/wiki/articles/video, retried needed); search repo: notes/Build Guides/Content/Jobs/Brawler.md:273, notes/Build Guides/Content/Dungeons/Mugwort's Hollow.md:79"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found: no coin store price (no stores.json entry for 22704), no vendor stock, no quest reward, no drop, no event, no wiki, article or video mention. The first-pass 'drop' guess is unsupported and not used. Sources left empty.",
  "Live status and retirement are unknown. The client defines the item, but nothing says whether it is obtainable or was retired.",
  "Lead: Chaz's Fiendish Necklace (86707) is the closest sibling in the Chaz set (Chaz Strongarm, Lakeshore). Chaz's three-boss quest chain (Mugwort's Hollow, Dark Spore Depths, Howling Hills) and Brawler Club follow-ups are the places to check whether the Chaz/Gleaming sets were quest or NPC rewards. Not evidence for this item.",
  "The lookup tool failed on the quoted names (FTS5 apostrophe syntax error). Rerun the client, wiki and video lookups with the apostrophe removed before final sign-off.",
  "Critique fixes applied: removed the false 'Chaz has only four variants' claim (locale 86697-86708 shows twelve, including Fiendish); dropped the placeholder stub evidence (locale:150426-150430, flagged) as a source; kept the ring-family and Chaz-set facts as context only."
 ]}
