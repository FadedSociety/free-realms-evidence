<!-- fleet job=event-infer id=vfloren-forest-corruption-v6 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[6518, 6758, 6, 1839] model=claude-haiku-5-5 -->
# Floren Forest corruption

```json
{
  "event": {"name": "Floren Forest corruption (unresolved: area-launch candidate and quest-chain candidate, not confirmed as one event)", "aliases": ["The Tainted Forest (quest title per locale:417359, not dated or tied to a live run)"]},
  "kind": "update",
  "live": "unsure",
  "occurrences": [],
  "recurring": null,
  "zones": ["Floren Forest"],
  "npcs": ["Ozymandias (shared with the Changeling Curse storyline; not scheduled as corruption-only)"],
  "quests": [],
  "activities": [
    "Fight into the dark woods of Floren Forest to find and defeat the source of the corruption (http://www.freerealms.com:80/article/detail.action?articleId=904, undated)",
    "Investigate the source of the problem (locale:15797, text-supported, undated)",
    "Defeat the source of the problem, Ozymandias (locale:16508; shared text block with Changeling Curse locale:16404, 16419-16424, 16507)"
  ],
  "items": [],
  "rewards": [],
  "evidence": [
    {"claim": "Article 'Explore the Floren Forest' says the Floren have been corrupted and now attack on sight, and invites players into the dark woods to defeat the source. Date is null.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=904"},
    {"claim": "Floren Forest is described as corrupted by something evil, with the source to be found deep in the forest.", "source": "locale:15789"},
    {"claim": "Ozymandias is named as the source of the problem in Floren Forest (text-supported; overlaps the Changeling Curse block).", "source": "locale:16508"},
    {"claim": "Investigate the source of the problem (exact text).", "source": "locale:15797"}
  ],
  "confidence": 0.2,
  "open": [
    "No dated source exists in the pack or in a lookup of articles and wiki for Floren Forest corruption or Ozymandias. Occurrences are empty and the event cannot be placed on a calendar.",
    "Live status unknown. Article 904 reads as an area-launch promotion and may be a plan. Do not treat it as a confirmed live run.",
    "Merged name: the area launch (article 904) and the corruption quest chain (The Tainted Forest, Ozymandias boss, stone idol) are probably different things. Keep them as separate candidates until a dated source ties them.",
    "Ozymandias is shared with Changeling Curse (locale:16404, 16419-16424, 16507, 16508). Its tie to corruption rests on locale:16508 and is not resolved.",
    "Stone idol and fragment steps (locale:22256, 21976, 24972, 23096, 23103, 24973, 37685) are on-topic but not confirmed live. Locale:21970 and 23096 are flagged not_live (cut quest), so they are excluded as live evidence. Their quest titles are unchecked.",
    "Items, prices and rewards: none tied to this event by any source. Blighted Floren (locale:16040), Withering Floren (locale:15961, flagged truncated) and the nectar-tea quest steps (locale:38408, 38410) are excluded. Vile Floren and Northern Wilds have no event tie.",
    "Video OCR for a bonus objective ('Restore Natural' vs 'Floral') is disputed and not tied to this event; excluded.",
    "'Corrupted Floren' NPC is from wiki and video nameplate only and not text-checked; left unverified.",
    "Recurrence: none. No webcast, contest, weekly or promotion evidence in the pack.",
    "Pack-cited ids locale:417358, 417359, 417360, 417361, 417362, 417366 and 442653 were not re-read in this pass; their text is pack-reported only."
  ],
  "confidence_note": "Not wireable. Needs a dated article (year and month) for article 904 or a client-side date before it goes on the calendar."
}
```
