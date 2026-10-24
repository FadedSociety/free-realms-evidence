<!-- fleet job=citem-infer id=cstudent-warrior-helm-135644-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[28650, 15087, 10, 2720] model=claude-haiku-5-5 -->
# Student Warrior Helm

{"item": {"name": "Student Warrior Helm", "locale_id": 135644, "kind": "clothing"},
 "sources": [{"type": "other", "detail": "Warrior starter outfit: granted as part of the 7-piece creation kit (profile 32 starter_items, with 46389, 46137, 46732, 46224, 47019 and the Student Warrior Cudgel 29963) when the Warrior job is unlocked via the T201 trainer; free, not sold", "where": "Warrior job unlock (Drill Sergeant Dewey, Snowhill, per notes/Build Guides/Content/Jobs/Warrior.md W1)", "price": null, "currency": null, "source": "repo:notes/Autopilot/T201.md:181 (starter_items[\"32\"] = [46644, ...]); repo:notes/Research/Pieces/033 Warrior progression.md:47-51 (profile 32 DefaultItems, MinProfileRank 1); repo:notes/Research/Job Starter Outfits.md:75; repo:scripts/fixtures/starter_items.json:69"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Student Warrior Helm' is locale 135644 (item), definition 46644, slot 1, class 15 (Warrior Gear), model warrior_<race>_<gender>_head_mohawkhelm.adr; no coin store price in stores data", "source": "locale:135644; client definition in pack; repo:tests/pieces/test_piece_033.py:55"},
  {"claim": "46644 is the first of the seven Warrior creation-kit items in profile 32 DefaultItems, all MinProfileRank 1", "source": "repo:notes/Research/Pieces/033 Warrior progression.md:47-51"},
  {"claim": "The starter kit ships in the play package as starter_items['32'] = [46644, 46389, 46137, 46732, 46224, 47019, 29963]", "source": "repo:notes/Autopilot/T201.md:179-181; repo:notes/Research/Job Starter Outfits.md:75"},
  {"claim": "The Warrior W1 quest does not grant the outfit; the T201 trainer issues the starter gear", "source": "repo:notes/Autopilot/T257.md:43; repo:prototype/osfr-tools/data/content/quests/warrior.json:42"},
  {"claim": "Sibling Student Warrior Cudgel is listed on the wiki as a quest weapon from 'Unlocking the Warrior job', retired", "source": "repo:notes/Build Guides/Content/Jobs/Warrior.md:170 (wiki weapon pages)"},
  {"claim": "Set 'Student Warrior' is the level-1 clothing tier of the Warrior sets", "source": "repo:notes/Build Guides/Content/Jobs/Warrior.md:164 (wiki job page)"}
 ],
 "confidence": 0.6,
 "open": [
  "No wiki page or article names the Student Warrior Helm itself; the only evidence is the starter-kit data, so the source is inferred from the profile 32 starter_items list, not from a player-facing source.",
  "Whether the helm is still granted on live Warrior unlock or retired is not stated by any source; the wiki marks the sibling Cudgel retired, but not the helm. Live status left as 'unsure'.",
  "The pack's first-pass 'live: yes' and 'source_guess: vendor' are not supported: no coin store price exists and no vendor stock lists the item. The starter-kit grant is treated as the source instead.",
  "The description field is empty in the client definition; no lore or text beyond the name exists.",
  "The 'mohawkhelm' model is a race/gender-tinted variant; the number of tints/variants sharing the name was not in the pack (definitions: 1)."
 ]}
