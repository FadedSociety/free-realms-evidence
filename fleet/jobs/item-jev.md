You sort item names from the Free Realms game client (a 2009-2014 kids' MMO by Sony Online Entertainment) for a team
rebuilding the game. The client holds every item ever defined: real player items, but also NPC-only gear, test and
developer items, cut content and internal copies. Each line is
"key: name | description | slot and class | model file | number of definitions | coin store price".

For EVERY line, answer exactly one output line: key|live|kind|source|flag
- live: yes (a player could own it in the live game), no (never a player item), or unsure.
- kind: clothing, weapon, pet, mount, furniture, consumable, card, collection, quest_item, tool, badge, other.
- source: your best guess of how players got it: vendor, marketplace (Station Cash), coin_shop, quest_reward, drop,
  event, prize_wheel, crafting, collection, membership, promotion, npc_only (worn only by NPCs), unknown.
  Hints: a coin store price means vendor; "SC", bundle or members wording means marketplace or membership; holiday or
  event names mean event; recipe ingredients and crafted gear mean crafting; "Collection" items mean collection.
- flag: empty unless the item is probably NOT a live player item; then one code and a few words:
  not_live (marked old/unused/cut), placeholder (test, sample, TBD names), dev_note (debug or admin items),
  npc_only (NPC or enemy outfit, boss weapon), internal (system or template copy), duplicate (a copy of another item).

Answer only the lines, one per key, nothing else.
