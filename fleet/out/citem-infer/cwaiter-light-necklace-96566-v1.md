<!-- fleet job=citem-infer id=cwaiter-light-necklace-96566-v1 status=nothing_found turns=5 usd=0.0035 tokens(read,write,in,out)=[30831, 14670, 12, 2751] model=claude-haiku-5-5 -->
# Waiter Light Necklace

{"item": {"name": "Waiter Light Necklace", "locale_id": 96566, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Waiter Light Necklace', locale 96566, definition_id 31160, slot 9, class 64, no coin store price, no models, empty description.", "source": "locale:96566; pack client_definition"},
  {"claim": "The 'Waiter' jewelry is a 12-piece family: Rings 96442/96445/96446/96454/96455/96456 and Necklaces 96562/96565/96566/96574/96575/96576 (Fire, Sun, Light, Air, Wind, Void). Their names are the only text the client carries for them.", "source": "locale:96442, 96445, 96446, 96454, 96455, 96456, 96562, 96565, 96566, 96574, 96575, 96576"},
  {"claim": "Repo flags tag the Waiter Fire/Sun/Light/Air/Wind/Void rings and the Waiter Fire/Sun necklaces as jokes: '\"Waiter\" is not a normal ring quality' and '\"Waiter\" tier name, likely gag/test jewelry'. This is an unverified tag by a reviewer, not a source.", "source": "refs:quest-lines/flags.json (ids 96442-96456, 96562, 96565 entries, flag field)"},
  {"claim": "No wiki page, article, video frame, quest reward, vendor stock, drop, event or store price names this item. Lookups in client text, wiki, articles and video returned only the locale names.", "source": "lookup queries 'Waiter Necklace' and 'Waiter Ring OR Waiter jewelry' (no wiki/article/video hits); search of repo and refs for 'Waiter' (only ClientItemDefinitions comments and locale dumps)"},
  {"claim": "The first-pass tag (live yes, quest_reward) is unsupported: no quest, vendor or drop in the evidence pack names this item, and the repo flags describe the set as gag/test jewelry.", "source": "jev_first_pass in pack; refs:quest-lines/flags.json"}
 ],
 "confidence": 0.2,
 "open": [
  "No real source found. Sources could not be assigned without evidence, so none are listed.",
  "Existence in the client is not proof of obtainability. The 'Waiter' set may be a gag or test item that was never sold or dropped. Whether it was ever live needs a wiki or forum mention, a player screenshot, or a server/store table entry.",
  "The jev first-pass 'live: yes' and 'quest_reward' guess conflicts with the repo joke/gag flags. Left unresolved.",
  "The Toaster-named necklace (locale 96577) sits in the same cluster in one citem pack; its source is not checked here.",
  "Definition id 31160 has no hits in repo stores or quests. A quest or vendor table keyed on that id, or on the locale ids, would settle it."
 ]}
