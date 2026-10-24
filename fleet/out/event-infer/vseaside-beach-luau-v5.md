<!-- fleet job=event-infer id=vseaside-beach-luau-v5 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[20714, 13676, 8, 3550] model=claude-haiku-5-5 -->
# Seaside Beach Luau

{
 "event": {
  "name": "Seaside Beach Luau",
  "aliases": ["Luau Beach Party (Community Event: Luau Beach Party, article 2062 title)", "Beach Party Luau (client UI string, locale:5525)"]
 },
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Friday 5 March 2010, 3pm Pacific (US and Latin America, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092"},
  {"year": 2011, "when": "Thursday 24 March 2011, 3pm Pacific (US and Latin America, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (fact 'Luau Beach Party', quote 'Thursday March 24th, 2011 3pm Pacific Time (U.S. and Latin America) Server 1')"},
  {"year": 2011, "when": "Friday 25 March 2011, 9:00am Pacific / 5:00pm UTC (UK and Europe, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (fact 'Luau Beach Party', UK/Europe session)"}
 ],
 "recurring": "Two dated runs in March (2010, 2011); article-sourced recurrence rule not found. Not schedulable from this pack.",
 "zones": ["Seaside"],
 "npcs": ["Community Ambassadors (trivia, dancing, Q&A)", "Tiger the Party Animal (client text locale:712074442 'Tiger the Party Animal wants you to celebrate in style...')"],
 "quests": [],
 "activities": ["dancing on the beach", "turning into crabs", "lighting fireworks", "trading collections", "trivia and Q&A run by Community Ambassadors", "taking pets for a swim (article 1136)"],
 "items": [
  {"name": "Hula Outfit", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1136 (fact statement names hula outfits for the beach party; quote covers pets only; weak tie, multi-event recap)"}
 ],
 "rewards": ["Luau Party Favor (from Tiger for wearing a luau outfit; locale:712074442, locale:4548) - quantity and effect unsourced"],
 "evidence": [
  {"claim": "Seaside Beach Luau was a community beach party in Seaside on Friday March 5, 2010, 3pm Pacific, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote 'Friday March 5th, 2010 3pm Pacific Time (U.S. and Latin America) Server 1')"},
  {"claim": "Activities were dancing, turning into crabs, lighting fireworks and trading collections.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote 'dance, turn into crabs, light fireworks, trade collections')"},
  {"claim": "The 2011 run was titled Community Event: Luau Beach Party in Seaside, with the same activities.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (quote 'Everyone will be hitting the sand in Seaside to dance, turn into crabs, light fireworks, trade collections'); client locale:31291"},
  {"claim": "2011 sessions: Thursday March 24, 2011 3pm Pacific (US/LatAm) and Friday March 25, 2011 9:00am Pacific / 5:00pm UTC (UK/Europe), Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"claim": "Pets could take a swim at a beach party; Hula Outfits and beach fashions were listed.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1136 (quote 'This time we were able to take our pets for a swim.'; hula/beach fashion wording in fact statement)"},
  {"claim": "Tiger the Party Animal is the luau NPC who gives a Luau Party Favor for wearing a luau outfit.", "source": "locale:712074442; locale:4548"}
 ],
 "confidence": 0.6,
 "open": [
  "Calendar not wireable: the sourced runs are history only (March 2010; March 2011). No recurrence rule is sourced.",
  "The 2010 UK/Europe session (9am Pacific / 5pm UTC on 5 March 2010) has no quote in the pack; excluded.",
  "The 2011 Spanish posts (articles 2064, 2065; 'Evento Comunitario: Fiesta Luau en la Playa') describe Playa Azul sessions in late March 2011. Whether Playa Azul is the same place as Seaside is unsourced, so Playa Azul is not an alias.",
  "Previous aliases 'Seaside Luau' and 'Playa Azul luau beach party' had no source and are removed. 'Seaside Beach Party Luau' was a misquote of locale:5525 (which reads 'Beach Party Luau') and is removed.",
  "Luau Outfit (Girls)/(Boys) removed: only name-only locale strings and a station_cash store frame; no event tie.",
  "Hula Outfit is a weak tie only; no price or dated event source.",
  "Luau Party Ticket and quest 'Luau Party' (locale:31368) are a separate ticket-triggered activity; excluded. Back to School Beach Party and Tiki Boombox excluded.",
  "The Ambassador dancing-in-the-surf detail was not retrievable from article 2065 and is dropped; activities rely on article 1092.",
  "Web codes and vendors for beach clothing are mentioned in article 1092's summary but no specific codes or vendors are sourced.",
  "Quest 'A Luau' (repeatable, from Tiger) appears in the previous answer but no quest title is confirmed as tied to this event here; quests left empty.",
  "Wiki pages (Tiger the Party Animal, Quest:A Luau) were not re-verified in this pass; the wiki category for the event returned no members.",
  "Event name/merge: the 2010 'Seaside Beach Luau' and the 2011 'Luau Beach Party' share location and activities; treated as one recurring event, but the pack does not say the same team ran both. Confidence reflects this."
 ]
}
