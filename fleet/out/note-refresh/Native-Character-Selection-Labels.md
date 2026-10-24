<!-- fleet job=note-refresh id=Native-Character-Selection-Labels status=done turns=14 usd=0.0124 tokens(read,write,in,out)=[308177, 39038, 30, 8953] model=claude-haiku-5-5 -->
# notes/Research/Native Character Selection Labels.md

**Verdict:** minor drift. One runner-path claim is false at the tip. The code-side claims I could check hold (selection layout, title-repair gates, the 23 negative cases, the `--character-select-title` requirements). The rest of the note cites private `lab/` evidence I cannot check from the repo.

**Corrections:**

1. `old:` The existing native-login runner copies `lab/references/asset-cache/client/custom` into disposable clients.
   `new:` The existing native-login runner calls `install_client_overlay` (`scripts/bundle/client_overlay.py` `install`), which copies the pinned `custom/sg_dressing_room*` files from the flat `lab/references/asset-cache/` cache into each disposable client's `custom/` folder. The `custom/` path is set per entry, not read from a cache subfolder.
   `why:` `repo:scripts/bundle/client_overlay.py:20` (CACHE = `references/asset-cache`), `:47-48` (client path `"custom/" + name` from flat cache names), `:71-81` (`install` copies `cache / name` to `root / path`); `repo:scripts/run-local-baseline.py:33`, `:83-87` (native-login branch calls `install_client_overlay(client)`). `repo:notes/Autopilot/T443.md:79-80` records that the dead `asset-cache/client/custom` branch was deleted because that folder does not exist.

**Checked and holding (no change):**
- `selection_reply` layout (status, bypass flag, entity count, GUID/server/status, length-prefixed appearance payload), and the saved creation attachments used via `appearance_payload`: `repo:prototype/osfr-tools/src/login.rs:643-680`.
- `--character-select-title` requires `--native-login`, validates hashes before run creation, applies the target after the overlay install, and refuses active runs and unrelated movies: `repo:scripts/run-local-baseline.py:65-69, 83-92`; `repo:scripts/journal_text_overlay.py:129-178`.
- "all23 negative cases": the offline preflight has 2 + 13 + 2 + 6 = 23 `rejects(...)` cases: `repo:scripts/check-journal-text-overlay.py:34-35, 48-83, 91-102`.
- The title operand: `repo:prototype/osfr-tools/..`-independent UI source `ui:character-select/scripts/__Packages/controls/CharacterItemRenderer.as:38-42` assigns `_name` from `data.name` and passes `this._id` to `frSetTextPreserveWidthV3`.
- The MODLOG entry for the title-v3 native screenshot and Go restore matches the note: `repo:MODLOG.md:295`.

**Unsure:**
- "The existing seven ordinary login tests pass." `repo:prototype/osfr-tools/tests/login.rs` has 13 `#[test]` functions (lines 78, 235, 305, 360, 412, 451, 471, 502, 540, 564, 617, 638, 665). Two are named `private_*`, which leaves 11. I found no source for a "seven" count, and I did not run the tests, so I left the sentence unchanged.
- Private evidence (`lab/reports/*`, `lab/references/character-select-title-v3`, SHA256 values, native run163518, the function00719550 log, the Cooking agent ownership) is not in the repo, so I did not verify it. The MODLOG and Combat Results review mention the same aggregate proof hash, `352ff0de…`, which is consistent with the note.
- The initial-selection claim (the first row sets ID and buttons without `SelectCharacter`) is not checked here.
