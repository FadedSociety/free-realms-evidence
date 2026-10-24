<!-- fleet job=citem-infer id=ccallahan-s-mystical-necklace-86712-v2 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[5343, 12377, 6, 1702] model=claude-haiku-5-5 -->
# Callahan's Mystical Necklace

{"item": {"name": "Callahan's Mystical Necklace", "locale_id": 86712, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item as locale:86712 with definition 22721, slot 9, class 43, no coin store price, no model files, no description.", "source": "client definition in evidence pack"},
  {"claim": "The name sits in an 11-item family 'Callahan's <Adjective> Necklace' (locale:86709-86717) with a sibling 'Chaz's <Adjective> Necklace' family (locale:86707-86708). The family shares one text block and no line names a vendor, quest, drop or event for any member.", "source": "locale:86707-86717 (client text lookup)"},
  {"claim": "Repo search for 'Callahan', 'Necklace' and '22721' finds no store, vendor, quest, recipe or reward entry for this item or definition. Only unrelated NPC merchant rows mention necklaces as stats.", "source": "repo search (ripgrep over repo root)"},
  {"claim": "The only 'Polished Fateful Necklace' evidence is a Consumed by the Past loot pickup from wraiths and Lukov, a different family with no quest reward recorded. It does not name this item.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:233; video:8F4ZomE2kxI/00026.jpg"},
  {"claim": "Scroll-buff names 'Mystical Scroll Buff' (locale:9472) and 'Fateful Scroll Buff' (locale:9477) share adjectives with this family. This is a naming overlap only, not a source. The earlier citation of locale:9442 is dropped because the id check flags it as not_live.", "source": "locale:9472, locale:9477 (naming only)"},
  {"claim": "Chaz Strongarm and Beth Callahan share the surname but no quest or reward text links either to necklaces.", "source": "locale:72959, 72991; repo:prototype/osfr-tools/data/content/npcs/lakeshore.json:2291"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. No wiki page, article fact, video frame, coin vendor stock, quest reward, drop, event, or other answer names Callahan's Mystical Necklace or its family. Sources stay empty; nothing is guessed.",
  "The first-pass tag 'live: yes, kind clothing, source drop' is unsupported and is not used for sources. Kind 'clothing' rests only on slot 9 and class 43.",
  "Live status is unsure. The owner-tagged necklace family (Callahan's, Chaz's, and Kai/Fastvi/Nova/Bullseye families elsewhere) may be a legacy or test set. Check the family against the live item catalog before setting live.",
  "Retired is null: nothing in the pack says whether it was retired or never released.",
  "Needed next: a player account or forum/wiki post that shows this necklace, plus its acquisition route (vendor, quest, event, or drop). The 'Consumed by the Past' Polished Fateful Necklace pickup is a different family and should not be merged into this item without a source."
 ]}
