<!-- fleet job=citem-infer id=cwizard-s-necklace-of-energy-font-131272-v1 status=done turns=8 usd=0.0056 tokens(read,write,in,out)=[94445, 20297, 18, 4217] model=claude-haiku-5-5 -->
# Wizard's Necklace of Energy Font

{"item": {"name": "Wizard's Necklace of Energy Font", "locale_id": 131272, "kind": "clothing"},
 "sources": [{"type": "prize_wheel", "detail": "Wizard Prize Wheel reward from the battle Bergram Stumpfinger's Ghost (defeat Bergram Stumpfinger; reward listed as 26 Coins on the page)", "where": "Blackspore Swamp (battle started at the tombstone just north of Mire's Edge; difficulty 5, levels 13+)", "price": "26 Coins (battle reward line; no sale price stated)", "currency": "coins", "source": "wiki page \"Bergram Stumpfinger's Ghost\" (wikitext, section 'Wizard Prize Wheel'), refs: freerealms-wiki/wikitext/4616-49163-5bd5c18287f0.wiki lines 74-81"}],
 "retired": null,
 "live": "unsure",
 "evidence": [{"claim": "Client item name exists as locale 131272, type item, one definition (id 75528), neck slot (8) and class 8, with no coin store price in repo stores data.", "source": "locale:131272; client definition in pack"},
  {"claim": "Bergram Stumpfinger's Ghost lists 'Wizard's Necklace of Energy Font' under the Wizard Prize Wheel, alongside Wizard's Necklace of Bark Skin V and Wizard's Power Shard of Vitality V, with 26 Coins.", "source": "wiki page Bergram Stumpfinger's Ghost (freerealms-wiki/wikitext/4616-49163-5bd5c18287f0.wiki lines 74-81)"},
  {"claim": "The same battle lists the Archer, Brawler, Medic, Ninja and Warrior versions of the Necklace of Energy Font on their own class prize wheels, so this is one of a six-class set.", "source": "wiki page Bergram Stumpfinger's Ghost lines 29-72; repo quest-lines/enemies.json entries for each class (the 'Wizard' entry at line 2053)"},
  {"claim": "Other Wizard prize-wheel battles checked on the wiki (Moldy Shamblers, Frostfang Snarlers, Chugawump, Feisty Floren, Return to Sender!, Robgoblin Creek!) do not list this necklace.", "source": "lookup wiki results for '[Wizard] [Prize] [Wheel]' pages"}],
 "confidence": 0.6,
 "open": ["No wiki article for the item itself and no retirement or removal date found, so retired is null and live is 'unsure' (the client defines it, but the wiki gives no current availability).",
  "The 26 Coins figure is the battle's listed coin amount; it is not confirmed as a price of the item or as a wheel cost, so no item price is recorded.",
  "The other answer's claim (prize wheel, Wizard) is confirmed by the wiki page; that answer cited the wiki, not the page. Its locale_id was null and is set to 131272 here.",
  "No vendor stock, coin store price, collection, crafting, or quest reward evidence was found in the pack or repo.",
  "No description text (empty in client) and no images or video for this item.",
  "Wiki page does not say whether the Wizard wheel entry is still live; the page's revision date is 2025 (revid 49163 range), so the entry was present at least in that revision."]}
