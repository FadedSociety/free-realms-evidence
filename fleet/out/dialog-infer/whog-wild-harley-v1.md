<!-- fleet job=dialog-infer id=whog-wild-harley-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[15129, 10717, 8, 2889] model=claude-haiku-5-5 -->
# Hog Wild Harley

{"quest": {"key": "hog_wild_harley", "title": "Hog Wild Harley"},
 "offer": {"locale_id": 29615, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 29614, "role": "objective_hint", "speaker": null},
  {"locale_id": 439812, "role": "objective_hint", "speaker": null},
  {"locale_id": 29616, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "29615 is the offer: asks the player to bring Harley back to Pete ('will you bring Harley back to me?'), matching the offer role.", "source": "locale:29615"},
  {"claim": "29614 is the quest objective summary (find Harley and escort her to safety); it is quest_objective type, not dialog, so it is not used as a slot.", "source": "locale:29614"},
  {"claim": "439812 'Find Harley' is the first objective text; its quest tag is not confirmed in the pack beyond the prior pass.", "source": "locale:439812 (prior pack)"},
  {"claim": "No progress reminder line exists in the client tagged to Hog Wild Harley; search for 'wandered off', 'Harley' and 'escort' surfaced no other Harley-tagged dialog.", "source": "locale search: Harley, escort, wandered off"},
  {"claim": "29616 mentions Harley and the manguana and reads like a completion thanks, but it is tagged 'Wheelie Pete (neighbouring quest)', so it is not assigned to complete.", "source": "locale:29616 tag"},
  {"claim": "Wheelie Pete's NPC answer attributes only 29611 and 439817 to him; it does not attribute 29615, so the speaker for the offer is left null.", "source": "npc answer: wheelie pete"},
  {"claim": "Reward line not found; wiki shows only a 'Mystery Reward' icon label.", "source": "quest answer open items"}
 ],
 "confidence": 0.35,
 "open": [
  "Offer speaker left null: 29615 is clearly Pete's voice (his hip, his hog) but Pete's NPC answer does not attribute it to him. Confirm the speaker before wiring.",
  "No progress dialog found in the client for this quest.",
  "Complete left null: 29616 is the only candidate but is tagged to a neighbouring quest. Decide whether it is this quest's completion thanks before using it.",
  "Escort step (439814) is unverified as live; the harleyEscort dev-note cluster suggests it was removed. Not wired as a required line here.",
  "Reward unknown, not none.",
  "Repeatability conflicts between wiki sources; not recorded here.",
  "Locale 439944 ('Wheelie Pete') was not re-checked; the locale regex lookup returned no matches for it in this pass."
 ]}
