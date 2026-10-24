<!-- fleet job=citem-infer id=csmall-striped-snail-40906-v1 status=done turns=8 usd=0.0047 tokens(read,write,in,out)=[90480, 19110, 18, 2731] model=claude-haiku-5-5 -->
# Small Striped Snail

{"item": {"name": "Small Striped Snail", "locale_id": 40906, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines 'Small Striped Snail' (locale 40906) with description 'This item can be added to the Striped Snails Collection' (locale 122159565 / ui locale 132347); definition_id 3690, one definition, no coin store price.", "source": "locale:40906; repo:quest-lines/citem-packs.json (cluster entry for locale:40906, definition_ids [3690] in the Angry Striped Snail pack's neighbours)"},
  {"claim": "The Striped Snails collection exists and is listed on the wiki's List of Collections as '[Striped] [Snails]', alongside Solid [Snails], Spotted [Snails] and Checkered snails.", "source": "wiki: List of Collections (page:ns0)"},
  {"claim": "Client text for the sibling collection items (Small/Large/Smart/Angry/Slimy/Smelly/King/Queen Striped Snail, locales 40906-40913) shares the same collection description line, so this is a collection-member item, not a vendor or coin-store item.", "source": "locale:40907-40913; locale:132347"},
  {"claim": "The client has no coin store price for this item (coin_store_prices empty), so there is no coin vendor sale evidence.", "source": "client definition in the evidence pack; repo:data/content/stores.json has no matching entry for item 3690 in the pack"},
  {"claim": "The cheap first-pass tag (live yes, kind collection, source_guess drop) is a hint only; no drop, quest or event evidence was found for this snail.", "source": "jev_first_pass in the evidence pack"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source found. No vendor stocks it, no wiki article names it, no article/video/quest/enemy-drop answer mentions it. The first-pass 'drop' guess is unsupported; do not treat it as a source.",
  "How the Striped Snail collection members are obtained (enemy drop from snail-type mobs, collection-turn-in, or a crafting/event path) is unknown. Check the wiki page for the Striped Snails collection (linked from List of Collections) and the snail mobs' drop tables before adding a source.",
  "Sibling item Angry Striped Snail (locale 40909, definition 3693) is tagged kind 'card' by the cheap model in the same pack; kind here is set to 'collection' from the client description, but the conflict should be checked.",
  "Retirement status unknown: no source states whether the snail collection was retired."
 ]}
