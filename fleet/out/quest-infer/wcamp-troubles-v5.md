<!-- fleet job=quest-infer id=wcamp-troubles-v5 status=no_submit turns=5 usd=0.0046 tokens(read,write,in,out)=[56470, 16363, 12, 3970] model=claude-haiku-5-5 -->
# Camp Troubles

{
 "quest": {"record_id": null, "title": "Camp Troubles", "title_locale_id": 429062},
 "live": "yes",
 "live_reason": "Title locale:429062 is an unflagged quest_title. Its offer line locale:429061 and the Camp Troubles-tagged dialog 429000, 429001, 429063 and objective 429064 are also unflagged. Nothing in the pack flags them not_live. No quest record exists, so the record id is unknown.",
 "zone": "Greenwood Forest (Camp Chatty)",
 "giver": {"name": "Chatty (offer speaker of locale:429061); wiki lists Counselor Edmond as giver", "npc_id": null, "locale_id": 429061},
 "line": {"name": "Camp Chatty / Bigfoot arc", "previous": [], "next": []},
 "objectives": [
  {"kind": "go", "text": "The foot prints lead to a copse of trees. That must be where Bigfoot hides out!", "text_locale_id": 429064, "target": "Bigfoot's Lair", "target_locale_id": 6756, "count": null},
  {"kind": "other", "text": "Help the camp counselors find Bigfoot's lair.", "text_locale_id": 429066, "target": "Bigfoot's Lair", "target_locale_id": 6756, "count": null},
  {"kind": "deliver", "text": "Return to Chatty", "text_locale_id": 429059, "target": "Chatty", "target_locale_id": null, "count": null}
 ],
 "dialog": {"offer": 429061, "progress": 429000, "complete": null},
 "rewards": [],
 "evidence": [
  {"claim": "Quest title 'Camp Troubles' is an unflagged quest_title", "source": "locale:429062"},
  {"claim": "Offer text: Chatty describes Bigfoot sightings and campers being scared off", "source": "locale:429061"},
  {"claim": "Description: Bigfoot scaring off campers; 'See if you can find its lair.'", "source": "locale:429063"},
  {"claim": "Footprint step leads to a copse of trees where Bigfoot hides", "source": "locale:429064"},
  {"claim": "'Help the camp counselors find Bigfoot's lair.' text exists; client hint is '-', so its quest membership rests on the repo note", "source": "locale:429066"},
  {"claim": "'I've been watching Bigfoot's movements.' is tagged quest_dialog | Camp Troubles", "source": "locale:429000"},
  {"claim": "'If we team up I think we can take him!' is tagged quest_dialog | Camp Troubles; not assigned to a slot", "source": "locale:429001"},
  {"claim": "'Return to Chatty' is tagged quest_objective | Camp Chatty | Camp Troubles in the client", "source": "locale:429059"},
  {"claim": "Bigfoot's Lair location name", "source": "locale:6756"},
  {"claim": "Camp Troubles given by Counselor Edmond per wiki; Edmond is a Camp Chatty counselor and main giver of the Bigfoot hunt", "source": "wiki:Counselor Edmond"},
  {"claim": "Repo NPC table lists Edmond's Camp Troubles and Chatty's Confronting Bigfoot turn-in", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md:39-40"}
 ],
 "confidence": 0.5,
 "open": [
  "Giver conflict: the offer speaker is Chatty (429061), but the wiki and repo NPC table name Counselor Edmond. The npc_id is unknown. The repo name hashes (4093915540, 72735948) are not locale ids, so I did not use them. Confirm the accept NPC from the NPC table.",
  "Repo ids 3182673722, 1503619310 and 3971714069 do not resolve as locale ids (3182673722 returns no such id). The repo's id claims are unreliable.",
  "Order of 429000 and 429001 is unknown. Both are Camp Troubles-tagged. I put 429000 as progress only as a guess. 429001 is left out of the slots. Complete dialog is null.",
  "429059 'Return to Chatty' is tagged Camp Troubles in the client, but the repo ties it to Confronting Bigfoot's turn-in. The client wins on tagging, so I kept it as a Camp Troubles objective. Whether it is the final turn-in or belongs to Confronting Bigfoot is unverified. Confronting Bigfoot's own record also lacks a prerequisite link.",
  "Previous: Meet and Greet (429055 'Did you already meet my camp counselors yet?') is only suggestive, so line.previous is empty. Next: Confronting Bigfoot is supported only by the wiki and repo tracker, with no prerequisite record. line.next is left empty until its record is checked.",
  "Rewards: none sourced for this quest. The Camp Chatty Hat is tied to Confronting Bigfoot in the repo.",
  "Record id and quest-id mapping are unknown; no quest record exists in the pack."
 ]
}
