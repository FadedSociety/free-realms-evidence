<!-- fleet job=dialog-infer id=wglide-training-i-m-advanced-v1 status=done turns=5 usd=0.0031 tokens(read,write,in,out)=[37031, 10680, 12, 2855] model=claude-haiku-5-5 -->
# Glide Training: I'm Advanced!

{"quest": {"key": "glide_training_im_advanced", "title": "Glide Training: I'm Advanced!"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 4419694, "speaker": null},
 "other_lines": [
  {"locale_id": 4419691, "role": "objective_hint", "speaker": null},
  {"locale_id": 441976, "role": "reward", "speaker": null},
  {"locale_id": 4419712, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is locale 4419692, \"Glide Training: I'm Advanced!\", tagged Lakeshore.", "source": "locale:4419692 (verified)"},
  {"claim": "Step objective: launch through the Lakeshore fiery hoop on an untrained glide-trainable ride; objective text names turning and diving.", "source": "locale:4419691 (tagged to this quest; verified text)"},
  {"claim": "Completion line for step 4: 'Good job! Your ride's grasp of the advanced gliding techniques like turning and diving has been transferred to the Training Saddle!... Come back tomorrow'. Text matches step 4 (turning and diving), not step 5.", "source": "locale:4419694 (verified text; tag hint is License to Glide, zone empty)"},
  {"claim": "Reward ticket is Proof of Training - Part 4 of 5.", "source": "locale:441976 (verified) and wiki Proof of Training - Part 4 of 5"},
  {"claim": "4419712 'Speak to Troy Ridewrangler near the ride corral in Seaside.' is a return-to-giver instruction written as objective text, not NPC speech, so it is not used as progress dialog.", "source": "locale:4419712 (verified text); npc answer labelled it quest_progress"},
  {"claim": "Troy Ridewrangler is the giver of the five-step Glide Training series; the quest sits between Confidence Is Key and License to Glide.", "source": "wiki Glide Training / Quest:Glide Training: I'm Advanced! Requirements; npc answer"}
 ],
 "confidence": 0.5,
 "open": [
  "No offer line for this step was identified in the client, so offer is null.",
  "No progress line was identified: 4419712 reads as an objective instruction, not Troy's speech.",
  "Complete line 4419694 is tagged to the License to Glide quest, and no client line attributes it to Troy. Its text fits step 4, so it is used, but speaker is left null rather than guessed.",
  "Locale ids 441980 and 441982 cited by the earlier pack did not verify in the client lookup and are not used. The Part 4 ticket is 441976 instead.",
  "Coin reward for this step is unknown; the wiki lists only the ticket.",
  "Zone: step is performed in Lakeshore, but Troy the giver is in Seaside. Place the NPC in Seaside.",
  "No quest record id exists; a new record must be created."
 ]}
