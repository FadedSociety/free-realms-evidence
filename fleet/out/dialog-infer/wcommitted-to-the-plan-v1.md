<!-- fleet job=dialog-infer id=wcommitted-to-the-plan-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[18197, 10235, 8, 2286] model=claude-haiku-5-5 -->
# Commited To The Plan

{"quest": {"key": "Commited To The Plan", "title": "Commited To The Plan"},
 "offer": {"locale_id": 29663, "speaker": "Noggle Cogloose"},
 "progress": {"locale_id": 29662, "speaker": "Noggle Cogloose"},
 "complete": {"locale_id": 29664, "speaker": "Noggle Cogloose"},
 "other_lines": [{"locale_id": 439896, "role": "objective_hint", "speaker": null}],
 "evidence": [
  {"claim": "29662 is Noggle's reminder to go use the jump pads and find the Legendary Sunstone in the Drake Boneyard; a progress line", "source": "locale:29662; npc answer for Noggle Cogloose lists 29662 as quest_progress for Committed to the Plan"},
  {"claim": "29663 announces step 13 done and tells the player to get started on finding the Legendary Sunstone; the quest-giving/offer line", "source": "locale:29663 text (tagged Drake Boneyard | Commited To The Plan)"},
  {"claim": "29664 reacts to the player reporting no Legendary Sunstone found; the closing line before Ruined Return, so treated as complete", "source": "locale:29664 text (tagged Commited To The Plan); speaker inferred from Noggle's voice, not named by the NPC answer"},
  {"claim": "Objective is 'Look for the Legendary Sunstone'", "source": "locale:439896 (owning quest unconfirmed; same wording as 29663's find-the-sunstone step)"},
  {"claim": "Quest line: previous Noggle Interrupted, next Ruined Return whose requirement is this quest", "source": "wiki Quest:Ruined Return requirements; wiki Noggle Cogloose quest list"},
  {"claim": "No reward line exists for this quest", "source": "no quest_reward locale tagged to it; only 29644 (Rizzle, Robot Woes) is a reward line"}
 ],
 "confidence": 0.5,
 "open": [
  "Mapping of 29663 as offer and 29664 as complete is inferred from text content, not from an explicit dialog-slot record; the NPC answer only attributed 29662 (progress).",
  "29664 speaker is not named in the text or by an NPC answer; Noggle is inferred from voice and the quest chain.",
  "No record_id for the quest exists in the pack; key uses the title.",
  "Reward is null: no reward line found for this quest. The 5 coins attributed to Ruined Return are unverified and not used here.",
  "Whether the completion trigger is the jump-pad step or a later Drake Boneyard step is unverified.",
  "439896 is a client objective string whose owning quest is unconfirmed; it may belong to the wider Legendary Sunstone quest (29645).",
  "Noggle's location (Noggle's Retreat vs Drake Boneyard) is unsettled."
 ]}
