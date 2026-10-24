<!-- fleet job=event-infer id=vfiesta-luau-en-la-playa-luau-beach-party-v4 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[19939, 11638, 8, 3715] model=claude-haiku-5-5 -->
# Fiesta Luau en la Playa (Luau Beach Party)

{
 "event": {"name": "Luau Beach Party (Fiesta Luau en la Playa)", "aliases": ["Fiesta Luau en la Playa", "Community Event: Luau Beach Party", "Luau Party (community event)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Thursday 24 March 2011, 3pm Pacific Time (US and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"year": 2011, "when": "Friday 25 March 2011, 9:00am Pacific Time (UK and Europe), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"}
 ],
 "recurring": null,
 "zones": ["Seaside"],
 "npcs": ["Tiger the Party Animal", "Community Ambassadors (unnamed group)"],
 "quests": ["A Luau"],
 "activities": ["dance on the beach/sea", "turn into crabs", "light fireworks", "trade collections", "socialize", "trivia and Q&A with Community Ambassadors", "equip a luau outfit and speak to Tiger during a Luau Party (quest objective, locale:422874)"],
 "items": [
  {"name": "Luau Party Ticket", "price": "18000 (store frame, regular price unconfirmed)", "currency": "coins", "source": "locale:5102398; locale:5102399 ('Purchasing this item will immediately begin a Luau Party for your current zone'); video:yBwnL7jnweI/00030.jpg. Not confirmed as event-only."},
  {"name": "Luau Outfit", "price": null, "currency": null, "source": "locale:5102139; quest objective locale:422875"},
  {"name": "Luau Outfit (Boys)", "price": null, "currency": null, "source": "locale:156883"},
  {"name": "Luau Outfit (Girls)", "price": null, "currency": null, "source": "locale:156882 and locale:5102140 (same name, probable duplicate ids; check which the quest uses)"}
 ],
 "rewards": ["Luau Party Favor (from Tiger when wearing a luau outfit, locale:422864, locale:4548)"],
 "evidence": [
  {"claim": "English article: a community event called Luau Beach Party took place in Seaside, with dancing, crab transformation, fireworks and collection trading.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"claim": "US/Latin America session on Thursday March 24, 2011, 3pm Pacific, Server 1; past tense in the article.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"claim": "UK/Europe session on Friday March 25, 2011, 9:00am Pacific / 5:00pm UTC, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
  {"claim": "Spanish articles describe the same luau beach party at Playa Azul (name for the same beach, inferred link). Sessions also given as 24 Mar 15:00 PST (23:00 CET) and 25 Mar 09:00 PST / 17:00 UTC.", "source": "http://www.freerealms.com/article/detail.action?articleId=2064 ; http://www.freerealms.com/article/detail.action?articleId=2065"},
  {"claim": "Community Ambassadors were present at the event to answer questions (2064 past tense). 2065 announces it in future tense.", "source": "http://www.freerealms.com/article/detail.action?articleId=2064 ; http://www.freerealms.com/article/detail.action?articleId=2065"},
  {"claim": "Client event title and server line name the Luau Beach Party on Server 1.", "source": "locale:31291; locale:31292"},
  {"claim": "Quest 'A Luau' objective: equip a luau outfit and speak to Tiger the Party Animal during a Luau Party. Its exclusive availability to luau events is NOT verified from the text read.", "source": "locale:422865; locale:422874; locale:422875"},
  {"claim": "Luau Party Ticket starts a Luau Party in the current zone when purchased.", "source": "locale:5102399 (verified by direct lookup)"},
  {"claim": "Tiger has retired from Luau duty to prepare for Snow Days (wiki news template, undated). Tiger also hosts Pet and Winter parties, so he is not luau-only.", "source": "wiki Template:News (page:ns10); locale:422870; locale:424776"}
 ],
 "confidence": 0.6,
 "open": [
  "Announcement date unknown: 2064 and 2065 give no posting date (2065 only a relative age). Article 2062 also gives no posting date in the pack. Live status rests on past tense in 2062 and the client event strings, not on a dated post.",
  "Time-zone conflict in the source: 2062 gives 3pm Pacific, while 2065 gives '23:00 CET' for the Thursday session. 23:00 CET = 15:00 PDT, so that figure matches PDT, not PST. The Friday '17:00 UTC' figure matches PST (9am PST), not PDT (9am PDT = 16:00 UTC). The article mixes conventions. Store the wall-clock Pacific times as given and do not pick a UTC value.",
  "Zone: only Seaside is tied to this event (article 2062). The generic 'A luau party has started in X' strings (locale:419938-419941) are not evidence that this event ran in Sanctuary, Blackspore or Greenwood Forest, and they are not used here.",
  "Activity wording in 2062 ('dance, turn into crabs, light fireworks, trade collections') is the same boilerplate as article 194 (Seaside Beach Party, Aug 14 2009). It does not by itself prove a separate identity; the 2011 date and the luau name are what tie 2062 to this event.",
  "Separate events not merged here: Seaside Beach Party Luau (locale:5525, 5528, a Hula-outfit beach party below the Abandoned Dojo), article 1136 (pet-swimming beach party with Hula Outfits), article 194 (Aug 14 2009 Seaside Beach Party), nighttime beach party (article 1118), Back to School Beach Party (locale 436158).",
  "Article 1092 (Friday March 5 2010, same time pattern, Server 1) may be an earlier run, but its text does not say it was a luau. Not counted as an occurrence. Recurrence is null: only one dated occurrence (two days) in the pack.",
  "Referee-hosted 'Luau Party' quest (locale:31368, dialogue locale:31354, locale:31369) may be a separate schedule; not read in full, not included.",
  "Luau Tiki Torch (locale:420140) and Luau Spit Fire (locale:423111) not tied to the event by any source; excluded.",
  "Luau Party Ticket regular price unconfirmed; 18000 comes from a store frame showing a -2000 discount line. Wiki price fields blank.",
  "Outfit prices not in any source. Outfits are also obtainable by quests, web codes, in-game currency and Station Cash (article 2065 summary), so they are not event-only.",
  "Duplicate outfit names: 156862 and 156864 (Luau Party Outfit Female/Girls) near-duplicates; 156864 and 156881 flagged (156881 DEPRECATED, not live). 156882 and 5102140 both 'Luau Outfit (Girls)'. Confirm which ids 'A Luau' requires.",
  "'A Luau' quest availability only during luau events: unverified. Tiger hosts other parties too.",
  "Tiger retirement (wiki Template:News) is undated; it may postdate the 2011 event. It does not change the 2011 evidence but limits current use of the quest and NPC.",
  "Articles 2062, 2064 and 2065 were cited from the pack summaries and lookup results; full article bodies were not re-read here."
 ]
}
