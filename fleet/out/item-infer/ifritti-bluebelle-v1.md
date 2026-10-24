<!-- fleet job=item-infer id=ifritti-bluebelle-v1 status=nothing_found turns=2 usd=0.0014 tokens(read,write,in,out)=[2930, 4622, 6, 1514] model=claude-haiku-5-5 -->
# Fritti Bluebelle

{"item": {"name": "Fritti Bluebelle (NPC, not an item)", "locale_id": 90186, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Fritti Bluebelle is an NPC (wiki category NPC, infobox status 'Vendor (Member Only)', location Snowhill), not a purchasable item.", "source": "https://freerealms.fandom.com/wiki/Fritti_Bluebelle"},
  {"claim": "Client name entry is an npc_name string.", "source": "locale:90186"},
  {"claim": "Wiki page says she sells Medic clothing and tools, but names no specific item and gives no price.", "source": "https://freerealms.fandom.com/wiki/Fritti_Bluebelle"},
  {"claim": "Repo notes say her stock is unknown and she was probably replaced by Spratt.", "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:112"},
  {"claim": "Her vendor entry is unresolved in the repo data.", "source": "prototype/osfr-tools/data/content/vendors_unresolved.json:8215"}
 ],
 "confidence": 0.2,
 "open": [
  "The brief asks for one item's sources, but the subject is the vendor NPC Fritti Bluebelle. Confirm the intended item name.",
  "Lead, not confirmed for her: the wiki Bonesaw page says it 'was previously sold by Fritti Bluebelle in Snowhill for coins, until retired on December 14, 2009' and is now trade-only. If the target item is the Bonesaw, its vendor source is Fritti Bluebelle (Snowhill, coins, price not given in pack), retired 2009-12-14. Source: https://freerealms.fandom.com/wiki/Bonesaw. Verify the price before use.",
  "No specific Medic clothing or tool items, prices, or revision history for her stock are in the pack. Her stock list is not available here."
 ]}
