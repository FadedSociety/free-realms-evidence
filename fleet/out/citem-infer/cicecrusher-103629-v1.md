<!-- fleet job=citem-infer id=cicecrusher-103629-v1 status=nothing_found turns=3 usd=0.0030 tokens(read,write,in,out)=[13332, 13882, 8, 2274] model=claude-haiku-5-5 -->
# Icecrusher

{"item": {"name": "Icecrusher", "locale_id": 103629, "kind": "weapon"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Locale 103629 is the text 'Icecrusher', but the client tags it npc_name, not item. The client's item definition 30561 uses it as its name (slot 7, class 5, model hammer_ar_ag_weapon_mega.adr), so it is probably a weapon name.", "source": "locale:103629; client definition pack"},
  {"claim": "Icecrusher appears in the client's text tables under two hash ids (ugdt 1434492258 and ucdt 2679415944), in the same text-table data as the other locale copies.", "source": "FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:38005, :70551"},
  {"claim": "The model hammer_ar_ag_weapon_mega.adr is shared by many item definitions in the legacy item table, so the model alone does not identify this item.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:85349 and following"},
  {"claim": "No wiki page, image text, article fact, or video frame names Icecrusher. The client-text lookup returns only locale:103629.", "source": "lookup (client, wiki, articles, video) for 'Icecrusher'"},
  {"claim": "No coin store price, vendor stock, quest reward, drop, or other answer mentions Icecrusher.", "source": "repo search and pack vendor_stock = []"},
  {"claim": "Its neighbours in the locale cluster (Angro's Vanquisher 103627, Broodling 103631, Broodmother 103634) are a Warrior weapon and two monster names. This may be a boss-related weapon, but that is not confirmed.", "source": "locale:103627, 103631, 103634; freerealms-wiki/harvest/lists/weapons.json:808 (Angro's Vanquisher wiki note)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found anywhere: no wiki article, no store price, no vendor, no quest or drop answer. Sources are left empty rather than guessed.",
  "The client tags 103629 as npc_name, so it may be an NPC or boss name shared with the weapon. Confirm which before treating it as an item.",
  "Definition 30561 has no description and no coin price. Its variant count (1) and the shared model need checking in the item table (ClientItemDefinitions) to confirm it is a live weapon and not a removed or test item.",
  "Icecrusher may be a Warrior-class weapon like Angro's Vanquisher, but nothing in the sources confirms this.",
  "The first-pass tag (live unsure, source unknown) is a hint only and was not used as evidence."
 ]}
