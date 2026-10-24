<!-- fleet job=item-infer id=ibuckled-skull-jacket-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5388, 7549, 6, 1951] model=claude-haiku-5-5 -->
# Buckled Skull Jacket

{"item": {"name": "Buckled Skull Jacket", "locale_id": 33990, "kind": "clothing"},
 "sources": [
  {"type": "drop", "detail": "Dungeon Precursor Ruins, generic 'item drop' (no enemy named on the wiki)", "where": "Precursor Ruins (Sunstone Valley)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket (rev 31246); repo:prototype/osfr-tools/data/content/dungeons/precursor_ruins.json:614"},
  {"type": "drop", "detail": "Sunstone Valley boss chest (boss unnamed; wiki does not say whether Venoxa's chest is one)", "where": "Sunstone Valley", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket (rev 31246); repo:prototype/osfr-tools/data/content/dungeons/precursor_ruins.json:630"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Wiki: a Members only Freestyle Jobs Clothing item drop, acquirable through the Dungeon Precursor Ruins or a Sunstone Valley Boss Chest", "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket (rev 31246)"},
  {"claim": "Client text name is 'Buckled Skull Jacket' at locale:33990", "source": "locale:33990"},
  {"claim": "Wiki categories include Members Only, Clothing, Chest, Freestyle Jobs, Sunstone Valley (membership gate, not a retirement fact)", "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket"},
  {"claim": "The wiki's 27 is a resell value, not a purchase price; the wiki text leaves the resell amount blank. Repo selling note lists Buckled Skull Jacket at 27 as a sell-back figure", "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket; repo:notes/Research/Pieces/084 Selling and buyback.md:102"},
  {"claim": "Item can be traded per wiki", "source": "https://freerealms.fandom.com/wiki/Buckled_Skull_Jacket"},
  {"claim": "No coin vendor, store, or vendors.json/stores.json row for item 33990 was found in the repo", "source": "repo search for 33990 / Buckled Skull"}
 ],
 "confidence": 0.5,
 "open": [
  "Sources are dungeon-level and chest-level only. No enemy name for Precursor Ruins and no boss name for the Sunstone Valley chest is evidenced, so no enemy drop is claimed. wireable = false until a named enemy or boss is confirmed.",
  "Membership gate: wiki category 'Members Only' means the item is membership-gated; this is recorded as a fact, not as a membership source.",
  "No purchase price anywhere. 27 coins is a resell value only and must not be stored as a vendor price.",
  "Retirement and current availability are unknown: the wiki gives no date and no retirement category.",
  "Repo note 'Precursor Ruins.md' cites client loc 413478426 for this item, but the client table gives the name at locale:33990. The note's id looks wrong; 33990 is the confirmed id.",
  "Wiki page is a single paragraph with no drop rates or images."
 ]}
