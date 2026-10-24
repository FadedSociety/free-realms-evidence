<!-- fleet job=citem-infer id=cprowling-rat-gi-122752-v4 status=nothing_found turns=2 usd=0.0029 tokens(read,write,in,out)=[6672, 14842, 6, 1897] model=claude-haiku-5-5 -->
# Prowling Rat Gi

{"item": {"name": "Prowling Rat Gi", "locale_id": 122752, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name line exists for Prowling Rat Gi (locale 122752), with the sibling set pieces Tabi Boots 122753, Armwraps 122754, Cowl 122755, Hakama 122756; the set is a ninja clothing set (slot 3, class 2).", "source": "locale:122752; locale:122753; locale:122754; locale:122755; locale:122756"},
  {"claim": "stores.json rows 8006-8008 are category 103 with item_ids 42753 (tint 1, 320 coins, member 288), 42758 (tint 2, 9453 coins) and 42763 (tint 3, 9453 coins). These are the only rows for the Gi's definition_ids that were checked; 42768-42808 have no row in the checked range.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8006-8008"},
  {"claim": "The 9453 tint 2/3 price is shared by many unrelated category-103 item_ids (e.g. 42454, 42459, 42534, 42539, 42838, 42843), so it is a tier price, not Gi-specific.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8001-8011"},
  {"claim": "item_id 42753 is also the rev_id of the weapon Bone Wand, so the store row's item is not confirmed as the Gi.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:6454-6456"},
  {"claim": "The wiki's Prowling Rat Bokken (a different Prowling Rat ninja weapon) was from Royal Vault chests and retired December 14, 2009. This is a sibling fact and does not apply to the Gi.", "source": "wiki page: Prowling Rat Bokken"},
  {"claim": "No wiki page, article, video, vendor stock row or quest names the Prowling Rat Gi.", "source": "lookup [client][wiki][articles][video] 'Prowling Rat'"}
 ],
 "confidence": 0.2,
 "open": [
  "Candidate only, not a source: store row item_id 42753 (category 103, tint 1, 320 coins, member 288) at repo:prototype/osfr-tools/data/content/stores.json:8006. It may be the Gi's variant, but the Bone Wand rev_id collision is unresolved and category 103 is not confirmed as clothing. Confirm before wiring as a coin_shop source.",
  "Candidate only: store rows 42758 and 42763 (tint 2/3, 9453 coins, member 8507) at stores.json:8007-8008. The 9453 price is shared by many unrelated items, so it does not identify the Gi.",
  "Definitions 42768-42808 have no store row in the checked range; full stores.json coverage for the Gi was not established.",
  "No dated source for retirement, current sale or drop. Retired stays null and live stays unsure.",
  "Cowl, Hakama, Tabi Boots and Armwraps have no wiki pages and were not sourced."
 ]}
