<!-- fleet job=citem-infer id=cbattle-worn-ancient-mask-67016-v1 status=done turns=8 usd=0.0049 tokens(read,write,in,out)=[71180, 17422, 18, 4085] model=claude-haiku-5-5 -->
# Battle Worn Ancient Mask

{"item": {"name": "Battle Worn Ancient Mask", "locale_id": 67016, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Dug-up ancient artifact piece for the Ancient Artifact Masks collection (collection entry 1 of 8, item definition 23403). The client confirms it is a collection piece; no source (dig, drop, quest, or vendor) for the piece itself is evidenced in the pack.", "where": null, "price": null, "currency": null, "source": "locale:132434; repo:prototype/osfr-tools/data/content/collection_catalogue.json:13851-13859 (collection id 175, name_id 67541, entry id 1278)"},
  {"type": "collection", "detail": "Reward for completing the Ancient Artifact Masks collection (all 8 masks): 6 coins and 50 XP (profile 43). This is the reward for the collection, not for the single mask.", "where": null, "price": "6 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13924-13936 (collection id 175)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Battle Worn Ancient Mask' is locale 67016, one of 8 Ancient Artifact Masks collection entries (67016-67023), with description 'This item can be added to the Ancient Artifact Masks Collection'.", "source": "locale:67016; locale:132434; repo:prototype/osfr-tools/data/content/collection_catalogue.json:13851-13859"},
  {"claim": "Collection 'Ancient Artifact Masks' (name 67541) is listed in the wiki's Rare collection category as '[Ancient] Artifact Masks'.", "source": "wiki page:ns0 'List of Collections'"},
  {"claim": "Ancient Artifact Masks is one of the ancient artifact collection family (Arrowhead, Bone, Chalice, Jugs, Plates, Statues, Urn), whose pieces are dug artifacts; the 'Ancient Artifacts' client quest and Briarwood dig text support this.", "source": "locale:35593; locale:17897; locale:37552; video:p5sDafXSQtQ/00114.jpg"},
  {"claim": "Client definition for item 23403 exists in the Legacy client item definitions and in the collection catalogue.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:480989-480990"},
  {"claim": "The pack reports no coin store price, so no coin vendor sale is evidenced.", "source": "pack client_definition.coin_store_prices = []"}
 ],
 "confidence": 0.4,
 "open": [
  "How the single Battle Worn Ancient Mask is obtained is not evidenced: no wiki page, no vendor, no quest reward, no drop, and no video frame names it. The likely route is the Briarwood ancient-artifact dig (Match 3 'Ancient Artifacts' minigame, locale 35593/17897), but no source ties this mask to that minigame, so it is left open rather than listed.",
  "Wiki and video only show the collection as a category (5/8 for Masks in the video frame), not per-piece sources.",
  "The 6 coins + 50 XP reward is for finishing the whole Masks collection; the exact collection-reward wording on the wiki page 'Ancient Artifact Masks' was not found by lookup, so the reward is cited from the repo catalogue only.",
  "Retired status is unknown: no source says whether the artifact dig or the collection is still live. The item is marked live=yes from the first-pass tag and the client's collection catalogue, not from a live-date source.",
  "Price: none. No coin store price in the client definition and no Station Cash or Coin Shop listing found."
 ]}
