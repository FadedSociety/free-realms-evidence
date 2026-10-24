<!-- fleet job=citem-infer id=ctime-saver-s-truffle-3026-v1 status=nothing_found turns=4 usd=0.0042 tokens(read,write,in,out)=[36443, 20897, 10, 2354] model=claude-haiku-5-5 -->
# Time Saver's Truffle

{"item": {"name": "Time Saver's Truffle", "locale_id": 3026, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Time Saver's Truffle' (locale 3026); description (locale 3027) reads 'Eating this food temporarily increases your talent as a blacksmith, chef, miner, and postman.' Food-type buff item; definition id 389, one variant, no coin store price.", "source": "locale:3026; locale:3027; pack client_definition"},
  {"claim": "The same name and description also appear in the client string table as ugdt 1208548788 and ucdt 1293821716 / 1169691933, in the same block as other talent-buff items (rings, necklaces, shards, and a carton of milk) that share the blacksmith/chef/miner/postman talent text.", "source": "refs: FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat lines 30963, 32002, 34271"},
  {"claim": "No wiki page, article fact, video frame, vendor stock entry (repo stores.json has no item 389 entry), quest reward, drop or event mention for this item was found in the repo, refs or lookup indexes.", "source": "search repo 'Truffle|389'; search refs 'Time Saver|Truffle'; lookup 'Truffle' (client and wiki)"},
  {"claim": "The nearby locale block 3021-3031 holds early-build strings: 3030 is tagged 'FLAG placeholder: test lobby' and 3023/3024 are movement buff texts, so this block may come from a test or early build rather than the live game.", "source": "locale:3021-3031 (pack client_cluster)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found: no vendor, quest, drop, event, crafting or store record names this truffle. Sources left empty rather than guessed.",
  "The first-pass tag (live: yes, source_guess: unknown) is a hint only; live status is unsure. The neighbouring locale block (3021-3031) looks like test or early-build text, which would make the item possibly not live.",
  "Related items exist in the client (Truffle, Tasty Truffle, Spicy Truffle, Delicious Truffle, Truffle Shuffle quest via Fenwink in Merry Vale). Those are different items; nothing ties Time Saver's Truffle to them in the evidence.",
  "Retired status unknown: no source states retirement either way.",
  "Next step: check the original client's crafting/recipe tables for item id 389 or the talent-food family, and any Fenwink/Scotty trade or cooking-contest rewards."
 ]}
