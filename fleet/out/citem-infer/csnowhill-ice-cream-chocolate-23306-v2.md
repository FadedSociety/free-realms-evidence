<!-- fleet job=citem-infer id=csnowhill-ice-cream-chocolate-23306-v2 status=done turns=3 usd=0.0018 tokens(read,write,in,out)=[12704, 6955, 8, 1570] model=claude-haiku-5-5 -->
# Snowhill Ice Cream: Chocolate

{"item": {"name": "Snowhill Ice Cream: Chocolate", "locale_id": 23306, "kind": "consumable"},
 "sources": [
  {"type": "vendor", "detail": "Razzle the Robgoblin, Coin Shop purchase (Sweets for Sniffles quest step: buy one Snowhill Ice Cream: Chocolate; Marzipan then takes it for the taste test)", "where": "Coin Shop (Razzle the Robgoblin; zone not named in the evidence)", "price": "12", "currency": "coins", "source": "wiki page Quest:Sweets for Sniffles ('Go buy some from Razzle the Robgoblin'; 'Purchase one Snowhill Ice Cream: Chocolate from the Coin Shop'); client coin_store_prices = 12 for definition 2896 (locale:23306); video:ukTXIyG6EKI/00006.jpg store listing shows 'Snowhill Ice Cream: C... 12 coins'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Wiki quest Sweets for Sniffles says to buy Chocolate Ice Cream from the Coin Shop, from Razzle the Robgoblin, then deliver to Marzipan (Skysong Ledge, Pony Vale).", "source": "wiki page Quest:Sweets for Sniffles"},
  {"claim": "Client definition: locale:23306, definition id 2896, coin_store_prices 12.", "source": "client definition (pack); locale:23306"},
  {"claim": "Store listing frame shows Snowhill Ice Cream: Chocolate at 12 coins.", "source": "video:ukTXIyG6EKI/00006.jpg"},
  {"claim": "Chocolate flavour is an ingredient in the Chef recipe Moonbean Sundae (x3). This is a use, not a source.", "source": "wiki page List of Recipes (Chef)"}
 ],
 "confidence": 0.8,
 "open": [
  "Price 12 coins is the client coin_store_prices value and the store frame; the repo stores.json row for item 2896 could not be re-read here (search returned no match for \"2896\" in stores.json). The critique reports its price_provenance as 'reconstructed', so do not treat it as independent confirmation.",
  "Retirement status and whether Razzle still sells it are unknown; no later-removal source was found.",
  "Zone for Razzle's Coin Shop stop is not named in the evidence.",
  "The previous answer's 'ingredient/cooking vendor stock' label was dropped: no evidence names it."
 ]}
