<!-- fleet job=citem-infer id=cbig-fancy-ring-66930-v1 status=done turns=5 usd=0.0036 tokens(read,write,in,out)=[33167, 12050, 12, 3582] model=claude-haiku-5-5 -->
# Big Fancy Ring

{"item": {"name": "Big Fancy Ring", "locale_id": 66930, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 3 of the 'Fancy Rings' collection (collection id 164, client_id 1073741999, wiki category 6, List of Collections). The item is a collection entry; the collection lists it, but no source found says how a player acquires the ring itself.", "where": "Sanctuary", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12816-12820 (name_id 66930, item_definition_id 23317, item_link sanctuary); repo:prototype/osfr-tools/data/content/collections.json:9926-9953 (Fancy Rings, source wiki page 'List of Collections', https://freerealms.fandom.com/wiki/List_of_Collections); lookup wiki hit 'List of Collections' lists [Fancy] [Rings]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Big Fancy Ring' (locale 66930); description reads 'This item can be added to the Fancy Rings Collection'; item definition id 23317; slot 0, class 0, no models.", "source": "locale:66930; client definition supplied in pack; locale:2773485885 description text"},
  {"claim": "The item is entry index 3 of the Fancy Rings collection, alongside Expensive Fancy Ring (66928, def 23315), Shiny Fancy Ring (66929, def 23316) and Fake Fancy Ring (66931, def 23318). The collection's entries all carry item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12790-12830"},
  {"claim": "The Fancy Rings collection is on the wiki's List of Collections page, so the collection itself is documented there, but no wiki article for the individual ring was found.", "source": "lookup wiki 'List of Collections'; repo:prototype/osfr-tools/data/content/collections.json:9930"},
  {"claim": "The collection's reward is 2 coins and 50 XP, with no item reward listed. So the ring is not a collection-completion reward.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12772-12784"},
  {"claim": "No coin store price, no coin vendor stock, and no quest reward, drop, or event mention of this ring were found. The only quest text about rings (Marriage Proposal, locale:23583/23586/77482) is flagged not_live and asks for iron ore and tourmaline for a crafted ring, with no link to 23317.", "source": "locale:23583; locale:23586; locale:77482; search of repo and refs for '23317' and 'Fancy Ring'"}
 ],
 "confidence": 0.3,
 "open": [
  "No real acquisition source found. The ring's only documented link is membership in the Fancy Rings collection. The sources list therefore contains only a collection-membership entry, not a true acquisition route. Check the live Sanctuary or Legacy data or the Sanctuary Resources for how entries are earned (vendor, crafting, or drop).",
  "The Fancy Rings collection entries lack a documented acquisition method. The Sanctuary 'Collections.json' reference was cited by collection_catalogue.json but was not checked directly.",
  "No price is known: no coin store price in the client definition and no wiki Coin Shop, SC Marketplace or prize-wheel category mention.",
  "Retired status is unknown: no source states whether the ring or the Fancy Rings collection was retired or made unobtainable.",
  "The jev first-pass tag said live 'yes' and kind 'collection'. The live answer is set to 'unsure' because the only evidence is the collection catalogue entry. The kind is 'collection' as the first pass suggested, though the item itself is a ring worn as an item.",
  "The Marriage Proposal quest text suggests a Sanctuary ring-crafting link, but that quest is flagged not_live and nothing ties it to item 23317. It is not used as a source."
 ]}
