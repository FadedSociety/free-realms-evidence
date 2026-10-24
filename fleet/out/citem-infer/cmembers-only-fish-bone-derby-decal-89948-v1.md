<!-- fleet job=citem-infer id=cmembers-only-fish-bone-derby-decal-89948-v1 status=done turns=6 usd=0.0051 tokens(read,write,in,out)=[71061, 21563, 14, 3359] model=claude-haiku-5-5 -->
# Members Only Fish Bone Derby Decal

{"item": {"name": "Members Only Fish Bone Derby Decal", "locale_id": 89948, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition exists: name locale 89948, description 'Confuse cats and your opponents.', definition_id 9260, slot 8, class 76, no models, no coin store price.", "source": "locale:89948; repo:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:175683-175686 (Comment 'Members Only Fish Bone Derby Decal', NameId 89948)"},
  {"claim": "Same definition appears in the other community server copies (Sanctuary, Sanctuary-PC2009, TCG-Files, FreeRealms-Legacy), so it is a shipped client item.", "source": "refs: Sanctuary/src/Resources/ClientItemDefinitions.json:175683; TCG-Files/Emulator/Resources/ClientItemDefinitions.json:195272; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:175683"},
  {"claim": "The wiki Items page has a Derby Decal list (Fire Totem, Fossil-Tooth, Green Crystal, Guitar, Bug-Eating Plant, Orb, Pizza Slice, Trophy, Web Spinner, Club Card) and Racing Decal entries (Bat Wing, Firecracker, Fish Bone). This item is not named on that page, so no wiki source exists for it.", "source": "lookup wiki page:ns0 Items"},
  {"claim": "Articles say racing and demolition derby decals were sold in the store so players could decorate their car (June 2011 era). This supports the decal line as a store product, but does not name this item.", "source": "articles/facts.json 'Racing and derby decal stickers' (article-199, freerealms.com/article/detail.action?articleId=199); 'Demolition Derby and racing decals' (article-197)"},
  {"claim": "A non-members 'Fish Bone Racing Decal' store bundle exists (NameId 89908, launched 2009-08-06, category group 103, Members-only price flag set). It is a different item from the Members Only Derby Decal and no bundle for NameId 89948 was found.", "source": "repo: Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:8636-8662 (Id 3204)"},
  {"claim": "The name 'Members Only' and the sibling 'Members Only' decals (Bat Wing 89952, Forest Totem 89966, Bug-Eating Plant, Web Spinner) suggest a members-only offer, but no source states that.", "source": "locale:89952; locale:89966; ClientItemDefinitions.json Comment 'Members Only Bug-Eating Plant Racing Decal'"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found for how this item is obtained. The name suggests a membership-only store offer, but no membership bundle, store bundle, wiki page, article, or vendor answer names it. Do not record membership as a source until one is found.",
  "The store bundle for the non-members Fish Bone Racing Decal (Id 3204) has price fields stored as codes, not as coin or Station Cash amounts. No price is stated here.",
  "The item's first pass says live: yes, but nothing supports that beyond its presence in the client. Liveness and retirement are unconfirmed.",
  "The first-pass 'source_guess: membership' is a hint only. Membership-pack contents in the Items wiki or membership articles should be checked for 'Members Only' decals.",
  "The cluster's critique field was empty, so no critiques needed fixing."
 ]}
