<!-- fleet job=quest-infer id=wperfecting-the-batter-v4 status=done turns=8 usd=0.0040 tokens(read,write,in,out)=[82061, 12781, 18, 3244] model=claude-haiku-5-5 -->
# Perfecting the Batter

{"quest": {"record_id": null, "title": "Perfecting the Batter", "title_locale_id": 428059},
 "live": "yes",
 "live_reason": "Title locale:428059 is an unflagged quest_title tagged Robgoblin Camp. The wiki Birthday Bash page lists 'Perfecting the Batter' as a Glerga quest, and the wiki Birthday Bash item list says the Cupcake Hat is acquired by completing it. No FLAG on the title or its objective. Caveat: a near-identical sibling quest title 'Glerga's Cake' (locale:428540) with objective 'Help Glerga at the Robgoblin Camp perfect her batter.' (locale:428535) also exists, so the exact split between the two is unresolved.",
 "zone": "Robgoblin Camp",
 "giver": {"name": "Glerga", "npc_id": null, "locale_id": 15854},
 "line": {"name": "Birthday Bash (Glerga's cake chain)",
   "previous": ["To Bake a Pretty Cake"],
   "next": ["Cakenstein's Last Stand"]},
 "objectives": [
  {"kind": "other", "text": "Help Glerga at the Robgoblin Camp perfect her batter by tasting her cake.", "text_locale_id": 428060, "target": "Glerga's cake", "target_locale_id": null, "count": null},
  {"kind": "other", "text": "Taste Glerga's new cake", "text_locale_id": 428547, "target": "Glerga", "target_locale_id": 15854, "count": null}
 ],
 "dialog": {"offer": null, "progress": null, "complete": null},
 "rewards": [{"kind": "item", "value": "Cupcake Hat (quest version)", "source": "wiki Birthday Bash: Cupcake Hat acquired by completing Perfecting the Batter"}],
 "evidence": [
  {"claim": "Quest title 'Perfecting the Batter' is an unflagged quest_title tagged Robgoblin Camp", "source": "locale:428059"},
  {"claim": "Objective: help Glerga perfect her batter by tasting her cake", "source": "locale:428060"},
  {"claim": "Glerga asks the player to taste test her cake", "source": "locale:428058"},
  {"claim": "Glerga is a named NPC (npc_name)", "source": "locale:15854"},
  {"claim": "Objective 'Taste Glerga's new cake' is a quest_objective tagged Glerga; it is not tagged to this quest title, so attribution is by content only", "source": "locale:428547"},
  {"claim": "Sibling quest title 'Glerga's Cake' with objective 'Help Glerga at the Robgoblin Camp perfect her batter.'", "source": "locale:428540"},
  {"claim": "Sibling objective 'Help Glerga at the Robgoblin Camp perfect her batter.'", "source": "locale:428535"},
  {"claim": "Birthday Bash chain: 'Bake a Pretty Cake' -> 'Perfecting the Batter' -> 'All Cakensteins Must Die' (all from Glerga)", "source": "wiki Birthday Bash"},
  {"claim": "Cupcake Hat quest version acquired by completing Perfecting the Batter", "source": "wiki Birthday Bash"},
  {"claim": "Cakenstein is created by Glerga's baking accident", "source": "articles/facts.json:8347"},
  {"claim": "Glerga is a Robgoblin Camp chef", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Wilds.md:90"}
 ],
 "confidence": 0.55,
 "open": [
  "Offer, progress and complete dialog ids are not tagged in the client; 428054, 428055, 428058 are plausible but unassigned.",
  "Objective kind is inferred from wording (taste the cake, Glerga is the target); no client field gives the kind.",
  "Giver NPC record id is unresolved; locale:15854 gives the name only.",
  "Previous 'To Bake a Pretty Cake' (locale:428053) is linked by wiki order only; the chain note says no quest record confirms it.",
  "Next 'Cakenstein's Last Stand' (locale:428064) is linked by content (428065 defeat the last Cakensteins) and wiki order ('All Cakensteins Must Die' is not matched to 428064 by title).",
  "Sibling 'Glerga's Cake' (locale:428540) may be the actual taste-test quest with 'Perfecting the Batter' as a variant or the other way round; not settled. 428547 has no quest tag, so its attribution is unconfirmed.",
  "Cupcake Hat item id not found in the client pack; reward is wiki-sourced only.",
  "No record id exists; a new record would be needed."
 ]}
