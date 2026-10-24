<!-- fleet job=event-infer id=vit-s-your-world-v4 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[7260, 8303, 6, 2804] model=claude-haiku-5-5 -->
# It's Your World

{
 "event": {
  "name": "The Dares E3 Performance (Snowhill stage concert, June 2 2009)",
  "aliases": ["The Dares E3 Performance (wiki The Dares)", "Rock Out with The Dares (article 106 title, from pack, not re-found in lookup)"]
 },
 "kind": "other",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "June 2, 4:00 pm Pacific (single live performance, streamed from E3)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=106 (fact:event); wiki page The Dares; wiki page Bruce (early June 2009)"},
  {"year": 2009, "when": "Pre-launch notice, late May 2009 (approximate, not verified)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=106 (summary: posted 3 days 2 hours before 2009-06-02 capture; post date not exact)"}
 ],
 "recurring": null,
 "zones": ["Snowhill"],
 "npcs": [],
 "quests": [],
 "activities": ["Watch The Dares' live in-game concert on the Snowhill stage"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "The Dares performed a live concert on the Snowhill stage in Free Realms, streamed in real time from E3, on June 2 at 4pm Pacific (article fact).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=106"},
  {"claim": "The concert was to feature the Free Realms theme song 'It's Your World'. Theme song is a separate pack item, not a separate event here.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=106"},
  {"claim": "Players who logged on Free Realms, server 1, at 4pm Pacific could see The Dares E3 Performance live at Snowhill's stage (post-event wording).", "source": "wiki page The Dares"},
  {"claim": "Bruce left the Snowhill Stage vacant in early June 2009 when The Dares held their Live E3 Performance, which gives the 2009 year.", "source": "wiki page Bruce"}
 ],
 "confidence": 0.6,
 "open": [
  "MERGE: the pack name \"It's Your World\" covers several things. This entry is only the June 2 2009 Snowhill concert. The theme song's iTunes release (articleId=132) and music video (articleId=1269, undated) are separate entries and are not included here.",
  "IDENTITY QUESTION: the wiki The Dares page URL slug reads 'e3-2009-free-realms-and-the-dares-set-world-record-concert'. That links a world-record concert to this E3 show, but the wiki text itself does not say so, and article 132 does not name this show. The record alias is NOT adopted. Confirm with an article before adding it.",
  "POST DATE UNVERIFIED: no article gives the posting day. The pre-launch row is approximate (late May 2009, from the 3-day capture offset).",
  "LIVE EVIDENCE: article 106 is worded as a fact about a performed concert, but its date field is empty. Live = yes rests on that fact plus the wiki The Dares and Bruce pages. A post-event dated article would strengthen it.",
  "POSTER: 'Coming to Snowhill, June 2nd 4:00 pm Pacific' appears only as wiki image text (Thedaresposter.jpg). Not re-verified in article text; the article's own wording is 'June 2nd'.",
  "ITEMS NOT ATTACHED: client names carrying 'Dares event' or 'The Dares Event' are unlinked candidates, not items of this show: locale:392265 (Event Boombox - Bouncer), 393083 (Event Controller), 393082 (Dares End Fireworks), 393084 (Event Boombox - Appluad Anim), 392282, 392284, 392286 (Dares Teleport ... during Dares event), 393088, 393090 (Boombox Charge/Cheer), 391674 and 391676 (dance 01/02). Price and currency unknown. Locale 391672 (dev_note) and 391675 (duplicate of 391674) are flagged and not evidence.",
  "NEIGHBOURING CONCERTS: locale:406760 mentions a 'next Dares concert' that needs Freewheelers as security, so there is at least one later Dares concert. It is not this June 2 2009 show, and this entry must not be extended to cover it. The milk-carton rock-collection quest family (locale 403232, 403234, 403250, 408601) is Dares-linked but not tied to this show.",
  "NPCS/QUESTS: The Dares is a band, not an NPC. Bruce was on tour and not at Snowhill for this show. Snowhill concert quests (locale 36861, 36831, 36818) are not tied to this June 2 show. Quests left empty.",
  "KIND: 'other' chosen over 'webcast' because the sources describe an in-game concert streamed from E3, not a web broadcast."
 ],
 "id_check": ["locale:391672 FLAGGED dev_note: not evidence", "locale:391675 FLAGGED duplicate of 391674: not evidence"]
}
