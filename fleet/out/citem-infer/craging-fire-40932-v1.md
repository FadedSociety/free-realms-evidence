<!-- fleet job=citem-infer id=craging-fire-40932-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[12983, 10706, 8, 2809] model=claude-haiku-5-5 -->
# Raging Fire

{"item": {"name": "Raging Fire", "locale_id": 40932, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 40932 is named 'Raging Fire' (ability-type string). Its only other client line is the name itself.", "source": "locale:40932"},
  {"claim": "Its client definition (definition id 3716) carries the description 'This item can be added to the Inferno Lanterns Collection', so it is a member of the Inferno Lanterns collection, not a standalone sellable item.", "source": "locale:132350"},
  {"claim": "'Inferno Lanterns' is a named collection on the wiki's List of Collections page, so the collection exists in the live game.", "source": "wiki: List of Collections"},
  {"claim": "The neighbouring client strings 40927-40937 (High Voltage, Brilliant Illumination, Gleaming Light, Molten Lava, Meteoric Rain, Exploding Atom, Ferocious Combustion, Extreme Embers, Intolerable Heat, Sea of Flames) are a sibling run of ability-type strings with the same fire/light theme, which suggests a set; no source says what they are for.", "source": "locale:40927-40937"},
  {"claim": "No wiki article, image, article fact, video frame, vendor stock row, quest, or drop names Raging Fire. The only wiki hit for the phrase is an unrelated user blog.", "source": "wiki: User blog:Storm dreams/About Me"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is confirmed. Its member-of-collection status is shown, but how a player obtains the item (which collection pack, promotion, or drop) is not in the evidence.",
  "Coin store conflict: repo:prototype/osfr-tools/data/content/stores.json line 12538 has a row {item_id 40932, category 101, tint_group 1, purchase 618 coins, member 556, sell 61}. The pack says the client definition has no coin store price and its definition id is 3716. The store row's item_id equals this item's locale id, not its definition id, so it may be a key mix-up. Not counted as a vendor source until someone checks which item id stores.json uses. If it does belong to Raging Fire, it would be a coin vendor sale at 618 coins (556 member price) with the sell price at 61 coins, sourced to repo:data/content/stores.json item 40932.",
  "The List of Collections wiki snippet was truncated, so it is not confirmed that Raging Fire is one of the Inferno Lanterns members. Check the full Inferno Lanterns entry.",
  "Liveness is unsure. The first-pass tag says live, but the evidence only shows the collection exists. The item may have been retired with the collection; no retirement source was found.",
  "Ability-type sibling strings (40927-40937) have no sources here. Check whether they are part of one collection or event set before using them to infer sources."
 ]}
