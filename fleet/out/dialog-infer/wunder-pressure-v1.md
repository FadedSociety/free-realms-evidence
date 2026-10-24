<!-- fleet job=dialog-infer id=wunder-pressure-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16325, 10394, 8, 2737] model=claude-haiku-5-5 -->
# Under Pressure

{"quest": {"key": "under_pressure", "title": "Under Pressure"},
 "offer": {"locale_id": 29671, "speaker": "Sarkin Stonehearth"},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 29670, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "29671 is the offer: a mercenary request ('You look pretty tough... mercenary work for me and my crew') asking the player to stop the Skullz Roughriders and Thugs, with the 'worth your while' payment line.", "source": "locale:29671 (full text checked)"},
  {"claim": "Speaker for the offer is Sarkin Stonehearth: the text speaks as the crew leader ('me and my crew') and Sarkin is the quest giver (npc 9500000851, locale 440348). No NPC answer explicitly attributes 29671 itself.", "source": "locale:29671 + earlier quest answer giver field + Sarkin NPC answer"},
  {"claim": "29670 is the quest objective description (dealing with the Skullz Roughriders and Thugs), tagged to Under Pressure, so it is an objective hint, not progress or completion dialog.", "source": "locale:29670 (quest_objective, hint Under Pressure)"},
  {"claim": "29669 is the quest title 'Under Pressure'.", "source": "locale:29669"},
  {"claim": "29672 ('Welcome back... you got em' all? ... impressive') reads like a turn-in, and the Sarkin NPC answer lists it as quest_complete for Under Pressure, but its client tag hint is Raider Repo and locale 29673 ('Raider Repo') follows it. Per the tag rule it is not used as this quest's complete line.", "source": "locale:29672 tag hint; Sarkin NPC answer"},
  {"claim": "No reward line exists for this quest. 29644 is Rizzle's reward line for Robot Woes, not this quest.", "source": "locale:29644 tag hint"}
 ],
 "confidence": 0.5,
 "open": [
  "complete is null: the only candidate is 29672, which is tagged to Raider Repo and is followed by the Raider Repo title; the Sarkin NPC answer's quest_complete attribution conflicts with that tag. Needs a designer decision or a confirmed turn-in id.",
  "progress is null: no client line is tagged as a reminder for Under Pressure.",
  "reward is null: the offer promises unspecified payment ('I'll make it worth your while') with no amount or item in the client text.",
  "Speaker of 29671 is inferred from the quest giver and the first-person 'me and my crew' wording, not from a direct NPC-answer attribution.",
  "Predecessor is unverified: Ruined Return (locale 29665) is only a candidate; no client line chains it to Under Pressure, so previous is left empty.",
  "Target mob has no locale id for 'Skullz Roughriders and Thugs'; target_locale_id left null.",
  "Level 16 gate from repo notes was not re-verified.",
  "No quest record exists in the repo, so the Raider Repo link cannot be wired yet."
 ]}
