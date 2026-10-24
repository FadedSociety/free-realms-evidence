<!-- fleet job=citem-infer id=cpet-cat-shorthair-plain-white-75158-v4 status=nothing_found turns=3 usd=0.0027 tokens(read,write,in,out)=[16388, 12263, 8, 1954] model=claude-haiku-5-5 -->
# Pet: Cat: Shorthair: plain_white

{"item": {"name": "Pet: Cat: Shorthair: plain_white", "locale_id": 75158, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 24008 maps to locale 75158 'Pet: Cat: Shorthair: plain_white', model cat_shorthair.adr, one definition, slot 0, class 0", "source": "locale:75158"},
  {"claim": "The only price data is a stores.json row for item 24008: purchase 540, member 486, sell 54, tint_group 2, tags L1,L2,L4,R2,T633,R1, with no price_provenance and no no_sale flag. This is the same default block as unrelated rows 23997, 23998, 24000, 24003 and 24010, so it is generic legacy data, not a checked sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6874-6888 (esp. 6885)"},
  {"claim": "Sibling cat tints 24001 (Roxie) and 24009 (Mr. Kitty) were cleared off coins: no_sale true, legacy 540 cost removed, 'no coin vendor stocks the item', re-priced to Station Cash (225 SC and 400 SC) from wiki pages. 24008 has no such provenance.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6878, 6886"},
  {"claim": "Pets notes say the client ships no pet price table; prices live only in store data. Pet routes listed there include Marketplace (Station Cash), Pet Adoption Centers, Mysterious Merchant, trading cards, Daily Wheel and limited events.", "source": "repo:notes/Build Guides/Gameplay/Pets.md lines 27, 100, 217, 220"},
  {"claim": "Wiki Pets category covers short-hair cats Milo (Cragara, Mysterious Merchant), Koko, Kiri (Mysterious Merchant) and Mittens (SC Marketplace). None is named plain_white.", "source": "wiki Pets category (ns0 Pets: Milo, Koko, Kiri, Mittens) as cited in the pack"},
  {"claim": "Lookup finds no wiki page, video frame or article naming plain_white for either shorthair or longhair. The only other client hit is the longhair sibling locale 75194 'Pet: Cat: Longhair: plain_white'.", "source": "lookup (wiki, client, video) for 'plain white cat pet'; locale:75194"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced acquisition source. The 540-coin row (stores.json line 6885) is a generic default block with no vendor, stock list, wiki page or video behind it, so it is not listed as a coin_shop source. Its sibling tints were explicitly cleared off coins, which contradicts a live coin sale.",
  "Possible routes not evidenced for this tint: Marketplace (Station Cash), Mysterious Merchant, Pet Adoption Centers (Buy Pet). Each needs a wiki page or vendor stock naming plain_white before listing.",
  "Live status and retirement are unknown. The first-pass 'live: yes' has no backing evidence.",
  "The previous answer's 'Coin Shop (no zone or vendor)' source and the first-pass 'source_guess: vendor' should both be dropped unless a stock row or wiki page is found."
 ]}
