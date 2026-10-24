<!-- fleet job=citem-infer id=cdraconic-warrior-pauldrons-30531-v1 status=done turns=6 usd=0.0046 tokens(read,write,in,out)=[62179, 21412, 14, 2618] model=claude-haiku-5-5 -->
# Draconic Warrior Pauldrons

{"item": {"name": "Draconic Warrior Pauldrons", "locale_id": 30531, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Unnamed coin vendor (store category 106); the store data does not name the NPC or shop", "where": null, "price": "1761 coins (member price 1584 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9292 (line 2712)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name is locale 30531 'Draconic Warrior Pauldrons', slot 6 (shoulders), item class 173, one definition (id 9292).", "source": "locale:30531; client definition"},
  {"claim": "Store data lists item 9292 at 1761 coins purchase, 1584 coins for members, with sell_price null and no_sale true.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9292 (line 2712)"},
  {"claim": "Sibling items 9284, 9286, 9288, 9291 (same 1761-coin block, same no_sale/source tags) are the same Draconic/Tiger-style set in the client cluster (locale 30526-30534).", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2708-2712; locale 30526-30534"},
  {"claim": "The client cluster names sit next to Neon Green/Pink Tiger Pauldrons, Skeletal Tunic, Starry Moons Hat, Wild Magic Robe, Spider Shot Hoodie, Abracadabra Robe, all with the same 'levels up with you' line (30534).", "source": "locale:30526-30534"},
  {"claim": "No wiki page, article, image or video names this item; the locale 150505 line is a generic placeholder and is not evidence.", "source": "lookup client/wiki/articles/video: no matches"}],
 "confidence": 0.35,
 "open": ["The store entry is no_sale:true with sell_price null, which suggests it was listed in the coin store data but not sold in the current shop; whether it was ever sold live and at which vendor is unconfirmed.",
  "Vendor NPC and zone are unknown: no vendor_stock answer names this item and the stores file gives only a category id (106), not a shop.",
  "No wiki price or retirement date found, so the retired field is null.",
  "The first-pass 'live: yes' is a cheap-model hint and is not supported by any current sale source; live status is marked unsure.",
  "Quest rewards, drops, events, prize wheel, crafting and collection sources were checked by the cluster and found none; none listed.",
  "Locale 42271 is a second name string for the same item (rich-text form) and carries no separate source."]}
