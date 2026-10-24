<!-- fleet job=citem-infer id=cdirty-nettleseed-mixture-66811-v1 status=done turns=9 usd=0.0062 tokens(read,write,in,out)=[122641, 22883, 20, 4238] model=claude-haiku-5-5 -->
# Dirty Nettleseed Mixture

{"item": {"name": "Dirty Nettleseed Mixture", "locale_id": 66811, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Dirty Nettleseed Mixture' is locale 66811, with description 'This item can be added to the Nettleseed Mixture Collection' (locale 132408; ucdt 3807164968). Item definition 23198.", "source": "locale:66811; locale:132408; repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 11376-11383 (entry id 1073, index 4, item_definition_id 23198, item_link 'sanctuary')"},
  {"claim": "The item is entry 4 of collection id 149, named 'Nettleseed Mixture' (name_id 67515, description_id 67627). The collection has 8 entries (Toxic 23195, Clean 23196, Purified 23197, Dirty 23198, Boiling 23199, Freezing 23200, Magical 23201, Mystical 23202).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 11339-11420; locale:67515"},
  {"claim": "The wiki's List of Collections (revision 27852, 2013-07-13) lists a '[Nettleseed] Mixture' collection, so the collection existed on the 2013 wiki. The wiki gives no per-item source for the mixtures.", "source": "wiki: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); repo:prototype/osfr-tools/data/content/collections.json line 11582 (wiki:8:234)"},
  {"claim": "Completing the Nettleseed Mixture collection pays 5 of item definition 3082 (a collection reward, not a source of the Dirty mixture itself).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 11421-11428"},
  {"claim": "No coin store price, vendor stock, wiki page, article, or video frame names the Dirty Nettleseed Mixture. The client definition has no coin_store_prices entry.", "source": "client definition in the evidence pack; repo search for 66811/79060112 (no store hits)"}
 ],
 "confidence": 0.3,
 "open": [
  "No evidenced source for how a player obtains the Dirty Nettleseed Mixture (vendor, drop, crafting, quest, or gathering). The rebuild needs this before any source row can be written. Candidates to check: Nettleseed enemy drops and the Nettleseed Liquid Concoction chain (the sibling item 'Dirty Nettleseed Liquid Concoction' is locale 66763, item 'Nettleseed Liquid Concoction Collection' is locale 132402), plus the Shrouded Gloam druid 'mixtures' quest (notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md line 270 says 'q4 mixtures'). None of these is tied to this item by a source.",
  "The Sanctuary data gives the collection's item_link as 'sanctuary', which indicates the mixtures came from a Sanctuary-era collection definition. The wiki and client do not say whether the mixtures were ever sold or are unobtainable now. retired is therefore unknown.",
  "The 'live: yes' tag comes from the cheap first pass and from the collection's presence in the 2013 wiki list. It is not confirmed by any source of a current acquisition path.",
  "The 'Dirty Nettleseed Water Sample' (ucdt 3307494430) is a different item and was not counted here. Check whether the water sample feeds the mixture before linking them.",
  "The kind is 'collection' from the description and collection membership. Confirm the item's real class (its client item class is 0 and it has no model)."
 ]}
