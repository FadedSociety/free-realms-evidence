<!-- fleet job=citem-infer id=csolid-dreadful-triangle-shard-69796-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5411, 8467, 6, 1963] model=claude-haiku-5-5 -->
# Solid Dreadful Triangle Shard

{"item": {"name": "Solid Dreadful Triangle Shard", "locale_id": 69796, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, category 121, unresolved vendor (no NPC or location named in the store data)", "where": null, "price": "1656 coins (member price 1490 coins, 10% member discount; sell price 165 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 22894 (line 6749); repo:data/content/stores.json item 22905 (line 6760)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 69796 is 'Solid Dreadful Triangle Shard' with empty description; definitions 22894 and 22905 share it.", "source": "locale:69796"},
  {"claim": "Store rows for definitions 22894 and 22905 are both category 121, 1656 coins, member 1490, sell 165, source tags L1, L2, L4, R2, T633, R1. Binding to locale 69796 is by definition id and client name only.", "source": "repo:data/content/stores.json item 22894; item 22905"},
  {"claim": "Posy's/Peep's Missing Bowl (Uncle Irving, Farnum Farmstead) rewards 1 Shimmering Air Triangle Shard (locale 96329), not Solid Dreadful. The quest binding in repo is to Shimmering Air only.", "source": "video:3JXpHghLOTs/00014; repo:prototype/osfr-tools/data/content/quests/adventurer.json:1451; notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md:135"},
  {"claim": "Triangle Shard tiers are job-gear accessory parts (Postman, Fisherman, Soccer Star job tier sets), so this shard is likely a job-tier component; no source confirms its use.", "source": "notes/Build Guides/Content/Jobs/Postman.md:226-228; notes/Build Guides/Content/Jobs/Fisherman.md:291"},
  {"claim": "No wiki page, article fact, video frame or enemy-drop record names this variant; lookup returns only the client name line.", "source": "lookup (client, wiki, articles, video) for 'Solid Dreadful Triangle Shard'"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor for the 1656-coin listing (definitions 22894/22905, category 121) is unidentified; the category is not resolved in repo data, so no NPC or location is stated.",
  "The Posy's Missing Bowl quest reward was removed as a source: it names only Shimmering Air Triangle Shard, not this variant.",
  "Whether the 1656-coin price applies to the other ten Triangle Shard tiers (69791-69801) is unchecked; only 22894 and 22905 were examined.",
  "Kind is 'other' rather than 'card' (first pass): the client gives slot 12 and class 50 only, and the item's use (job accessory component, collection, or card) is unconfirmed.",
  "Whether the Shard is still sold or was retired is unknown; no retirement source found."
 ]}
