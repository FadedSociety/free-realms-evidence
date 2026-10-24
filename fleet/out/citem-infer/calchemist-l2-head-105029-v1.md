<!-- fleet job=citem-infer id=calchemist-l2-head-105029-v1 status=nothing_found turns=5 usd=0.0036 tokens(read,write,in,out)=[26892, 15052, 12, 2818] model=claude-haiku-5-5 -->
# Alchemist L2 Head

{"item": {"name": "Alchemist L2 Head", "locale_id": 105029, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Alchemist L2 Head' (locale 105029), slot 1 (head), class 32, model caster_<race>_<gender>_head_pointedcap.adr, 51 definitions (12 ids listed: 31947-31958), no coin store price.", "source": "refs:quest-lines/citem-packs.json 'calchemist-l2-head-105029'; locale:105029"},
  {"claim": "Sibling set pieces exist in the client: Alchemist L1 Head (104994), L1 Chest (104644), L2 Chest (104609), L3 Head (104749), L3 Chest (104539), L4 Head (104784), L4 Chest (104469), L5 Chest (104399), plus the category 'Alchemist Gear' (locale 8) and 'Alchemist Tools' (locale 9). No set text beyond names.", "source": "locale:8, locale:9, locale:104994, locale:104644, locale:104609, locale:104749, locale:104539, locale:104784, locale:104469, locale:104399"},
  {"claim": "Same-name client lines ('Alchemist L2 Head') are the only client text tagged to this item; no description given.", "source": "locale:105029"},
  {"claim": "Lookup of the wiki, articles, and video found no page, image, article fact or frame naming this item; the wiki has no 'Alchemist' set page in the index.", "source": "lookup query 'Alchemist L2 Head' and 'Alchemist Chest OR Alchemist Head OR Alchemist Gear' (no matches)"},
  {"claim": "Repo vendor data (vendors.json) has no entry for ids 31947-31958 or locale 105029; no coin store price exists in stores.json for this item.", "source": "repo search for 105029/Alchemist (repo:prototype/osfr-tools/data/content/vendors.json matched only unrelated id 131947)"},
  {"claim": "The first-pass tag 'quest_reward' is a cheap-model guess only; no quest, drop, vendor, or event in the pack names this item.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.2,
 "open": [
  "No real source found. The 'quest_reward' guess is unsupported: no quest text in locale names an Alchemist head piece as a reward (the alchemist quest lines mention Eggert, Apprentice Bubbles, Potion of Truth, Alchemist's Cauldron, but none name this item).",
  "Check the Free Realms Legacy and Lxzxrus server ClientItemDefinitions (comments such as 'Alchemist L5 Chest' sit beside the definitions) for a vendor/quest table keyed to these ids; not checked for this item's ids beyond the comment match.",
  "Check the Alchemist class/caster gear set (L1-L5 tiers) as a level-tiered class armor: whether tiers are vendor-sold, quest-rewarded or crafted is unknown. Look for the Alchemist tier items in the wiki Crafting or class gear pages.",
  "Live status is unknown: client presence does not prove it was obtainable on the live server.",
  "Pack asked for variants: 51 definitions per the client but only 12 ids listed; races/genders not enumerated."
 ]}
