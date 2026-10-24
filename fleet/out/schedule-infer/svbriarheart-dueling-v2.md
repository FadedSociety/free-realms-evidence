<!-- fleet job=schedule-infer id=svbriarheart-dueling-v2 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[30886, 12751, 10, 2578] model=claude-haiku-5-5 -->
# Briarheart Warpstone open duel (Dec 4, year unknown)

{"event": {"name": "Briarheart Warpstone open duel (Dec 4, 2009)", "key": "briarheart-warpstone-open-duel-dec-4"},
"kind": "community",
"season": null,
"slots": null,
"weekly": null,
"original_dates": [{"year": 2009, "start": "2009-12-04", "end": "2009-12-04", "source": "http://www.freerealms.com:80/article/detail.action?articleId=651 says 'Friday December 4th' and posted 1 week 3 days before capture; refs/freerealms-com/cdx-urls.json:9819-9820 captures articleId=651 at 20091213041325, so posting is about 2009-12-03/04 and Dec 4 2009 is a Friday. (R) year 2009 reconstructed from the capture timestamp and the relative posting date, not stated in the article. Live status unconfirmed."}],
"zones": ["Briarheart Warpstone"],
"runs": {"npcs": [], "props_or_areas": ["Briarheart Warpstone (meeting point; locale:24730 'Briarheart Warpstone'; article 651 quote 'Just show up at the Briarheart warpstone ready to duel')", "private dueling area (destination of an accepted duel)"], "quests": [], "activities": ["Open PvP duel: started from another player's radial menu 'Duel' option; accepting player is moved to a private dueling area. Open to all levels and jobs on Server 1."], "rewards": []},
"announce": null,
"revival": {"recurrence": "admin_only", "why": "One announced community duel on one date (Friday Dec 4, 2009, reconstructed (R)). No source shows it recurs and no season or cadence is supported, so staff should start it. Not a yearly season and not a daily slot."},
"evidence": [
{"claim": "Article 651 announces an open player-vs-player duel at the Briarheart Warpstone on Friday December 4th, Server 1, open to all levels and jobs, in two regional windows (US/Latin America and UK/Europe).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=651 ; articles/articles.json:11072 summary; articles/facts.json:19127"},
{"claim": "The article quote 'we're having an open duel at the Briarheart Warpstone' and the phrase 'the Briarheart Dueling event' both appear in article 651, so the alias 'Briarheart Dueling' has article support.", "source": "articles/facts.json:19135, articles/facts.json:41080 (articleId=651)"},
{"claim": "Duels start from another player's radial menu 'Duel' option; the accepting player is moved to a private dueling area.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=651 (summary in articles/articles.json:11072)"},
{"claim": "'Briarheart Warpstone' is a client place name.", "source": "locale:24730"},
{"claim": "Article 651 was captured by the archive on 2009-12-13 04:13:25, which bounds the posting date to about 2009-12-03/04 given the article's '1 week, 3 days before capture'.", "source": "refs/freerealms-com/cdx-urls.json:9819-9820"},
{"claim": "Day of the Duel (Highroad Junction, 31 Jul 2009, 3-5pm Pacific, Ambassador Pex) is a different place and date. It is not merged with this event, but it may be the same event family.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=173"}
],
"confidence": 0.5,
"open": [
"Year 2009 is reconstructed (R) from the archive capture date and the relative posting date. The article does not print a year.",
"Live status unsure: article 651 announces the duel. No second article, forum post or video confirms it ran.",
"Clock times 3-5 and 9-11 Pacific come from the article summary, which does not give am/pm. They are left out of slots and not wired until the article text is checked.",
"Recurrence unknown: one dated occurrence. Check whether the Day of the Duel series (article 173) recurred and whether it had a Briarheart edition.",
"No items, rewards, NPCs or quests are sourced for this event. Ambassador Pex belongs to article 173 only.",
"Client 'Card Duelist' strings refer to the TCG and are not this event.",
"Not wireable as a recurring schedule row. Admin-start only, and only after live status and times are confirmed."
]}
