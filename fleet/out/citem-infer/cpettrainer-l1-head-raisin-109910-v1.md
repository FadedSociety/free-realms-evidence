<!-- fleet job=citem-infer id=cpettrainer-l1-head-raisin-109910-v1 status=nothing_found turns=6 usd=0.0050 tokens(read,write,in,out)=[57327, 24442, 14, 2792] model=claude-haiku-5-5 -->
# pettrainer_L1_head_raisin

{"item": {"name": "pettrainer_L1_head_raisin", "locale_id": 109910, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 34101 (name locale 109910, slot 1 head, class 1, model freestyle_<race>_<gender>_head_baseballcap.adr). No coin store price in the client definition.", "source": "locale:109910; pack client_definition"},
  {"claim": "It is one tint of the Pet Trainer / Animal Handler L1 head-cap set (about 30+ color names, e.g. raincloud 109909, olive 109906, plum 109907, spruce 109915), which is the Pet Trainer job's level-1 outfit family.", "source": "locale:109905-109915 (client_cluster); quest-lines/citem-packs.json entries for pettrainer_L1_head_* (same cluster, no sources recorded)"},
  {"claim": "The Pet Trainer job exists and was used to raise pets; the job was later simplified into trophies.", "source": "articles/facts.json (Pet Trainer, statement about trophies); articles article 574 summary"},
  {"claim": "No wiki page, image, video frame, vendor stock list, quest reward, drop, or event text names this item or the L1 head set in any source searched (lookup client/wiki/articles/video; repo data; refs).", "source": "lookup and search results, this run"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The set is most likely earned through Pet Trainer job progression (a level-1 outfit), but no quest, vendor, or reward record in the repo or refs names pettrainer_L1_head_raisin or any pettrainer_L1_head_* / Animal Handler head item, so no source is asserted.",
  "Check the Pet Trainer job's trainer (Roscoe / Kirill Moonrunner per wiki NPC list) and the job's clothing shop for the L1 head set; neither was verified against this item.",
  "Check whether Animal Handler/Pet Trainer heads were sold in the Coin Shop or Marketplace; no coin_store_prices entry exists for definition 34101.",
  "Retired status unknown; the Pet Trainer job was simplified (trophy system), so the L1 set may be retired, but no source states the date or that this tint was removed.",
  "Jev first-pass tag said vendor; it is a hint only and is not supported by any cited evidence.",
  "The 'raisin' tint name has no wiki or video evidence of appearance."
 ]}
