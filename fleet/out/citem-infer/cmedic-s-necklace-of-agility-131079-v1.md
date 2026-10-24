<!-- fleet job=citem-infer id=cmedic-s-necklace-of-agility-131079-v1 status=nothing_found turns=3 usd=0.0026 tokens(read,write,in,out)=[12561, 11753, 8, 2023] model=claude-haiku-5-5 -->
# Medic's Necklace of Agility

{"item": {"name": "Medic's Necklace of Agility", "locale_id": 131079, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the name at locale:131079 with one definition (75335), necklace slot 8, item class 7, no model files, no coin store price.", "source": "locale:131079; client definition in evidence pack"},
  {"claim": "Name sits in a Medic necklace/ring family (locale 131074-131084) that includes three placeholder names (tbd1, tbd2, tbd3) flagged as placeholder by the client text table.", "source": "locale:131080, locale:131081, locale:131082, locale:131083, locale:131084"},
  {"claim": "Sibling Medic necklaces with a known vendor stock are Bark Skin, Vitality and Energy Font. The Agility line is not among them.", "source": "locale:131059-131068; repo:prototype/osfr-tools/data/content/npcs/stillwater_crossing.json (Kimble stock, line 7944); notes/Build Guides/Content/NPCs/NPCs - Stillwater Crossing.md:66"},
  {"claim": "Kimble, the Medic gear merchant at Stillwater Crossing, stocks Trauma Care Medic set pieces, Medic's Power Shard of Regeneration III, Medic's Ring of Energy III, Medic's Necklace of Bark Skin III and Medic's Bonesaw. No Agility necklace is listed.", "source": "repo:prototype/osfr-tools/data/content/npcs/stillwater_crossing.json:7944-7947"},
  {"claim": "Searches of the repo (vendors.json, dungeons, quests, recipes), the wiki, client text and articles returned no mention of Medic's Necklace of Agility beyond its own locale entry.", "source": "search of repo/refs/client/wiki/articles/video for the name and definition id 75335"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. The item has no vendor stock, quest reward, drop, event, prize wheel, crafting, collection or promotion mention in any root. Per the rules it stays unsourced.",
  "Live status unknown. The name sits in a cluster with three tbd placeholder entries and a Necklace of Energy Font that the dungeon data lists as a Bergram Stumpfinger's Ghost reward, so this may be an unreleased or placeholder definition. The first-pass 'live: yes' tag is a hint only and is not confirmed.",
  "Kind 'clothing' follows slot 8 and class 7 in the client definition, not a verified in-game item.",
  "No description text, model files or coin price in the client definition, so no price or currency can be stated.",
  "Recommend checking a live Medic job vendor, Kimble's full stock over time, and the Medic ring/necklace drop tables before assigning any source."
 ]}
