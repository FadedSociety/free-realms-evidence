<!-- fleet job=citem-infer id=cbutterfly-2047-v2 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[6573, 11701, 6, 1881] model=claude-haiku-5-5 -->
# Butterfly

{"item": {"name": "Butterfly", "locale_id": 2047, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Locale 2047 is typed npc_name and reads 'Butterfly'. It is not typed as an item name, so no item definition is confirmed by it.", "source": "locale:2047"},
  {"claim": "Client definition 77530 is a character-create wing (name locale 2047, model fairy_f_wings_butterfly.adr, slot 7, dyetint), linked to 'Butterfly Wing Pattern Card' in the character-create mappings. It is not a pet.", "source": "client Resources/CharacterCreate/ItemDefinitions.txt:137; Resources/CharacterCreate/CharacterCreateItemMappings.txt:114"},
  {"claim": "Item id 17537 has no client definition text in the client Resources (searched by id; the only hits are unrelated asset hashes). Its store row has no name.", "source": "client search for 17537; repo:prototype/osfr-tools/data/content/stores.json:4328"},
  {"claim": "stores.json:4328 is one row in a long run of category-200 entries (ids 17529 to 17549 and beyond) that all carry 10000 coins (member 9000), tint group 1, no_sale true. The row is unattributed: it cannot be tied to a pet or item called Butterfly. The 10000 price is therefore not a price for this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4320-4340"},
  {"claim": "The August 2010 Coin Shop housing items (Butterfly Rug, Side Table, Bed) are housing items, not this item.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1730; http://www.freerealms.com/article/detail.action?articleId=1734; http://www.freerealms.com/article/detail.action?articleId=1732"},
  {"claim": "Previous answer's collection source (Butterfly Vanity Pet, locale 139768) is removed: locale 139768 is flagged as a developer note (jweathers), and locales 139765/139767 name a different companion ('Butterfly Companion'), not this item.", "source": "locale:139768; locale:139765; locale:139767"},
  {"claim": "No vendor, quest reward, drop, event, prize wheel, or wiki page was found that names this item.", "source": "vendor_stock empty in evidence pack; no wiki page or video frame found"}
 ],
 "confidence": 0.15,
 "open": [
  "Not resolved as an item. Locale 2047 is an NPC-name string, and no item definition with the pet description ('This simple pet will only follow you around and keep you company.') was found in the client files. The first-pass 'pet / vendor / live yes' tag is unsupported and was not used.",
  "Definition 77530 is a character-create wing and must be removed from this item's definition list. Definition 17537 has no client definition text.",
  "The 10000-coin (member 9000) store price is an unattributed row (stores.json:4328, category 200, tint group 1). Do not record it as this item's price until item 17537 is named.",
  "'Butterfly Companion' (locale 139765, spawn 139767) is a separate lead for a companion pet. Its item id, model and price are not found; it needs its own evidence pack.",
  "Wiki tooltips 'Butterfly Club' and 'Butterfly Blade' are separate weapons with the same name, not evidence for this item.",
  "Live status and any sale or retirement history cannot be confirmed from this pack."
 ]}
