<!-- fleet job=citem-infer id=craging-rampage-helm-713-v2 status=nothing_found turns=3 usd=0.0044 tokens(read,write,in,out)=[23225, 22954, 8, 2685] model=claude-haiku-5-5 -->
# Raging Rampage Helm

{"item": {"name": "Raging Rampage Helm", "locale_id": 713, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Raging Rampage Helm' is locale 713 (item). The set's other pieces are locale 693 Bracers, 718 Cape, 723 Boots, 765 Corselet, 786 Leggings (flagged dev_note raw template markup), 826 Harness, 861 Skirt.", "source": "locale:713; lookup client results for locale:693, 718, 723, 765, 786, 826, 861"},
  {"claim": "The same piece names appear in the Free Realms-Legacy and Lxzxrus-Free-Realms-Server ClientItemDefinitions.json as item comments (Helm at line 7212 in both). These are name labels only; they carry no source, vendor, price or drop data.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:7212; Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:7212"},
  {"claim": "Client text sits in a locale cluster with 'Fierce Frenzy' pieces (708, 755, 811) and 'Farm Unlocks Are Here!' (709, 710). Nothing in the cluster ties the set to a source, and the farm promotion is a separate vending item.", "source": "locale:708, 709, 710; quest-lines/line-packs.json (cluster listing)"},
  {"claim": "Wiki 'Shrouded Gloam' says the Gloam invasion and General Drahk fights reward 'a [chest] that gives dwarf/druid armor, a housing item, a consumable that grants an illusion, coins, or pets.' The page does not name any Raging Rampage piece, so this is only a candidate mechanism.", "source": "lookup wiki page 'Shrouded Gloam'"},
  {"claim": "Locale 714 restricts the Gloam Construct chest to players who helped defeat the Gloam Construct invasion. It does not name this helm or say what the chest contains.", "source": "locale:714"},
  {"claim": "No coin store price, no coin vendor stock, no quest reward, no enemy drop row, and no wiki article, image, article fact or video frame names this helm. Repo search for Rampage/Gloam found only notes and unrelated 'rampage' strings.", "source": "client definition pack (coin_store_prices empty); repo search; lookup wiki/articles/video ('Raging Rampage' and 'Raging Rampage Helm set armor reward': no matches)"},
  {"claim": "The previous answer's event source (Gloam invasion) is not evidenced for this helm. The wiki line supports only that the invasion's chest holds armor. Video frames 00744.jpg and 00738.jpg were not checked against this helm in this pass.", "source": "wiki 'Shrouded Gloam'; previous answer critiques"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source is evidenced. The Gloam Construct invasion chest (wiki 'Shrouded Gloam': 'a chest that gives dwarf/druid armor') is an unconfirmed lead; no source says the Raging Rampage set is in it. The previous answer's event entry is withdrawn.",
  "Check the Gloam invasion chest's contents against a reward table or a player report before listing it as a source. Check the video frames 00744.jpg and 00738.jpg for the helm on screen.",
  "The 51 definitions (ids 337, 2319-2323, 20237-20242 among them) suggest tints or race variants. No source says which variant is which sold or dropped form.",
  "Retirement and live status are unknown. No dated source exists for the Gloam invasion or for this set.",
  "The client description is empty and no price or currency is known."
 ]}
