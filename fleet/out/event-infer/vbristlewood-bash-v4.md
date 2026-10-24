<!-- fleet job=event-infer id=vbristlewood-bash-v4 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6984, 9181, 6, 2356] model=claude-haiku-5-5 -->
# Bristlewood Bash

{
 "event": {"name": "Bristlewood Bash", "aliases": ["Scheduled: Community Event: Bristlewood Bash (locale:6671)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "Friday 5 February 2010, 3pm Pacific Time (U.S. and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (date from the article summary only; the raw quote 'Join us in Briarwood for a special party in the highest towers of the Tanglewood Fort!' and '3pm Pacific Time (U.S. and Latin America) Server 1' carry no date; article date field is null)"}
 ],
 "recurring": null,
 "zones": ["Briarwood", "Tanglewood Fort (highest towers)"],
 "npcs": ["Mandy Vice (Briarwood Party Planner; spelled 'Mandy Vide' in http://www.freerealms.com/article/detail.action?articleId=763)"],
 "quests": [],
 "activities": ["Attend the party in the highest towers of Tanglewood Fort, Briarwood",
  "Get a teleport to the party from the Briarwood Party Planner (Mandy Vice), per article 937"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "A Community Event named Bristlewood Bash was announced as a party in the highest towers of Tanglewood Fort, Briarwood.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (quote: 'Join us in Briarwood for a special party in the highest towers of the Tanglewood Fort!')"},
  {"claim": "Start time quoted as 3pm Pacific Time (U.S. and Latin America) on Server 1. No UK/Europe slot is in the quote.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (quote: '3pm Pacific Time (U.S. and Latin America) Server 1')"},
  {"claim": "Date Friday February 5th, 2010 for the party.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (summary only; not in the raw quote)"},
  {"claim": "Members can get a teleport to the party from the Briarwood Party Planner, Mandy Vice.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (quote: 'Members can speak to the [Briarwood] [Party] Planner, [Mandy] [Vice] to get a teleport to the [party].')"},
  {"claim": "The scheduled-event title exists in the client.", "source": "locale:6671 ('Scheduled: Community Event: Bristlewood Bash')"},
  {"claim": "Mandy Vice and Briarwood Party Planner exist in the client.", "source": "locale:422676; locale:422677"},
  {"claim": "Tanglewood Fort is north of the Bristlewood Warpstone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=937 (quote: 'North of the [Bristlewood] Warpstone is the imposing Tanglewood Fort.')"}
 ],
 "confidence": 0.3,
 "open": [
  "Live status unsure: only the pre-event announcement (article 937, 'Join us') is sourced. No post-event article or confirmation that it ran was found. Do not treat as a live occurrence until confirmed.",
  "Date is summary-derived. The raw article 937 text in the pack has no date. Check the live article for the date before wiring.",
  "UK/Europe slot unresolved. The earlier answer's values (UK/Europe hour 9, GMT 18) do not reconcile with 3pm Pacific (23:00 GMT in February) and have no quote. Dropped.",
  "Game Guide calendar access (from the pack summary) is not in the quoted article 937 text. Not claimed. Verify in the live article.",
  "Probable alias, not added: locale:434535 'Community Event: Tanglewood Tower party' and locale:434536 (same towers text, SERVER 1). Also locale:18232 'Tanglewood Tower party'. Not tied to the dated event by any source; article 763 (undated) describes the towers party as a standing Party Planner feature. Possible merge of a standing feature with this event. Unresolved.",
  "Client strings locale:6675 ('dance party in the towers', Briarwood Party) and locale:18233 are unattributed to this event; excluded from activities and evidence.",
  "Quests, items, rewards: none tied to this event. locale:427274 'Briarwood party' is unattributed. Wiki category: empty in the pack. Video frame piWfe7lXZ9I/00234.jpg (Lethal Mushroom) is from another area and excluded.",
  "Recurring: null. Only one dated occurrence; no article says it recurs.",
  "NPC spelling conflict: 'Mandy Vice' (articles 937 and client) vs 'Mandy Vide' (article 763). Vice kept.",
  "Wireable: no. Needs live-article date confirmation and a post-event source."
 ]
}
