<!-- fleet job=citem-infer id=ctoy-small-pillar-148421-v1 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[31277, 15213, 12, 2065] model=claude-haiku-5-5 -->
# Toy Small Pillar

{"item": {"name": "Toy Small Pillar", "locale_id": 148421, "kind": "furniture"},
 "sources": [{"type": "vendor", "detail": "Coin store vendor, unnamed in our data (stores.json category_id 4, the same category as the neighbouring housing building-block rows 36873-36903)", "where": "Coin store (category 4); specific vendor NPC and zone not identified", "price": "5 coins (member price 4 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36901 (purchase_price_coins 5, member_price_coins 4, sell_price_coins 1)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client definition: 'Toy Small Pillar', description 'This is a 2 x 2 x 2 pillar.', definition 36901, one variant, model hsg_small_pilar_block_v2_01.adr", "source": "locale:148421"},
  {"claim": "Coin store row exists for item 36901 at 5 coins, member price 4, sell-back 1, tagged T633 (sell-back is one tenth of buy price)", "source": "repo:prototype/osfr-tools/data/content/stores.json:12183; notes/Research/Coin Shop.md:33-46"},
  {"claim": "Sits in a set of housing building blocks (Toy/Marble/Wood/Brick/Cobblestone small floor, pillar and wall) whose names are adjacent in the client text; the set is also sold in the store at 5-20 coins", "source": "locale:148416 through locale:148426; repo stores.json:12156-12185"},
  {"claim": "Wiki Snow Days housing page lists a 'Snow Days [Small] [Pillar]' set piece, showing small pillars were sold as housing building-block sets; no wiki page names this Toy item", "source": "lookup wiki page Snow Days (not a direct source for this item)"}],
 "confidence": 0.6,
 "open": ["Vendor NPC and zone for the coin store row are not named in our data; the category 4 label was not resolved, so the vendor is unconfirmed.",
  "No wiki page, image, article or video names Toy Small Pillar; no quest reward, drop, event or prize-wheel source found.",
  "Retirement status unknown: no source states whether it was removed or still sold.",
  "Live status is 'yes' only from the coin store row (and the first-pass guess); it is not confirmed by a wiki or article.",
  "The first-pass guess 'vendor' is consistent with the store row, but the price is from our store data, not a wiki price, so no sale-price comparison exists."]}
