<!-- fleet job=citem-infer id=cenergy-transfer-medic-helmet-133131-v2 status=no_submit turns=2 usd=0.0025 tokens(read,write,in,out)=[6169, 9436, 6, 2542] model=claude-haiku-5-5 -->
# Energy Transfer Medic Helmet

```json
{"item": {"name": "Energy Transfer Medic Helmet", "locale_id": 133131, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Bishop (sells exclusively Medic job items), Briarwood, near the Briarheart warpstone", "where": "Briarwood", "price": "1076 coins (stores.json reference price, not an NPC-verified quote); member price 968 coins; sell price 107 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Bishop (Sells list includes 'Energy Transfer Medic Helmet'); repo:prototype/osfr-tools/data/content/stores.json:15829 (item 76123, purchase_price_coins 1076, member_price_coins 968, sell_price_coins 107); repo:prototype/osfr-tools/data/content/vendors.json:8531-8545 (price marked as reference); repo:prototype/osfr-tools/data/content/vendors_unresolved.json:1601-1621 (Bishop npc 9500000092, Energy Transfer Medic set incl. 76123, unresolved file); notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:210"},
  {"type": "prize_wheel", "detail": "Medic prize wheel (job-specific wheel), item named on the list; the wheel entry gives a name only, no item id", "where": "Tanglewood Fort", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Tanglewood_Fort (page lists '[Medic] Prize Wheel' with 'Energy Transfer Medic' entries, snippet truncated); notes/Build Guides/Content/Dungeons/Tanglewood Fort.md:80; repo:prototype/osfr-tools/data/content/dungeons/tanglewood_fort.json:2716-2722 (target_name 'Energy Transfer Medic Helmet', no definition id)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 76123 'Energy Transfer Medic Helmet' has name locale 133131, slot 1, class 7, and a coin store price of 1076.", "source": "locale:133131; client definition; repo:prototype/osfr-tools/data/content/stores.json:15829"},
  {"claim": "The wiki Bishop page says he sells exclusively Medic job items and lists the Energy Transfer Medic Helmet under Sells, alongside the other five Energy Transfer Medic pieces.", "source": "https://freerealms.fandom.com/wiki/Bishop (lookup, revision 2026-05-13)"},
  {"claim": "The Briarwood NPC notes list Bishop with the Energy Transfer Medic set, added 27 Aug 2013.", "source": "notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:210"},
  {"claim": "The vendor data maps item 76123 to Bishop's stock with a 1076 coin reference price, flagged as not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:8531-8545"},
  {"claim": "The Medic prize wheel at Tanglewood Fort lists the Energy Transfer Medic Helmet.", "source": "notes/Build Guides/Content/Dungeons/Tanglewood Fort.md:80; repo:prototype/osfr-tools/data/content/dungeons/tanglewood_fort.json:2716-2722; https://freerealms.fandom.com/wiki/Tanglewood_Fort"},
  {"claim": "The client name has no description and no wiki page gives a retirement note.", "source": "client definition; lookup of wiki (Bishop, Tanglewood Fort, Forest Troll Fort)"}
 ],
 "confidence": 0.7,
 "open": [
  "Live status is inferred only from the current Bishop wiki listing (rev 2026-05-13). No in-game capture or retirement note was found, so live is 'unsure' and retired is unknown.",
  "The 1076-coin price (member 968, sell 107) is a stores.json reference price. The wiki Bishop snippet shows no coin price, so it is not NPC-verified.",
  "The Tanglewood Medic prize wheel row names the helmet but gives no item id, so the link to 76123 rests on the name match. The wheel's cost is not captured in the snippets (Tanglewood's page shows a 77 Coins figure near the wheel listings, but it is not tied to this item).",
  "The Forest Troll Fort wiki snippet lists 'Stopping Power [Medic] [Helmet]' and 'Energy Transfer Medic Jacket' on a Medic wheel, but not this helmet, so no Forest Troll Fort source is added."
 ],
 "critiques_addressed": "Price now labelled as stores.json reference, not wiki-sourced; live changed from 'yes' to 'unsure'; vendors_unresolved.json added as Briarwood stock link; prize_wheel source added per the world critique, with the id gap flagged."
}
```
