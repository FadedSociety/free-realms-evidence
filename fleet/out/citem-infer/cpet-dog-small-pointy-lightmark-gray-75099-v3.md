<!-- fleet job=citem-infer id=cpet-dog-small-pointy-lightmark-gray-75099-v3 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[5991, 15272, 6, 1918] model=claude-haiku-5-5 -->
# Pet: Dog: Small Pointy: lightmark-gray

{"item": {"name": "Pet: Dog: Small Pointy: lightmark-gray", "locale_id": 75099, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines this pet as definition 23949, name locale:75099, model dog_small_pointy.adr, slot 0, class 0", "source": "client definition in evidence pack; locale:75099"},
  {"claim": "Store row for item 23949 reads purchase 540, member 486 (10% discount), sell 54, with source tags L1, L2, L4, R2, T633, R1. The R1 tag marks the 540 as a defaulted value, not a checked price.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6826"},
  {"claim": "The 540 figure is the legacy ClientItemDefinitions Cost field used as a starting coin price; the research note says it is unchecked against a real client transaction.", "source": "repo:notes/Research/Coin Shop.md line 33"},
  {"claim": "Row 23949 has the same 540/486/54 values and tag set as its neighbours 23938-23958, apart from the rows cleared to Station Cash (23941, 23943, 23957). The value is a block default, not an item-specific price.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6815-6835"},
  {"claim": "The sibling rows 23941, 23943 and 23957 were cleared from the coin price because no coin vendor stocks them and they sell for Station Cash on the SC Marketplace (Hurricane 400 SC, Scooter 400 SC, Echo 225 SC).", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6818, 6820, 6834 (T638)"},
  {"claim": "The client's Dog pet cluster locale:75085-75104 is a set of Small Pointy and Floppy/Fluffy tints; the lookup found no wiki page, article, video frame, or quest/drop answer that names 23949 or locale:75099.", "source": "lookup of client, wiki, articles, video; repo:quest-lines/flags.tsv lines 7670-7675 (variant names)"},
  {"claim": "The coin_store_prices [540] in the client definition pack entry is not independent support: the pack says it is taken from our store data, and that data is the defaulted block value above.", "source": "evidence pack client_definition; repo:stores.json line 6826"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. The only candidate is a coin-store price of 540 coins (member 486, sell 54), which is a defaulted legacy Cost value (R1) shared by roughly every neighbouring row. It is not a confirmed vendor sale, so it is left out of sources. Needed: a vendor stock record, a wiki or forum price, or a quest/drop/event source for definition 23949 / locale:75099.",
  "Liveness is unknown. The client defines the item, but no source shows it is sold now or was removed. Retired is null.",
  "Not wireable: acquisition cannot be set from this pack. Earlier answer's coin_shop source (vendor null, 540 coins) is withdrawn, as both critiques found it rests on a defaulted value.",
  "The price pattern does not establish this tint's vendor. Other Small Pointy tints (75085-75104) were not checked individually for sources."
 ]}
