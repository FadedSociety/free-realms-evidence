<!-- fleet job=citem-infer id=cred-rose-1239-v1 status=nothing_found turns=4 usd=0.0032 tokens(read,write,in,out)=[27828, 14611, 10, 2151] model=claude-haiku-5-5 -->
# Red Rose

{"item": {"name": "Red Rose", "locale_id": 1239, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Red Rose' (locale:1239) has description 'This item can be added to the Roses Collection' (locale:4182306231 / UI string locale:132286), so it is a collection-piece item, not a wearable or weapon. Definition id 3091, one definition, no coin store price, no model files.", "source": "locale:1239; locale:132286; repo: client definition 3091"},
  {"claim": "Sister items in the same client cluster: Pink Rose (1238), White Rose (1240), Yellow Rose (1241), Blush Rose (1242), Orange Rose (1243), Lavender Rose (1244). A separate 'Snowhill Roses Collection' description exists (locale:132492), so Snowhill has its own rose set.", "source": "locale:1238-1244; locale:132492"},
  {"claim": "The wiki 'List of Collections' page lists a '[Roses]' collection and a 'Snowhill [Roses]' collection, so the collection itself is documented, but the wiki search returned no per-item acquisition data for the rose pieces.", "source": "wiki: List of Collections"},
  {"claim": "Video frames show red rose bushes in Adventurer-19 / Warrior-1 era areas (decor landmarks, not an item source). They do not show where the item is obtained.", "source": "video:K1a5FBOeiIo/00150.jpg; video:K1a5FBOeiIo/00090.jpg; video:o1tuH17AoM0/00018.jpg"},
  {"claim": "Red Rose has no vendor stock, no coin store price, and no other answer in the pack mentions it. The locale 'Red rose petals' (locale:7620) and 'Ruby red rose necklace' (locale:96936) are different items.", "source": "pack: vendor_stock empty; locale:7620; locale:96936"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The likely source is the Roses Collection rewards, but no wiki page, article, quest, or vendor in the evidence names how a player gets these rose pieces or what the collection's final reward is. Needs a wiki 'Roses' collection page or the collection reward table from the server data.",
  "The 'Roses' and 'Snowhill Roses' collection stages and rewards are unknown. Check the List of Collections '[Roses]' link target for stage items and whether Red Rose is a stage piece or a drop.",
  "Live status is unconfirmed. The first-pass tag says live: yes, but it is a hint only. The collection may be tied to an event (Snowhill) and possibly retired.",
  "No price, currency, or retirement evidence. Do not add a store source without a stores.json entry or a wiki category."
 ]}
