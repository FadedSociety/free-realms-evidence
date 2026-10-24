<!-- fleet job=item-infer id=itunic-of-the-branch-druid-v3 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6261, 12052, 6, 2212] model=claude-haiku-5-5 -->
# Tunic of the Branch Druid

{"item": {"name": "Tunic of the Branch Druid", "locale_id": 3835, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Cragara, the Mysterious Merchant (roaming snail vendor; sold for Station Cash, Member price is a 10% discount)", "where": "Mysterious Merchant (Cragara roams six towns: Seaside, Merry Vale, Snowhill, Blackspore Swamp, Briarwood, Sunstone Valley)", "price": "125 Station Cash regular; 112 Station Cash for Members. Wiki body text has the amounts blanked; these figures are wiki metadata only (station_cash [125, 112]) and the 10% discount is inferred from them.", "currency": "station_cash", "source": "wiki page 'Tunic of the Branch Druid' (rev 45725), Mysterious Merchant section and 'Category:Mysterious Merchant'; wiki station_cash metadata [125, 112]; repo notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md row 164 and NPCs - Snowhill.md row 150 (Cragara roams six towns, random limited stock)"},
  {"type": "drop", "detail": "Item drop during the Shrouded Glade Invasion. Enemy and drop rate are not named by any source.", "where": "Shrouded Glade (invasion event)", "price": null, "currency": null, "source": "wiki page 'Tunic of the Branch Druid' ('It can be acquired as an item drop during the Shrouded Glade Invasion'); locale:2313 (The Invasion of Shrouded Glade) as event context"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is 'Tunic of the Branch Druid' (unflagged client item string).", "source": "locale:3835"},
  {"claim": "Multi-job, chest slot, combat clothing, Level 1, requires Ninja, Warrior, or Wizard.", "source": "wiki page 'Tunic of the Branch Druid'"},
  {"claim": "Sold by Cragara, the Mysterious Merchant, for Station Cash at 125 regular and 112 for Members. Metadata only: the body text is blanked, so the text does not confirm these amounts.", "source": "wiki page 'Tunic of the Branch Druid' Mysterious Merchant section; wiki station_cash metadata [125, 112]"},
  {"claim": "Cragara is a random roaming Mysterious Merchant, so stock and availability are not fixed; the wiki's 'Currently' has no date.", "source": "repo notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md row 164; NPCs - Snowhill.md row 150; wiki page 'Tunic of the Branch Druid'"},
  {"claim": "Obtainable as an item drop during the Shrouded Glade Invasion. The source gives no enemy or drop rate.", "source": "wiki page 'Tunic of the Branch Druid'; locale:2313"},
  {"claim": "locale:3836 is dropped as evidence: it is flagged as a duplicate flavor-text string of 3832 and supports no acquisition path. The June 2012 and Gloam siege framing is dropped: article 2614 is not in the pack and does not support it. The enemy 'General Drahk's Elite Gloam Constructs' is not named as the dropper; locale:439 is only the invasion announcement.", "source": "id_check and critiques in pack; lookup locale:3836 (FLAG duplicate); locale:439"}
 ],
 "confidence": 0.5,
 "open": [
  "Station Cash prices 125 / 112 rest only on wiki metadata; the body text is blanked. The 10% discount is inferred. Confirm against a live Cragara sighting or a store entry.",
  "No store entry for this tunic was found in repo data (vendors.json, vendors_unresolved.json); the repo lists 'Glove of the Branch Druid' under Cragara but not this tunic.",
  "Cragara's current availability is unknown; the wiki says 'Currently' with no date, so the item may be a limited rotating stock item. Retired is null because no source says it was retired.",
  "Shrouded Glade Invasion drop: enemy, drop rate and loot table are unknown; no drop table found in the repo.",
  "No coin price: the wiki coin field is empty and no coin vendor in the pack stocks it.",
  "Sibling Cragara wiki pages carry the same blanked amounts, so there is no independent cross-check of the Station Cash price."
 ],
 "critiques_addressed": "Dropped locale:3836 evidence; marked prices as wiki-metadata-only; removed June 2012/Gloam siege framing; kept the drop at event level with the enemy unnamed; retired null and live unsure kept as the critiques accepted."
}
