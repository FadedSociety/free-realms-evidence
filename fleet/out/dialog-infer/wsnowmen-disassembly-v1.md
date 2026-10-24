<!-- fleet job=dialog-infer id=wsnowmen-disassembly-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[7975, 9075, 6, 1628] model=claude-haiku-5-5 -->
# Snowmen Disassembly

{"quest": {"key": "Snowmen Disassembly", "title": "Snowmen Disassembly"},
 "offer": {"locale_id": 420291, "speaker": "Candi Ivy"},
 "progress": null,
 "complete": {"locale_id": 420294, "speaker": "Candi Ivy"},
 "other_lines": [
  {"locale_id": 420293, "role": "objective_hint", "speaker": null},
  {"locale_id": 420292, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line asks the player to help thin out snowmen ('Will you help me thin out their numbers?'), matching an offer role", "source": "locale:420291 (quest_dialog, Snowhill, Snowmen Disassembly)"},
  {"claim": "Complete line thanks the player ('Well done, [*player*]...')", "source": "locale:420294 (quest_dialog, Snowhill, Snowmen Disassembly)"},
  {"claim": "Quest title is Snowmen Disassembly", "source": "locale:420292 (quest_title)"},
  {"claim": "Objective text: thin out present-snatching snowmen for Candi", "source": "locale:420293 (quest_objective)"},
  {"claim": "Candi Ivy is the giver and the one who offers and completes this quest", "source": "npc answer 'candi ivy' lists Snowmen Disassembly in quests_given; wiki Candi Ivy quest list includes [Snowmen] [Disassembly]; speaker of 420291 is implied by its text ('I can't protect the Gifting Tree') and the quest hint"},
  {"claim": "Reward is a Subarctic Winterwear Jacket, acquired by completing the quest", "source": "wiki page Subarctic Winterwear Jacket only; no client reward line found"}
 ],
 "confidence": 0.6,
 "open": [
  "No progress line exists in the client tagged to this quest; slot left null. 420290 ('Nice work! This should definitely slow down...') belongs to The Great Robgoblin Robbery Ring and was not used.",
  "Speaker of 420294 is not stated in its text; attributed to Candi Ivy from the quest hint and npc answer. 420291 speaker is likewise inferred.",
  "Objective kind/target/count unresolved: no client line links 420292 to a kill verb or target. Video-derived 'Knock out Snowmen 5/100' is not client text and is not used.",
  "Client lines 420661/420662 are not tagged to this quest and are not used.",
  "Reward: jacket comes from the wiki only; coin reward unknown. No reward locale line, so reward slot is absent from other_lines.",
  "Live status unsettled: the 'membership-exclusive' note is wiki-only, not client evidence. Quest record id and giver npc_id not resolved."
 ],
 "confidence_note": "Locale ids for offer, complete and title are verified against the locale table."}
