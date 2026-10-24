<!-- fleet job=citem-infer id=cninja-s-necklace-of-bark-skin-iv-131127-v2 status=done turns=3 usd=0.0046 tokens(read,write,in,out)=[20771, 22408, 8, 3260] model=claude-haiku-5-5 -->
# Ninja's Necklace of Bark Skin IV

{"item": {"name": "Ninja's Necklace of Bark Skin IV", "locale_id": 131127, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Striking Cheetah (human Ninja Job merchant)", "where": "northernmost Blackspore Swamp", "price": "1504 coins (reference; member price 1353 coins; sell-back 150 coins). Reconstructed legacy reference, not a captured in-game quote", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:17350 (item 75383, price_provenance kind reconstructed); repo:prototype/osfr-tools/data/content/vendors.json:7070-7110 (stock_source: wiki Striking Cheetah, section Sells, revision 2023-11-18, listed_as this name); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md row 97 (Striking Cheetah, Kanja Ninja set stock, wiki-only). The Striking Cheetah wiki page itself was not re-read in this pass, and its snippet did not show the necklace line."},
  {"type": "prize_wheel", "detail": "[Ninja] Prize Wheel at wiki mission pages Shady Smugglers!, Stealthy Despoilers, Bandit Hideout!, Briar Patch (also listed alongside Battle Item Mystery Pack)", "where": "Shady Smugglers!, Stealthy Despoilers, Bandit Hideout!, Briar Patch (Blackspore/Mire area dungeons and missions)", "price": null, "currency": null, "source": "wiki pages 'Shady Smugglers!', 'Stealthy Despoilers', 'Bandit Hideout!' (lookup wiki: '[Ninja] [Prize] [Wheel]' lists '[Ninja]'s Necklace of [Bark] [Skin] IV'); notes/Build Guides/Content/Dungeons/Stealthy Despoilers.md:71 (Ninja row); notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md:102 ('Briar Patch and others use Necklaces of Bark Skin IV')"},
  {"type": "other", "detail": "Mission/dungeon reward rows (Ninja class rewards per dungeon, Battle Item Mystery Pack alongside)", "where": "Stealthy Despoilers (Ninja row), Shady Smugglers!, Bandit Hideout!", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Stealthy Despoilers.md:71; wiki pages named above"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131127 is exactly \"Ninja's Necklace of Bark Skin IV\"; sibling tiers I-V and Vitality/Regeneration sit in locale 131122-131132", "source": "locale:131127; client cluster in pack"},
  {"claim": "Coin store item 75383 with purchase 1504, member 1353, sell 150, provenance reconstructed from legacy reference", "source": "repo:prototype/osfr-tools/data/content/stores.json:17350"},
  {"claim": "Vendor mapping cites wiki Striking Cheetah Sells with this exact name, revision 2023-11-18", "source": "repo:prototype/osfr-tools/data/content/vendors.json:7070-7094"},
  {"claim": "Blackspore notes list Striking Cheetah as a Ninja Job merchant (27 Aug 2013), stock Kanja Ninja set and Jagged Scythes, not this necklace in the note row", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:97"},
  {"claim": "Wiki Ninja Prize Wheel rows on several mission pages include this necklace alongside Battle Item Mystery Pack", "source": "lookup wiki: 'Shady Smugglers!', 'Stealthy Despoilers', 'Bandit Hideout!'"},
  {"claim": "Archer, Brawler, Medic, Warrior and Wizard Bark Skin IV necklaces also exist as sibling variants, so the 'Ninja' name is one of six job variants", "source": "repo:prototype/osfr-tools/data/content/vendors.json (Archer/Brawler/Warrior at 1394, 2014, 3254); locale strings"}
 ],
 "confidence": 0.5,
 "open": [
  "The Striking Cheetah vendor link rests on vendors.json's citation of the wiki Sells section; the wiki page was not re-read and the necklace line was not seen in the snippet. Treat as cited, not re-verified.",
  "1504/1353/150 coins are a reconstructed legacy reference from stores.json, not a captured NPC or wiki price. Do not treat as a confirmed Striking Cheetah price.",
  "The wiki mission pages show 8/16/26/32/60/80 'Coins' figures next to the prize wheel rows; the meaning (spin cost, reward value, or other) is not established by the snippets, so no price is assigned to the wheel source.",
  "Retired or live status is not established. The last dated evidence is the 2023-11-18 wiki revision; no source shows removal. Live is marked unsure.",
  "Exact wheel mechanism (wheel spin vs Battle Item Mystery Pack vs direct mission reward) is not shown in the snippets.",
  "Slot 8 and class 2 are from the client definition and were not checked against the wiki.",
  "The prior answer's claim that no wiki prize-wheel or event source exists was wrong; the wiki prize-wheel sources above are added."
 ]}
