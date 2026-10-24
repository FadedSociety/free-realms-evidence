<!-- fleet job=citem-infer id=cfluffy-cloud-3-31506-v2 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[14392, 10451, 8, 2246] model=claude-haiku-5-5 -->
# Fluffy Cloud (3)

{"item": {"name": "Fluffy Cloud (3)", "locale_id": 31506, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, category 147, tint group 1 (definition 14303) and tint groups for definitions 15497-15504; no vendor or shop is named in the store data", "where": "Coin store, category 147 (no named vendor)", "price": "50 coins (member price 45 coins, 10% member discount); no_sale true (not resellable)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3785 (item 14303) and lines 3956-3963 (items 15497-15504)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 31506 is 'Fluffy Cloud (3)', description 'Weather reports predict fluffy clouds.', 10 definitions, slot 0, class 0, models hsg_cloud_01.adr / hsg_fluffy_cloud_01.adr / hsg_fluffy_cloud_02.adr", "source": "locale:31506"},
  {"claim": "stores.json item 14303 is category 147, purchase 50 coins, member 45, no_sale true (re-checked this session)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3785"},
  {"claim": "stores.json item 16898 is category 147, tint group 2, 500 coins, member 450, sell-back 50, no_sale false; sibling rows 16895, 16899 share the same pattern. Nothing ties 16898 to locale 31506.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 4261; lines 4258, 4262"},
  {"claim": "Wiki Items list and Quest:Rob Robbie Daily list a '[Fluffy] [Cloud]' entry; these are name-only leads with no price or record id, so they are not counted as sources", "source": "wiki: Items; Quest:Rob Robbie Daily"},
  {"claim": "Article says '[Fluffy] [Cloud] Bridge' was added as a housing item (a sibling item, not this record)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1521"}
 ],
 "confidence": 0.4,
 "open": [
  "The 500-coin row (definition 16898, stores.json line 4261) is dropped from sources: nothing ties 16898 to locale 31506, and its neighbours 16895/16899 are sibling 500-coin clouds. Confirm against the client definition table before adding it.",
  "The 50-coin source is a store listing by definition id only; no named vendor, shop, or wiki page confirms the link from these ids to the name 'Fluffy Cloud (3)'.",
  "No wiki page or article names 'Fluffy Cloud (3)'; the wiki '[Fluffy] Clouds' Items entry may be this item's wiki name but has no price.",
  "Retirement and sale dates are not established. The no_sale flag only blocks resale; it does not show removal. The rows show store-data presence, not a confirmed current sale.",
  "No quest reward, enemy drop, event, prize wheel, or crafting source found in the pack."
 ]}
