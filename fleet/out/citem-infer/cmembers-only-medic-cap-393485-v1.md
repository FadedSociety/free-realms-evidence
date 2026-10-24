<!-- fleet job=citem-infer id=cmembers-only-medic-cap-393485-v1 status=nothing_found turns=4 usd=0.0032 tokens(read,write,in,out)=[25923, 13252, 10, 2523] model=claude-haiku-5-5 -->
# Members Only Medic Cap

{"item": {"name": "Members Only Medic Cap", "locale_id": 393485, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item: name locale:393485 'Members Only Medic Cap', definition 70322, slot 1 (head), class 7, model military_<race>_<gender>_head_baseball.adr, no coin store price.", "source": "locale:393485; client definition in the evidence pack"},
  {"claim": "The item sits in a nine-item client set of 'Members Only' job-gear pieces (Blacksmith Goggles 393480, Brawler Pauldrons 393481, Demo Derby Driver Helmet 393482, Kart Driver Helmet 393483, Fisherman Pants 393484, Ninja Cowl 393486, Warrior Pauldrons 393488, Wizard Cloak 393489). The name prefix matches the 'Members Only' job-membership framing.", "source": "locale:393480-393489 (client cluster in the evidence pack)"},
  {"claim": "The wiki puts the Medic job in the Members Only category, so a members-only Medic cap is consistent with membership gating.", "source": "wiki page 'Medic' (Category:[Members] [Only]); notes/Build Guides/Content/Jobs/Medic.md:34"},
  {"claim": "The wiki's monthly member packs (e.g. November 2009 Trendy Sunglasses / Sport Shades / Felt Beret, December SBS-1000) show that membership-gated clothing was handed out in Monthly [Member] Packs, but no page links this cap to one.", "source": "wiki pages 'Trendy Sunglasses', 'Sport Shades', 'Felt Beret', 'SBS-1000'"},
  {"claim": "The Members Only Demo Derby Driver Helmet is listed as a members-only single helmet with no named source.", "source": "notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:191 [client]"}
 ],
 "confidence": 0.2,
 "open": [
  "No wiki page, article, video frame, vendor stock, quest reward or drop names Members Only Medic Cap. Its acquisition channel is unconfirmed; 'membership' is only the first-pass guess.",
  "The sibling items have no sourced acquisition either, so the set's channel (monthly member pack, job membership bonus, or a promotion) cannot be inferred from them.",
  "Whether it was a monthly member pack item (and which month) is unknown. The Trendy Sunglasses, Sport Shades and Felt Beret pages show that member packs gave clothing, but none names this cap.",
  "No coin store price in stores.json, so it is not a coin vendor sale.",
  "Live status and retirement are unknown. The jev first pass says live, but that is a hint, not evidence.",
  "Next checks: search the wiki for 'Members Only' job-gear sets and the Monthly Member Pack item lists for each month; check the Medic job's Members Only rewards; check the Medic Membership Upgrade Bundle (client 249744385) contents."
 ]}
