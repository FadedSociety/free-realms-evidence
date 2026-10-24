<!-- fleet job=citem-infer id=cjolter-s-necklace-407940-v1 status=nothing_found turns=7 usd=0.0073 tokens(read,write,in,out)=[114034, 33778, 16, 3799] model=claude-haiku-5-5 -->
# Jolter's Necklace

{"item": {"name": "Jolter's Necklace", "locale_id": 407940, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is Jolter's Necklace, locale 407940; description 'This necklace increases your kick power.'; definition 67931; slot 8; class 136; no model files; no coin store price.", "source": "locale:407940; repo:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json (Comment 'Jolter's Necklace', ~line 1155919)"},
  {"claim": "Jolter's family is a soccer kick-power jewelry tier set. Its siblings are Jolter's Ring (407943), Jolter's Triangle Power Shard (407934) and Elite Pink Jolter's Square Shard (407937), next to Charger's and Champion's variants (407935-407942, 407944-407945).", "source": "locale:407934-407945 (client_cluster in the pack; lookup client results)"},
  {"claim": "The soccer jewelry in the repo notes is grouped as Amateur, Pro and All-Star tiers, and the kick-power necklace/ring/square-shard text sits in the 'in soccer' and generic variants. Jolter's text is the generic 'increases your kick power' wording (locale 407952/407955/407949 style), so it may be a generic copy shared with other jobs, not a soccer-only item.", "source": "repo:notes/Build Guides/Content/Jobs/Soccer Star.md:257-261 (Jewelry and shards section)"},
  {"claim": "Name-based search across the wiki, articles, video and the repo notes finds no page, article, video frame, vendor, quest, drop or event naming Jolter's Necklace or its Charger/Champion siblings. The only repo hits are the locale dumps and the Lxzxrus definition file.", "source": "lookup (client/wiki/articles/video) and search (repo, refs) for 'Jolter', 'Charger's', 'Champion's Necklace', '407940', '67931'"},
  {"claim": "The first-pass tag (live yes, kind clothing, source marketplace) is a cheap-model hint only; no evidence in the pack or the searches confirms the marketplace source.", "source": "jev_first_pass in the pack"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. The item has no wiki page, no vendor stock, no coin store price, no quest, drop, event or crafting reference in any searched source, so no source is listed.",
  "Jev's 'marketplace' guess has no support. Do not list the SC Marketplace unless a wiki page or store record confirms it.",
  "Still to check: whether the Charger's and Champion's siblings (407941/407942/407944/407945) have a wiki page or source; a sibling source would likely apply to Jolter's too. Also check the Lxzxrus server and the TCG/Legacy refs for a reward table keyed on the 4079xx locale range.",
  "Confirm whether the family is a soccer set (Soccer Star questline rewards) or a generic kick-power set. The repo notes leave the Soccer tier-to-stat mapping undecoded.",
  "Kind: the schema has no jewelry value; the item is an equip-slot 8 necklace, so 'clothing' is a placeholder choice.",
  "Live status is unsure: the client defines the item, but no store or source record shows it is currently obtainable or retired."
 ]}
