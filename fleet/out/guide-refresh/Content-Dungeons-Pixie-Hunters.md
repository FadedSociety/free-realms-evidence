<!-- fleet job=guide-refresh id=Content-Dungeons-Pixie-Hunters status=nothing_found turns=13 usd=0.0177 tokens(read,write,in,out)=[371927, 62963, 28, 12174] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Pixie Hunters.md

**Verdict:** current. I found no claim in `Pixie Hunters.md` that is false at the tip, and no citation that has moved. The note makes no claim about our server code, so the code checks were for consistency only.

**Corrections:** none.

**Checks that held:**
- Locale strings. The client text checks out for `loc 3465291836`, `3041464716`, `3611613118`, `469484404`, `2561540889`, `1666491557`, `1025611698`, `3444465588`, `129771388`, `3368843201`, `3919267900`, `1163175640`, `1922873446`, `695744272`, `2180850741`, `1479963776`, `4064549042`, `3705311519`, `3070263815`, `2664870581`, `204699500`, `631483049`, `903513980`, `3307692916`, `2173006625`, `2240935617`, `1028588083`, `3250915691` and `3407142357`. The "Mysterious pillars" string `3070263815` is the Den of Secrets bonus, as the Conflicts section says (`notes/Build Guides/Content/Dungeons/Den of Secrets.md:37`).
- No "Win Combat Encounter Pixie Hunters" string exists in the locale. The "Win Combat Encounter" family covers other battles, and no Pixie-specific bonus string turned up. This supports the Achievement and Goals rows.
- Server data agrees with the Requirements table. `prototype/osfr-tools/data/content/field_battles.json:1282` has `required_combat_level: 0` for battle 12311. `prototype/osfr-tools/data/content/dungeons/pixie_hunters.json:106-140` records no minimum combat job level and a recommended player level of 3, which matches "None (recommended 3 and higher)".
- Server data agrees with the Enemies row. The roster is two Fairy Cultists (930010) and one Cruel Fairy Cultist (930056) (`field_battles.json:1299-1347`).

**Unsure:**
- **Entrance.** The note says the entrance is a Mysterious Pillar (wiki and video). The server marker for battle 12311 is a visible Fairy Cultist actor at Merry Vale `[-888, -33.5, -376]`, not a pillar (`field_battles.json:1290-1293`, `1369`). `notes/Autopilot/T103.md:82-84` says the pillar visual is unresolved. The note's claim is about the original game, so I left it alone.
- **Cruel Fairy Cultist.** The note says whether the Cruel variant is used "here" is not shown. Our shipped battle 12311 uses one as a reconstructed roster member (`field_battles.json:1320-1331`, `1365`). The original game's use is still unknown, so the claim holds as written.
- **Missing status.** The note does not say that the server ships this battle as field battle 12311, built under T103 and later F136/F138 (`notes/Autopilot/T103.md:5-34`). It is not false, so it is not a correction. A builder may want it added.
- **Coin figure.** Our shipped battle pays 25 coins (`field_battles.json:1349`). The Gaps section correctly calls the wiki's 6 coins and 86 stars unverified, and it does not mention the 25.
