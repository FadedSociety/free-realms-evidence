<!-- fleet job=item-infer id=igem-wand-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3125, 5554, 6, 1873] model=claude-haiku-5-5 -->
# Gem Wand

{"item": {"name": "Gem Wand", "locale_id": 14034, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Figwit Figgletons (sold the Gem Wand; past tense on wiki)", "where": "Briarwood", "price": "1236", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Gem_Wand (wiki text: 'previously sold by Figwit Figgletons in Briarwood for coins'; infobox coins 1236, rev 47382; category Vendor Weapons)"},
  {"type": "other", "detail": "Random reward from Level 15-20 Royal Vault chests (treasure vault)", "where": "Royal Vault (treasure chests)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Gem_Wand (wiki text: 'randomly acquired from Level 15-20 Royal Vault chests', citing 'Free Realms:Treasure Vault Tutorial -OBSOLETE-' on YouTube)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Gem Wand is a level 12 Wizard weapon (Lightning Blast, Zap 1492 dmg, Lightning Blast 6107 dmg).", "source": "https://freerealms.fandom.com/wiki/Gem_Wand"},
  {"claim": "Previously sold by Figwit Figgletons in Briarwood for 1236 coins (infobox value; the in-text price is blank).", "source": "https://freerealms.fandom.com/wiki/Gem_Wand"},
  {"claim": "Randomly acquired from Level 15-20 Royal Vault chests.", "source": "https://freerealms.fandom.com/wiki/Gem_Wand"},
  {"claim": "Retired December 14, 2009; currently only available through trade.", "source": "https://freerealms.fandom.com/wiki/Gem_Wand"},
  {"claim": "Client name locale 14034 = 'Gem Wand'.", "source": "locale:14034"},
  {"claim": "Figwit Figgletons exists as a Briarwood NPC record with no confirmed shop stock.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:139 (shop: None known); prototype/osfr-tools/data/content/npcs/briarwood.json:25466"}
 ],
 "confidence": 0.6,
 "open": [
  "The wiki's in-text price is blank; 1236 comes from the infobox field only. Confirm against a dated vendor screenshot or the Briarwood vendor data.",
  "Figwit Figgletons is listed in the repo with no known shop stock and no standing location; the vendor sale rests only on the wiki page's past-tense statement.",
  "Royal Vault chest source rests on a wiki sentence citing an obsolete YouTube tutorial; no video frame or chest table confirmed it.",
  "Wiki says 'currently only available through trade', so no live Coin Shop, SC Marketplace, or prize wheel source is listed. The pack shows no such categories.",
  "No pack critiques were supplied."
 ]}
