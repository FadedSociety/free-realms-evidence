<!-- fleet job=dialog-infer id=wtrick-or-treat-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[12178, 7961, 8, 3015] model=claude-haiku-5-5 -->
# Trick-or-Treat

{"quest": {"key": "Trick-or-Treat", "title": "Trick-or-Treat"},
 "offer": {"locale_id": 415049, "speaker": null},
 "progress": {"locale_id": 415825, "speaker": null},
 "complete": {"locale_id": 415052, "speaker": null},
 "other_lines": [
  {"locale_id": 415051, "role": "objective_hint", "speaker": null},
  {"locale_id": 415822, "role": "objective_hint", "speaker": null},
  {"locale_id": 415824, "role": "followup", "speaker": "Halloween Harry"}
 ],
 "evidence": [
  {"claim": "Quest title is 'Trick-or-Treat'", "source": "locale:415050 (quest_title)"},
  {"claim": "Offer text explains that people give candy only after a /scare and is a greeting/ask ('Have you ever trick-or-treated before?')", "source": "locale:415049 (npc_dialog, hint Trick-or-Treat). Full text confirmed by locale search."},
  {"claim": "Objective: look for people with the Halloween icon and /scare them", "source": "locale:415051 (quest_objective)"},
  {"claim": "Sanctuary objective: travel around Sanctuary collecting candy from people in costume", "source": "locale:415822 (quest_objective, hint 'Trick-or-Treat around Sanctuary')"},
  {"claim": "Show Halloween Harry the collected candy", "source": "locale:415824 (quest_objective); Halloween Harry NPC answer attributes it as quest_progress for Trick-or-Treat"},
  {"claim": "Reminder that folks need a good scare / select [scare] or type /scare", "source": "locale:415825 (quest_dialog, hint 'Trick-or-Treat around Sanctuary')"},
  {"claim": "Completion-style thanks for a candy stash, mentions trick-or-treating every day in Sanctuary during the Halloween celebration", "source": "locale:415052 (quest_dialog, Sanctuary, hint Trick-or-Treat); wording inferred, no quest-state link"},
  {"claim": "Giver is Halloween Harry, npc_id 9500000493, quests_given includes Trick-or-Treat", "source": "quest answer; NPC answer for Halloween Harry (zone Sanctuary, Pixiewood)"}
 ],
 "confidence": 0.5,
 "open": [
  "Offer speaker null: locale:415049 is npc_dialog with no name in its text, and the Halloween Harry NPC answer does not list it. Harry is the giver, but attribution is not confirmed.",
  "Progress: no line tagged exactly to Trick-or-Treat is a reminder dialog. 415824 is an objective ('Show Halloween Harry...') that Harry's answer attributes as progress, but it is quest_objective type, so it is placed under other_lines. 415825 is the closest reminder dialog, but its hint is 'Trick-or-Treat around Sanctuary', not the exact quest title. Speaker null.",
  "Complete 415052: wording fits a thanks/turn-in, but it is inferred, not tied to quest state. Its hint is 'Trick-or-Treat'. Speaker null because no NPC answer attributes it.",
  "Reward: no reward line in client text. Candy item id and amount not recovered, so no reward entry.",
  "Zone Sanctuary (Pixiewood) is supported by the repo and Harry's NPC answer. Pixiewood Hills vs. main street is unresolved, and a spawn check is still needed.",
  "Repeat gating (daily, 'every day' per 415052) is noted in the text but the cooldown is not verified.",
  "Halloween Fanatic next link and the A Formal Report conflict from the earlier answer are unverified and not wired here."
 ]
}
