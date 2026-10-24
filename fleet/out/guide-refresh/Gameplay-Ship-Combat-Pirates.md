<!-- fleet job=guide-refresh id=Gameplay-Ship-Combat-Pirates status=nothing_found turns=17 usd=0.0204 tokens(read,write,in,out)=[628294, 67343, 36, 11307] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Ship Combat (Pirates).md

**Verdict:** current. Every checkable claim I tested matches the tip. No corrections.

**What I checked:**
- **Header counts.** "309 accepted functions: 66 confirmed, 73 likely, 96 speculative, 74 unknown", "Network-linked (`wire`): 7", and "Subsystems: `minigame.shipcombat` (291), `net.pirates` (18)". The `label` table gives minigame.shipcombat confirmed 61 / likely 66 / speculative 95 / unknown 69 (= 291) and net.pirates 5 / 7 / 1 / 5 (= 18). Totals are 66 / 73 / 96 / 74, all `accepted`. The `wire` labels are exactly the seven 🌐 rows in the note (00ca7480, 00a69480, 00a653c0, 00a65460, 00a665e0, 00a65780, 00a67110). The per-class subtotals (12, 1, 1, 7, 5, 5, 5, 6, 12, 2, 6, 3, 4, 1, 1, 2, 1, 5, 2, and 210 for "(no class)") sum to 291. The shard-source counts sum to 309.
- **Row addresses, names and confidence.** About 90 rows, sampled across all sections, match `fn`/`label` for address, name and confidence. Samples include ControllerShip::Ctor, ShipCombatProcessor_VSlot1, the ShipCombatCannonConfigDtor at 00a62030, the CreateProxiedStructure dtor at 00a620d0 (unknown), HandleCameraConfig, the pickup, jet-stream and zone config loaders (confirmed), and the net.pirates readers and ctors.
- **Build Guides.md:22** ("309 functions (66 confirmed, 73 likely)") agrees with the note.

**Unsure:**
- The "What it does" prose for individual rows is client decompilation. I spot-checked it against the label records but did not re-derive it from the pseudocode.
- The shard links at the bottom (`[[S0298 …]]` through `[[S0581]]`) point to shard notes that are not in `notes/Research` or the top-level notes folder. I did not find them, so I could not confirm the link targets.
- The "How it works" section is a placeholder ("Not written yet"). That is accurate, so I left it alone.
- The note makes no claim about our Rust server (`prototype/osfr-tools`), and I found no ship-combat server code. The Build Ledger says "ship combat | Researched | none", which is consistent with that.
