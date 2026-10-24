<!-- fleet job=dialog-infer id=wunmasking-the-villain-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[17655, 9566, 8, 2630] model=claude-haiku-5-5 -->
# Unmasking the Villain

{"quest": {"key": "unmasking-the-villain", "title": "Unmasking the Villain"},
 "offer": {"locale_id": 441744, "speaker": null},
 "progress": {"locale_id": 441745, "speaker": null},
 "complete": {"locale_id": 441748, "speaker": null},
 "other_lines": [
  {"locale_id": 441747, "role": "objective_hint", "speaker": "Mayor McFairy"},
  {"locale_id": 441732, "role": "followup", "speaker": null},
  {"locale_id": 442016, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Unmasking the Villain' (Merry Vale)", "source": "locale:441746 (quest_title)"},
  {"claim": "Offer-stage line: says it will forge an artifact revealing The Dark One's hidden location, and asks the player to wait while it is readied", "source": "locale:441744 full text"},
  {"claim": "Progress-stage line: hands over the tool ('Keep this with you'), says The Dark One is deep in the caverns leading to the Den of Secrets, and tells the player to find him and stop his dark magic", "source": "locale:441745 full text"},
  {"claim": "Complete-stage line: names a Gloam necromancer as the defeated foe and thanks/credits the player and gang", "source": "locale:441748"},
  {"claim": "Objective text naming Mayor McFairy as the one who gave the tools", "source": "locale:441747"},
  {"claim": "Mayor McFairy is listed as giver of Unmasking the Villain, with no attributed dialog lines", "source": "npc answer 'mayor mcfairy' (quests_given; dialog [])"},
  {"claim": "Quest is in the Merry Vale series after 'Mayor McFairy!' (441742), but the link is by repo ordering only", "source": "previous pass / repo NPCs - Merry Vale.md:198"},
  {"claim": "Reward text not found", "source": "no reward locale line tagged to this quest"}
 ],
 "confidence": 0.5,
 "open": [
  "No speaker is attributed to offer 441744, progress 441745 or complete 441748 by any tag, text name or NPC dialog answer. All three are null. The Mayor McFairy npc answer lists the quest but carries no dialog, so attributing the lines to him would be a guess.",
  "Giver Mayor McFairy is supported only by the npc answer's quests_given list and objective 441747. npc_id is unknown.",
  "Offer vs progress is a judgement call: 441745 explains the task and reads more like a reminder/hand-off, while 441744 is a lead-in ('give me a few moments') that does not ask anything. Mapping follows the earlier pass.",
  "No quest record id exists; one must be created from title 441746 and objective 442016.",
  "Next link in the series is unverified. The earlier 'No More Necro' / 4420xxx ids could not be confirmed and are not used.",
  "'The Dark One' has no NPC record or npc_name string. Its identity with the Gloam necromancer in 441748 is inference only.",
  "No reward line found; repo reward (4100297378, boots) belongs to Necronomicus Unleashed and is excluded.",
  "No critiques were carried in the pack beyond these open items."
 ]}
