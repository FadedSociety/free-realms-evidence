<!-- fleet job=dialog-infer id=wunder-pressure-v3 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[21732, 12719, 8, 1952] model=claude-haiku-5-5 -->
# Under Pressure

{"quest": {"key": "under_pressure", "title": "Under Pressure"},
 "offer": {"locale_id": 29671, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [{"locale_id": 29670, "role": "objective_hint", "speaker": "Sarkin Stonehearth"}],
 "evidence": [
  {"claim": "29669 is the quest title 'Under Pressure'.", "source": "locale:29669 (quest_title)"},
  {"claim": "29671 is a mercenary request to put a stop to the Skullz Roughriders and Thugs, with payment promised ('worth your while'). It is an offer.", "source": "locale:29671 (full text checked, quest_dialog)"},
  {"claim": "29670 is the objective text for this quest, and the Sarkin Stonehearth NPC answer attributes it to Under Pressure.", "source": "locale:29670 (quest_objective, tagged Under Pressure); Sarkin Stonehearth NPC answer"},
  {"claim": "29672 reads as a Skullz turn-in ('you got em' all?'), and the Sarkin NPC answer lists it as quest_complete for Under Pressure. Its client tag hint is Raider Repo, so it is not bound: the rules exclude lines tagged to another quest.", "source": "locale:29672 (quest_dialog, hint Raider Repo); Sarkin Stonehearth NPC answer"},
  {"claim": "No reward line exists for this quest. 29644 is Rizzle's reward line for Robot Woes.", "source": "locale:29644 tag hint"}
 ],
 "confidence": 0.5,
 "open": [
  "complete left null on purpose. The strongest candidate is locale:29672 (Sarkin Stonehearth; its text answers this quest's Skullz objective, and the NPC answer lists it as quest_complete for Under Pressure). It is excluded only because its client tag hint is Raider Repo, and the rules bar lines tagged to another quest. The critiques asked for it to be bound; I did not, because that conflicts with the tag rule. A designer should decide: if the tag is a block artifact, bind 29672 as complete with speaker Sarkin Stonehearth.",
  "offer speaker left null: 29671 names no speaker, its tag is the mob-name string, and the NPC answer does not list it. 'me and my crew' implies Sarkin, the quest giver (npc 9500000851), but that is inference only.",
  "progress null: no client line is tagged as a reminder for Under Pressure.",
  "reward null: the offer promises unspecified payment with no amount or item in client or wiki text; reward kind unknown.",
  "No locale id for the mob name 'Skullz Roughriders and Thugs'; target_locale_id left null.",
  "Predecessor unverified: Ruined Return (locale 29665) is only a candidate; no client line chains it to Under Pressure, so previous is empty.",
  "Level 16 gate from repo notes was not re-verified.",
  "No quest record exists in the repo, so the Raider Repo link (locale 29673 title, lines 29674-29676) cannot be wired yet."
 ],
 "id_check": []}
