<!-- fleet job=citem-infer id=cwand-essence-of-wind-67481-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6042, 9063, 6, 2099] model=claude-haiku-5-5 -->
# Wand Essence of Wind

{"item": {"name": "Wand Essence of Wind", "locale_id": 67481, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Collection entry granted for completing the Wizard Wand Materials collection (cascade: Dragons Breath, Floren Moustache Leaf, Yeti Hair, Robgoblin Booger, Metal Rod, Crystal Gems, Pixie Dust, Carved Wood). The essence is one of four entries of the Wizard Magical Wand Essences collection (locale 67599); completing that collection unlocks the Magical Essence Ornate Wand (wiki, not re-verified).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 17568-17582 (reward item 23868 x1, coins 7, collection_add 233); repo:prototype/osfr-tools/data/content/collection_catalogue.json line 17608; repo:prototype/osfr-tools/data/content/collections.json lines 4846-4851, 5040-5041; wiki page:Job Specific (Collections) ('[Wand] Essence of Wind -- This is the reward for completing [Wizard] [Wand] [Materials]'); wiki page:Wizard Magical Wand Essences"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Wand Essence of Wind' is locale 67481, definition 23868.", "source": "locale:67481"},
  {"claim": "Description 'This item can be added to the Wizard Magical Wand Essences Collection' is locale 132490 (the id 3069306743 cited earlier does not exist).", "source": "locale:132490"},
  {"claim": "Collection name 'Wizard Magical Wand Essences' is locale 67599; Wizard Wand Materials collection name is locale 67598 with description locale 132489.", "source": "locale:67599; locale:67598; locale:132489"},
  {"claim": "Wand Essence of Wind is the reward for completing the Wizard Wand Materials collection, per the wiki Job Specific (Collections) page and the repo collection catalogue (item 23868 x1 plus 7 coins).", "source": "wiki page:Job Specific (Collections); repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 17568-17582"},
  {"claim": "Wiki List of Collections tags [Wizard] Magical [Wand] Essences and [Wizard] [Wand] [Materials] with the Members Only icon (20px|Members Only), so the Wizard collections are members-only per the wiki index.", "source": "wiki page:List of Collections"},
  {"claim": "No coin store price, vendor, quest, enemy drop or event entry for this essence was found; client coin_store_prices is empty.", "source": "client definition; repo search for 23868 (only collection_catalogue.json hits)"},
  {"claim": "Wiki 'Wizard' job page lists the Wizard Collections (Stories, Wand Essences, Wand Materials), linking the family.", "source": "wiki page:Wizard"}
 ],
 "confidence": 0.6,
 "open": [
  "Sources for the Wizard Wand Materials (Dragons Breath, Floren Moustache Leaf, Yeti Hair, Robgoblin Booger, Metal Rod, Crystal Gems, Pixie Dust) are not evidenced in this pack, so the materials' drops/vendors remain unknown; the essence path is only complete once those are sourced.",
  "No price on wiki or store data; not sold for coins or Station Cash as far as the evidence shows.",
  "Retirement and current live status are not stated by any source; the collection appears on a 2013 wiki revision, so live is unsure.",
  "Members Only tag applies to the Wizard collections per the wiki index; whether this specific reward is gated by membership in the rebuild is not confirmed by an acquisition source.",
  "Magical Essence Ornate Wand details (level 20, Cannot Trade) were not re-verified in this pass."
 ]}
