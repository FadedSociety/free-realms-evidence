<!-- fleet job=citem-infer id=crunner-grape-necklace-96268-v1 status=nothing_found turns=4 usd=0.0025 tokens(read,write,in,out)=[18638, 9464, 10, 2197] model=claude-haiku-5-5 -->
# Runner Grape Necklace

{"item": {"name": "Runner Grape Necklace", "locale_id": 96268, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item: name locale 96268, one definition (30862), slot 9, class 66, no model files, no coin store price.", "source": "locale:96268"},
  {"claim": "It is one of a six-colour family sharing the name pattern 'Runner <Colour> Necklace' (Blue 96266, Green 96267, Grape 96268, Yellow 96269, Mustard 96270, Orange 96271). The family has no description text in the client.", "source": "locale:96266-96271"},
  {"claim": "No wiki page, video frame or article names any Runner necklace. The only 'Runner' hits are unrelated vehicle chassis (Arrow/Elliptical/Speedy Runner) and Runner NPCs (Mandy at Farnum, Finn in Sanctuary, the Seaside runner).", "source": "lookup (wiki, video, articles, client) returned no matches for 'Runner Necklace'"},
  {"claim": "Repo data (stores, vendors, quests, recipes) has no reference to 30862 or to any Runner necklace name.", "source": "search repo '30862|Runner' and 'Runner.*Necklace'"},
  {"claim": "The inventory frame in video XtvRqM7RejE/00302.jpg lists an 'Arrow [Runner] Chassis' and an '[Necklace] of Agility' but no Runner necklace.", "source": "video:XtvRqM7RejE/00302.jpg"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found for any Runner necklace. The cluster has no vendor stock, no coin store price, no wiki page and no quest or drop text.",
  "The colour family sits next to the Runner race/time-trial NPCs (Mandy at Farnum Farmstead, Finn in Sanctuary, the Seaside fastest-runner challenge), so a race or time-trial reward is plausible. That is a guess, not evidence; check quest reward tables for those trials for item id 30862.",
  "The first-pass tag 'live: yes, source unknown' is a hint only. Liveness is unconfirmed: no current source means it may be a retired or test item.",
  "Kind 'clothing' comes from slot 9 (necklace accessory) and class 66. Confirm the class mapping before storing it.",
  "Description is empty in the client, so no in-game text states how to get it."
 ]}
