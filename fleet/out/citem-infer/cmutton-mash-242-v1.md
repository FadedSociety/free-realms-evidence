<!-- fleet job=citem-infer id=cmutton-mash-242-v1 status=nothing_found turns=6 usd=0.0049 tokens(read,write,in,out)=[66632, 20559, 14, 3238] model=claude-haiku-5-5 -->
# Mutton Mash

{"item": {"name": "Mutton Mash", "locale_id": 242, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 242 'Mutton Mash' (item); its description reads 'Eating this food will temporarily change the player into a Wolf.' (locale 3152 is the same wording, so the description is shared with other illusion foods).", "source": "locale:242; locale:3152"},
  {"claim": "Mutton Mash is a member of the client's 'Illusion Food' family (locale 237-247 cluster: Yeti, Troll Popsicle, Bear Vine Golem, Wolf Vine Golem, Man-Eating Plant, Owl, Bat, Grotto Bat Cakes, Forest Troll Waffles, Shambler). Those are illusion-transform foods, mostly with a fixed duration (e.g. Bark Chocolate: 'Dog Large Floppy - 30 minutes').", "source": "locale:237-247; locale:233, 236, 248, 255-257; wiki image:item_tooltip 'Bark chocolate.jpg'"},
  {"claim": "The wiki 'Items' page lists '[Mutton] Mash' among food items, so a wiki entry exists, but the snippet returned gives no acquisition source, price, or date.", "source": "wiki page:ns0 'Items'"},
  {"claim": "Client definitions 2947 and 3006 share the name 'Mutton Mash' (two definitions, one name, slot 0, class 9). No coin store price is recorded for either, so no coin vendor sale is evidenced.", "source": "client definition (repo stores search: no match for 2947/3006 or 'Mutton' in data/content)"},
  {"claim": "No vendor stock, quest reward, enemy drop, event, or prize-wheel source names Mutton Mash or the Illusion Food family in the repo or wiki search.", "source": "repo search 'Illusion Food|Mutton|Troll Popsicle|Grotto Bat' (no hits); lookup 'Illusion Food' and 'Mutton' (wiki, articles, video: no acquisition text)"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. The wiki Items page links Mutton Mash but the snippet gives no acquisition text. Check the full wiki Items page or an 'Illusion Food' category page for where these foods came from (event, membership, prize wheel, or crafting).",
  "The first-pass tag 'live: yes' is unverified. The wiki listing suggests it existed, but no retirement date or availability source was found.",
  "Two definitions (2947, 3006) share the name. Which one is live, and whether they differ in duration or model, is unknown.",
  "The description says 'temporarily' and gives no duration. The Wolf transform duration (and whether it matches the 'thirty minutes' wording of locale 3149/3153) needs a source.",
  "Video frames and articles returned nothing for these foods. A holiday or event article about illusion foods could still name the source."
 ]}
