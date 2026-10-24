<!-- fleet job=event-infer id=vambassadors-v5 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[15702, 8312, 8, 2577] model=claude-haiku-5-5 -->
# Community Ambassadors

{"event": {"name": "Community Ambassadors (weekly community events)", "aliases": ["Community Ambassadors", "Ambassador Events", "Community Events (Community Ambassadors)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
   {"year": 2011, "when": "late March (Luau Beach Party; exact day not stated, post date null)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"}
 ],
 "recurring": null,
 "zones": ["Seaside (Luau Beach Party only, per article 2062 summary)"],
 "npcs": ["Community Ambassadors (group name; wiki page 'Ambassadors')"],
 "quests": [],
 "activities": ["kart races", "house shows", "duels", "trivia questions", "dancing in the surf", "answering player questions about the game"],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "Community Ambassadors were present at the Luau Beach Party to ask trivia questions, dance in the surf and answer player questions.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (re-checked by lookup)"},
   {"claim": "The Community Ambassadors run weekly community events where players race karts, show off houses and duel. The article is an undated recap of one New Year Home Show and one Dress Up Your Pet Day parade, so it supports the activities but not a schedule.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=877"},
   {"claim": "A single weekly Community Event was a winner-takes-all kart race at Thunder Falls Speedway. Undated, one week only; not a program-level zone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
   {"claim": "Client event titles are 'Community Event: <name>' and the friends-list text reads 'Add Ambassador Events to your friends list', which supports the alias Ambassador Events.", "source": "locale:2777, locale:2779"}
 ],
 "confidence": 0.35,
 "open": [
   "Merge warning: the pack merges the standing community-event program with one-off sub-events. The Luau Beach Party (article 2062) is a single sub-event; it should have its own entry, not be the program's occurrence.",
   "Schedule not confirmed: the previous answer cited article 1854 for 'every Thursday 4pm PST and Friday 9am PST' and articles 1214 and 1987 for a weekly Thursday cadence. A re-check of article 1854 returned no matches this time, so that schedule is unverified here and the program's recurrence is left null. If confirmed, recurring would be 'weekly, Thursday 4pm PST and Friday 9am PST'.",
   "Date: article 2062's post date is null in the pack. The 'late March 2011' date comes from the article summary's relative age ('1 week, 1 day ago'), not a stated date in the text, so the year and month are weak.",
   "Zones: Seaside is supported only by the Luau summary. Wugachug and Sanctuary come from the single Dress Up Your Pet Day parade (article 877) and are removed as program zones. Snowhill comes only from the 2011 Kick Off Party (article 1984, not in this pack's facts) and is not listed. Briarwood, Blackspore and Shrouded Glade come only from hourly hide-and-seek dialog (locale:18575-18581), a sub-event cadence, and are removed. Articles 1214 and 1987 say 'a different location' without naming places.",
   "Wiki: the category for this event is empty in the pack, so no wiki page is cited for the program. The claim that the wiki Community Events page describes a staff calendar had no locator and is dropped.",
   "Items and quests: none tied to the program in the pack. Luau Party Ticket, Ballet Boombox and Party for Pets/A Luau belong to sub-events and are not listed.",
   "Live: unsure. Nothing in the pack shows the program ran in the final 2014 era.",
   "Critique responses: zones narrowed to sourced items only; the uncited wiki claim removed; the 2011 Kick Off Party removed from occurrences; Thunder Falls Speedway reworded as a single-week example rather than a program zone; the schedule claim moved to open because it could not be re-verified."
 ]
}
