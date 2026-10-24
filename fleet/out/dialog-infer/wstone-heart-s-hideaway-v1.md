<!-- fleet job=dialog-infer id=wstone-heart-s-hideaway-v1 status=done turns=8 usd=0.0038 tokens(read,write,in,out)=[53152, 14222, 18, 3077] model=claude-haiku-5-5 -->
# Stone Heart's Hideaway

{"quest": {"key": "stone_heart_s_hideaway", "title": "Stone Heart's Hideaway"},
 "offer": {"locale_id": 427180, "speaker": "Cudip"},
 "progress": {"locale_id": 427520, "speaker": "Cudip"},
 "complete": {"locale_id": 427183, "speaker": "Cudip"},
 "other_lines": [
  {"locale_id": 427533, "role": "objective_hint", "speaker": null},
  {"locale_id": 427517, "role": "objective_hint", "speaker": null},
  {"locale_id": 427513, "role": "objective_hint", "speaker": null},
  {"locale_id": 427519, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "427180 is the offer: Cudip says he has begun a new top secret solution, the main ingredient is only in Stone Heart's Hideaway, and he cannot go in himself but 'you could...'", "source": "locale:427180 (quest_dialog, tagged Sacred Grove/Cudip); npc answer lists 427180 for Cudip"},
  {"claim": "427520 is the progress reminder: the flowers cannot be found standing outside; the player must enter Stone Heart's Hideaway", "source": "locale:427520 (quest_objective, Merry Vale/Cudip); npc answer lists 427180 as progress but its text is the reminder, so 427520 is used for progress"},
  {"claim": "427183 is the completion line: 'These are just what I needed. Let the experimentation begin!' reacts to delivered flowers, so it is the thank/complete line", "source": "locale:427183 text; npc answer lists 427183 as quest_complete for this quest by Cudip"},
  {"claim": "Entrance objective text", "source": "locale:427533 (western side of Merry Vale)"},
  {"claim": "Flower collect objective text, with flowers target name", "source": "locale:427517, 427513; target name 'flowers' locale:427516"},
  {"claim": "Deliver objective: bring flowers back to Cudip in Merry Vale", "source": "locale:427519"},
  {"claim": "No reward line exists in the client for this daily; rewards are unknown", "source": "repo note Stone Heart's Hideaway.md line 61 ('Cudip's daily quest: Rewards unknown.')"}
 ],
 "confidence": 0.6,
 "open": [
  "No quest record id; a builder must create one. Title is the instance name (locale:426971); no separate quest-title string was found.",
  "Cudip's npc_id is not verified (repo note gives ucdt 445081455 / ugdt 3204778426, unconfirmed).",
  "Offer 427180 is tagged to the Sacred Grove hint, not Merry Vale. Its text names this hideaway and fits an offer, so it is kept, but the hint conflict is unresolved.",
  "The earlier pass listed 427180 as progress; I moved it to offer because its text introduces the task and asks the player to go, while 427520 reads as the in-progress reminder.",
  "Complete line 427183 is attributed to Cudip by the NPC answer and fits a thank-you, but it carries no quest hint of its own in the client index.",
  "Flower item name id and required count are not in the client; 427516 is the only flower string, and no count is known.",
  "No reward line or reward amounts found; reward left as none.",
  "Previous/next quest links (Softening the Stone before, unknown after) rest on the wiki order, not client text."
 ]}
