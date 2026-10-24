<!-- fleet job=citem-infer id=ctransmission-spring-67059-v1 status=done turns=6 usd=0.0026 tokens(read,write,in,out)=[26915, 7389, 14, 2805] model=claude-haiku-5-5 -->
# Transmission Spring

{"item": {"name": "Transmission Spring", "locale_id": 67059, "kind": "collection"},
 "sources": [
  {"type": "drop", "detail": "Treasure chests dug up by pets (the Springs chests; the Pets wiki page groups Oiled, Bouncy, Golden and Tightly Coiled Metal Springs as pet-chest finds). Not confirmed for this specific spring; the wiki names the set, not the individual piece.", "where": null, "price": null, "currency": null, "source": "wiki Pets page (https://www.freerealms.wiki/wiki/Pets, 'Springs' passage); repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 14322-14417 (collection id 180, entry index 4, item_definition_id 23446)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Transmission Spring is item definition 23446 and name locale 67059, entry 4 of the Oiled Metal Springs collection (collection name locale 67546, 'Oiled Metal Springs').", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json line 14361-14364; locale:67546; locale:132439"},
  {"claim": "Client definition says the item can be added to the Oiled Metal Springs Collection; it has no coin store price and no coin vendor stock.", "source": "client definition (definition_ids 23446); repo:data/content/stores.json has no entry for 23446"},
  {"claim": "Springs chests are opened by pets; the set is one of four Springs collections (Bouncy, Golden, Oiled, Tightly Coiled Metal Springs).", "source": "wiki Pets page"},
  {"claim": "Completing the Oiled Metal Springs collection grants 4 coins and 50 XP in the collection catalogue reward block.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 14404-14412"}
 ],
 "confidence": 0.5,
 "open": ["No wiki page, video or article names Transmission Spring specifically; the drop source is inferred from the Springs set on the Pets page.",
  "Which enemy/chest table yields this exact spring is unknown; the Pets page does not say the set's chests are the only source.",
  "Not checked whether the Oiled Metal Springs collection was retired or is still live; the retired and live fields are therefore unsure.",
  "The pack's first-pass 'live: yes' is a hint only; the catalogue entry shows the item exists in the data but not that it is currently obtainable.",
  "The pack gave no price; the item is not sold by a coin vendor or the coin shop per the evidence seen."]}
