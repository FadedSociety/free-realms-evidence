<!-- fleet job=event-infer id=vseaside-beach-luau-v9 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6797, 7770, 6, 1975] model=claude-haiku-5-5 -->
# Seaside Beach Luau

{
 "event": {"name": "Seaside Beach Luau", "aliases": []},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Friday 5 March 2010, 3pm Pacific (US and Latin America, Server 1); the article also gives 9:00am Pacific / 5:00pm UTC for UK and Europe, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote: 'Friday March 5th, 2010 3pm Pacific Time (U.S. and Latin America) Server 1')"},
  {"year": 2011, "when": "late March 2011, Seaside, Server 1 (summary-sourced; exact day not quoted)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (summary only; date quote still to verify). Confidence low; kept separate, not merged, until the quote is checked."}
 ],
 "recurring": null,
 "zones": ["Seaside"],
 "npcs": ["Community Ambassadors (article 1092 summary; not named individually)"],
 "quests": [],
 "activities": [
  "dancing on the beach",
  "turning into crabs",
  "lighting fireworks",
  "trading collections",
  "trivia questions and dancing in the surf with Community Ambassadors (article 1092 summary; not quote-verified)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "A community beach party in Seaside was held Friday 5 March 2010, 3pm Pacific, US/LatAm, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092"},
  {"claim": "Activities were dance, turn into crabs, light fireworks and trade collections.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1092 (quote: 'dance, turn into crabs, light fireworks, trade collections and basically have a good time.')"},
  {"claim": "Article 2062 ('[Luau] [Beach] [Party]') describes a community event in Seaside on Server 1 with the same activities (dance, turn into crabs, light fireworks, trade collections), so it is a probable second run of this event, pending its date quote.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"claim": "Article 1136 recap lists a Seaside Beach Luau among recent events where pets could swim. The recap covers several events, so it is not tied to this run's date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1136 (quote: 'This time we were able to take our pets for a swim.')"}
 ],
 "confidence": 0.6,
 "open": [
  "Article 2062's 2011 date is from its summary only; the quote is not retrieved. Verify before treating 2011 as confirmed.",
  "Client name 'Seaside Beach Party Luau' (locale:5528) was cited by an earlier pass; a text search in this check returned no match, so it is unverified and not used as an alias.",
  "No recurrence rule is sourced; two dated runs are not enough for a schedule rule, so recurring is null.",
  "Hula Outfit removed as an item: no source ties a specific Hula Outfit item to this event. Article 1136 mentions Hula Outfits in a multi-event recap.",
  "Client 'Luau Party Ticket' (locale 5102398, 'Purchasing this item will immediately begin a Luau Party for your current zone') and zone announcements (locale 419938-419941) suggest a separate on-demand luau feature. Not folded into this scheduled community event; no dates sourced.",
  "'Tiger the Party Animal' and the 'Luau Party' outfit/party-favor strings are a separate client feature and are excluded.",
  "Quest 'A Luau' (locale:422865) exists but no source ties it to Seaside; quests left empty.",
  "Wiki category for this event returned no members.",
  "Article dates are null in the pack; the 2010 date comes from the quoted sentence in article 1092.",
  "locale:712074442 does not exist and was removed."
 ]
}
