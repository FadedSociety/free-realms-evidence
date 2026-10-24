<!-- fleet job=dialog-infer id=wninja-gathered-shadows-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[14511, 8004, 8, 2083] model=claude-haiku-5-5 -->
# Ninja: Gathered Shadows

{"quest": {"key": "ninja_gathered_shadows", "title": "Ninja: Gathered Shadows"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 78911, "speaker": null},
 "other_lines": [{"locale_id": 78910, "role": "objective_hint", "speaker": null}],
 "evidence": [
  {"claim": "Quest title is 'Ninja: Gathered Shadows', tagged Lakeshore.", "source": "locale:78909"},
  {"claim": "Objective: as a Ninja, fight through Danger Peaks and confront Sarah.", "source": "locale:78910"},
  {"claim": "78911 is this quest's closing thanks ('I am in your debt for honoring my request... we have no time to dwell on your success'), tagged to this quest and Lakeshore. It is the only tagged line that thanks rather than asks or reminds, so it is used as complete.", "source": "locale:78911"},
  {"claim": "Sarah stole Ty's signet ring and oversees Shadow Talon ninjas at Danger Peaks, which is the objective target context.", "source": "locale:78908 (tagged Sarah, Danger Peaks; not this quest's tag, used only as context)"},
  {"claim": "78912 ('defeat the troll... Troll Fort stirs for an attack') names a different task, so it is not this quest's line. It fits the next quest, Ninja: Stilling the Waters (78914).", "source": "locale:78912, locale:78914"},
  {"claim": "No offer or progress dialog line tagged to this quest was found; 78910 is a quest_objective, not dialog.", "source": "locale search on tags 78909-78912"},
  {"claim": "Ty is the giver only per the wiki Ty page; no client line names Ty as speaker for 78911.", "source": "lookup wiki Ty page"}
 ],
 "confidence": 0.4,
 "open": [
  "Speaker for 78911 is null: the text names no one, and no NPC answer attributed it. Ty is the probable speaker from the wiki giver page, but that is not confirmed by a client line.",
  "No offer, progress or reward line exists for this quest in the pack; those slots are null.",
  "Sarah has no resolved NPC id, so no speaker or target id is set. 78908 is tagged to Sarah, not this quest, and was not used as a line.",
  "Live status is unsure: there is no completion record or shipped-completion source, so treat this quest's lines as unverified against the live game.",
  "Previous link is unknown. Next link Stilling the Waters is medium confidence and rests on 78912 being a hand-off, which is not this quest's line.",
  "No critiques were attached to the pack, so none needed fixing."
 ]}
