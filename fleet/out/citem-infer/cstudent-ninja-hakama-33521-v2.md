<!-- fleet job=citem-infer id=cstudent-ninja-hakama-33521-v2 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[17623, 12538, 8, 2081] model=claude-haiku-5-5 -->
# Student Ninja Hakama

{"item": {"name": "Student Ninja Hakama", "locale_id": 33521, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Ninja job starter kit (rank-1 creation/DefaultItems grant), Legacy/Sanctuary Profiles.json selection; not confirmed against retail. Not a sale, quest, drop or event in any source found.", "where": "Ninja job (profile 2), starting kit", "price": null, "currency": null, "source": "notes/Research/Pieces/034 Ninja progression.md:45-47 (DefaultItems includes 19787); notes/Research/Job Starter Outfits.md:69 (19787@355614, Ninja 2, R; the list is a Legacy-sourced selection, see its line 42 and 154 'not proved' caveat); locale:33521"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Student Ninja Hakama' is locale 33521 (re-verified: locale query returns '33521: Student Ninja Hakama').", "source": "locale:33521"},
  {"claim": "Definition 19787 exists in the client item definitions (Id line 193) and is referenced by the inventory packet sample (Definition 19787).", "source": "refs: OpenSourceFreeRealms/ofrserver/Customize/ClientItemDefinitions.json:193; PacketSendSelfToClient.json:49500"},
  {"claim": "19787 is one of six Ninja rank-1 starter definitions in the proposed Ninja DefaultItems list, all Legacy-selected (policy marked R, not retail-proved).", "source": "notes/Research/Job Starter Outfits.md:69; notes/Research/Pieces/034 Ninja progression.md:45-47"},
  {"claim": "Client text lists the name alongside other Ninja Hakama variants (Nokizaru, Shinobi, Chunin, Jonin, Sensei, Nusumi, Kanja, Soke), i.e. a ninja rank-tier clothing family; no sale line attached to the Student tier in the client text.", "source": "refs: FreeRealmsLocaleTools/test/.../en_us_data.dat:43880 (Student Ninja Hakama) and neighbouring Ninja Hakama entries"},
  {"claim": "Video frame lists 'Student Ninja Hakama' among item names with other Student job pieces; shows client presence only, not obtainability.", "source": "video:98uNKkDRvQU/00266.jpg"},
  {"claim": "No wiki page, article, coin store price (coin_store_prices empty) or vendor stock row names this item. The first-pass 'vendor' guess is unsupported and the first-pass 'live: yes' is not confirmed.", "source": "client definition pack; lookup wiki/articles/client for \"Student Ninja Hakama\" returned only locale:33521"}
 ],
 "confidence": 0.5,
 "open": [
  "Only source is the starter-kit DefaultItems grant from Legacy/Sanctuary data. The notes say no native retail default-outfit table was proved, so the grant is unverified against retail. 'Not sold' is not evidenced and has been dropped.",
  "Wireable: false. A starter grant has no price, quest, enemy or event, so this item cannot be wired as acquirable from current evidence.",
  "Whether the kit is granted at character creation only or re-granted on Ninja job unlock is not established.",
  "Retired status and later availability (Ninja job sales, Student set vendor, promotions) not found in wiki, articles or client text; retired is unknown.",
  "Variant count: the model is a single legs ADR with <race>/<gender> placeholders; only one definition (19787) is confirmed.",
  "Removed the stray 'repo:data/content/... none' reference from the earlier answer; it pointed at no file."
 ]}
