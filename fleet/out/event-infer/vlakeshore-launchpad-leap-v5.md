<!-- fleet job=event-infer id=vlakeshore-launchpad-leap-v5 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[7954, 10325, 6, 3503] model=claude-haiku-5-5 -->
# Lakeshore Launchpad Leap

## Launch Pad Leap (community event): two announced runs, filed separately

The pack's single record merged two dated announcements under one name. Split into two records, as the calendar critique asked. Both are announcements; neither is confirmed as run. `live` is "unsure" for both.

### Record A: Seaside Launch Pad Leap (Jan 2010)
```json
{"event": {"name": "Seaside Launch Pad Leap", "aliases": ["Launch Pad Leap", "Launchpad Leap", "Seaside Launchpad Leap"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [{"year": 2010, "when": "Fri Jan 29, 2010 (announced), Server 1, Seaside beach; 3pm Pacific (U.S./Latin America) start as announced", "source": "http://www.freerealms.com:80/article/detail.action?articleId=906 (2010-01-29)"}],
 "recurring": null,
 "zones": ["Seaside (beach)"],
 "npcs": [],
 "quests": [],
 "activities": ["Meet on the Seaside beach and bounce on launch pads together as a group (announced)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 906 is dated 2010-01-29 and invites players to meet on the Seaside beach for a Launch Pad Leap on Server 1. Quote: 'Meet up on the beach and we'll...'.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=906 (2010-01-29)"},
  {"claim": "Article 906 gives the U.S./Latin America start as '3pm Pacific Time (U.S. and Latin America) Server 1'.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=906 (2010-01-29)"},
  {"claim": "Locale 31302 (Snow Day: Launch Pad Leap) reads 'Head to the beach where we'll be enjoying group launch pad jumping! SERVER 1'. This matches article 906's Seaside beach, Server 1 wording.", "source": "locale:31302"}],
 "confidence": 0.4,
 "open": [
  "The article 906 summary says 'was held', but the quote is an announcement. Treat as announced until a post-event report confirms the run.",
  "Snow Day link: locales 31301, 31302 ('Snow Day: Launch Pad Leap', beach, Server 1) and 426677/426678 ('Snow Day: Snowhill Leap', Snowhill) name the Launch Pad Leap with the Snow Days event. Snow Days is a holiday series (locales 1653 'Snow Days Are Back!', 15043-15048, 436455-436460, 441081). The client ties Launch Pad Leap to Snow Days by name, so it may be a Snow Days activity. The pack does not give Snow Days dates for the Seaside run, so this is not confirmed here. Snow Days as a whole is a separate record to check.",
  "The article gives 'Pacific 9:00am / 6:00pm GMT' for UK/Europe in some announcements. That GMT figure does not match Pacific time in January (PST, 9am = 17:00 GMT). Not used for scheduling. Pacific time only.",
  "No cadence is stated. recurring is null.",
  "No NPC, quest, item, price or reward is tied to this run in the pack. Locale 7038 'Seaside Launchpad Leap' is a name match only. Locale 7117 'Launchpad Leap Party' names a Seaside party with no NPC or date.",
  "Locale 426819 'ability - Launch Pad Leap' is an ability name, not event content."
 ]}
```

### Record B: Lakeshore Launch Pad Leap (Apr 2010)
```json
{"event": {"name": "Lakeshore Launch Pad Leap", "aliases": ["Launch Pad Leap", "Launchpad Leap", "Community Event: Lakeshore Launch Pad Leap"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [{"year": 2010, "when": "Thu Apr 15, 2010 (announced), Server 1, Lakeshore dock; 3pm Pacific (U.S./Latin America) start as announced", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1254 (2010-04-15)"}],
 "recurring": null,
 "zones": ["Lakeshore (dock)"],
 "npcs": [],
 "quests": [],
 "activities": ["Meet on the Lakeshore dock and bounce on the launch pads together (announced)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 1254 (2010-04-15) calls it 'This week's Community Event is a Launch Pad Leap in Lakeshore! Meet up on the dock'.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1254 (2010-04-15)"},
  {"claim": "Article 1254 gives '3pm Pacific Time (U.S. and Latin America) Server 1' and '9:00am Pacific Time / 6:00pm GMT (UK and Europe) Server 1'. Only the Pacific times are used here.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1254 (2010-04-15)"},
  {"claim": "Locale 6538 names 'Community Event: Lakeshore Launch Pad Leap'.", "source": "locale:6538"}],
 "confidence": 0.4,
 "open": [
  "'This week's Community Event' hints at a weekly slot, but one article does not establish a cadence. recurring is null.",
  "The 'then dance at a nearby dock' step appears only in the model-written summary, not in a quote. Excluded.",
  "The 6pm GMT figure conflicts with April PDT (9am PDT = 16:00 GMT). Not used for scheduling.",
  "Locale 31301 'Snow Day: Launch Pad Leap' may link this run to the Snow Days series. Not confirmed; see Record A.",
  "No NPC, quest, item or reward is tied to this run in the pack."
 ]}
```

### Notes for the rebuild
- Neither record is wireable yet. Both are announcements with no post-event confirmation, no cadence and no item or NPC tie.
- The pack's "was held" facts are not confirmed runs. The quotes are announcements.
- Snow Days (holiday series, locales 1653, 15043-15048, 436455-436460, 441081) is the likely parent of the Snow Day Launch Pad Leap strings. It needs its own record with dated articles before either run is linked to it.
- Article 1830 (Snowhill launchpad party) and article 1435 (launchpad housing item) were not re-checked here.
