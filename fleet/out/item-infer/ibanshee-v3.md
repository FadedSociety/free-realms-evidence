<!-- fleet job=item-infer id=ibanshee-v3 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[5361, 6927, 6, 1605] model=claude-haiku-5-5 -->
# Banshee

{"item": {"name": "Banshee", "locale_id": 3082, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:3082 is the npc_name 'Banshee'. The subject is an NPC boss in Bone Bog Cemetery, Blackspore Swamp, not an item.", "source": "locale:3082; https://freerealms.fandom.com/wiki/Banshee (rev 50200)"},
  {"claim": "The wiki Banshee page lists the boss in Bone Bog Cemetery and under Appearances 'Trading Card Game Series 1', with no card name, pack, or price.", "source": "https://freerealms.fandom.com/wiki/Banshee (rev 50200)"},
  {"claim": "Quest objective 'Defeat the cemetery banshee!' is a real string.", "source": "locale:414879"},
  {"claim": "Bone Bog Cemetery page lists 'Banshee' under Bosses and the goal 'Defeat the cemetery [banshee]!'.", "source": "wiki page: Bone Bog Cemetery"},
  {"claim": "Friday the 13th event (article 2571) turned players into a banshee form; a transformation, not an item received.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "Other client strings containing 'Banshee' are NPC or ability names: 'Banshee Boss' (npc_name, 4419449 and 4419451 flagged duplicate; quest_title 4419468), 'Howling Banshee' (3267, 5102898), 'Screeching Banshee' (45053), 'Banshee Bolt' (200), 'Banshee Form' (6580), 'Banshee Scream' (414867). None is typed as an item or card.", "source": "locale:4419449; locale:4419451; locale:4419468; locale:3267; locale:5102898; locale:45053; locale:200; locale:6580; locale:414867"},
  {"claim": "Id 407646356 was removed; it is not a client locale id.", "source": "id_check in pack"}
 ],
 "confidence": 0.6,
 "open": [
  "The subject is an NPC boss, not a purchasable item, so no vendor, Station Cash, Coin Shop, prize wheel, crafting, collection, drop, or event source applies on the evidence here.",
  "The wiki's 'Trading Card Game Series 1' appearance is unresolved. A 'Banshee Boss' TCG string may exist in the TCG data (en_us_data_tcg.dat, reported by a critique but not verified here). If it is a card, its pack source and price need a separate check. Client locale 4419449 is npc_name, not a card.",
  "Confirm with the job owner whether a Banshee trading card was meant. If so, redirect the job to that card.",
  "The 'bonus: find and defeat the 3 Bone Bog Skeletons' goal has no verified locale id.",
  "Enemy drop table for the Banshee boss is not in the pack.",
  "Locale ids 3267, 45053, 4419449, 6580, 200 were seen as strings but not tied to any item source."
 ]}
