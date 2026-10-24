<!-- fleet job=citem-infer id=cbasic-golden-spring-67070-v3 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[14174, 8751, 8, 2073] model=claude-haiku-5-5 -->
# Basic Golden Spring

{"item": {"name": "Basic Golden Spring", "locale_id": 67070, "kind": "collection"},
 "sources": [{"type": "other", "detail": "Treasure chests opened by pets (general Metal Springs collection route; not confirmed for this variant). Pets wiki: pets 'locate and dig up treasure chests', and opening treasure is 'the only way to complete the Springs collections' (Bouncy, Golden, Oiled, Tightly Coiled Metal Springs).", "where": null, "price": null, "currency": null, "source": "wiki page: Pets (Springs paragraph); locale:132440; locale:67659"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 67070 'Basic Golden Spring' (definition 23457) carries the line 'This item can be added to the Golden Metal Springs Collection'.", "source": "locale:67070; locale:132440; client definition 23457"},
  {"claim": "The Golden Metal Springs Collection is 'A collection of golden metal springs' (locale:67659), one of four Metal Springs collections (Bouncy, Golden, Oiled, Tightly Coiled; locale:132437-132440, 67544-67547).", "source": "locale:67659; locale:132437-132440; locale:67544-67547"},
  {"claim": "The repo collection catalogue lists item definition 23457 (name 67070) as entry index 7 in a collection, with item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14484-14488"},
  {"claim": "Pets wiki says pets locate and dig up treasure chests, and that opening treasure is the only way to complete the Springs collections. The wiki text does not name Basic Golden Spring or a specific chest pool.", "source": "wiki page: Pets (lookup result, garbled text)"},
  {"claim": "A player's wish list dated June 12, 2009 (blog m=6&y=2009&d=12) lists Basic Golden Spring as still needed, so the item was in play in mid-2009.", "source": "http://www.freerealmsforums.com:80/forums/blog.php?s=1f772506c3c6049562755027a923058a&do=list&m=6&y=2009&d=12"},
  {"claim": "No coin store price (definition 23457 has none), no vendor stock, and no quest or event answer names this item.", "source": "client definition in pack; vendor_stock and mentioned_by_other_answers in pack"}
 ],
 "confidence": 0.35,
 "open": [
  "Not wireable yet: no source ties Basic Golden Spring to a specific chest, zone, or spawn table. The chest route is the wiki's statement for the Springs collections as a whole.",
  "Corrected the prior critiques' point: the Pets wiki does say 'dig up' and 'the only way' for the Springs collections. The earlier answer misquoted it. The caveat remains that no page ties this variant to a chest pool.",
  "Blog date is June 12, 2009 (m=6, d=12), not December 2009.",
  "Retirement unknown. Nothing in the pack says when the Springs collections ended. The 2009 wish list shows only mid-2009 availability. live stays 'unsure'.",
  "Other Golden Spring variants (Small, Cheap, Expensive, Loose, Advanced, Useless) were not checked for a shared source.",
  "Needed: a chest table or in-game confirmation naming Basic Golden Spring, plus a price if any."
 ]}
