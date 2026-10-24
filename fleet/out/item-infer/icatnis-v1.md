<!-- fleet job=item-infer id=icatnis-v1 status=nothing_found turns=2 usd=0.0019 tokens(read,write,in,out)=[3290, 8603, 6, 1567] model=claude-haiku-5-5 -->
# Catnis

{"item": {"name": "Catnis", "locale_id": 5101987, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Catnis' is an NPC name, not an item: client string 5101987 is tagged npc_name", "source": "locale:5101987"},
  {"claim": "Wiki page describes Catnis as a human NPC merchant at the north-western edge of Blackspore Swamp who sells exclusively Archer job items; categories NPC, Females, Human, Archer, Merchant, Blackspore", "source": "wiki Catnis (rev 48937)"},
  {"claim": "Wiki Merchants page lists Catnis under Job Specific: Archer", "source": "wiki Merchants"},
  {"claim": "Wiki says Catnis was introduced in-game on August 6, 2013", "source": "wiki Catnis"}
 ],
 "confidence": 0.9,
 "open": [
  "Subject mismatch: the pack asks for the source of an item named Catnis, but Catnis is an NPC merchant. No item of that name exists in the client text or the wiki, so no item sources were assigned.",
  "The wiki's Sells list for Catnis (no prices, no currency given): Bobtailed Archer Quiver, Bobtailed Archer Leggings, Bobtailed Archer Cap, Bobtailed Archer Gloves, Bobtailed Archer Boots, Bobtailed Archer Hoodie, Archer's Flair Shard of Autumn, Archer's Power Shard of Regeneration IV, Archer's Ring of Energy IV, Archer's Necklace of Bark Skin IV, Archer's Recurve Bow of Flame, Archer's Recurve Bow of Blizzards, Archer's Recurve Bow of Volleys. If one of these is the real target, rerun with that item; her vendor stock is wiki-sourced only (no client dialog or vendor table was found tying her to these items).",
  "Repo notes (quest-lines/npcs.json) record a name-id mismatch for Catnis (ucdt 2867311549 vs client 5101987) and wiki-only placement in Blackspore Swamp; her role and stock are not client-verified.",
  "No coin, Station Cash, Coin Shop, or prize wheel price is given for her stock on the wiki page."
 ]}
