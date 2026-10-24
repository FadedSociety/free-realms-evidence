<!-- fleet job=citem-infer id=ccobblestone-small-wall-148425-v1 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[17916, 10347, 10, 1610] model=claude-haiku-5-5 -->
# Cobblestone Small Wall

{"item": {"name": "Cobblestone Small Wall", "locale_id": 148425, "kind": "furniture"},
 "sources": [{"type": "vendor", "detail": "Housing building-materials coin store (store category 4); exact vendor NPC not identified in the repo store record", "where": null, "price": "5 coins (member price 4 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36905 (line 12187: purchase_price_coins 5, member_price_coins 4, sell_price_coins 1)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name and description: 'Cobblestone Small Wall', 'This is a 2 x 1 x 2 wall.', definition 36905, model hsg_small_wall_block_v2_01.adr", "source": "locale:148425"},
  {"claim": "Store record sells item 36905 for 5 coins, sibling of the cobblestone/brick/wood/toy/marble housing pieces in the same store block (items 36873-36908 at 5-20 coins)", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36905"},
  {"claim": "Same-set client names (Cobblestone Small Pillar, Brick Small Wall, Wood Small Wall, Cobblestone Cube) share locale block 148420-148430", "source": "locale:148420 through locale:148430"},
  {"claim": "Cobblestone builders packs exist as a wiki item category, but the wiki does not list this wall as a pack component", "source": "wiki page:ns0 Items (Cobblestone Builders Pack entries)"}],
 "confidence": 0.6,
 "open": ["The vendor NPC and zone that sell store category 4 are not named in the repo record; the vendor must be confirmed from a vendor or store listing before the rebuild assigns it.", "No wiki article covers this item; the only price evidence is the repo store record, not a wiki price, so no sale price is recorded.", "Whether it is also sold in the Station Cash marketplace or appears in a builders pack is unverified.", "The first-pass tag 'live: yes' is consistent with the store record (source_tags L1, L2, L4, R2, T633, R1) but is only a hint."]}
