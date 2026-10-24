<!-- fleet job=dialog-infer id=wbigfoot-s-endangered-v1 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[22050, 8252, 10, 2726] model=claude-haiku-5-5 -->
# Bigfoot's Endangered

{"quest": {"key": "bigfoots_endangered", "title": "Bigfoot's Endangered"},
 "offer": {"locale_id": 429370, "speaker": null},
 "progress": {"locale_id": 429380, "speaker": null},
 "complete": {"locale_id": 429373, "speaker": null},
 "other_lines": [
  {"locale_id": 429372, "role": "other", "speaker": "Counselor Jacen"},
  {"locale_id": 429375, "role": "objective_hint", "speaker": null},
  {"locale_id": 429376, "role": "objective_hint", "speaker": null},
  {"locale_id": 429378, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is Bigfoot's Endangered", "source": "locale:429371"},
  {"claim": "429370 explains the task and asks the player to find and chase off the Camp Chatty counselors, so it is the offer line", "source": "locale:429370"},
  {"claim": "429380 asks whether the counselors were chased off yet, so it is the in-progress reminder", "source": "locale:429380"},
  {"claim": "429373 says Bigfoot will be OK and thanks the player, so it is the completion line", "source": "locale:429373"},
  {"claim": "429372 is attributed to Counselor Jacen as a quest offer in the NPC answer; it is a narrated description ('Help him out.') and is kept as an alternate offer text, not the primary offer", "source": "npc answer: counselor jacen, locale:429372"},
  {"claim": "429375 and 429376 are objective texts for chasing off / defeating the counselors", "source": "locale:429375, locale:429376"},
  {"claim": "429378 is an objective text ('Return to Counselor Jacen'), not dialog; the NPC answer's quest_progress label for it is not treated as a spoken line", "source": "locale:429378"},
  {"claim": "No reward line exists in the client for this quest", "source": "repo note Bigfoot Defender.md:57 lists rewards as unknown; no tagged reward text found"}
 ],
 "confidence": 0.6,
 "open": [
  "No client line names the speaker of 429370, 429380 or 429373. Counselor Jacen is the giver per the wiki and repo NPC note, but the NPC answer attributes only 429372 and 429378 to him, so speaker is left null for the offer, progress and complete lines.",
  "Offer choice: 429370 is used because it carries the task text. 429372 is an alternative offer candidate that the NPC answer attributes to Jacen; a builder may pick it instead.",
  "429378 was listed as quest_progress by the NPC answer but is an objective string, so it is placed in other_lines as an objective hint.",
  "No reward line found; rewards remain unknown.",
  "Kill targets beyond Kaela (Edmond, Tyra, Jake) have no client ids; 429404 belongs to the Bigfoot battle cluster and is not wired here.",
  "Order relative to the Bigfoot Defender battle and the next quest in the chain is not settled by text; the repeat cooldown is unknown.",
  "Bigfoot Thrash lines (429387, 429392-429398) belong to the battle and are not this quest's dialog."
 ]}
