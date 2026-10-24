<!-- fleet job=bug-hunt id=src-startup-world-rs-L1 status=nothing_found turns=4 usd=0.0066 tokens(read,write,in,out)=[42768, 28723, 10, 5129] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_world.rs lines 1-800 of 1043

Reviewed `prototype/osfr-tools/src/startup_world.rs` lines 1-800 in full, and checked the callers of the window's public functions. I found no defect I could tie to a line and show to be reachable from a remote client.

What I checked:

- **Reader primitives (lines 56-122):** `take` uses `checked_add` and `slice::get`, so short or overflowing reads return `Err`. The `try_into().unwrap()` calls at lines 79-91 are safe because `take(n)` always returns exactly `n` bytes. `string()` rejects negative lengths before `as usize`. `count()` caps counts at `MAX_ROWS` (100,000).
- **Allocation (lines 191-192, 364-367, 493-502):** `with_capacity` is sized by a count capped at 100,000. Each row consumes at least 4 bytes, so a short packet fails early. The growth is bounded by a constant, not by the attacker.
- **POI parse (lines 288-309):** `payload_length` is checked for sign and then passed through `take`, which bounds it. The row loop consumes at least one byte per iteration, and `finish()` checks for trailing bytes.
- **Writer/reader symmetry:** I compared field order and widths for QuickChatRow, PointOfInterest, the journal tables, WelcomeScreen, Motd, NpcAttachment, and NpcEffectTag (lines 159-174, 230-268, 361-380, 467-549, 703-758). They match.
- **Reach:** the `parse_*` functions are called from `startup_snapshot.rs:504-523`, which reads capture files from disk (`read_capture_inner`), not live client packets. Every failure there is returned as `Err`, not unwrapped. The `build_*` functions take server-side data (capture rows, `quest_engine.rs:1309`), so the `expect` calls in `put_string`/`put_count`/POI build are not reachable with client-controlled lengths.

Not reported: the `(R)` unknown-field semantics, and the up-to-~6 MB `with_capacity` for welcome claim codes, which is a constant bound and not a concrete failure. Lines 801-1043 are outside this window and were not reviewed.
