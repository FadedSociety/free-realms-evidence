<!-- fleet job=citem-infer id=cpet-dog-large-floppy-darkmark-ivory-75112-v2 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16451, 12012, 8, 2327] model=claude-haiku-5-5 -->
# Pet: Dog: Large Floppy: darkmark-ivory

{"item": {"name": "Pet: Dog: Large Floppy: darkmark-ivory", "locale_id": 75112, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store price only: the client definition carries a coin store price of 540 for this pet. No vendor stock row, wiki listing, video or article places this dog in any Coin Shop merchant's stock, so the sale itself is unconfirmed.", "where": null, "price": "540 coins (client Cost; stores.json purchase price). Member price 486 is computed arithmetic (10% member discount), not a second observed price.", "currency": "coins", "source": "locale:75112; repo:prototype/osfr-tools/data/content/stores.json item 23962; repo:notes/Research/Coin Shop.md (stores.json rows generated from the client ClientItemDefinitions Cost field; R2 member price is arithmetic)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item 23962, name locale 75112 'Pet: Dog: Large Floppy: darkmark-ivory', kind pet, one definition, model dog_large_floppy.adr, coin_store_prices 540", "source": "locale:75112; client definition pack"},
  {"claim": "The stores.json row for 23962 is a generated price table entry (client Cost field, with member price and sell-back computed), not a stock list", "source": "repo:notes/Research/Coin Shop.md lines 31-34"},
  {"claim": "Sell-back 54 is server policy (one tenth of buy price, T633), not a source of the item", "source": "repo:notes/Research/Coin Shop.md lines 38, 48-54"},
  {"claim": "Pet vendor category moved to Coin Shop merchants (general news; does not name this dog)", "source": "wiki Template:News (Weekly Update 10/29/13), as quoted in the pack"},
  {"claim": "Cobblestone Village pet vendors Jennifer and Gloria sell pet outfits and accessories; no item-level list exists for them", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Cobblestone Village.md lines 23, 68-69; repo:notes/Build Guides/Content/Jobs/Pet Trainer.md line 249"},
  {"claim": "Sibling Large Floppy dog variants sit together in the client text table (locale 75104-75117, plus 75149-75151 for solid-ivory, darkmark-tan, spots-ivory)", "source": "lookup client results; locale:75107-75117"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor stock row, wiki page, image, article or video names this dog. The coin_shop entry is a price-only fact from the client Cost field; the claim that a Coin Shop merchant sells it is unevidenced and was removed as a sale claim.",
  "The Pet Pal classification in the previous answer has no source tying this dog to Pet Pals; dropped.",
  "Jennifer and Gloria (Cobblestone Village pet vendors) are the likely pet-vendor sellers of pet items, but no per-item list links this dog to them. Gloria's wiki line 'Pet Pal related items' (rev 2013-11-16) is category-level only.",
  "Date of sale, whether it is still sold, and any retirement are unknown; no source found. Live is unsure; the first-pass 'live: yes' is not confirmed.",
  "Sibling variant prices and ids were not checked beyond the name cluster.",
  "The 540 price is the client Cost value, not a dated wiki price; any earlier vendor price is not established."
 ]}
