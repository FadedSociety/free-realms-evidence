<!-- fleet job=citem-infer id=cn-urgent-care-medic-pants-pl-urgent-care-medic-pants-133096-v2 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[21592, 7884, 10, 2249] model=claude-haiku-5-5 -->
# {n}Urgent Care Medic Pants{pl="Urgent Care Medic Pants"}

{"item": {"name": "Urgent Care Medic Pants", "locale_id": 133096, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Gaius (Medic job merchant; sells exclusively [Medic] job items). Sells list includes [Urgent] [Care] [Medic] [Pants].", "where": "Seaside, near the Information Center", "price": "403 coins listed in repo reference data (stores.json, item 76088); not a captured NPC quote, so treat as unverified", "currency": "coins", "source": "wiki page 'Gaius' (Sells section, lookup verified); repo:prototype/osfr-tools/data/content/vendors.json lines 26007-26048 (npc_id 9500000585, item_id 76088). Price: repo:data/content/stores.json line 15801 as cited in the prior answer; I could not re-open that file to verify it."},
  {"type": "prize_wheel", "detail": "[Medic] Prize Wheel (dungeon prize wheel entry; the page lists [Urgent] [Care] [Medic] [Pants])", "where": "Dungeon prize wheels", "price": null, "currency": null, "source": "wiki page '[Medic] Prize Wheel' (lookup verified: lists '[Urgent] [Care] [Medic] [Pants]'). Probable match; the Thugawug Sneak! and Ice Troll Scout! pages instead name 'Urgent Care Medic Fatigues', which has no client match, so they are not used as support."}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 133096 is 'Urgent Care Medic Pants', part of a 10-item Medic set (133091-133101).", "source": "locale:133096; client cluster"},
  {"claim": "The wiki Gaius page's Sells section lists [Urgent] [Care] [Medic] [Pants] alongside the Backpack, Cap, Gloves, Boots and Shirt.", "source": "wiki page Gaius (lookup verified)"},
  {"claim": "The [Medic] Prize Wheel wiki page lists [Urgent] [Care] [Medic] [Pants].", "source": "wiki page '[Medic] Prize Wheel' (lookup verified)"},
  {"claim": "The Thugawug Sneak! and Ice Troll Scout! pages list 'Urgent Care Medic Fatigues', not Pants, so they do not confirm the Pants.", "source": "wiki pages Thugawug Sneak! and Ice Troll Scout! (lookup verified)"},
  {"claim": "The 403 / 362 / 40 coin figures are reference store data, not an observed Gaius quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 26016 and 26045 (per critique)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 403-coin price (362 member, 40 sell) is repo reference data only. Confirm on a live Gaius screen or a dated wiki price before treating it as exact.",
  "The Gaius listing's last revision date (2013-08-31) was not re-verified in this pass.",
  "The repo file data/content/stores.json could not be opened from this environment, so the line 15801 row was not re-checked.",
  "The prize wheel entry is a name match only: the wiki says 'Pants' on the [Medic] Prize Wheel but 'Fatigues' on the dungeon pages. Confirm in game which garment the wheel drops.",
  "The Robgoblin Treasure Trove 'random Medic set piece' drop is removed: no source names the Pants as one of its possible pieces.",
  "Live status is unsure. The item still exists in the client and on the Gaius listing; no retirement notice was found, but the item's current availability was not checked."
 ]}
