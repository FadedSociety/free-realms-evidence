<!-- fleet job=citem-infer id=cancient-bone-140834-v1 status=nothing_found turns=4 usd=0.0022 tokens(read,write,in,out)=[17168, 7695, 10, 2074] model=claude-haiku-5-5 -->
# Ancient Bone

{"item": {"name": "Ancient Bone", "locale_id": 140834, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Ancient Bone' is locale:140834 (definition 48262); it has no description, no slots/classes, no models and no coin store price, so it is not a coin-store item.", "source": "locale:140834"},
  {"claim": "'Ancient Bone' is the collection piece of the collection 'Ancient Bone Artifacts' (name_id 67537, client_id 1073742035, wiki key wiki:7:211), listed on the wiki List of Collections page (revision 27852, 2013-07-13). The collection entries are not known (entries_known: false).", "source": "repo:prototype/osfr-tools/data/content/collections.json:10938; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "The List of Collections page groups 'Ancient Bone Artifacts' under the Common tier, alongside the other Ancient Artifact sets.", "source": "wiki: List of Collections"},
  {"claim": "A collection-progress screen shows 'Ancient Bone Artifacts (1/8)' next to other Ancient Artifact sets, so the set has 8 pieces.", "source": "video:p5sDafXSQtQ/00114.jpg; video:p5sDafXSQtQ/00116.jpg"},
  {"claim": "Wiki pages mention the Bone Bog Cemetery (the Gloam Council cemetery, reached through the Ancient Wall, with elementals and tormented spirits) as a place of Ancient-themed content, but none names the source of the bone pieces.", "source": "wiki: Gloam Council; wiki: Blackspore Swamp; articles: http://www.freerealms.com/article/detail.action?articleId=538"}
 ],
 "confidence": 0.3,
 "open": [
  "No source found for how Ancient Bone is obtained. The jev first-pass guess ('drop') is unsupported: no wiki page, article, vendor, quest or drop table names it.",
  "The pack's 'quest_item' kind is also unconfirmed; the item is best classed as a collection piece of 'Ancient Bone Artifacts' (8 pieces), not a quest item.",
  "Coin vendor stock is empty and no coin store price exists in the client definition, so no vendor or coin-shop source can be given.",
  "The 'Ancient Bone Artifacts' collection has no known entries or reward in our data (entries_known false, reward null). The reward for completing it and the locations of the 8 pieces are unknown.",
  "The sibling items (Spoiled Eggs through Old Letter, locale 140829-140839) are a separate client cluster and their sources were not checked here; they may share a source pattern.",
  "Whether the item is live or retired is unknown. The collection appears on the 2013 wiki list and in video, which suggests it existed in live play, but no retirement date is recorded."
 ]}
