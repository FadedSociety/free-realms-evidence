<!-- fleet job=citem-infer id=cbriarwood-club-card-7-414454-v2 status=nothing_found turns=2 usd=0.0026 tokens(read,write,in,out)=[5442, 12262, 6, 2032] model=claude-haiku-5-5 -->
# Briarwood Club Card 7

{"item": {"name": "Briarwood Club Card 7", "locale_id": 414454, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 68906 is named 'Briarwood Club Card 7' (locale 414454). Its description is 'This item can be added to the Briarwood Club Cards Collection' (locale 132508). It has no model and no coin store price.", "source": "locale:414454; locale:132508; client definition in pack"},
  {"claim": "The set is titled 'Briarwood Club Cards' and is tagged quest_title, not a collection or pickup label.", "source": "locale:414426"},
  {"claim": "The objective text says to search around Sir Wellington in Briarwood to find all of the Briarwood Club Cards and receive a prize. This is objective wording only. It does not show how a single card is obtained, and the prize is not named.", "source": "locale:414425"},
  {"claim": "Sir Wellington is a Briarwood NPC (dig site and Card Duelist opponent). Client text places him outside the Vale of the Ancients in Bristlewood, and 'beyond the hedge maze' appears in a separate string.", "source": "locale:17867; locale:584342201 (per notes); notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:115 and :337"},
  {"claim": "Sir Wellington's card-game quest lines (play cards with him) sit in the same Briarwood text cluster. No client or repo text links them to the Club Cards.", "source": "locale:413768; locale:413772; locale:413812"},
  {"claim": "No wiki page, article, video frame, coin vendor, store price, enemy drop or event names the Briarwood Club Cards. Searches of the client, wiki, articles and video and of the repo found no match besides the strings above.", "source": "lookup (client, wiki, articles, video) and repo search for 'Club Card|Briarwood Club|Wellington'"},
  {"claim": "Jev's first-pass 'source_guess: drop' is not supported by any evidence and is not used.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.2,
 "open": [
  "Acquisition route is unknown. The critique is right that 'world pickup by searching' is inferred from objective wording, not evidenced. The granting quest or pickup mechanic has not been identified, so no source is listed.",
  "The prize for finding all eight cards (locale 414425) is not identified in the client text or repo. Its item and source are unknown.",
  "Whether the cards are world pickups, quest rewards or drops is unverified. The client has no quest or enemy string naming them.",
  "No coin vendor, Station Cash listing, Coin Shop entry or Prize Wheel entry exists for this card. The client definition has no store price.",
  "Live status is unverified. Nothing shows the set was live on the 2009-2014 server or retired later. Jev's 'live: yes' is unsupported.",
  "Unrelated cluster strings (locale 414456 'Pile of Cards', locale 414457-414459 Gardener's Gummyfruit Gumbo) were not used.",
  "The earlier answer cited 'Design and NPCs - Briarwood.md'; the file is at notes/Build Guides/Content/NPCs/NPCs - Briarwood.md. The earlier answer's 'collection piece, not a stocked item' and 'world pickup' statements are not evidenced and are withdrawn.",
  "Wireable: false. A builder cannot wire a source or price from this pack."
 ],
 "wireable": false}
