<!-- fleet job=item-infer id=itzu-v3 status=nothing_found turns=2 usd=0.0027 tokens(read,write,in,out)=[5262, 12659, 6, 2154] model=claude-haiku-5-5 -->
# Tzu

{"item": {"name": "Tzu", "locale_id": 5102442, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:5102442 is an npc_name string ('Tzu'), so the subject is an NPC merchant, not a purchasable item.", "source": "locale:5102442"},
  {"claim": "Tzu is a male Human NPC Merchant near the Shrouded Glade Warpstone, introduced in the 1 October 2013 update, who sells Warrior job items. The wiki gives no prices or currency for any stock item.", "source": "https://freerealms.fandom.com/wiki/Tzu (rev 33646)"},
  {"claim": "Tzu's stock per the wiki: Called Shot Warrior Pauldrons, Breeches, Helm, Gauntlets, Hightops, Tunic; Warrior's Flair Shard of Prosperity; Warrior's Power Shard of Vitality V; Warrior's Necklace of Vitality V; Warrior's Ring of Regeneration V; Warrior's Warlord Axe of Thunder, Hurling, Whirlwind, Earthquake, Cleaving.", "source": "https://freerealms.fandom.com/wiki/Tzu (rev 33646)"},
  {"claim": "The repo vendor record for Tzu lists the same stock and cites the wiki page as its source.", "source": "prototype/osfr-tools/data/content/vendors.json:31201-31290"},
  {"claim": "Repo note Jobs/Warrior.md:72 says Warlord Axe weapons (via Hackum, Snowhill) were retired 14 December 2009; the file resolves (the earlier 'does not resolve' claim was wrong). This is a repo note citing the wiki, not a wiki statement, and it conflicts with Tzu's 2013 stock list naming Warlord Axes.", "source": "notes/Build Guides/Content/Jobs/Warrior.md:72; notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:115"}
 ],
 "confidence": 0.3,
 "open": [
  "Subject 'Tzu' is an NPC, not an item, so no item-level acquisition source applies. To complete the record, run one pack per stocked item listed above. Each should carry 'vendor: Tzu, Shrouded Glade Warpstone' with source https://freerealms.fandom.com/wiki/Tzu and vendors.json:31201.",
  "Price and currency for every Tzu stock item are unknown: the wiki page gives none, and no coin shop, SC marketplace or retired category appears on it.",
  "Retirement of the Warlord Axe variants (Thunder, Hurling, Whirlwind, Earthquake, Cleaving) is unresolved. Repo note Warrior.md:72 says Warlord Axe weapons were retired 14 Dec 2009, but Tzu's wiki page lists them as current stock for an Oct 2013 introduction. Those two claims conflict and need a dated source per variant.",
  "The Called Shot set, Flair Shard, Power Shard, Necklace and Ring have no retirement evidence in this pack; live status is unverified.",
  "The NPC location (Shrouded Glade Warpstone) and the 1 Oct 2013 introduction date come from the wiki only, with no client or video check in this pass."
 ]
}
