<!-- fleet job=dialog-infer id=wscrap-collector-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[27847, 11219, 10, 2594] model=claude-haiku-5-5 -->
# Scrap Collector

{"quest": {"key": "scrap_collector", "title": "Scrap Collector"},
 "offer": {"locale_id": 5102580, "speaker": "Sunstone Jones"},
 "progress": null,
 "complete": {"locale_id": 5102584, "speaker": "Sunstone Jones"},
 "other_lines": [
  {"locale_id": 5102579, "role": "objective_hint", "speaker": null},
  {"locale_id": 5102582, "role": "objective_hint", "speaker": null},
  {"locale_id": 5102583, "role": "objective_hint", "speaker": null},
  {"locale_id": 5102581, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line: Jones tells the player to go complete combat encounters for secret treasure map scraps; it is the quest's start dialog.", "source": "locale:5102580 (full text checked); npc answer sunstone jones dialog kind quest_offer"},
  {"claim": "Complete line: Jones thanks the player ('Nice work, kid') and sends them to Kara Loft to assemble the scraps; it is the turn-in dialog.", "source": "locale:5102584 (full text checked); npc answer sunstone jones dialog kind quest_complete"},
  {"claim": "Objective texts: combat encounters for scraps, 'Map scraps collected' (goal 3, from wiki '/3'), and 'Return to Sunstone Jones'.", "source": "locale:5102579, 5102582, 5102583; wiki Quest:Scrap Collector"},
  {"claim": "Quest is Sanctuary, given by Sunstone Jones south of the hospital; part of the Lost Treasures Month line, next is Hunting Treasure (Kara Loft).", "source": "npc answer sunstone jones (zone Sanctuary); wiki Sunstone Jones and Lost Treasures Month"},
  {"claim": "locale:5102581 is Kara Loft-voiced ('I believe I can assemble these scraps. Check back with me...'), an in-between line, not a reminder. It does not name its speaker, so speaker is null.", "source": "locale:5102581 (full text checked)"},
  {"claim": "Reward is coins with a random amount; no numeric value or reward line id exists.", "source": "wiki Quest:Scrap Collector ('coin amount' Random); no reward locale line found"}
 ],
 "confidence": 0.8,
 "open": [
  "record_id is null: no confirmed quest record id. The 657220927 value in the earlier notes is unconfirmed.",
  "giver npc_id is null: the name hashes in Sanctuary.json are not confirmed NPC ids.",
  "progress is null: no client line reminds the player of this quest while in progress. locale:5102581 is a Kara Loft follow-up (it says 'check back in a few moments'), not a progress reminder, and it does not name its speaker. Left as followup with speaker null.",
  "reward: coins 'Random' comes only from the wiki; no numeric amount or reward locale line exists, so no reward line id is given.",
  "Combat encounter count per scrap is not in the client; objective count 3 is from the wiki.",
  "Whether Lost Treasures Month still runs on live servers is unconfirmed (wiki supports only the 2013 introduction).",
  "No explicit critiques were included in the pack; the earlier open items above are carried forward unchanged."
 ]}
