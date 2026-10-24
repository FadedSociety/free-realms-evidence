<!-- fleet job=dialog-infer id=wstatus-reports-v1 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[13237, 7446, 8, 1756] model=claude-haiku-5-5 -->
# Status Reports

{"quest": {"key": "status_reports", "title": "Status Reports"},
 "offer": {"locale_id": 93035, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 93038, "speaker": null},
 "other_lines": [
  {"locale_id": 93037, "role": "objective_hint", "speaker": null},
  {"locale_id": 93045, "role": "objective_hint", "speaker": null},
  {"locale_id": 93047, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "93035 is the offer: the mayor-style speaker says they are behind on collecting status reports and asks the player to gather them.", "source": "locale:93035 (full text verified via locale query)"},
  {"claim": "93038 is the completion: thanks the player and says everything is in order.", "source": "locale:93038 (full text verified via locale query)"},
  {"claim": "93036 is the quest title 'Status Reports', tagged Snowhill.", "source": "locale:93036 tag"},
  {"claim": "93037 is the primary objective text; 93040 is a near-duplicate objective wording and was not chosen.", "source": "locale:93037, locale:93040 (lookup)"},
  {"claim": "Mayor Crystalline is listed on the wiki with Quest:Status Reports, but the wiki is not a dialog attribution source, so the speaker is left null.", "source": "wiki page Mayor Crystalline"},
  {"claim": "No progress/reminder line and no reward line was found tagged to this quest.", "source": "client tag search"}
 ],
 "confidence": 0.5,
 "open": [
  "Giver/speaker unresolved: neither 93035 nor 93038 names a speaker, and no NPC answer attributed them. The wiki's Mayor Crystalline (locale 182) association is plausible but not used as a speaker attribution, so speaker is null.",
  "No progress line exists in the pack for this quest; progress left null.",
  "Objectives 93045 (Report from Flynn) and 93047 (Report from Brandywine) are name-only with no quest-to-NPC link; listed as objective_hint with unknown targets. 93050/93052 belong to the Brandywine hot-chocolate quest and were excluded.",
  "389075 is unflagged but has no zone or title link to this quest; excluded.",
  "No reward text found; rewards unknown rather than absent.",
  "Line chain position (previous/next) unknown; not set.",
  "Live status is unsure, so the whole binding needs confirmation against the server quest record before wiring."
 ]}
