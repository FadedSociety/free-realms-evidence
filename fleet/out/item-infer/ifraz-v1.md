<!-- fleet job=item-infer id=ifraz-v1 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[3215, 6137, 6, 1391] model=claude-haiku-5-5 -->
# Fraz

{"item": {"name": "Fraz", "locale_id": 5102199, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Fraz' (locale 5102199) is an npc_name string, not an item name.", "source": "locale:5102199"},
  {"claim": "Fraz is a pixie NPC merchant in Wugachug who sells Brawler job gear (Bum Rush Brawler pieces, Brawler's Power Shard of Regeneration II, Ring of Energy II, Necklace of Bark Skin II, Hammer of Roundhouse, Hammer of Sweeps).", "source": "https://freerealms.fandom.com/wiki/Fraz"},
  {"claim": "Fraz was introduced in-game on August 6, 2013.", "source": "https://freerealms.fandom.com/wiki/Fraz (Trivia)"},
  {"claim": "Repo notes say the Fraz shop is a 2013-update vendor that a launch-era rebuild would not have.", "source": "notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:187"},
  {"claim": "Repo vendor data lists Fraz as an NPC vendor (NPC Id 1624, NameId 5102199).", "source": "prototype/osfr-tools/data/content/npcs/wugachug.json:4785"}
 ],
 "confidence": 0.9,
 "open": [
  "The pack targets an NPC, not an item. No item named Fraz exists in the client text or wiki. The sources of the items Fraz sells are the items' own packs, not this one.",
  "Fraz's stock is Brawler job gear. Each stocked item needs its own evidence pack to get its real sources and prices. The pack supplies no prices for the stock.",
  "Fraz's stock is listed on the wiki with no prices, and the wiki gives no coin or Station Cash figures for Fraz. Prices are unknown.",
  "Per the repo notes, Fraz is a 2013-era vendor, so the rebuild may not need this NPC at launch. This is a design question, not a sourcing one."
 ]}
