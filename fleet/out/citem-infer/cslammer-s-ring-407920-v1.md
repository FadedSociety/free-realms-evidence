<!-- fleet job=citem-infer id=cslammer-s-ring-407920-v1 status=nothing_found turns=10 usd=0.0069 tokens(read,write,in,out)=[174728, 24943, 22, 4063] model=claude-haiku-5-5 -->
# Slammer's Ring

{"item": {"name": "Slammer's Ring", "locale_id": 407920, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 407920 \"Slammer's Ring\"; description locale 407956 \"This ring increases your tackle power.\" (one definition, id 67911, slot 8 = Accessory1 'Ring', class 136; no coin store price).", "source": "locale:407920; locale:407956; pack client definition"},
  {"claim": "Same-family items sit in locale 407910-407925 (Shooter's/Slammer's/Defender's Triangle Power Shard, Square Shard, Necklace, Ring; Snapper's/Basher's/Guard's Triangle and Square shards). They are a family of accessory jewelry with no wiki page, vendor, or source text attached.", "source": "locale:407910-407925"},
  {"claim": "The closest sourced-looking sibling is Blasting Ring (locale 407790/407802), whose description is the 'in soccer' variant 'This ring increases your tackle power in soccer.' Only the client text exists; no wiki or source for it either.", "source": "locale:407802"},
  {"claim": "Soccer Star jewelry tiers (Amateur/Pro/All-Star necklace, ring, shards) are documented in the repo as client-only with unknown stat mapping and no sources; the Slammer's family names do not appear in that page or in any repo data (vendors.json, stores.json, prize-wheel notes).", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:247-261"},
  {"claim": "Searches of repo data, wiki, articles and video for 'Slammer' / 'Shooter's Ring' / '67911' returned no source, vendor, drop, quest or event for this item.", "source": "repo search; lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. The first-pass 'vendor' guess has no support: no vendor_stock, no coin store price, no wiki page, no article or video mention.",
  "Unknown which job or content set owns the Slammer/Shooter/Defender/Snapper/Basher/Guard family (name pattern suggests a sports or dungeon-wheel job set, but unproven). The Soccer Star 'Tackle Power' description suggests a soccer-era item, not confirmed.",
  "Unknown whether it is live. Need a wiki page, a prize-wheel or dungeon page listing it, or a store listing.",
  "Kind is set to 'other' because it is an accessory ring (slot 8), not a clothing piece; confirm against the rebuild's kind taxonomy.",
  "Next checks: the Soccer Star wiki page's jewelry list, Dungeon prize-wheel pages that list a ring with a tier name, and Station Cash Marketplace listings for 'Ring' accessories with Tackle Power."
 ]}
