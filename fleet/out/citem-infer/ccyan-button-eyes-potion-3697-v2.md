<!-- fleet job=citem-infer id=ccyan-button-eyes-potion-3697-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5475, 8196, 6, 2113] model=claude-haiku-5-5 -->
# Cyan Button Eyes Potion

{"item": {"name": "Cyan Button Eyes Potion", "locale_id": 3697, "kind": "consumable"},
 "sources": [
  {"type": "collection", "detail": "Final reward of the Robgoblin Junk collection family (Forks / Spoons / Knives / Plates / Pathfinder's Gloves / Okay, Cool, Better, Awesome Buttons stages), as listed on the wiki. The repo reward block grants 5 x item_definition_id 55412 (plus 5 x 55414, 1 x 3794, 4 coins). Which exact collection triggers it (Better Buttons alone or the whole family) is not confirmed.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8091-8106; wiki page 'List of Collections' (Robgoblin Junk row: Final Reward 'Button [Eyes] [Potion]')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Cyan Button Eyes Potion' is locale 3697, one of eight colour potions (Red 3693 to Magenta 3700) plus Firefly Swirls (3701) and Butterfly Swirls (3702) potions.", "source": "locale:3693-3702"},
  {"claim": "The collection reward block grants item_definition_id 55412 (x5), which is one of the two definitions (55412, 55413) the client files under this name. The id-to-colour mapping is not shown in the pack.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8099-8100"},
  {"claim": "The wiki 'List of Collections' Robgoblin Junk family ends in a Final Reward column containing 'Button [Eyes] [Potion]'.", "source": "wiki page 'List of Collections'"},
  {"claim": "Locale 3704 ('This potion gives humans button eyes!', named Red) and 3705 ('This potion gives pixies button eyes!', named Blue) are generic description strings shared across colour potions. They do not identify Cyan.", "source": "locale:3704; locale:3705"},
  {"claim": "No coin store price, coin vendor stock, Station Cash listing, or dedicated wiki article was found for this potion.", "source": "client definition in pack; repo stores.json not matched on 55412; lookup wiki/articles/client"}
 ],
 "confidence": 0.4,
 "open": [
  "Variant mapping unresolved: the reward grants 55412 but the client does not tie 55412 to the Cyan name. 55413 is unassigned. Treat the reward as 'one of the Button Eyes Potion variants'.",
  "Trigger unverified: whether the reward comes from the Better Buttons stage alone or from completing the whole Robgoblin Junk family is not confirmed. The wiki row layout was not clear enough to settle it.",
  "Items 55414 and 3794 in the same reward block are unidentified here and are not assumed to be this potion.",
  "The pack's 'marketplace' first-pass guess is not supported: no SC Marketplace, Coin Shop, or coin-vendor price was found, so none is listed.",
  "Swirls potions (3701, 3702) and the other colour potions may share this collection source; not checked.",
  "Retirement and current availability are unknown; no source states either. Live status is 'unsure'."
 ]}
