<!-- fleet job=dialog-infer id=wthe-eggcellent-egg-hunt-v2 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[32774, 12932, 10, 2461] model=claude-haiku-5-5 -->
# The Eggcellent Egg Hunt

{"quest": {"key": "The Eggcellent Egg Hunt", "title": "The Eggcellent Egg Hunt"},
 "offer": {"locale_id": 5100090, "speaker": "Alyssa Eggelyn"},
 "progress": null,
 "complete": {"locale_id": 5100089, "speaker": "Alyssa Eggelyn"},
 "other_lines": [
  {"locale_id": 5100015, "role": "reward", "speaker": null},
  {"locale_id": 5100012, "role": "other", "speaker": null},
  {"locale_id": 5100014, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Complete line 5100089 thanks the player for finding the egg and gives a special egg to open on Spring Eggstravaganza day. Its text matches the wiki's 'Hooray you found it...' completion quote, which the wiki places on the Eggcellent Egg Hunt page (lookup on the quote returned the wiki Eggcellent page).", "source": "locale:5100089; lookup wiki Quest:The Eggcellent Egg Hunt"},
  {"claim": "Offer candidate 5100090 asks the player to find Alyssa's missing egg ('please use your special skills to find my missing egg'), which fits an offer's ask role and matches the wiki Goals line that one of Alyssa's eggs has been hidden. It is untagged to any quest, so the link is text-based only.", "source": "locale:5100090; wiki Quest:The Eggcellent Egg Hunt Requirements/Goals"},
  {"claim": "Alyssa Eggelyn (npc_name locale:5100004) is the giver and speaker of 5100089 and 5100090.", "source": "npc answer alyssa eggelyn; wiki giver; locale:5100004"},
  {"claim": "Reward line 5100015 is tagged to this quest: colour all 4 eggs to open the special egg on March 31st.", "source": "locale:5100015 (quest_reward tag)"},
  {"claim": "Title 5100012 is the unflagged title of this quest. 5100014 ('The Eggcitingly Eggcellent Egg Hunt') is tagged quest_title with hint The Eggcellent Egg Hunt in the client, so it is listed as a tagged title line, not as another quest's line. 5100013 is FLAGged and excluded.", "source": "locale:5100012 / 5100014 / 5100013"}
 ],
 "confidence": 0.55,
 "open": [
  "Offer 5100090 is untagged and the NPC answer classed it as quest_progress. It is bound on text fit (an ask to find the missing egg) and the wiki Goals match. Treat it as a caveated candidate. Its 'did it again' wording could also belong to a sibling quest (5100094 is the Eggxtremely offer), so verify against a quest record before wiring.",
  "Complete 5100089 is untagged; its link to this quest rests on the wiki completion quote match. Sibling completes 5100091 and 5100093 were not bound.",
  "Progress is null: no in-progress reminder line for this quest was found in the client.",
  "Objective text has no confirmed locale id. 5100006 is tagged to The Spring Eggstravaganza and was not used.",
  "The lake location (northernmost point of the lake bordering Blackspore Swamp) comes from the wiki only, with no locale id.",
  "Reward items (Egg Coloring Kit, Alyssa's Oddly Swirled Egg) have no locale ids. Jack the Rabbit pet pal is claimed during the event per the wiki; no locale id, not included as a dialog line.",
  "No coin reward was found.",
  "Alyssa's standing spot (Pixiewood Hills) is wiki-only and unverified. Live status rests on the wiki's 2013 dates and the unflagged title, with no live-build record.",
  "Locale 5100094 (Eggxtremely offer) and 5100092 (Eggcitingly offer) belong to sibling quests and are not used."
 ]}
