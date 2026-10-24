<!-- fleet job=event-infer id=vseaside-beach-luau-v6 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[8196, 9861, 6, 2607] model=claude-haiku-5-5 -->
# Seaside Beach Luau

{"event": {"name": "Seaside Beach Luau", "aliases": ["Community Event: Luau Beach Party (locale:31291; article 2062 title, 2011 run, not dated here)", "Beach Party Luau (locale:5525)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Friday 5 March 2010, 3pm Pacific (US and Latin America, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote: 'Friday March 5th, 2010 3pm Pacific Time (U.S. and Latin America) Server 1')"}
 ],
 "recurring": null,
 "zones": ["Seaside"],
 "npcs": [],
 "quests": [],
 "activities": ["dancing on the beach", "turning into crabs", "lighting fireworks", "trading collections"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Seaside Beach Luau was a community beach party in Seaside on Friday 5 March 2010, 3pm Pacific (US/LatAm), Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (fact:event and quote confirmed in lookup)"},
  {"claim": "The same article's fact gives a UK/Europe session at 9:00am Pacific / 5:00pm UTC on the same date, Server 1. The quote in the pack covers only the US session.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (fact statement only)"},
  {"claim": "Activities were dancing, turning into crabs, lighting fireworks and trading collections.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote: 'dance, turn into crabs, light fireworks, trade collections')"},
  {"claim": "Article 2062 describes a community event called Luau Beach Party in Seaside with the same activities; its locale name is Community Event: Luau Beach Party.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (fact:event confirmed in lookup); locale:31291"},
  {"claim": "Beach Party Luau is a client UI string.", "source": "locale:5525"},
  {"claim": "Tiger the Party Animal's luau NPC text (wear a luau outfit for a party favor) and 'Equip a luau outfit and speak to Tiger the Party Animal during a Luau Party' exist in the client.", "source": "locale:422866; locale:422874 (ids corrected from the prior answer's locale:712074442, which does not exist)"}
 ],
 "confidence": 0.4,
 "open": [
  "Calendar not wireable: one dated run is sourced (5 March 2010). No recurrence rule is sourced; do not treat as yearly or schedulable.",
  "The 2011 runs ('Thursday 24 March 2011' 3pm PT and 'Friday 25 March 2011' 9am PT / 5pm UTC, both cited to article 2062) could not be reproduced in lookup. Article 2062 exists and its activity fact is confirmed, but no date quote was shown. Excluded until the quote is found.",
  "The 2010 UK/Europe session appears only in article 1092's fact statement, not in a quoted sentence. Kept as a note, not as a separate occurrence.",
  "locale:712074442 does not exist. Tiger the Party Animal is locale:420171; the luau text is locale:422866. Luau Party Favor (locale:4548) exists but its tie to the Seaside event and its quantity/effect are unsourced; removed from rewards.",
  "Client text ties Tiger's luau outfit/party favor to a 'Luau Party' (locale:422874, 422864, 31368, 31354). Whether that is the same activity as the Seaside Beach Luau is unsourced; kept separate.",
  "Quest 'A Luau' (locale:422865) exists, but no source ties it to the Seaside event. Quests left empty.",
  "Hula Outfit removed: the only source is article 1136, a multi-event recap, and the quote there covers pets only. Not tied to this event.",
  "Pet swim (article 1136, 'This time we were able to take our pets for a swim') is in a recap of several events and is not confirmed for the Seaside luau. Removed from activities.",
  "Community Ambassador dancing/trivia detail was not retrievable from article 2065 and is dropped. Web codes and vendors for beach clothing are unsourced.",
  "Merge risk: the 2010 'Seaside Beach Luau' and the 2011 'Luau Beach Party' share location and activities. The pack does not say they are the same event run by the same team. Treated as possibly one event, unconfirmed.",
  "Spanish 2011 posts (articles 2064, 2065; Playa Azul) are not confirmed as the same place or event. Not an alias.",
  "Wiki category for this event returned no members; wiki pages not re-verified."
 ]}
