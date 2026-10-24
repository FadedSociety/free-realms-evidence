<!-- fleet job=dialog-infer id=wthe-legendary-sunstone-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[20094, 12121, 8, 2039] model=claude-haiku-5-5 -->
# The Legendary Sunstone

{"quest": {"key": "The Legendary Sunstone", "title": "The Legendary Sunstone"},
 "offer": {"locale_id": 29646, "speaker": "Rizzle"},
 "progress": {"locale_id": 29647, "speaker": "Rizzle"},
 "complete": null,
 "other_lines": [
  {"locale_id": 439873, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title 'The Legendary Sunstone' is locale 29645, a quest_title with no FLAG.", "source": "locale:29645"},
  {"claim": "29646 is the offer: Rizzle thanks you and points you at the dwarf searching for the Legendary Sunstone, with the quality junk reward wording. It asks/explains, so it fits an offer.", "source": "locale:29646 / npc answer rizzle (quest_offer)"},
  {"claim": "29647 is Rizzle's follow-up pointer: 'Help the dwarf' and you could be rich. It reminds the player of the active task, so it is used as progress. It is a second Rizzle line, not an explicit reminder, so this is an inference.", "source": "locale:29647 / npc answer rizzle"},
  {"claim": "439873 is a quest-log description ('Rizzle has pointed you at a strange dwarf in search of the Legendary Sunstone'), not spoken dialog, so it is recorded as an objective hint, not as a speech slot.", "source": "locale:439873 / npc answer rizzle (quest_offer)"},
  {"claim": "No completion line exists for this quest. 29644 is Robot Woes' completion, and 29648 onward belongs to Noggle's chain (Ambush Recovery and later).", "source": "locale:29644 / locale:29648 / npc answers rizzle, noggle cogloose"},
  {"claim": "Reward: coins 5 from the wiki only. The 'quality junk' wording in 29646 is flavour, not a confirmed grant.", "source": "wiki: Quest:The Legendary Sunstone / locale:29646"}
 ],
 "confidence": 0.6,
 "open": [
  "No completion dialog exists in the client for this quest, so complete is null.",
  "Progress 29647 is inferred from its 'Help the dwarf' wording, not an explicit reminder line. Rizzle is the attributed speaker by the NPC answer.",
  "439873 and 439895 are quest-log descriptions, not spoken lines. 439895 ('Noggle wants you to find...') is not used because it names a different giver and its hint is Noggle's.",
  "The 5-coin reward is from the wiki only. The client has no reward figure, and the junk payout is unconfirmed.",
  "Numeric NPC ids for Rizzle and Noggle Cogloose are unknown, and no quest record id exists in our data."
 ]}
