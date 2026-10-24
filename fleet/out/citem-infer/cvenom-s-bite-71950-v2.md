<!-- fleet job=citem-infer id=cvenom-s-bite-71950-v2 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[22117, 10215, 10, 2551] model=claude-haiku-5-5 -->
# Venom's Bite

{"item": {"name": "Venom's Bite", "locale_id": 71950, "kind": "weapon"},
 "sources": [
  {"type": "drop", "detail": "Dropped at random by certain 'boss' enemies in members-only dungeons (Blue Text weapon rule; specific enemy and dungeon not named for this item)", "where": "Dungeons (unnamed)", "price": null, "currency": null, "source": "wiki page:ns14 Category:Blue Text Weapons (lookup: 'They were members only weapons that were acquired in dungeons where they were dropped at random by certain \"boss\" enemies')"},
  {"type": "other", "detail": "Player-to-player trade only (sibling-page rule: Tidal Scythe, same level 8 / power 4 Blue Text row, 'can only be acquired through trade'; Venom's Bite's own page not found)", "where": null, "price": null, "currency": null, "source": "freerealms-wiki/wikitext/16975-26501-8555c0ca6965.wiki:3; freerealms-wiki/wikitext/3831-21850-8a08ba4573a2.wiki:68"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client item 'Venom's Bite' is locale 71950, definition 22200, slot 7, class 30, model axe_ar_ag_weapon_scythe.adr; no coin store price in the client definition.", "source": "client definition in task pack; locale:71950"},
  {"claim": "Venom's Bite is in the Venom's Blue Text weapon row (level 8, power 4) with Sting, Crush, Spur, Malice, Touch.", "source": "freerealms-wiki/wikitext/3831-21850-8a08ba4573a2.wiki:68; freerealms-wiki/harvest/lists/tables.json:2174-2184"},
  {"claim": "Blue Text weapons were members-only dungeon drops from boss enemies, and their names were retired (category-level statement; not checked on Venom's Bite's own page).", "source": "wiki page:ns14 Category:Blue Text Weapons; wiki page:ns0 Blue Text weapon"},
  {"claim": "Sibling Tidal Scythe is a Blue Text weapon that can only be acquired through trade.", "source": "freerealms-wiki/wikitext/16975-26501-8555c0ca6965.wiki:3"},
  {"claim": "Name 'Venom's Bite' (71950) is distinct from the Snakes in a Maze ability 'Venom Bite' (115808).", "source": "locale:71950; locale:115808; notes/Build Guides/Content/Dungeons/Snakes in a Maze.md:44"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki article for Venom's Bite itself was found; all source claims are category-level or sibling-page inferences.",
  "Dungeon drop: the named boss enemy, dungeon and drop rate are not identified in any evidence; the drop source comes from the Blue Text category rule.",
  "Trade-only status is inferred from sibling Tidal Scythe's page, not Venom's Bite's own page.",
  "The earlier claim that Venom's Crush is in Category:Retired Weapons was dropped: the cited citem-packs.json is a pack of answers, not a wiki source, and the category listing was not verified.",
  "Retired: true rests on the Blue Text category wording ('before being retired'); no date of retirement found. live 'no' follows from that; confirm with a current-tip check.",
  "wireable is false: no price, no vendor, no quest, no named enemy."
 ],
 "wireable": false}
