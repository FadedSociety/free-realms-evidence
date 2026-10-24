<!-- fleet job=item-infer id=icliff-v5 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[5772, 7473, 6, 1687] model=claude-haiku-5-5 -->
# Cliff

{"item": {"name": "Cliff", "locale_id": 5102419, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:5102419 is the npc_name string 'Cliff'. A search of the client text for 'Cliff' finds no item named Cliff; the other hits are place names, 'Cliff Diving' (locale:408104), 'Sunset Cliffs' (408119), and Heddy Heathcliff.", "source": "locale:5102419; locale search 'Cliff'"},
  {"claim": "The wiki page 'Cliff' describes a male Human NPC Merchant near the Wugachug Postbox in Wugachug, selling Postman job items. It is an NPC page, not an item page.", "source": "wiki page: Cliff"},
  {"claim": "The wiki 'Merchants' page lists Cliff under the Postman job, found near the Wugachug Postbox.", "source": "wiki page: Merchants"},
  {"claim": "The wiki page gives the introduction date as the October 1, 2013 update. This is a single wiki claim with no corroboration in the pack.", "source": "wiki page: Cliff"}
 ],
 "confidence": 0.9,
 "open": [
  "Cliff is an NPC (locale:5102419), not an item. This record has no item sources and no price, and it should not enter the item table. The answer is nothing_found for an item named Cliff. live is 'unsure' only because the schema has no null option; there is no live or retired evidence for an NPC.",
  "Cliff's wiki 'Sells' list names items that are real items to be researched separately: Postman's Power Shard of Timing III (locale:15169), Postman's Necklace of Timing III (locale:15159), Postman's Ring of Talent III (locale:15158), and the Priority Postman pieces (locale:132989-132995; 'Priority Postman Shoes' appears twice on the wiki list). Client names for 15158, 15159 and 132989 were confirmed in the prior critique. I did not re-check 15169 or 132990-132995 in this pass. The wiki gives no prices or currency for any of them, so each needs its own pack for price, source and live status.",
  "The 2013 introduction date is single-sourced to the wiki 'Cliff' page and is not used here to set any live or retired status.",
  "Prior answer's claim that the III-tier Postman items were missing from the client was wrong. Locale search finds them, including Postman's Power Shard of Talent III (locale:15168)."
 ]}
