<!-- fleet job=note-refresh id=Opening-Journal-Reconstructed-Labels status=done turns=9 usd=0.0125 tokens(read,write,in,out)=[202528, 51727, 20, 7952] model=claude-haiku-5-5 -->
# notes/Research/Opening Journal Reconstructed Labels.md

**Verdict:** Code-level claims are current. The acceptance-status claims are badly stale: the note says native rendering and both UI repairs are still pending, but later native runs accepted them.

**Checked and holding (no change):** `OpeningJournal` reads optional `journal-text.json`, binds it to the opening hash, rejects source/ID mismatches and incomplete zero-ID coverage, and substitutes only the name/description IDs in full-self and Add records (`repo:prototype/osfr-tools/src/opening_journal.rs:97-171`, `:489-497`). Live 49/9+10 keys still use `goal.id` (`opening_journal.rs:356-358`). Missing presentation file gives an empty map, so the original serializer runs (`opening_journal.rs:97-101`). `prepare-journal-text.py` uses pinned `ba2ede225...` and the community writer, and `run-local-baseline.py` takes `--journal-text` and `--character-select-title` with the required `--native-login` (`scripts/prepare-journal-text.py:16`, `scripts/run-local-baseline.py:42-43`, `:63-66`). Both fixed locale files are validated before the copy, and the apply step rejects an active run (`scripts/journal_text_overlay.py:110-126`). The 23-case preflight count is consistent with `scripts/check-journal-text-overlay.py:34-102`.

**Corrections:**

1. `old:` **Native rendering remains pending.**
   `new:` **Native rendering is accepted** in run162238: an independent viewer saw the readable reconstructed Chef/equipment/Rainleaf/Gummyfruit labels with five restored green goals.
   `why:` `repo:notes/Reviews/Journal Text Overlay v2.md:17` ("This display gate is now accepted"); `repo:notes/Tasks.md:31,82`; `repo:MODLOG.md:305`.

2. `old:` Native acceptance is pending.
   `new:` Native acceptance is done: the saved character name was verified in run164218 and the readable journal labels in run162238.
   `why:` `repo:notes/Tasks.md:31` ("Verify the paired journal locale and character-selection title options in native162238/164218 … saved name preserve the current campaign hash"); `repo:notes/Research/Opening Journal Reconstructed Labels.md:47` is the sentence this replaces.

3. `old:` Do not claim either UI repair accepted until those actual-client checks pass.
   `new:` Both UI repairs are accepted (run162238 for the journal labels, run164218 for the character name). Run162238 emitted no incremental 49 packets, so the live-key behaviour rests on run154503 (`notes/Reviews/Journal Text Overlay v2.md:17`).
   `why:` `repo:notes/Reviews/Journal Text Overlay v2.md:17`; `repo:notes/Tasks.md:31`. The "Next native acceptance" sentence in the note's last paragraph is historical now.

**Unsure:**
- The counts 113286 stock entries, 85932 IDs, 28 additions, IDs 619–1236, 51 goals, 24 labelled objectives (14 zero-ID, 4 ingredient, 3 fire, 3 artifact) and 17 records. The code asserts these (`scripts/journal_text_overlay.py:66,89`; `scripts/prepare-journal-text.py:109-122`) and the review repeats them, but I could not open the `lab/` data to recount.
- "Its original renderer used `_id` for title; JPEXS changes the single operand to `_name`" and the 56/55 script comparison. The harness checks the proof file (`scripts/journal_text_overlay.py:154-156`), but I did not check the renderer bytes.
- "Locale8 is en_US" and the `00e8e360` / `00e861e0` native paths. The first is consistent with `locale` = 8 in the code. The second matches the existing entry in `notes/Build Guides/Client Engine/UI Framework (GFC and XML).md:56`, but I did not inspect the client directly.
