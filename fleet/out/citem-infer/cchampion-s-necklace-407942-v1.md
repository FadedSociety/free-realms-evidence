<!-- fleet job=citem-infer id=cchampion-s-necklace-407942-v1 status=done turns=8 usd=0.0066 tokens(read,write,in,out)=[88340, 27434, 18, 4579] model=claude-haiku-5-5 -->
# Champion's Necklace

{"item": {"name": "Champion's Necklace", "locale_id": 407942, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: Id 67933, NameId 407942, DescriptionId text 'This necklace increases your toughness.', Slot 8 (neck), Class 136, one definition, no models, no coin store price.", "source": "client definition in pack; locale:407942"},
  {"claim": "Sibling tiers of the same family: Jolter's Necklace (67931, NameId 407940) and Charger's Necklace (NameId 407941), plus Jolter's/Charger's/Champion's Rings (407943-407945) and the Square Shards (407937-407939). Legacy definitions show MinProfileRank 16 and the same slot/class for the family.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 1155918-1155935 (Id 67931) and the ring/shard entries around 1155995-1156014"},
  {"claim": "Store data has coin prices for the Square Shard family (category 121: 67925-67930 at 2557 coins, 67927 at 3000 coins, sell 255/300), but no entry exists for 67931-67933 (necklaces) or the rings in stores.json, so no coin vendor price is recorded for Champion's Necklace.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 14625-14630 (no item 67933 found by search)"},
  {"claim": "The Soccer Star note lists a different Amateur/Pro/All-Star jewelry set with other name ids, so it is not this family.", "source": "repo:notes/Build Guides/Content/Jobs/Soccer Star.md lines 251-255"},
  {"claim": "No wiki page, article fact, video frame, vendor stock line, quest reward or drop names Champion's Necklace or its family (lookup queries with apostrophes failed on FTS syntax; a retry without the apostrophe found only Archer's Necklace of Vitality and unrelated Champion mobs).", "source": "lookup results (Champion Necklace query); refs search for Necklace in *.md returned none"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. The item is in the client, but no vendor, quest, drop, prize wheel, marketplace, event or crafting record names it.",
  "The owning job or content line for the Jolter/Charger/Champion family is not identified. The family's job, tier unlock and sources need a lookup that works on the apostrophe names (the lookup tool rejected the apostrophe in every query).",
  "The legacy Cost of 2557 on Jolter's Necklace (67931) is a legacy field and is not a store price; it is not used as a source price.",
  "The category 121 shard prices in stores.json (67925-67930) are coin vendor sales. Whether the necklaces are sold in the same vendor is unverified, so no price is assigned here.",
  "Live status and retirement are unknown; the first-pass 'live: yes' is a hint only and is not confirmed by any source."
 ]}
