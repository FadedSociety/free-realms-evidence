<!-- fleet job=item-infer id=isonja-v2 status=blocked turns=1 usd=0.0012 tokens(read,write,in,out)=[0, 5210, 4, 1167] model=claude-haiku-5-5 -->
# Sonja

{"item": {"name": "Sonja", "locale_id": 5102437, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Sonja' (locale 5102437) is an npc_name string, so the subject is a merchant NPC, not a Free Realms item.", "source": "locale:5102437; https://freerealms.fandom.com/wiki/Sonja"},
  {"claim": "The wiki lists Sonja as a female Human merchant in Snowhill who sells Warrior job items, introduced in the October 1, 2013 update. Her stock list has no prices or currency.", "source": "https://freerealms.fandom.com/wiki/Sonja"},
  {"claim": "The repo records the same stock list for Sonja, with no prices.", "source": "prototype/osfr-tools/data/content/vendors.json:34994; notes/Build Guides/Content/NPCs/NPCs - Snowhill.md row 109"}
 ],
 "confidence": 0.1,
 "open": [
  "Blocked: the pack is for an NPC, not an item, so no single item's sources can be stated. Resubmit with one stocked item name, for example Warrior's Battle Hammer of Hurling, Warrior's Necklace of Vitality III, or Combat Bonus Warrior Helm.",
  "No per-item price or currency for any Sonja stock item appears in the pack (wiki coin and station_cash lists are empty), so no vendor, price or currency source can be wired from it.",
  "Whether Sonja still sells these items is unverified; the pack has no retirement source.",
  "repo vendors_unresolved.json also holds a Sonja entry (around line 8467), so her vendor link is not fully resolved.",
  "Dropped the earlier Medic Flu Season / Template:News claim: the source is not in the pack and it does not bear on item acquisition."
 ]}
