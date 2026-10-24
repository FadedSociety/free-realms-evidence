<!-- fleet job=item-infer id=igilbert-v2 status=nothing_found turns=2 usd=0.0023 tokens(read,write,in,out)=[5278, 10839, 6, 1806] model=claude-haiku-5-5 -->
# Gilbert

{"item": {"name": "Gilbert", "locale_id": 5101980, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Locale 5101980 is tagged npc_name, so 'Gilbert' is a pixie archer merchant NPC, not an item.", "source": "locale:5101980"},
  {"claim": "Gilbert is a pixie male merchant near the Greenwood Forest warpstone who sells Archer job items; added 6 Aug 2013.", "source": "https://freerealms.fandom.com/wiki/Gilbert (rev 48996)"},
  {"claim": "The wiki Sells list for Gilbert names 12 items (six Hen Feather Archer pieces, two Archer's Flair Shards, Archer's Power Shard of Vitality I, Archer's Necklace of Vitality I, Archer's Ring of Regeneration I, Archer's Bow of Volleys). No prices are given.", "source": "https://freerealms.fandom.com/wiki/Gilbert (Sells section)"},
  {"claim": "Repo vendor data already records Gilbert as a vendor (npc_name Gilbert) in the vendors and NPC files, with the same wiki page as source.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:15858; repo:prototype/osfr-tools/data/content/npcs/greenwood_forest.json:10960"},
  {"claim": "Hen Feather Archer Gloves is a level 1 Archer hand item that the wiki says comes from the Cursed Graveyard, Hewey's Escape, Hot Springs Haven and King of the Ring! prize wheels. It is also on Gilbert's Sells list, so a named-item run must reconcile vendor and prize-wheel sources.", "source": "lookup wiki page 'Hen Feather Archer Gloves'"}
 ],
 "confidence": 0.2,
 "open": [
  "The target is an NPC, not an item. No item-level sources were emitted, so none are invented for the NPC name.",
  "If the target is one of Gilbert's 12 Archer items, rerun with that exact item name. Gilbert would then be a vendor source with the wiki Sells section as evidence. The wiki gives no coin or Station Cash price for any of them, and vendor_stock in the pack is empty, so price stays unknown.",
  "The critique's request to add a vendor source for all 12 items is not followed: the pack names no item target, and the Gloves wiki page lists prize wheels as a separate source.",
  "Retired status and whether Gilbert's stock is still live are not stated in any source in the pack. Only the 2013 introduction date is known."
 ]}
