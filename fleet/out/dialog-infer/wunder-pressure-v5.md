<!-- fleet job=dialog-infer id=wunder-pressure-v5 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[22202, 12107, 8, 2139] model=claude-haiku-5-5 -->
# Under Pressure

{"quest": {"key": "under_pressure", "title": "Under Pressure"},
 "offer": {"locale_id": 29671, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 29670, "role": "objective_hint", "speaker": "Sarkin Stonehearth"}
 ],
 "evidence": [
  {"claim": "29669 is the quest title 'Under Pressure'.", "source": "locale:29669 (quest_title)"},
  {"claim": "29671 is a mercenary request to stop the Skullz Roughriders and Thugs for pay, so it fits the offer role.", "source": "locale:29671 (quest_dialog, text verified)"},
  {"claim": "29670 is this quest's objective text (Skullz Roughriders and Thugs harassing Sarkin's crew).", "source": "locale:29670 (quest_objective, tagged Under Pressure, text verified); Sarkin Stonehearth NPC answer"},
  {"claim": "29672 text is a Skullz turn-in ('you got em all?'), which fits complete, but its client tag is Raider Repo. The tag rule excludes lines tagged to another quest, so it is not bound here.", "source": "locale:29672 (quest_dialog, hint Raider Repo, text verified); Sarkin Stonehearth NPC answer lists it as quest_complete for Under Pressure"},
  {"claim": "Sarkin Stonehearth is the giver of Under Pressure (npc 9500000851, locale 440348) and is listed as the Dig's level 16 giver for this quest.", "source": "wiki Sunstone Valley 'The Dig' entry; repo answer"},
  {"claim": "29674-29676 are Raider Repo progress/offer lines and 29673 is its title; none belong to Under Pressure.", "source": "locale:29673-29676 tags"}
 ],
 "confidence": 0.5,
 "open": [
  "complete left null on purpose. 29672 is the only Skullz turn-in candidate and its text fits, and the Sarkin NPC answer lists it as quest_complete for Under Pressure. But its client tag is 'Raider Repo', and the rules exclude lines tagged to another quest. The critiques asked to bind it anyway; I did not override the tag rule. If a designer confirms the tag is a chain artifact, bind complete = 29672 with speaker Sarkin Stonehearth. Until then wireable is false.",
  "offer.speaker left null: 29671 has no speaker name in its text, its tag is the mob-name string, and no NPC answer attributes it to Sarkin. 'me and my crew' and the giver listing suggest Sarkin, but that is not a named attribution.",
  "progress null: no client line tagged to Under Pressure is a reminder.",
  "reward null: 29671 promises payment ('I'll make it worth your while') with no amount or item; no reward line is tagged to this quest. 29644 is Robot Woes' reward line and is not used.",
  "No locale id for the mob name 'Skullz Roughriders and Thugs'; target_locale_id left null.",
  "Predecessor unverified: Ruined Return (locale 29665) is only an unverified candidate with no chaining client line, so previous is empty.",
  "Level 16 gate from repo notes was not re-verified.",
  "No quest record exists in the repo, so the Raider Repo follow-up (locale 29673-29676) cannot be wired yet."
 ]}
