<!-- fleet job=citem-infer id=csparkling-grape-96689-v2 status=nothing_found turns=2 usd=0.0022 tokens(read,write,in,out)=[4831, 11977, 6, 1391] model=claude-haiku-5-5 -->
# Sparkling Grape

{"item": {"name": "Sparkling Grape", "locale_id": 96689, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Sparkling Grape' exists: locale 96689 is the name, and the client item definition id 31283 carries the name as its comment (slot 0, class 9). Its description is 'Eating this food temporarily increases your talent as a Blacksmith, Chef, Miner, and Postman.'", "source": "locale:96689; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:638960-638961 (Comment 'Sparkling Grape', Id 31283)"},
  {"claim": "No store, vendor, or recipe row keys to definition 31283 or locale 96689. Repo search for 31283 and 'Sparkling' finds no store or vendor row. The only 131283 hits are unrelated vendor/name ids, and the 'Sparkling Water' hit is a test fixture.", "source": "search repo (data/content, tests); search refs"},
  {"claim": "The lookup tool returns only the client name line for 'Sparkling Grape'. No wiki page, article, or video frame names it.", "source": "lookup client/wiki/articles/video 'Sparkling Grape'"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. Vendors, coin store prices (stores.json has no row for 31283), quests, drops, events, and crafting all come back empty. Leave sources empty until a wiki page, player report, or store/recipe row turns up.",
  "Live status is unsure. The first-pass tag says live and source 'event', but that is a hint only. Nothing in the evidence confirms either way.",
  "Dropped from the prior answer: the claim that the Maker's Bran Muffin / Raw Root / Lettuce Head set was pulled from live (locale 96690-96692 are flagged not_live, so they are not live evidence), and the claim that locale 47445 is the same food-buff text (not verified). The sibling 'Time Saver's Truffle' comparison (locale 3027) is not used as a source.",
  "The Legacy definition dump carries the grape's name only as a comment. It gives no source, date, or event for the item."
 ]}
