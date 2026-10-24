<!-- fleet job=item-infer id=imerhione-v1 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[3315, 5803, 6, 1399] model=claude-haiku-5-5 -->
# Merhione

{"item": {"name": "Merhione", "locale_id": 5102515, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:5102515 is an npc_name string, 'Merhione'. It names an NPC, not an item.", "source": "locale:5102515"},
  {"claim": "The wiki page 'Merhione' describes a human NPC merchant in northern Seaside who sells Wizard job items. Its categories are NPC, Females, Human, Merchant, Seaside and Wizard.", "source": "https://freerealms.fandom.com/wiki/Merhione"},
  {"claim": "The wiki 'Merchants' page lists Merhione as found in Northern Seaside, alongside other merchant NPCs.", "source": "wiki page 'Merchants'"},
  {"claim": "The repo's NPC notes record Merhione as a Wizard job merchant added 15 October 2013 in Northern Seaside, with no item of her own.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:127"}
 ],
 "confidence": 0.9,
 "open": [
  "The pack asks for the source of an item, but its subject is an NPC vendor. The wiki page has no item name, price or item category for Merhione herself, so no item sources are recorded.",
  "The items she sells are separate items with their own sources, and none is named in this pack as the target. Her stock is Hedge Wizard Talisman, Hedge Wizard Skirt, Hedge Wizard Slacks, Hedge Wizard Cap, Hedge Wizard Gloves, Hedge Wizard Shoes, Hedge Wizard Short Cloak, Wizard's Flair Shard of Gifted, Wizard's Power Shard of Regeneration II, Wizard's Ring of Energy II, Wizard's Necklace of Bark Skin II, Wizard's Wand of Firestorm and Wizard's Wand of Glaciers. Re-run with one of these as the item.",
  "The wiki page gives no prices for her stock. The repo's vendor data (prototype/osfr-tools/data/content/vendors.json, around line 27163) has a Merhione entry, but it is not quoted in the pack and was not verified here.",
  "The wiki page does not say whether Merhione is still active. Her 2013 introduction date comes from the wiki trivia section only."
 ]}
