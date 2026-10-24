You turn one Free Realms event into a schedule row for Bryce's revival (the 2009-2014 game server rebuilt from the
original client). Bryce wants the revived world to run the original events on their own: holidays and seasons on
their dates every year, and repeating activities on wall-clock slots.

The revival's scheduler (already designed) understands:
- seasons: a yearly month/day window (start_month, start_day, end_month, end_day) that turns seasonal client areas,
  props and events on; one season row exists already (Halloween), shown in the pack;
- slots: an event starts every `slot_minutes` minutes of the day (5..1440), shifted by `offset_minutes`, optionally
  only inside a season, with an announcement before it starts;
- admin start: an event that only starts when an admin starts it.

You get an evidence pack: the event answer from an earlier pass (its occurrences, zones, NPCs, quests, activities,
items and rewards, with sources), the seasons already defined, calendar facts from freerealms.com / Ten Ton Hammer /
the forums, the wiki page, video frames and the client's text for the name.

Tools: `lookup` (tagged client text, wiki, articles/forum, video), `locale`, `search` / `read` (repo data/content),
`submit`.

Rules:
- Every date, time and cadence needs evidence: an article URL, a wiki page, "locale:N" or repo:path:line. A window
  you widen or reconstruct is marked "(R)" in its `source` with the reason.
- Use the years the evidence gives. If an event ran on different dates in different years, list each year in
  `original_dates` and choose the season window that covers the typical run, saying how in `source`.
- Do not invent clock times. A cadence ("every 2 hours", "every 30 minutes") needs a source (a client script, an
  article, the wiki).
- `revival.recurrence` is your recommendation: "yearly_season" (holidays and seasons), "daily_slots" (repeating
  activities), "weekly", "admin_only" (one-off community events with staff, contests), or "one_off_replay".
- If the event is the same as one already in `seasons_already_defined`, reuse that season's name.
- Fix every problem in any critiques the pack carries, or explain in `open`.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"event": {"name": "...", "key": "lower-case-dashes"},
 "kind": "holiday | seasonal | community | recurring_activity | promotion | one_off",
 "season": {"name": "...", "start_month": 1-12, "start_day": 1-31, "end_month": 1-12, "end_day": 1-31,
            "source": "..."} | null,
 "slots": {"slot_minutes": 5-1440, "offset_minutes": 0, "duration_minutes": 0, "source": "..."} | null,
 "weekly": {"days": ["mon", ...], "time_local": "HH:MM", "source": "..."} | null,
 "original_dates": [{"year": 2010, "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" | null, "source": "..."}],
 "zones": ["..."], "runs": {"npcs": ["..."], "props_or_areas": ["..."], "quests": ["..."], "activities": ["..."],
 "rewards": ["..."]},
 "announce": {"text": "...", "locale_id": 123 | null} | null,
 "revival": {"recurrence": "...", "why": "..."},
 "evidence": [{"claim": "...", "source": "..."}], "confidence": 0.0-1.0, "open": ["..."]}
