<!-- fleet job=dialog-infer id=wstemming-the-tide-v1 status=done turns=5 usd=0.0037 tokens(read,write,in,out)=[38009, 12061, 12, 3571] model=claude-haiku-5-5 -->
# Stemming the Tide

{"quest": {"key": "stemming_the_tide", "title": "Stemming the Tide"},
 "offer": {"locale_id": 5100926, "speaker": null},
 "progress": {"locale_id": 5100928, "speaker": null},
 "complete": {"locale_id": 5100931, "speaker": null},
 "other_lines": [
  {"locale_id": 5100930, "role": "objective_hint", "speaker": "Crabcake"},
  {"locale_id": 5100972, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is Stemming the Tide (title id 5100929; duplicate 5100970 also reads Stemming the Tide).", "source": "locale:5100929 / locale:5100970"},
  {"claim": "Offer candidate 5100926 explains the black-pearl problem and why it matters; it is tagged to this quest and does not name another task. It explains rather than asks, so the offer role is a best fit.", "source": "locale:5100926"},
  {"claim": "Progress candidate 5100928 tells the player to help defeat the King of Low Tide, matching the single kill objective.", "source": "locale:5100928"},
  {"claim": "Completion candidate 5100931 says the player freed the Cray from the Gloam, which matches this quest's outcome.", "source": "locale:5100931"},
  {"claim": "Cleansing the Pearls completion is 5100927 ('Thank you ... pearls you have purified'), so it is excluded from this quest.", "source": "locale:5100927 with locale:5100924/5100925 (Cleansing the Pearls) and locale:5101409"},
  {"claim": "Objective text is Defeat the King of Low Tide (5100972); King of Low Tide name exists as quest_title id 5101484.", "source": "locale:5100972 / locale:5101484"},
  {"claim": "Crabcake is the giver and the one who speaks the objective hint 5100930.", "source": "npc answer crabcake: dialog list includes locale:5100930 for Stemming the Tide; giver name Crabcake"},
  {"claim": "No reward text found for this quest.", "source": "locale search; wiki/articles search returned none"}
 ],
 "confidence": 0.5,
 "open": [
  "Speaker is null for offer, progress and complete: none of 5100926, 5100928 or 5100931 is attributed to Crabcake or any NPC by the NPC answer or the locale tag. The tag hint names the quest, not a speaker. Crabcake is the giver, so a builder may assign him after checking the NPC table.",
  "Offer/progress/complete mapping is inferred from text, not from a confirmed dialog-table link. Offer 5100926 explains rather than asks.",
  "Giver locale id 5101601 from the quest answer does not resolve in the locale table, so it was not used.",
  "Previous and next links ('Cleansing the Pearls', 'History of the Dojo') were not re-verified here.",
  "Kill count is unverified; a single defeat is assumed from the objective text.",
  "locale:5101564 ('Has the King of Low Tide been freed from the Gloam?') is a quest_dialog that may be a progress reminder, but its hint is '-' and it has no quest tag, so it was not used.",
  "locale:5101673 ('Complete Stemming the Tide.') reads like an achievement or journal line, not NPC dialog, so it was not used.",
  "The NPC id for King of Low Tide and the 5101484 FLAG status were not confirmed. Repo title id 2477341132 is stale."
 ]}
