<!-- fleet job=citem-infer id=cfaintly-glowing-blue-flair-shard-386226-v4 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[6707, 14782, 6, 1675] model=claude-haiku-5-5 -->
# Faintly Glowing Blue Flair Shard

{"item": {"name": "Faintly Glowing Blue Flair Shard", "locale_id": 386226, "kind": "other"},
 "sources": [
  {"type": "quest_reward", "detail": "Completion of the quest \"You Can't Steal What's Already Yours\" (reward item not named in client quest text; quest giver unconfirmed)", "where": "Robgoblin camp near the Snowhill Warpstone (objective location only, not confirmed as giver location)", "price": null, "currency": null, "source": "wiki page \"Faintly Glowing Blue Flair Shard\" (acquired by completing the quest); quest title locale:77573; objectives locale:77574, 77580, 77581, 77582; completion dialog locale:77575 (\"Take this for your troubles\", names no item)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item 55354 is named Faintly Glowing Blue Flair Shard, slot 13, class 69, one definition; description says it places a blue glow effect on the weapon", "source": "locale:386226; client definition (definition_ids [55354])"},
  {"claim": "Wiki says the shard is a level 1 flair shard usable in any job, acquired by completing the quest You Can't Steal What's Already Yours, Cannot Trade, categories Flair Shard and Quest Flair", "source": "wiki page \"Faintly Glowing Blue Flair Shard\""},
  {"claim": "Tooltip shows Resell Value 89, Cannot Trade, Required Level 1 Any Job", "source": "image:item_tooltip (wiki file Faintly Glowing Blue Flair Shard item.jpg)"},
  {"claim": "Completion dialog says a reward is given but does not name the shard", "source": "locale:77575"},
  {"claim": "Repo search for 55354 / Flair Shard / quest name found no quest-reward table entry or vendor row naming this shard beyond the store data row", "source": "search repo (no hit under data/content quest tables)"}
 ],
 "confidence": 0.4,
 "open": [
  "Quest reward rests on the wiki sentence alone. No quest-reward table entry for item 55354 was found, and locale:77575 does not name the item. Wiki-sourced; reward item unconfirmed in client data.",
  "Quest giver unknown; the Robgoblin camp is the objective location, not a confirmed giver location.",
  "Unresolved price conflict: stores.json item 55354 (repo:prototype/osfr-tools/data/content/stores.json:13843) and the client definition (coin_store_prices [890]) list purchase 890 / member 801 / sell 89 with no provenance, NPC, zone or wiki Coin Shop listing. The wiki says Cannot Trade and quest-only, and the 89 matches the tooltip's Resell Value, not a purchase price. Not listed as a source. Kept here so it is not silently dropped; needs a coin-vendor check before any coin price is wired. Sibling rows 55350-55353 show 270 with the same missing provenance.",
  "Live status unsure: wiki category Quest Flair and Cannot Trade are the only status signals and neither establishes current availability. No source states retired or still sold.",
  "locale:386222 (\"You have all saved the forest...\") sits in the same client cluster and may point to a Forest-event reward for the Flair Shard family; unverified, not listed as a source. Check that event's reward table."
 ]}
