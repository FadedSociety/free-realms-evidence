<!-- fleet job=citem-infer id=cmystical-lakeshore-water-sample-41158-v2 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[22866, 17911, 8, 2398] model=claude-haiku-5-5 -->
# Mystical Lakeshore Water Sample

{"item": {"name": "Mystical Lakeshore Water Sample", "locale_id": 41158, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 41158 reads 'This item can be added to the Lakeshore Water Samples Collection' (definition 3942). This shows collection membership only; it does not show how the item is obtained or whether it is sellable.", "source": "locale:41158; client definition definition_ids [3942]"},
  {"claim": "Sibling Lakeshore tiers 41151-41157 (Toxic, Clean, Purified, Dirty, Boiling, Freezing, Magical) share the same 'Lakeshore Water Sample' naming pattern and sit together in the client text table, so the tier family is a collection set.", "source": "locale:41151-41157; locale:41158"},
  {"claim": "Client text 67624 'Liquid concoctions made up from a rare selection of Lakeshore water samples.' is a separate Lakeshore water-samples item (not this sample). It is the only Lakeshore collection-level item found in client text and suggests a collection reward path, but no text ties it to this Mystical tier.", "source": "locale:67624"},
  {"claim": "Embir Clearwell's Lakeshore water-sample quest asks the player to collect a water sample from Lakeshore (objective text), and the Shrouded Glade quest asks for water samples from falls. Neither text names a reward or the Mystical tier.", "source": "locale:91069; locale:115680; locale:70849; locale:70855; repo:notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:132"},
  {"claim": "The earlier video claim (video:pjvw6oAT-zQ/00084.jpg shows the Lakeshore samples in a Lakeshore collection) is withdrawn: the frame's Collections panel reads 'This item can be added to the Sacred Keys Collection'. It shows a toxic Lakeshore sample only in a nearby inventory list.", "source": "video:pjvw6oAT-zQ/00084.jpg"},
  {"claim": "No coin store price (client coin_store_prices empty), no vendor stock, no wiki page, no article fact, and no drop or event text names this item. Lookups across client, wiki, articles and video returned only the client name/collection lines.", "source": "client definition; lookup client/wiki/articles/video"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced for the Mystical Lakeshore Water Sample. Sources are left empty rather than guessed. The first-pass 'drop' guess has no supporting text.",
  "How the Lakeshore Water Samples collection pays out (per-tier drops, quest rewards, or completion reward such as locale 67624's liquid concoction item) is unknown. Check the collection's reward rules before adding a source.",
  "The Mystical tier's rarity and whether it is a rare drop or a collection-completion reward are unknown.",
  "The video frame video:pjvw6oAT-zQ/00084.jpg was previously cited as showing the samples in a Lakeshore collection; the critique showed it reads 'Sacred Keys Collection'. Withdrawn.",
  "The exact collection name ('Lakeshore Water Samples Collection' in client text vs 'Lakeshore Water Sample collection' in repo notes) still needs one source.",
  "Live status is unconfirmed. The first-pass 'live: yes' is a hint only. The Mystical Merry Vale and Mystical Seaside siblings exist in client text, but no wiki or repo source was found for them either.",
  "No coin store, SC marketplace, prize wheel, or membership listing was found in the repo stores data or wiki for this item."
 ]}
