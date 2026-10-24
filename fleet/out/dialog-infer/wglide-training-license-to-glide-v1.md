<!-- fleet job=dialog-infer id=wglide-training-license-to-glide-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[16931, 9371, 8, 2089] model=claude-haiku-5-5 -->
# Glide Training: License to Glide

{"quest": {"key": "Glide Training: License to Glide", "title": "Glide Training: License to Glide"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 4419698, "speaker": "Troy Ridewrangler"},
 "other_lines": [
  {"locale_id": 4419695, "role": "objective_hint", "speaker": null},
  {"locale_id": 4419697, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title is Glide Training: License to Glide (quest_title, no zone)", "source": "locale:4419696"},
  {"claim": "Completion line is Seaside-tagged, carries this quest's hint, says the saddle is complete and offers to transfer knowledge; it is a thank/pay line from Troy", "source": "locale:4419698 (full text verified via locale lookup); Troy named by NPC answer and quest giver record"},
  {"claim": "Fifth-step objective: launch pads in Seaside, jump through fiery hoop while riding untrained glide-trainable ride", "source": "locale:4419695 (verified full text)"},
  {"claim": "Seaside objective restating Troy's request to launch through a fiery hoop in Seaside", "source": "locale:4419697 (verified)"},
  {"claim": "4419693 is tagged Lakeshore and names Lakeshore, so it belongs to the step-4 quest, not this one; excluded", "source": "locale:4419693"},
  {"claim": "4419694 praises turning and diving (step-4 content) and is not a Seaside line; excluded as belonging to Glide Training: I'm Advanced!", "source": "locale:4419694"},
  {"claim": "4419712 is the 'Speak to Troy near the ride corral' objective of the separate quest Return to Troy Ridewrangler (4419711); the earlier pass's attribution of it as this line's progress is wrong and it is excluded", "source": "locale:4419711, locale:4419712"},
  {"claim": "No reward line tied to this step; saddle reward is series-level only", "source": "locale:1798 and wiki (series reward)"}
 ],
 "confidence": 0.6,
 "open": [
  "No quest record exists; record_id must be created by the builder.",
  "No NPC offer or progress dialog line found for this step; offer and progress are null.",
  "Reward: only series-level Training Saddle of Gliding (locale 1798); no step-5 payout line, so no reward slot filled.",
  "Hoop target has no client object id; needs a repo object id for the Seaside launch pad hoop.",
  "Troy's Seaside location is described three ways (Warpstone, ride stable, ride corral) and not reconciled.",
  "Speaker for 4419698 rests on the Troy giver attribution (npc_id 9500000639); the name locale id 440997 could not be re-verified through the locale tool.",
  "Earlier pass's dialog.complete and objective list were partly wrong (4419712, 4419693, 4419694 excluded as above)."
 ]}
