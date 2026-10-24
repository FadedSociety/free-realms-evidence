<!-- fleet job=dialog-infer id=wthe-perfect-disguise-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7321, 9056, 6, 2144] model=claude-haiku-5-5 -->
# The Perfect Disguise

{"quest": {"key": "the_perfect_disguise", "title": "The Perfect Disguise"},
 "offer": null,
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 420283, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'The Perfect Disguise' (record 64, Snowhill, giver Candi Ivy).", "source": "locale:420284 (quest_title, hint The Perfect Disguise); quest answer giver Candi Ivy locale 419832"},
  {"claim": "Only quest-tagged objective text for this quest: sneak into the robgoblin camp, get a disguise from Spindle, who is testing a morphing device.", "source": "locale:420283 (quest_objective, hint The Perfect Disguise)"},
  {"claim": "No offer, progress or complete dialog line is tagged to The Perfect Disguise in the client text, so those slots are null.", "source": "lookup of client text for 'disguise'/'robgoblin camp'/'Spindle' returned no quest_dialog tagged to this quest"},
  {"claim": "Candi Ivy's attributed dialog 420536 is tagged to Robgoblin Robbery Ring and 420492 to Present Problems; 419853/419880 are offers with no quest tag. None are tied to The Perfect Disguise, so they are not used.", "source": "npc answer candi ivy dialog list"},
  {"claim": "Spindle's secret morphing device objective 420285 belongs to a separate Spindle quest hint, not this one.", "source": "locale:420285 (hint Spindle's Secret Morphing Device)"},
  {"claim": "Spindle objective 420506 ('Obtain a disguise from Spindle...') is a different quest-task line and is not assigned here.", "source": "lookup client: locale:420506 (quest_objective, hint Spindle)"}
 ],
 "confidence": 0.5,
 "open": [
  "No offer, progress or complete dialog is tagged to The Perfect Disguise; slots left null rather than borrowing lines from neighbouring Snow Days quests.",
  "420283 is the only objective; it has no named speaker, so speaker is null. Its text names Spindle and the disguise, but it is a quest-log objective, not spoken dialog.",
  "420506 ('Obtain a disguise from Spindle so you can sneak into the Robgoblin's camp') may be this quest's step or the Spindle morphing quest's; not assigned, needs verification.",
  "Candi Ivy NPC id not verified (repo note gives 4272345714, unconfirmed); omitted.",
  "No reward line; wiki-only Subarctic Winterwear Pants is unverified and omitted.",
  "Membership gating conflicts between wiki (members) and repo record (members_only false); not resolved here.",
  "Next quest title: client is 'The Great Robgoblin Robbery Ring' (420288); wiki spelling 'Robgoblin Robbery Ring' differs.",
  "Repo note reference 'Perfect Disguise (403844845)' in NPCs - Snowhill.md marks text as not matched, consistent with no dialog found."
 ]}
