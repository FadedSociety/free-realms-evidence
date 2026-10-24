<!-- fleet job=citem-infer id=cninja-s-necklace-of-vitality-iii-131131-v2 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[19166, 13410, 8, 2206] model=claude-haiku-5-5 -->
# Ninja's Necklace of Vitality III

{"item": {"name": "Ninja's Necklace of Vitality III", "locale_id": 131131, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Dizzy Toad (Pixie NPC Merchant; sells exclusively Ninja Job Items)", "where": "Perry's Pastures, south of Snowhill", "price": "106 coins (reconstructed reference, not observed); 95 coins member price (derived 10% discount, not observed)", "currency": "coins", "source": "wiki page Dizzy Toad (https://freerealms.fandom.com/wiki/Dizzy_Toad: location and 'sells exclusively Ninja Job Items'; introduced August 27, 2013); repo:prototype/osfr-tools/data/content/vendors.json lines 33059-33070 (npc 9500000742, item_ids include 75387); repo:prototype/osfr-tools/data/content/stores.json line 17353 (item 75387, purchase 106, member 95, price_provenance kind 'reconstructed', basis 'Legacy reference Cost and MemberDiscount; no captured retail NPC quote')"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Dizzy Toad is a Pixie NPC Merchant found at Perry's Pastures, south of Snowhill, introduced August 27, 2013, and sells exclusively Ninja Job Items.", "source": "wiki page Dizzy Toad (https://freerealms.fandom.com/wiki/Dizzy_Toad)"},
  {"claim": "Dizzy Toad's vendor entry in the repo lists item 75387 (this necklace) in his stock.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 33059-33070"},
  {"claim": "Client definition 75387 carries coin_store_prices [106]; this corroborates the 106 figure but does not tie it to Dizzy Toad.", "source": "client definition 75387 (pack client_definition.coin_store_prices)"},
  {"claim": "Client name locale 131131 is exactly 'Ninja's Necklace of Vitality III', within a set of Vitality I-V and Bark Skin III-V necklaces and Ring of Energy I-III.", "source": "locale:131131; client cluster locale:131126-131136"},
  {"claim": "The Brawler's Necklace of Vitality III Coin Shop claim is a sibling item and is not evidence for the Ninja version.", "source": "pack previous_answer evidence (wiki page Brawler's Necklace of Vitality III)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 106 coin and 95 member prices are not observed anywhere. They come from stores.json item 75387, marked 'reconstructed' from Legacy reference Cost and a 10% member discount, with no captured retail NPC quote. Treat them as reference prices only.",
  "The wiki Dizzy Toad snippet I could read lists only part of the Sells section, so this necklace's presence on the wiki sell list was not directly seen; the claim rests on the repo vendors.json entry plus the wiki's 'exclusively Ninja Job Items' line.",
  "The 'rev 2013-10-03' date in the earlier answer could not be verified; the wiki's own intro line (August 27, 2013) is the reliable date.",
  "No wiki page exists for this necklace; no Coin Shop, Prize Wheel, or Mysterious Merchant category was confirmed for it.",
  "Whether Dizzy Toad still stocks this item or it was removed later is not stated in any source; retired is null."
 ],
 "critiques_addressed": "Location corrected to Perry's Pastures (wiki) with snowhill.json kept only as a file pointer; price marked as reconstructed rather than sourced; client coin_store_prices cited as corroboration; unverified revision date dropped in favour of the wiki intro line."}
