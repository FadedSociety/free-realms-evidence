<!-- fleet job=dialog-infer id=wrescue-in-the-ruins-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6983, 8749, 6, 2031] model=claude-haiku-5-5 -->
# Rescue In The Ruins

{"quest": {"key": "rescue_in_the_ruins", "title": "Rescue In The Ruins"},
 "offer": {"locale_id": 29686, "speaker": "Sarkin Stonehearth"},
 "progress": {"locale_id": 440106, "speaker": "Assistant Bogse"},
 "complete": {"locale_id": 29688, "speaker": "Assistant Bogse"},
 "other_lines": [
  {"locale_id": 29687, "role": "followup", "speaker": "Assistant Bogse"},
  {"locale_id": 439926, "role": "objective_hint", "speaker": null},
  {"locale_id": 439929, "role": "objective_hint", "speaker": null},
  {"locale_id": 439930, "role": "objective_hint", "speaker": null},
  {"locale_id": 439932, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer: Sarkin explains Bogse vanished and asks the player to go after him in the Precursor Ruins", "source": "locale:29686 (quest_dialog, tagged Precursor Ruins | Sarkin); npc answer for Sarkin lists it as quest_offer for Rescue In The Ruins"},
  {"claim": "Progress reminder: Bogse asks whether the player found him in the Precursor Ruins and urges haste", "source": "locale:440106 (quest_dialog, tagged Assistant Bogse; text names finding Bogse in the Precursor Ruins). Not in the earlier pack; found via lookup"},
  {"claim": "Complete: Bogse thanks the player for saving him and offers future help from camp", "source": "locale:29688 (quest_dialog, tagged Precursor Ruins | Assistant Bogse)"},
  {"claim": "Title and objective texts for the quest", "source": "locale:29685 (title), 439926/439929/439930/439932 (objectives)"},
  {"claim": "29687 is Bogse's first in-quest line: he says the spiders grabbed him and asks the player to save him; it explains the task rather than reminding progress or thanking, so it is not used as progress", "source": "locale:29687"}
 ],
 "confidence": 0.7,
 "open": [
  "Progress choice 440106 is inferred: it is tagged to Assistant Bogse, not Sarkin, and its text names finding Bogse in the Precursor Ruins, but no NPC answer attributed it. Speaker is from the tag hint.",
  "Complete line 29688 is spoken by Bogse per its tag hint; the quest's return objective is to Sarkin, so a builder may need to check whether it is delivered by Sarkin or Bogse in-game.",
  "Reward: no confirmed client reward line. Cactoid is wiki-only and unverified, so reward is left out of the result.",
  "npc_id for Sarkin Stonehearth and the Precursor Ruins dungeon record are unresolved (not confirmed in this pass).",
  "next in the quest line is unresolved and is not a confirmed chain end."
 ]}
