<!-- fleet job=citem-infer id=celite-human-doll-66676-v1 status=done turns=4 usd=0.0018 tokens(read,write,in,out)=[13734, 5877, 10, 1769] model=claude-haiku-5-5 -->
# Elite Human Doll

{"item": {"name": "Elite Human Doll", "locale_id": 66676, "kind": "collection"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (category 19), purchase price 10 coins; member price 9 coins (10% member discount); sell-back 1 coin. Vendor NPC/shop not named in our store data.", "where": null, "price": "10 coins (member price 9 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 23063 (prototype/osfr-tools/data/content/stores.json:6773)"},
  {"type": "collection", "detail": "Reward for completing the Human Dolls collection (part of the Free Realms [Elite] Dolls set)", "where": null, "price": null, "currency": null, "source": "Wiki page 'Toys (Collections)': '[Elite] Human Doll -- This is the reward for completing Human [Dolls]'; client locale:132387 'This item can be added to the Free Realms Elite Dolls Collection'"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item name locale 66676 is 'Elite Human Doll', description says it can be added to the Free Realms Elite Dolls Collection", "source": "locale:66676; locale:132387"},
  {"claim": "Coin store entry for item 23063 with purchase price 10 coins, member price 9 coins", "source": "repo:data/content/stores.json item 23063"},
  {"claim": "Elite Human Doll is the reward for completing the Human Dolls collection, listed under Free Realms [Elite] Dolls", "source": "Wiki page: Toys (Collections); also List of Collections (Human Dolls)"},
  {"claim": "Quest-title client text 'Free Realms Elite Dolls' groups the set", "source": "locale:67494"}
 ],
 "confidence": 0.6,
 "open": ["Coin store vendor/shop for item 23063 is not named in the store data or wiki; the 10-coin sale is taken from our store file only, with no wiki price cross-check.",
  "Wiki does not give the number or type of dolls that must be completed for the Human Dolls collection reward, nor the quest or where to turn it in.",
  "Whether the 10-coin store sale is still live or was retired is not confirmed by any dated source.",
  "The jev first pass tagged source 'collection' and live 'yes'; the store price and wiki collection reward agree with that, but the wiki line is the only source for the collection reward."]}
