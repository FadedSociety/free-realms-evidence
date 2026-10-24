<!-- fleet job=bug-hunt id=src-restoration-piece-026-rs-L801 status=nothing_found turns=4 usd=0.0017 tokens(read,write,in,out)=[11444, 5951, 10, 1779] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_026.rs lines 801-820 of 820

Window `prototype/osfr-tools/src/restoration/piece_026.rs` lines 801-820 (the rename retry loop and temp-file cleanup at the end of `atomic_write`, which starts at line 763) contains no defect I can show.

What I checked:
- **Retry loop (801-814):** retries only when `cfg!(windows)` and the raw OS error is 5 or 32, and stops after 20 retries. Every other error returns immediately. The loop cannot run unbounded, and the 25 ms sleep is a fixed bound, not client-driven.
- **Cleanup (816-818):** on any error from the closure, the temporary file is removed. On success the temp file has already been renamed away, so nothing is deleted that should survive. `file` is dropped before the rename (line 799), so the Windows rename is not blocked by an open handle.
- **Reach:** `atomic_write` is called only from `save_stock` (piece_026.rs:727) and `restore_after_failed_housing_write` (piece_026.rs:720). Both pass `self.stock_path`, which is server configuration, and `bytes` from server-side `to_bytes()` of in-memory state. No client packet field reaches the path or the bytes, so there is no client-controlled panic, allocation, or authority issue here.
- **Atomicity at the call sites:** the error from `atomic_write` is mapped to `RollbackFailed` or `PersistStock` and not swallowed. The rollback path at 716-722 is the caller's concern, outside this window.

Only a 500 ms worst-case stall on Windows is possible, which is not a defect under the criteria.
