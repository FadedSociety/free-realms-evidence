<!-- fleet job=citem-infer id=csmart-solid-ant-40772-v1 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[22430, 9774, 10, 1761] model=claude-haiku-5-5 -->
# Smart Solid Ant

{"item": {"name": "Smart Solid Ant", "locale_id": 40772, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 3556 names the item 'Smart Solid Ant' (locale 40772) with the description 'This item can be added to the Solid Ants Collection'.", "source": "locale:40772; locale:132330 (ui 'Solid Ants Collection', same description line)"},
  {"claim": "The wiki 'List of Collections' page includes a '[Solid] [Ants]' collection, alongside the Spotted and Striped ant collections, so the Solid Ants Collection exists as a live-listed collection.", "source": "wiki: List of Collections"},
  {"claim": "The item sits in a cluster of eleven ant strings (40767-40777: Spotted, Solid ant variants and King/Queen forms) that appear to be the one set's members.", "source": "client text table, locale:40767-40777"},
  {"claim": "The collection's description line 'A collection of solid-bodied ants.' is client text for the collection objective.", "source": "locale:7798"}
 ],
 "confidence": 0.3,
 "open": [
  "No source found for how a player obtains Smart Solid Ant: no vendor stock, store price (coin_store_prices is empty), quest reward, drop, event, prize wheel, or crafting evidence in the pack or in repo/wiki/article searches. Left unsourced rather than guessed.",
  "The name string 40772 is tagged 'npc_name' in the client text table, not 'item'. The cluster strings are also tagged npc_name, so the ants may be creature/NPC-style entries used by a collection rather than inventory items. Confirm the item class before treating it as a purchasable item (class_ids [0], slots [0], no models).",
  "The wiki List of Collections names the Solid collection only as '[Solid] [Ants]' and gives no member list or reward, so membership of 'Smart Solid Ant' in that collection is confirmed only by the client description, not by a wiki page.",
  "Live status is unconfirmed: the first-pass 'live: yes' is a hint only, and no wiki page, article, or video covers this item or the Solid Ants collection reward.",
  "No video frames or article facts name the item."
 ]}
