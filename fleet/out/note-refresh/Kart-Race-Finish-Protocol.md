<!-- fleet job=note-refresh id=Kart-Race-Finish-Protocol status=done turns=16 usd=0.0215 tokens(read,write,in,out)=[662872, 71708, 34, 11787] model=claude-haiku-5-5 -->
# notes/Research/Kart Race Finish Protocol.md

**Verdict:** minor drift. The client-side findings hold at the tip. The one stale statement is that the server writer is still "future"; it now exists.

**Corrections:**

- `old:` `## Synthetic vectors for the future server writer`
  `new:` `## Synthetic vectors for the server writer`
  `why:` `prototype/osfr-tools/src/kart_service.rs:2693-2707` (`progress_frame`) builds the local racer's 33/14 block from `progress_template`, writing guid, `laps_completed`, `lap_limit`, best lap and total time, then calls `kart_progress_native::encode_progress`. `prototype/osfr-tools/src/kart_entry.rs:682` also encodes every racer's progress through the same codec. The race finishes server-side at `prototype/osfr-tools/src/kart_racing.rs:547-548` (`Phase::Finished` once `laps_completed >= layout.laps`), and `claim_reward` is in `prototype/osfr-tools/src/kart_gateway.rs:723-733`.

**Checked and holding (no change):**

- Subtype-14 layout and offsets (guid 0x00, slot 0x08, laps 0x14, local flag 0x18, lap limit 0x19, best lap 0x21, total 0x25, four trailing u64s, 73 bytes): `prototype/osfr-tools/src/kart_progress_native.rs:5-9, 58-69, 104-124, 201-217`.
- Subtype 1 is one i32 and subtype 12 is one u64: `kart_progress_native.rs:44-56, 259-274`.
- `Finished` is not on the wire and is derived from laps and limit: `kart_progress_native.rs:21-27, 281-297`.
- The `progress_finish` vector hex matches the test fixture: guid `0x4000000001`, laps 3, limit 3, best 58.25, total 179.75, 0x1d 61.5. I recomputed the float bytes (`00007642`, `00006942`, `00c03343`). Matches `prototype/osfr-tools/tests/kart_progress_native.rs:40-69`.
- Client side: `ScriptsBase.lua:37351` (`if finished == 1`), `:37360` (`RaceResults` source), `:48292` (`RaceResultsCol`) all match the note. `FUN_00ce3330` references `0x1a0`, `0x15ec`, `0x161c`, `0x1620` and `0xe60`, consistent with the row-writer description.

**Unsure:**

- The "Owned artifacts" and "Verification" paths under `lab/reports/kart-finish-binding-20261009T154032Z/` (proof.json, vectors.json, trace-kart-finish-binding.py, trace-run.log) and the sha256 values. The `lab/` directory is not present in this repo checkout, so I could not check the files, the hashes, or the reproducer output (`finished_rows: 0`, `progress_frames: 9358`).
- The capture statistics (9,358 frames, 494 non-zero time frames, state sequence 3-9, no subtype 12) cannot be checked without the capture.
- "The finish sequence is not observed in any capture" (Uncertainties) is still accurate for this capture. I did not find a later captured finish in the notes. The Build Ledger's "Native-verified (3 laps, 50 coins and 25 XP paid once)" at `notes/Design/Build Ledger.md:103` suggests a native finish was run later, but it does not say whether the wire frames were captured.
- The Machine-code addresses in "Machine-code confirmation" (`00ba7813`, `00ba7820`, `00ba77c4`, etc.) were not re-verified against the byte-level client data.
