<!-- fleet job=citem-infer id=cn-heal-support-boots-pl-heal-support-boots-122289-v2 status=nothing_found turns=6 usd=0.0034 tokens(read,write,in,out)=[45968, 12369, 14, 2701] model=claude-haiku-5-5 -->
# {n}Heal Support Boots{pl="Heal Support Boots"}

{"item": {"name": "Heal Support Boots", "locale_id": 122289, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines Heal Support Boots as NameId 122289 with Slot 5, Class 7, Cost 618, CategoryId 105, ModelName military_<race>_<gender>_feet_boots.adr, MinProfileRank 13 (definitions 42290 and 42295 both carry NameId 122289)", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 907786-907805 and 907874-907890"},
  {"claim": "Item 42292 is the Heal Support Cap (NameId 122291, Slot 1, CategoryId 101), not the Boots. The stores.json row for 42292 (category 101, 618 coins, member 556, sell 61) therefore prices the Cap, and cannot be used as a Boots source.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 907828-907850; repo:prototype/osfr-tools/data/content/stores.json:12718"},
  {"claim": "No store row in repo data exists for item 42290 or 42295 (the Boots definitions), so no Boots coin-store listing is evidenced.", "source": "repo search for item_id 42290 / 42295 under prototype/osfr-tools/data: no match"},
  {"claim": "Locale 122289 is the only client text for the Boots; no wiki page, image, article fact, video frame, vendor stock, quest reward, drop or event names it.", "source": "lookup on client, wiki, articles (only locale:122289 returned)"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced source for Heal Support Boots. The previous answer's vendor source (item 42292, 618 coins, category 101) is wrong: 42292 is the Heal Support Cap (NameId 122291). That row must be removed from the Boots record.",
  "The Boots' client Cost field is 618 on definitions 42290 and 42295, but the client Cost is not a store listing. Confirm whether any coin vendor sells a Boots definition before stating a Boots price.",
  "Definition 42290 and 42295 are Boots definitions, and the pack's definition list (42290-42345 step 5) mixes Boots with other pieces (e.g. 42291 Gloves, 42293 Fatigues, 42294/42299 elsewhere). The 16 definitions were not individually checked for store rows beyond 42290 and 42295.",
  "No wiki page for Heal Support Boots. The Heal Support Bonesaw 'trade only' note cited in the prior answer was not verified here and does not transfer to the Boots.",
  "No quest, drop, event, membership, or promotion source found; no vendor NPC named. Retirement status unknown.",
  "Locale 122289 has no description text (DescriptionId 1114 is shared by the whole set and was not checked)."
 ]}
