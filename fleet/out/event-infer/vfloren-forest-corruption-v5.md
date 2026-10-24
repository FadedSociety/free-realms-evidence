<!-- fleet job=event-infer id=vfloren-forest-corruption-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6879, 8959, 6, 2185] model=claude-haiku-5-5 -->
# Floren Forest corruption

```json
{
 "event": {
   "name": "Floren Forest corruption",
   "aliases": ["The Tainted Forest (quest title, locale:417359, pack-cited, not re-checked here)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Floren Forest"],
 "npcs": ["Ozymandias (shared with Changeling Curse, see open)", "Corrupted Floren (wiki and video nameplate only, not text-checked)"],
 "quests": [],
 "activities": [
   "Fight into the dark woods of Floren Forest to find and defeat the source of the corruption (http://www.freerealms.com:80/article/detail.action?articleId=904)",
   "Investigate the source of the problem (locale:15797: 'The most unnatural of magic is taking hold of the Floren Forest. Investigate the source of the problem.')",
   "Defeat the source of the problem, Ozymandias (locale:16508)",
   "Investigate the stone idol in Floren Forest (locale:22256; the idol is described at locale:21970)",
   "Look into the fragment found in Floren Forest and take it to Lief (locale:23096, 23103)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "Floren were corrupted and now attack on sight; players are invited to fight into the dark woods to find and defeat the source of the corruption. Article is undated.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=904"},
   {"claim": "Floren Forest is described as corrupted by something evil, with travel deep into the forest to find and defeat the source.", "source": "locale:15789"},
   {"claim": "Ozymandias is named as the source of the corruption in the Floren Forest.", "source": "locale:16508"},
   {"claim": "Sakka asks the player to investigate a stone idol with a wicked visage in Floren Forest; hostile floren are mentioned in the same chain.", "source": "locale:21970, 21976, 22256"}
 ],
 "confidence": 0.3,
 "open": [
   "No dated source. The only article (articleId=904) has date null and no year, month or days. Occurrences stay empty, and the event cannot be placed on a calendar or marked wireable.",
   "Live status unknown. Article 904 reads as an area launch promotion, which may be a plan rather than a confirmed live run.",
   "Merged name: the pack may combine two things. (a) the Floren Forest area launch (article 904) and (b) the corruption quest chain (The Tainted Forest, the Ozymandias and stone-idol steps). Treat them as separate candidates until a dated source ties them.",
   "Ozymandias is shared with the Changeling Curse storyline (locale:16404, 16419-16424, 16507, 16508, 93968). Its tie to this corruption rests on locale:16508 and the wiki Floren Forest page only.",
   "Activity wording corrected: the pack's 'Investigate the corruption in Floren Forest' is not an exact quote. Exact text of locale:15797 is 'Investigate the source of the problem.' Locale 15796 was not re-read here.",
   "Pack-cited ids locale:417360, 417362, 417366, 442653 and 417358/417361 were not re-read in this pass. The critique reports their text matches the activity wording, but that is pack-reported.",
   "Quest chain steps not confirmed as exact titles: 'The Tainted Forest' (locale:417359) is the only title in the pack, and I did not re-check it. Stone idol and fragment steps (22256, 23096, 23103, 24973, 21976, 24972, 37685) are on-topic, but their quest titles are unknown.",
   "Video OCR is disputed for a bonus objective ('Defeat the Floren! Bonus: Restore Natural' vs 'Floral'). Excluded: it is not tied to this event by any source.",
   "Items, prices and rewards: none tied to this event by any source. Blighted Floren (locale:16040) and Withering Floren (locale:15961, flagged as a truncated fragment) are not tied. Withering Floren quest steps (locale:38408, 38410) belong to a different nectar-tea quest and are excluded.",
   "Vile Floren and Northern Wilds appear only on wiki pages with no event tie, so they are excluded.",
   "Recurrence: none. No webcast, contest, weekly or promotion evidence in the pack."
 ]
}
```
