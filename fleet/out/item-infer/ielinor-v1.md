<!-- fleet job=item-infer id=ielinor-v1 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[3191, 8286, 6, 1447] model=claude-haiku-5-5 -->
# Elinor

{"item": {"name": "Elinor", "locale_id": 5101996, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Elinor is a human NPC merchant (Archer gear vendor) near the Shrouded Glade Pet Park, not an item. Her wiki page says she 'sells exclusively Archer Job items'.", "source": "https://freerealms.fandom.com/wiki/Elinor"},
  {"claim": "Client text locale:5101996 is tagged npc_name 'Elinor', so the name belongs to an NPC, not an item.", "source": "locale:5101996"},
  {"claim": "Repo data models Elinor as an NPC spawn (human_f_merchant_archer_caucasian.agr, shrouded_glade.json) with the vendor stock listed in vendors.json and vendors_unresolved.json.", "source": "repo:prototype/osfr-tools/data/content/npcs/shrouded_glade.json:14577"},
  {"claim": "Wiki Merchants page lists Elinor among Archer job merchants found near the Shrouded Glade Pet Center.", "source": "https://freerealms.fandom.com/wiki/Merchants"},
  {"claim": "Wiki page says Elinor was introduced in-game on August 6, 2013.", "source": "https://freerealms.fandom.com/wiki/Elinor"}
 ],
 "confidence": 0.9,
 "open": [
  "The request is for an item, but 'Elinor' is an NPC merchant. No item named Elinor exists in the client text or the wiki, so no item sources were recorded.",
  "If the intended item is one she sells, rerun with that item's name. Her stock per the wiki: Pin Hole Archer Quiver, Leggings, Shades, Gloves, Boots, Hoodie; Archer's Raptor Bow of Flame, of Stunning, of Splintering, of Volleys. The wiki gives no prices for these, and the pack has no vendor-stock or price evidence for them.",
  "Wiki gives no coin or Station Cash prices for Elinor's stock, so no price is recorded here."
 ]}
