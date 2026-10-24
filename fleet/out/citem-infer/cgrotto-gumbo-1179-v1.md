<!-- fleet job=citem-infer id=cgrotto-gumbo-1179-v1 status=nothing_found turns=6 usd=0.0045 tokens(read,write,in,out)=[60860, 19265, 14, 2985] model=claude-haiku-5-5 -->
# Grotto Gumbo

{"item": {"name": "Grotto Gumbo", "locale_id": 1179, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Grotto Gumbo', locale 1179; description: 'Eating this food will change the player into a female changeling brawler for thirty minutes.'", "source": "locale:1179 and locale:2732"},
  {"claim": "Part of a 'Grotto' food set (locale 1174-1184: Honeyglazed Fish Sticks, Pureed Pear Pie, Grotto Omelette, Grotto Candies, Grotto Beans, Grotto Gumbo, Grotto Stew, Grotto Noodles, Grotto Lollipop, Grotto Creampuffs, Grotto Casserole). Each is a changeling-transform food; the client has a matching description series for each changeling role (locale 2729-2738: cook, elder, brawler, scout, gardener, ninja).", "source": "locale:1174-1184; locale:2729-2738"},
  {"claim": "Client defines one definition (id 4020), slot 0, item class 9, no model files, and no coin store price in repo:data/content/stores.json.", "source": "client definition pack"},
  {"claim": "No wiki page, article, video frame, or repo data row names Grotto Gumbo or any Grotto food as sold, dropped, or rewarded. The repo's only '4020' hits are unrelated NPC ids.", "source": "lookup (client, wiki, articles, video: no hits beyond locale rows); search repo for 'Grotto' and '4020'"},
  {"claim": "Changeling-related quest text exists (Forgotten Caves food supply, Briarheart Cavern changelings), but no text links these foods to a quest reward or vendor.", "source": "locale:15970, locale:16045"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found for Grotto Gumbo: no vendor stock, coin store price, quest reward, drop, event, or promotion evidence in any available root. Do not seed a source from the first-pass 'vendor' guess; it has no evidence.",
  "Likely a changeling transformation food from the Briarwood/Forgotten Caves changeling storyline or a changeling-themed event, but this is unverified. Needs a wiki page on the changeling food set or a legacy source (FreeRealms-Legacy vendor or quest tables keyed to item 4020) to confirm.",
  "Retired/live status unknown. Not in the pack's coin store data, so live status cannot be confirmed from our store data either.",
  "Sibling items (Grotto Stew 1180, Grotto Noodles 1181, Grotto Bat Cakes 245) also lack sources in the available data; check them together once a source is found."
 ]}
