<!-- fleet job=citem-infer id=cmystical-seaside-water-sample-41142-v2 status=nothing_found turns=2 usd=0.0029 tokens(read,write,in,out)=[6093, 16169, 6, 1673] model=claude-haiku-5-5 -->
# Mystical Seaside Water Sample

{"item": {"name": "Mystical Seaside Water Sample", "locale_id": 41142, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 41142 is 'Mystical Seaside Water Sample', with description 'This item can be added to the Seaside Water Samples Collection'. Item definition 3926 is entry 8 of collection 117 'Seaside Water Samples' (name_id 7768).", "source": "locale:41142; repo:prototype/osfr-tools/data/content/collection_catalogue.json:9817-9821"},
  {"claim": "The set name 'Seaside Water Samples' appears on the wiki's List of Collections (rev 2013-07-13). That entry gives only the name; entries and reward are not listed there, so it confirms the set name only.", "source": "repo:prototype/osfr-tools/data/content/collections.json:11411-11436 (wiki:8:228, https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "The set-completion reward (7 coins, item 23164 x1, 50 XP, collection_add 145) belongs to completing the whole set, not to acquiring this sample. It is not a source for the sample.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9824-9841"},
  {"claim": "The video frame video:pjvw6oAT-zQ/00084.jpg shows the Collections tab with a 'Toxic [Seaside] [Water] [Sample]' entry and a 'Sacred Keys Collection' description. It does not show the Mystical Seaside sample. The previous answer's claim that it did is wrong.", "source": "video:pjvw6oAT-zQ/00084.jpg"},
  {"claim": "The client has no coin store price, no vendor stock, no quest or drop text, and no wiki page for this item. The Embir Clearwell water-sample quest names Shrouded Glade, Misty Mountain and Lakeshore, not Seaside.", "source": "client coin_store_prices []; notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:132"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source for the sample itself. The pack has no wiki page, coin store price, vendor, quest, drop, event or prize-wheel source that names it.",
  "live is unsure, not yes. The set's listing on the wiki confirms the set name only. The sample's own live status is unconfirmed.",
  "Retirement status is unknown.",
  "Item 23164 (set reward) is unnamed in the pack and is not a source for this item.",
  "Lead only: the Mystical variants of Seaside, Merry Vale and Sanctuary samples share a naming pattern, which may point to a shared promotion or event. Unconfirmed.",
  "Locale strings 'Mystical Seaside Mixture' (1218404998) and 'Mystical Seaside Liquid Concoction' (2599451004, 3571927349) sit near this item in the client table. Their sources are unchecked."
 ]}
