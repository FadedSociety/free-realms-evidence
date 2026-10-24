<!-- fleet job=quest-infer id=wthe-eggcitingly-eggcellent-egg-hunt-v3 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[33521, 12949, 10, 3207] model=claude-haiku-5-5 -->
# The Eggcitingly Eggcellent Egg Hunt

{"quest": {"record_id": null, "title": "The Eggcitingly Eggcellent Egg Hunt", "title_locale_id": 5100014},
"live": "yes",
"live_reason": "Title locale:5100014 is an unflagged quest_title. Wiki Bunny Goggles page says this quest was introduced March 30th, 2013 and its prize claimed during Spring Eggstravaganza 2013. Event-limited (Spring Eggstravaganza only), not a permanent quest.",
"zone": "Sanctuary (giver in Pixiewood Hills); stolen egg hunted in Sacred Grove (location conflict, see open)",
"giver": {"name": "Alyssa Eggelyn", "npc_id": null, "locale_id": 5100004},
"line": {"name": "Spring Eggstravaganza daily quest series (4 quests)", "previous": ["The Eggcellent Egg Hunt"], "next": ["The Eggxtremely Eggcitingly Eggcellent Egg Hunt"]},
"objectives": [
 {"kind": "go", "text": "Find Alyssa Eggelyn's stolen egg (wiki Goals/Steps; client has the same wording at locale:5100142, 5100144, 5100149 but these are not verified as this quest's objective)", "text_locale_id": 5100142, "target": "Alyssa Eggelyn's stolen egg", "target_locale_id": null, "count": 1},
 {"kind": "talk", "text": "Return to Alyssa Eggelyn in Pixiewood Hills with the egg", "text_locale_id": null, "target": "Alyssa Eggelyn", "target_locale_id": 5100004, "count": null}
],
"dialog": {"offer": 5100092, "progress": null, "complete": 5100091},
"rewards": [
 {"kind": "other", "value": "Special egg from Alyssa, not to be opened until Spring Eggstravaganza (opens March 31st)", "source": "wiki:Quest:The Eggcitingly Eggcellent Egg Hunt (Steps); locale:5100091 (matching completion text)"},
 {"kind": "item", "value": "Bunny Goggles (head slot clothing, freestyle jobs), claimed from the quest completion prize during Spring Eggstravaganza 2013", "source": "wiki:Bunny Goggles"}
],
"evidence": [
 {"claim": "Quest title is an unflagged quest_title", "source": "locale:5100014"},
 {"claim": "Giver NPC name Alyssa Eggelyn", "source": "locale:5100004"},
 {"claim": "Offer dialog 'A third egg has gone missing...' matches the wiki Steps quote", "source": "locale:5100092; wiki:Quest:The Eggcitingly Eggcellent Egg Hunt (Steps)"},
 {"claim": "Completion dialog 'I can't believe it! You are eggstremely good...' matches the wiki Steps quote and the special-egg reward", "source": "locale:5100091; wiki:Quest:The Eggcitingly Eggcellent Egg Hunt (Steps)"},
 {"claim": "Stolen-egg objective wording exists in client", "source": "locale:5100142"},
 {"claim": "Series order: Eggcellent, then Eggcitingly Eggcellent (this), then Eggxtremely Eggcitingly Eggcellent; this quest's Requirements name the Eggcellent quest", "source": "wiki:Quest:The Eggcitingly Eggcellent Egg Hunt (Requirements); wiki:Quest:The Eggxtremely Eggcitingly Eggcellent Egg Hunt (Requirements)"},
 {"claim": "Next quest title variant exists in client as flagged alternate title", "source": "locale:5100013"},
 {"claim": "Bunny Goggles acquired via this quest's completion prize in Spring Eggstravaganza 2013", "source": "wiki:Bunny Goggles"},
 {"claim": "Event-only; giver in Pixiewood Hills, Sanctuary", "source": "wiki:Quest:The Eggcitingly Eggcellent Egg Hunt (To Start, Notes)"},
 {"claim": "Locale 5100093 is a completion line ('Now I can enjoy the Spring Eggstravaganza...') that does not match this quest's wiki Steps; not assigned here", "source": "locale:5100093"},
 {"claim": "Locale 5100006-5100008 and 5100015 are tagged to the Eggcellent quest's hint, not this one; not used as this quest's text", "source": "locale:5100006; locale:5100008; locale:5100015"}
],
"confidence": 0.6,
"open": [
 "No record exists; a new record id must be assigned.",
 "Hidden-egg location conflicts: wiki Goals say Sacred Grove, wiki Steps say a hill near a house by Floren Forest. Not resolved; the go-objective spawn point is unknown.",
 "Objective text 5100142 is a client string with the same wording as the wiki Goals, but its quest hint was not confirmed; treat as probable, not verified.",
 "Progress dialog not found in client; locale:5100086-5100089 (stolen-egg and 'Hooray you found it' lines) are unassigned and could be this quest's progress/completion text; hints not verified.",
 "Client 5100093 'Eggcellent work...' is not this quest's Steps text and is excluded; it may belong to a later quest in the series.",
 "Bunny Goggles is sourced only to the wiki Bunny Goggles page; no client reward link was found (locale:5100099 'Bunny Goggles' exists but is unlinked).",
 "Next-quest link is wiki-sourced; that quest's record does not exist in our data yet.",
 "NPC 672706230 is a name_string_id from repo notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:133 (per prior critique), not a verified NPC record id; left null here.",
 "Exact 2013 date is from the wiki only."
]}
