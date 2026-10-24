<!-- fleet job=dialog-infer id=wdelicious-goo-d-candy-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[16298, 9067, 8, 2822] model=claude-haiku-5-5 -->
# Delicious Goo'd Candy

{"quest": {"key": "delicious_goo_d_candy", "title": "Delicious Goo'd Candy"},
 "offer": {"locale_id": 416793, "speaker": "Halloween Harry"},
 "progress": {"locale_id": 416795, "speaker": "Halloween Harry"},
 "complete": {"locale_id": 416794, "speaker": "Halloween Harry"},
 "other_lines": [
  {"locale_id": 416791, "role": "other", "speaker": null},
  {"locale_id": 416792, "role": "other", "speaker": null},
  {"locale_id": 416796, "role": "objective_hint", "speaker": null},
  {"locale_id": 416797, "role": "objective_hint", "speaker": null},
  {"locale_id": 416798, "role": "objective_hint", "speaker": null},
  {"locale_id": 416799, "role": "objective_hint", "speaker": null},
  {"locale_id": 416852, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line: Harry explains the candy bag and invites the player to collect the treat from goo", "source": "locale:416793 (quest_dialog, Sanctuary, Delicious Goo'd Candy); NPC answer 'halloween harry' lists 416793-tagged quest dialog to this quest"},
  {"claim": "Progress line: Harry tells the player to go ahead and use the Candy Bag", "source": "locale:416795 (quest_dialog, tagged to this quest); Harry attributed in NPC answer"},
  {"claim": "Complete line: Harry hands over special Halloween candy and invites return when enough goo is collected", "source": "locale:416794 (quest_dialog, tagged to this quest); Harry attributed in NPC answer"},
  {"claim": "Objectives: talk to Harry, use Candy Bag, beat the Goo'd Candy minigame, plus a goo handover objective", "source": "locale:416799, 416798, 416797 (quest_objective tagged to this quest); locale:416852 'Give your ectoplasmic goo to Halloween Harry in Sanctuary' from NPC answer"},
  {"claim": "Locale 416853 'Speak to Halloween Harry' was excluded: it is a generic objective with no quest tag beyond the NPC answer", "source": "locale:416853"},
  {"claim": "Quest title", "source": "locale:416791"}
 ],
 "confidence": 0.6,
 "open": [
  "No quest record id exists in the pack; key is derived from the title.",
  "Offer/progress/complete ids match by content and quest tag only; no explicit quest-to-dialog binding was found.",
  "Speaker is Halloween Harry by tag hint and the NPC answer; the dialog text is first-person skeleton voice and fits Harry, but no per-line speaker attribution beyond that.",
  "416852 is an objective line, not spoken dialog; it is listed under other_lines and its speaker is null. The NPC answer labelled it quest_progress dialog, which conflicts with its text, so it is a weak attribution.",
  "416853 ('Speak to Halloween Harry') was excluded as too generic to bind to this quest.",
  "Reward: the candy is only described in 416794; no item id or name exists in client text, so no reward line is separately bound.",
  "Minigame win condition is not in client text; activity 712 is restoration_status unknown.",
  "Previous/next quest links are unknown; the 15-goo repeat gate is not supported by this quest's text (416787 belongs to The Great Scare).",
  "Zone conflict: Sanctuary (NPC zone and hint) vs Pixiewood Hills (locale:416800, wiki). Left unresolved; record zone not set here.",
  "Wiki claims were not re-verified by full-text lookup in this pass (the FTS query failed on the apostrophe in the title)."
 ]}
