You tag lines of text from the Free Realms game client (a 2009-2014 kids' MMO by Sony Online Entertainment) so a team
rebuilding the game can find every quest's text. Each line is "id: text". Lines with nearby ids were usually written
together: one quest's title, objectives and dialog sit next to each other.

For EVERY line, answer exactly one output line: id|type|zone|hint|flag
- type, one of:
  - quest_title: a quest's name.
  - quest_objective: a task, such as collect, defeat, talk to, go to or deliver.
  - quest_dialog: what an NPC says while giving, updating or finishing a quest.
  - quest_reward
  - npc_name
  - npc_dialog: NPC talk not tied to a quest.
  - item
  - place
  - ability
  - ui: menus, buttons, errors and system messages.
  - other
- zone: the in-game area the line belongs to, if the text or its neighbours say so (for example Seaside, Snowhill,
  Briarwood, Sanctuary, Lakeshore, Shady Shores, Blackspore, Sunstone Valley, Pixie Woods). Otherwise -.
- hint: for quest lines, the quest title it belongs to, if the neighbours tell you. Otherwise the main NPC, item or
  place it names. Otherwise -.
- flag: "-" when the line looks like real shipped content. Otherwise a short reason this line is probably NOT live
  quest content, so a human can check it:
  - not_live: marked NOT LIVE, cut, unused or old;
  - placeholder: sample, test or TBD text;
  - dev_note: an internal note;
  - joke: nonsense or a gag line that cannot be a quest, like "ooga booga";
  - duplicate: same as a neighbour;
  - fragment: a single word or reply option with no quest meaning on its own.
  Add a few words after the code if useful, for example: not_live: title starts NOT LIVE.

Give no other text, and keep the ids exactly.

When you are finished, call `submit` with status "done" and the output lines as the result.
