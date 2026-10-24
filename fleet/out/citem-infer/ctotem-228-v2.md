<!-- fleet job=citem-infer id=ctotem-228-v2 status=nothing_found turns=6 usd=0.0044 tokens(read,write,in,out)=[63218, 17235, 14, 3288] model=claude-haiku-5-5 -->
# Totem

{"item": {"name": "Totem", "locale_id": 228, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition Id 827 has Comment 'Totem', Type 1, NameId 228, DescriptionId 1114, MinProfileRank 1, MemberDiscount 10. It sits between Slimy Yeti Snot (NameId 227) and Fork Bracelet (NameId 229) in the definition list, so it belongs to the same unlabelled early cluster.", "source": "refs: Sanctuary/src/Resources/ClientItemDefinitions.json:17733-17738"},
  {"claim": "Locale 228 is the bare word 'Totem'. Locale 228 is the name only, with no description of its own. The client's own description id 1114 is also used by the neighbouring definition for Slimy Yeti Snot (227), so it is not a unique description.", "source": "locale:228; refs: Sanctuary/src/Resources/ClientItemDefinitions.json:17722-17724"},
  {"claim": "Definition 827 has no store row, no Consumables/vendor entry, no quest reward, and no drop link in the repo data searched. The only other Id 827 hits are a QuickChat id (ChatText 422062, ItemId 0), a Collections.json entry id (collection 114 entry, which points to ItemDefinitionId 3895, not 827), and a collection node spawn id. None of those is this definition.", "source": "refs search for (ItemId|GameItemId|MarketingItemId|Id): 827 across Sanctuary, Sanctuary-main-20261019, Lxzxrus, TCG-Files and FreeRealms-Legacy; refs: Sanctuary-main-20261019/src/Resources/Collections.json:4230-4234"},
  {"claim": "The 'Totem Boombox' (locale 5433, item definition 8185, store bundle 50119) is a different item. It is not definition 827, and the previous answer's sources apply to that item only.", "source": "locale:5433; locale:5434; previous answer (Totem Boombox)"},
  {"claim": "No wiki page, article, or video frame names the one-word item 'Totem' (locale 228). The wiki and article hits for 'Totem' are for Totem Boombox, Totem Radio, and the totem-pole / camp totem items (Chatty, Robbie, Owl, Troll, Man-Eating Plant), which use other locale ids.", "source": "lookup client+wiki 'Totem'; locale:23405-23410, 40203"}
 ],
 "confidence": 0.3,
 "open": [
  "Definition 827 (locale 228 'Totem') has no source in any data set searched: no vendor, store, quest, drop, event, or collection link. The result is nothing_found, not a sourced answer.",
  "The item is probably an unused or internal placeholder definition (the client name is a fragment, and the Sanctuary Comment is the only label). This is an inference, not a confirmed fact. Live status is unknown.",
  "The previous answer's Totem Boombox sources (TCG Set 5 reward, Mysterious Merchant category, StoreBundles 50119, Consumables 8185) belong to a different definition (8185, name locale 5433). They do not apply to definition 827. The earlier answer's evidence[0] that cited locale 228 should be dropped.",
  "Check the 'Totem' collection/totem-pole pieces only if the team wants to link definition 827 to a set. The Collections.json 'Id 827' is an entry id, not this definition."
 ]}
