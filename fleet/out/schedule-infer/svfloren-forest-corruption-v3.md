<!-- fleet job=schedule-infer id=svfloren-forest-corruption-v3 status=blocked turns=2 usd=0.0020 tokens(read,write,in,out)=[7428, 7648, 6, 1924] model=claude-haiku-5-5 -->
# Floren Forest corruption (unresolved: area-launch candidate and quest-chain candidate, not confirmed as one event)

{"event": {"name": "Floren Forest corruption (unresolved: area-launch candidate and quest-chain candidate, not confirmed as one event)", "key": "floren-forest-corruption"},
"kind": "promotion",
"season": null,
"slots": null,
"weekly": null,
"original_dates": [],
"zones": ["Floren Forest"],
"runs": {
 "npcs": ["Ozymandias (shared text block with Changeling Curse; not attributed to corruption alone)"],
 "props_or_areas": ["Floren Forest dark woods (article 904 describes the area launch; undated)"],
 "quests": [],
 "activities": ["Investigate the source of the problem (locale:15797)", "Defeat the source of the problem, Ozymandias (locale:16508, shared with Changeling Curse)"],
 "rewards": []
},
"announce": null,
"revival": {"recurrence": null, "why": "Not wireable. No dated source: article 904 (http://www.freerealms.com:80/article/detail.action?articleId=904) is undated, occurrences are empty, and no season window, slot cadence, weekly time or admin cadence is sourced. Recurrence is left null rather than one_off_replay, because a replay value implies a known date. Do not load this row into the scheduler until article 904 (or a client-side date) gives a year and month. Area launch and quest chain stay separate candidates."},
"evidence": [
 {"claim": "Article 904 promotes Floren Forest as a new area; the Floren are corrupted and players are invited into the dark woods to defeat the source. No date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=904"},
 {"claim": "Floren Forest is corrupted by something evil; find the source and defeat it.", "source": "locale:15789"},
 {"claim": "Investigate the source of the problem.", "source": "locale:15797"},
 {"claim": "Defeat the source of the problem, the one called Ozymandias (text block shared with Changeling Curse).", "source": "locale:16508"},
 {"claim": "Halloween is the only defined season; its window does not cover this event, so season is null.", "source": "reference Sanctuary 10f129e src/Resources/Zones/FabledRealms.json:28-51"}
],
"confidence": 0.15,
"open": [
 "No dated source found. Article 904 is undated in the pack. A lookup pass this round (articles, wiki, client; terms 'Floren Forest corrupted source Ozymandias') returned no matches, so the article could not be re-checked here.",
 "Live status unknown; do not treat as a confirmed live run.",
 "kind set to 'promotion' only as the best fit for an area-launch article; unconfirmed. The pack's 'one_off' contradicted its empty original_dates.",
 "recurrence null: the schema has no 'undated' value and one_off_replay implies a date. Needs a human decision once dated.",
 "Quest chain (The Tainted Forest, locale:417359, stone idol steps locale:22256, 21976, 24972, 23103, 24973, 37685) is undated and unverified. Locales 21970 and 23096 are flagged not_live and excluded.",
 "Ozymandias tie to corruption rests only on locale:16508, shared with Changeling Curse.",
 "'Corrupted Floren' NPC is from wiki and video nameplate only, not text-checked.",
 "No items, prices, rewards, contests, webcasts or cadences are sourced for this event."
],
"event_answer_final": true}
