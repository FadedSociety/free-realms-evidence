<!-- fleet job=citem-infer id=cpractitioner-wizard-fez-133430-v1 status=done turns=6 usd=0.0042 tokens(read,write,in,out)=[41212, 16440, 14, 3480] model=claude-haiku-5-5 -->
# Practitioner Wizard Fez

{"item": {"name": "Practitioner Wizard Fez", "locale_id": 133430, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Glenda (Wizard job NPC, sells Wizard job items; Practitioner Wizard set)", "where": "Stillwater Crossing (near the warpstone)", "price": "627 Coins (reference price from stores.json; member price 564 Coins, 10% member discount; sell-back 62 Coins). Not a captured NPC quote.", "currency": "coins", "source": "repo:data/content/stores.json item 76422 (purchase_price_coins 627); repo:prototype/osfr-tools/data/content/vendors.json item_id 76422 (stock_source: wiki page Glenda, section Sells, https://freerealms.fandom.com/wiki/Glenda); freerealms-wiki cache, Glenda page lists 'Practitioner Wizard Fez' under Sells"},
  {"type": "prize_wheel", "detail": "Prize wheel, Wizard job slot (Howling Hills dungeon wheel). Each wheel also has a 343 Coins slot; 343 Coins is the wheel's coin slot, not this item's price.", "where": "Howling Hills (dungeon, difficulty 3)", "price": null, "currency": null, "source": "wiki page Howling Hills (Prize Wheel by job, Wizard row); repo:notes/Build Guides/Content/Dungeons/Howling Hills.md:81; repo:prototype/osfr-tools/data/content/dungeons/howling_hills.json:2791"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item definition: name 'Practitioner Wizard Fez', locale 133430, definition 76422, slot 1 (head), class 8, model caster_<race>_<gender>_head_fez.adr", "source": "locale:133430; repo:prototype/osfr-tools/data/content/vendors.json item 76422"},
  {"claim": "Glenda sells Practitioner Wizard Fez (Wizard job items: Talisman, Skirt, Slacks, Fez, Gloves, Shoes, Cloak)", "source": "wiki page Glenda, Sells section (via repo:prototype/osfr-tools/data/content/vendors.json item 76422 stock_source, revision 2025-03-21)"},
  {"claim": "Store reference price 627 Coins, member 564 Coins, sell 62 Coins", "source": "repo:data/content/stores.json line 16076 (item 76422, category 101, tint group 1)"},
  {"claim": "Howling Hills Wizard prize wheel lists Practitioner Wizard Fez", "source": "wiki page Howling Hills, Prize wheel by job; repo:notes/Build Guides/Content/Dungeons/Howling Hills.md:81"},
  {"claim": "Fez appears in the inventory frames of gameplay video, alongside other Wizard job pieces (not a source by itself)", "source": "video:gxAPpQZccYw/00010.jpg"},
  {"claim": "Set siblings sit together in the locale (133425-133435, Practitioner and Adherent Wizard pieces)", "source": "locale:133425..133435"}
 ],
 "confidence": 0.7,
 "open": [
  "Retirement status not confirmed by any source in the pack; the Glenda wiki listing is dated 2025-03-21 and the 627 Coins price is a stores.json reference, not a captured NPC quote. Check a current Glenda sell list before treating the vendor price as live.",
  "The Glenda wiki page's own printed coin price for the Fez was not found in the lookup results; the 627 figure comes from stores.json.",
  "The Howling Hills prize wheel source is a wiki claim; the wheel's drop rate and whether the slot is still live are not stated.",
  "The client definition has an empty description, so the item text does not say how it is obtained.",
  "No quest reward, enemy drop, event, or crafting source was found for this item in the pack."
 ]}
