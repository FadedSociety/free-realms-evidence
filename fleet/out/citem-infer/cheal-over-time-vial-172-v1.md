<!-- fleet job=citem-infer id=cheal-over-time-vial-172-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[14576, 11391, 8, 1593] model=claude-haiku-5-5 -->
# Heal Over Time Vial

{"item": {"name": "Heal Over Time Vial", "locale_id": 172, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Heal Over Time Vial' (locale:172, item type, no FLAG), with description 'This potion heals over a set amount of time.' (locale:167).", "source": "locale:172; locale:167"},
  {"claim": "Client definition is definition_id 32, class_id 9, slot 0, with no models and no coin store price.", "source": "client definition in evidence pack"},
  {"claim": "Neighbouring client strings look like development leftovers: locale:168/169 are 'Checkpoint (5)' and 'Checkpoint (20)' debug labels, locale:170 'Turtle' is a placeholder test creature, and locale:171 and 173 are 'Heal Over Time Potion II (PH)' and 'Heal Over Time Potion IV (PH)' placeholder items.", "source": "locale:168; locale:169; locale:170; locale:171; locale:173"},
  {"claim": "Locale:174 'Heal Over Time Potion' is a separate non-placeholder item string; no source ties it to the Vial.", "source": "locale:174"},
  {"claim": "No wiki page, image, article fact, video frame, coin vendor stock entry, quest reward, drop, or other answer names the Heal Over Time Vial. Searches of the repo JSON for locale id 172 and for 'Heal Over Time' or 'Vial' found nothing usable.", "source": "lookup (client, wiki, articles); search repo"},
  {"claim": "The wiki's real potion pages (e.g. Wheeler Health Potion, Wheeler Energy Potion) are sourced from the Daily Wheel, but these do not name the Vial.", "source": "wiki Wheeler Health Potion; wiki Wheeler Energy Potion"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Nothing in the pack or the repo links item 32 / locale 172 to a vendor, quest, drop, event, prize wheel, or promotion.",
  "The first-pass tag says live 'yes', but that is a cheap-model hint only. The surrounding strings (Checkpoint debug labels, Turtle, PH placeholder potions) suggest this is a test or dev item. Treat as likely not live unless a source shows otherwise.",
  "Check whether the 'Heal Over Time' effect is used by any live potion, and whether the Vial appears in any real item-grant tables before deciding its live status.",
  "Locale:174 'Heal Over Time Potion' is unresolved and may be the live name for the same effect; compare its definition and sources."
 ]}
