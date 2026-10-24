<!-- fleet job=note-refresh id=Native-Combat-Controls status=nothing_found turns=11 usd=0.0110 tokens(read,write,in,out)=[221155, 36889, 24, 8270] model=claude-haiku-5-5 -->
# notes/Research/Native Combat Controls.md

**Verdict:** current. Every checkable claim about the code at the tip still holds. The note is almost entirely about the preserved original executable and original Lua, and the repo's own references to it agree with it.

**Corrections:** none.

Checked and confirmed:
- **Dispatch chain** (`client_sql` fn table): `00b02880` calls `00a2ac20` and `0093bff0`; `00a2ac20`'s only caller is `00b02880`. `008a7eb0` calls `008a5850` first, then `008a7e40` with mode 4, 3, 2 or 1. `008a7e40` callees are `009aaeb0`, `009b6590`, `009cf430` and `00a12840`. `009cf430` calls `00a36a70`.
- **Flash-type predicate** `008a5850`: types 3, 6–9, 14–16, 22–23 and 1009 return 1, matching the note and `Build Guides/Gameplay/Minigame Framework.md`.
- **Tab selector** `00a2ac20` references `+0x178` (disposition) and `+0x6f8` (dead flag). `008c6c10` is its store-target callee.
- **Lua** (`ui:ScriptsBase.lua:30481-30488`): `activateAbility` calls `Ui.ClickedAbility(b, 3)`, `Fishing:ClickedAbility(b)`, or `Ui.ClickedAbility(b)`. `BaseClient.ClosestInteractionTargetData` is at 43501, and `Ui.DoClosestInteraction()` is at 43539–43540.
- **Cursors** (`client:Resources/Cursors.txt:3,7`): `1^cursor_interaction_combat^` and `5^cursor_talk^` match.
- **Repo cross-references:** `Build Guides/Gameplay/Combat and Abilities.md` (lines 57, 68, 157) and the `S0220`/`S0292`/`game.actionbar` maps cite this note and agree with its addresses and routing. `Reviews/Native Basic Attack Controls 083946.md` (MiniGameType4 at byte 67, ZoneContext8 at byte 28) is consistent with the field correction. `MODLOG.md:230` agrees with it too.

**Unsure:**
- `lab/reports/extract-native-combat-controls.py`, the "48 records" count, the "14 functions" count, and the `native-combat-controls.c/.json` outputs. The repo's `.gitignore` excludes `/lab/` (line 28, "lab data lives in the sibling ../lab"), so I could not check these from the tip. Tests and `scripts/pieces/piece_053.py` do reference `lab/reports/native-combat-controls.json`, so the output file is expected to exist outside the repo.
- The serializer field claim (ZoneContext at the cave details' first value8, MiniGameType as the last1 of `[title,-1,description,1,profile,1]`). The pinned community serializer is outside `repo`, so I could not verify it.
- The owner `gateway_oracle` is named in the note but does not appear anywhere in the repo or briefs, so I could not verify its investigation status.
- "Repeated X can keep reopening Darkthorne" and the claim that the closest-target ranking is not inferred. These describe runtime behaviour, which I cannot check statically.
