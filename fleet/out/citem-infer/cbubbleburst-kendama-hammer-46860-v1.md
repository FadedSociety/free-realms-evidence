<!-- fleet job=citem-infer id=cbubbleburst-kendama-hammer-46860-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[12366, 9206, 8, 1701] model=claude-haiku-5-5 -->
# Bubbleburst Kendama Hammer

{"item": {"name": "Bubbleburst Kendama Hammer", "locale_id": 46860, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only (Blue Text weapon). No vendor, quest, drop or event source is recorded.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Bubbleburst_Kendama_Hammer (wiki text: \"can only be acquired through trade\"); repo:prototype/osfr-tools/data/reference/weapons.json:9713"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Item is a level 4 Brawler weapon, Power 3, Blue Text weapon, acquirable only through trade.", "source": "https://freerealms.fandom.com/wiki/Bubbleburst_Kendama_Hammer"},
  {"claim": "Wiki category 'Retired Weapons' is present on the page.", "source": "https://freerealms.fandom.com/wiki/Bubbleburst_Kendama_Hammer"},
  {"claim": "Client definition id 22110, name locale 46860, slot 7, class 5, model hammer_ar_ag_weapon_kendama.adr; no coin store price.", "source": "locale:46860; repo:prototype/osfr-tools/data/reference/weapons.json:9746"},
  {"claim": "Wiki item tooltip shows Resell Value 81, Power 3, Required Level 4 Brawler, abilities Glancing Blow (776 dmg) and Leg Sweep (2716 dmg).", "source": "wiki image:item_tooltip Bubbleburst Kendama Hammer item.jpg"},
  {"claim": "Sibling 'Bubbleburst' weapons (Blade, Bow, Battle Axe, Scalpel, Wand) share the same naming set and the same Blue Text/trade-era style; this suggests a single promotional set but no source confirms it.", "source": "locale:46851, 46854, 46857, 46863, 46866 (client text)"},
  {"claim": "The first-pass tag said 'event' as source guess; no article, video or vendor evidence supports this, so it is not used as a source.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.4,
 "open": [
  "The only source is the wiki line 'can only be acquired through trade'. Player trade is not a vendor, quest, drop, or store; no trade partner, date, or event is recorded.",
  "The 'event' guess from the first-pass tag has no evidence; the Bubbleburst set may have come from an event, but this is unverified.",
  "No coin store price exists in the client or stores.json, so no coin vendor sale is claimed.",
  "No wiki price is given (the tooltip shows Resell Value 81 only, which is not an acquisition price). The client 'cost' of 811 in weapons.json is not a sourced price, so it is not used.",
  "Wiki page has no 'Retired' date; retirement is taken from the 'Retired Weapons' category only."
 ]}
