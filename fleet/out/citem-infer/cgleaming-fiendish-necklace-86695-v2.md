<!-- fleet job=citem-infer id=cgleaming-fiendish-necklace-86695-v2 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[5447, 6409, 6, 1705] model=claude-haiku-5-5 -->
# Gleaming Fiendish Necklace

{"item": {"name": "Gleaming Fiendish Necklace", "locale_id": 86695, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Gleaming Fiendish Necklace' (definition_id 22704, slot 8, class 50, no coin store price). Description: menacing necklace of haunted silver that increases Health regeneration for any Combat Job.", "source": "locale:86695; pack client_definition"},
  {"claim": "It sits in a family of 'Gleaming <Adjective> Necklace' names: 86684 Dreadful, 86685 Fateful, 86686 Infernal, 86687 Spectral, 86688 Mystical, 86689 Phantasmal, 86690 Eternal, 86691 Celestial, 86692 Ethereal, 86693 Unearthly, 86694 Cosmic, 86696 Corporeal; also 96216-96221 (Ocean, Jungle, Grape, Honey, Ruby, Pumpkin), 96547 (Fire), 96550-96551 (Sun, Light), 96559-96561 (Air, Wind, Void).", "source": "locale:86684-86696, locale:96216-96221, locale:96547, locale:96550, locale:96551, locale:96559-96561"},
  {"claim": "Chaz's necklace variants in the client are Fateful, Infernal, Spectral and Mystical only (no Fiendish variant).", "source": "locale:86697-86700"},
  {"claim": "Placeholder stub lines 'This is a Gleaming ... necklace item.' exist for Dreadful, Fateful, Infernal, Spectral and Mystical (150426-150430). None exists for Fiendish, and these stubs are placeholder text, not live evidence.", "source": "locale:150426-150430"},
  {"claim": "A full-text lookup and a repo-wide search for 'Gleaming', 'Fiendish' and 22704 found no wiki page, article, video frame, vendor stock, quest, drop, or event naming this item. The repo search returned no matches.", "source": "lookup (client, locale:86695 only); search repo: no matches"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found: no coin store price (no stores.json entry for 22704), no vendor stock, no quest reward, no drop, no event, no wiki or video mention. The first-pass 'drop' guess is unsupported and not used.",
  "Live status and retirement are unknown. The client defines the item, but no source says whether it is obtainable now or was retired.",
  "Critique fixes applied: removed the citation to repo:quest-lines/citem-nofind.json (no Gleaming/Fiendish matches in repo); removed the 'Chaz's Fiendish Necklace' variant claim; removed the flags.json claim (no Gleaming entries in repo); marked the FreeRealms-Legacy/Lxzxrus ClientItemDefinitions.json comment as unverified, since I did not confirm it in refs and it is a code comment, not source data; ring-family claim (locale:86460) dropped as unverified.",
  "Next step: check the refs roots (FreeRealms-Legacy, Sanctuary) and the wiki for 'Chaz' or 'Gleaming' necklace sets to find the NPC or event that gave the set. The Chaz quest links are the most likely lead."
 ]}
