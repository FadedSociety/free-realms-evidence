<!-- fleet job=citem-infer id=csurgeon-dreadful-ring-86413-v1 status=nothing_found turns=4 usd=0.0025 tokens(read,write,in,out)=[17626, 9949, 10, 2234] model=claude-haiku-5-5 -->
# Surgeon Dreadful Ring

{"item": {"name": "Surgeon Dreadful Ring", "locale_id": 86413, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:86413 'Surgeon Dreadful Ring'; definition 22422, slot 8, class 43, no coin store price (stores.json has no row for it)", "source": "client definition in evidence pack"},
  {"claim": "Part of an 11-item ring family: Surgeon Dreadful/Fateful/Infernal/Spectral/Mystical/Phantasmal/Eternal/Celestial/Ethereal Ring (locale 86413-86421), with a parallel Ruffian set (86404-86412) and Ruffian Necklace set (86639-86647)", "source": "locale:86404-86421, locale:86639-86647"},
  {"claim": "The same 'Dreadful/Fateful' tier-prefix pattern also appears on other job-named rings (Physician, Sage, Champion, Rascal, Grunt, Stalker, Vagabond, Nomad, Hero, Granite, etc.), which suggests a job/class-tier ring family, but no source states how any member is obtained", "source": "locale strings in opening-journal-text-v2/locale/en_us_data.dat (lines 2999, 17606, 10143 etc.)"},
  {"claim": "A video frame shows 'Granite [Fateful] [Ring]' as a reward from the Cook-off Catastrophe quest (Medic job level, Green misty grove). This is a different ring name, so it is not evidence for Surgeon Dreadful Ring itself, but it shows the Fateful tier rings come from quest rewards", "source": "video:506rO_mhaSs/00248.jpg, video:506rO_mhaSs/00250.jpg"},
  {"claim": "No wiki page, article, vendor stock, or other answer names Surgeon Dreadful Ring", "source": "lookup over client, wiki, articles, video; repo and refs search returned only locale/data-dump hits"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Sources must be confirmed from the job/quest/crafting data for the Surgeon (Medic-line) ring family before filling the sources list.",
  "The description is empty and no models are listed, so the item's appearance and class restriction are unverified.",
  "Live status is unsure: the client defines it, but no store, wiki, or video evidence shows it sold or dropped.",
  "The Granite [Fateful] [Ring] quest reward (Cook-off Catastrophe) is a different item and was not counted as a source for this ring. Check whether Surgeon tier rings are issued by the same quest or by a Medic-job reward table.",
  "The Ruffian and Surgeon ring families share one naming scheme. Check the Ruffian ring sources, if any are found, against this item."
 ]}
