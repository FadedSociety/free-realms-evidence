<!-- fleet job=item-infer id=ibroheim-backfire-v2 status=nothing_found turns=2 usd=0.0019 tokens(read,write,in,out)=[4712, 9289, 6, 1391] model=claude-haiku-5-5 -->
# Broheim Backfire

{"item": {"name": "Broheim Backfire", "locale_id": 439699, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Broheim Backfire is a dwarf NPC merchant (Male, Dwarf, Gray hair, Brown eyes) in Red's Haven, Sunstone Valley, with Occupation Merchant. The page says he 'sells crafting supplies from the Coin Shop'. It gives no item names, prices or currency, so it does not name an item source.", "source": "https://freerealms.fandom.com/wiki/Broheim_Backfire (rev 45821)"},
  {"claim": "Locale 439699 is the NPC's name, tagged 'ability' in the client text table. It is not an item name.", "source": "locale:439699"},
  {"claim": "The NPC is in the Sunstone Valley NPC list and the Freewheeler biker gang members list on the wiki.", "source": "wiki page:Sunstone Valley; wiki page:Freewheeler biker gang; wiki page:Dwarves"},
  {"claim": "Repo NPC data gives the NPC NameId 439699 (legacy Npcs.json Id=3857, dwarf_m_biker model). The repo's notes say his stock list was not recorded and no price is recorded.", "source": "repo:prototype/osfr-tools/data/content/npcs/sunstone_valley.json:2858-2864; repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md:51,345"},
  {"claim": "Video frame text: the name appears on screen, but the evidence does not clearly show it as his own nameplate. Correction to the earlier answer, which overstated this.", "source": "video:fMOGHMuA2Hc/00228.jpg (other_text; structured field lists only a Wheelie Pete nameplate)"}
 ],
 "confidence": 0.85,
 "open": [
  "The target is an NPC, not an item. No item source can be assigned from this pack. Ask for the intended item name.",
  "If the intent is his coin-vendor stock: the wiki names no items and no prices, and the repo's vendors_unresolved.json has an unresolved vendor entry for him (prototype/osfr-tools/data/content/vendors_unresolved.json:8990-9016) with no item list. Pull the actual stock from a verified source before recording any vendor, price, or currency.",
  "The earlier answer's nameplate claim for video:fMOGHMuA2Hc/00228.jpg was overstated and is corrected here.",
  "Live status of the NPC is unverified; the wiki page carries no date for when he was active."
 ]}
