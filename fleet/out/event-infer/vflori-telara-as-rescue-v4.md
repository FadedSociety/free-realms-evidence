<!-- fleet job=event-infer id=vflori-telara-as-rescue-v4 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[15602, 10618, 8, 3581] model=claude-haiku-5-5 -->
# Flori Telarañas rescue

{
 "event": {
  "name": "Grexan's Camp spider rescue (Buttercup Webbywand / Flori Telarañas storyline)",
  "aliases": ["Flori Telarañas rescue", "Buttercup Webbywand spider rescue (Spanish articles name the NPC Flori Telarañas)", "Eight-Legged Friend (client quest title, from earlier pass; not re-checked here)"]
 },
 "kind": "other",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Briarwood (quest zone; wiki Category:Briarwood on Buttercup Webbywand; article 924 route starts at the Briarwood warpstone)", "Grexan's Camp (location where the spider is held; locale:162 'Grexan's Camp')", "Thorny Forest (teleport-stone route only, article 927)"],
 "npcs": ["Buttercup Webbywand (wiki ns0 page; locale:20282 'Buttercup')", "Flori Telarañas (articles 927 and 928 only; Spanish; likely the same character under another name, unconfirmed)"],
 "quests": ["Eight-Legged Friend (locale:390870, taken from the earlier pass; this pass's locale lookup by ID failed, so re-verify)"],
 "activities": ["Teleport to the Briarwood teleport stone or warpstone and climb the hill to the tunnel (article 924 and 928)", "Find the NPC just outside the tunnel (articles 924, 927, 928)", "Explore Grexan's Camp and rescue the captured pet spider (locale:116034 'Free the spider held captive in Grexan's Camp.'; locale:390663 'Save Buttercup Webbywand's spider from Grexan's Camp.')", "Avoid being wrapped in a cocoon (article 928, Spanish quote 'te podrías ver envuelto en una crisálida si es que te descuidas')"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 924 (Buttercup Webbywand) gives the quest: teleport to the Briarwood warpstone, head up the hill to a large tunnel, find Buttercup, explore Grexan's Camp and rescue the spider.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=924"},
  {"claim": "Article 928 (Spanish) gives the same route with Flori Telarañas: Briarwood teleport stone, climb the hill, find Flori outside the tunnel, rescue the pet spider, beware the cocoon.", "source": "http://www.freerealms.com/article/detail.action?articleId=928"},
  {"claim": "Article 927 (Spanish) gives a Thorny Forest teleport-stone route to the same camp and the same Flori rescue.", "source": "http://www.freerealms.com/article/detail.action?articleId=927"},
  {"claim": "Article 98 names Buttercup Webbywand with the task 'Rescue the spider kidnapped by trolls' at Grexan's Camp.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=98"},
  {"claim": "Buttercup Webbywand is a wizard pixie NPC in Briarwood whose pet spider is captured when she explores Grexan's Camp.", "source": "wiki page 'Buttercup Webbywand' (ns0; Category:NPC, Pixie, Wizard, Briarwood)"},
  {"claim": "Client text ties the rescue to Buttercup's spider.", "source": "locale:390663 'Save Buttercup Webbywand's spider from Grexan's Camp.'"},
  {"claim": "Client text ties the rescue to a captive spider in Grexan's Camp.", "source": "locale:116034 'Free the spider held captive in Grexan's Camp.'"},
  {"claim": "Articles 924 (Buttercup), 927 and 928 (Flori) describe the same story: same camp, same Briarwood/Thorny Forest route, same hill-and-tunnel approach, same captured pet spider. This points to one storyline under two NPC names (likely a Spanish-localized or re-titled copy), but no dated source names both.", "source": "articles 924, 927, 928"},
  {"claim": "Flori Telarañas is a mage whose pet spider is captured by a troll at Grexan's Camp, and she asks players to rescue it.", "source": "http://www.freerealms.com/article/detail.action?articleId=928 (fact:npc)"}
 ],
 "confidence": 0.35,
 "open": [
  "Dates: articles 924, 927, 928 and 98 carry no year or month in the pack or this lookup, so occurrences is empty and the live window is unknown.",
  "live = unsure: article 928 is titled 'Free Realms - What is New?', which hints at a live announcement, but there is no date. Locale 390727 ('not_live? no; see note') is unresolved and could indicate a pre-launch preview. Treat as unscheduled.",
  "Alias/identity: Flori Telarañas and Buttercup Webbywand share the same story and route. The merge is likely but not confirmed; no dated source names both. Keep them as aliases only after a dated source links them. Flori appears only in Spanish articles 927 and 928.",
  "Quest title 'Eight-Legged Friend' (locale:390870) and its objective/dialog IDs came from the earlier pass; the ID lookup failed in this pass, so re-verify before wiring.",
  "'Train A Spider' (locale:390662) is dropped from quests: its only link is the rescue objective (locale:390663), and its sub-objectives point to the General Grexan spider-training battle (locale:5667 'Defeat General Grexan before the trolls become unstoppable!' and locale:18948 'Defeat General Grexan.'). That battle is a separate content line and is not counted here.",
  "Items: locale:390551 (item named 'Buttercup Webbywand') is not tied to this event by any source, so it is excluded. Spider Sprayer and Spider-Etched Gravestone are unrelated.",
  "Rewards: no source found for any reward.",
  "recurring stays null. 'Each time she explores' is in-story flavour, not a schedule; only one undated storyline is known.",
  "Zones: Briarwood and Grexan's Camp are supported by the wiki category and article 924; Thorny Forest is only the teleport route in article 927. Whether Grexan's Camp is its own zone is not established.",
  "wiki_category_members and quest_answers_mentioning_it were empty in the pack. Do not wire this into the calendar until a dated source is found."
 ]
}
