<!-- fleet job=item-infer id=iazure-v3 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[5979, 8014, 6, 1985] model=claude-haiku-5-5 -->
# Azure

{"item": {"name": "Azure", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "no",
 "evidence": [
  {"claim": "Azure is a human male NPC boss and evil wizard in Briarwood's Briar Patch. The wiki page is a character/boss page, not an item page. Its categories are NPC, Enemies, Boss, Males, Human, Wizard, Briarwood, Trading Card Game, and it has no coin, Station Cash or IGD entries.", "source": "https://freerealms.fandom.com/wiki/Azure (rev 50192)"},
  {"claim": "Bare name 'Azure' is client text 6455, but the id check flags it as a single-word fragment. It is not used as live evidence and locale_id is left null.", "source": "locale:6455"},
  {"claim": "Boss description: 'Azure, the evil wizard is preparing to grant powerful abilities to the forest foes... stop him before an uprising unfolds!'", "source": "locale:7010"},
  {"claim": "Quest text: 'The evil wizard Azure performs sinister experiments in the Briar Patch. Put a stop to him!'", "source": "locale:74131"},
  {"claim": "Quest objective: 'Enter the Briar Patch and defeat the wizard Azure.'", "source": "locale:419112"},
  {"claim": "Quest objective: 'Defeat Azure.'", "source": "locale:7009"},
  {"claim": "Mutation text: 'Azure has mutated several creatures in Briar Patch.'", "source": "locale:130534"},
  {"claim": "Wiki page lists 'The Mushroom Gigas!' and 'Trading Card Game Series 2' as appearances. These are appearances of the NPC, not item sources.", "source": "https://freerealms.fandom.com/wiki/Azure (rev 50192)"},
  {"claim": "'Azure Painting' (locale 13940) is a separate Premium Painting housing item, not this NPC. Its client text (locale 13941) says Azure was featured in the Shattered Past Card Set, Shattered Past Premium Painting 9/153. This describes the painting record only and does not explain why the NPC page carries the TCG category.", "source": "locale:13940; locale:13941; wiki page 'Azure Painting'"}
 ],
 "confidence": 0.8,
 "open": [
  "The request names an item 'Azure', but the subject is the Azure NPC boss, which is not sellable, droppable, or craftable. No item sources are listed for the NPC.",
  "If the intended item is 'Azure Painting' (locale 13940), it needs its own pack. The wiki says it was sold on the Station Cash Marketplace the week of November 25, 2013, but the price is garbled ('regular price of , and to members at the 10..'), so the price and retirement status are unverified.",
  "Briar Patch and The Mushroom Gigas! reward figures (182 stars, 77 stars, Archer Prize Wheel) from the prior answer were not verified and are omitted. They are boss-encounter rewards, not item sources.",
  "Critique fixes applied: 6455 is no longer cited as live evidence; 419123 was dropped (correct quote is 419112); the TCG link is attributed to the painting record (13941) and to the wiki's 'Trading Card Game Series 2' appearance line, not to an Azure card."
 ]}
