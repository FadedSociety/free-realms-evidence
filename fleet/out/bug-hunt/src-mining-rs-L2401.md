<!-- fleet job=bug-hunt id=src-mining-rs-L2401 status=nothing_found turns=7 usd=0.0047 tokens(read,write,in,out)=[49019, 18804, 16, 3699] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mining.rs lines 2401-2434 of 2434

Reviewed `prototype/osfr-tools/src/mining.rs` lines 2401-2434 (`launch_packet`, `read_i32`, `invalid`, `validate_asset_name`). No defect I can tie to a line.

What I checked:

- **`read_i32` (2411-2413)**: unchecked slice `b[p..p+4]` could panic, but every caller on a client path is length-guarded upstream. `handle` rejects `inner.len() < 15` at mining.rs:576-578 before any `read_i32(inner, 3|7|11)` at 602-614. `decode_payload` rejects `b.len() < 20` at 2341-2343 before `read_i32(b, 15)` at 2344. The only other callers are at 2344 and the 602-614 block. The offsets are constants, so no overflow.
- **`launch_packet` (2401-2409)**: the name length is cast to `i32`, but `movie` is `content.launch_movie`, which `validate_asset_name` caps at 64 bytes at load (mining.rs:321-322). The byte layout matches the sibling `flash_launch_packet` in minigame.rs:708-716 (`26/12`, then `MiniGameFlash` and the movie as i32-length-prefixed strings, then a 0 byte). The movie name comes from the server-side `mining.json` content file, not from the client, so it is not client-controlled.
- **`validate_asset_name` (2421-2434)**: rejects empty, >64 bytes, a leading or trailing `.`, and any byte outside `[A-Za-z0-9_.]`, so no `/` or `\` can appear. The name is never used as a filesystem path in this file (only in packet bodies, mining.rs:627 and 936), so `..` inside a name is harmless. Its doc comment matches the check. It is applied at load (`Type8Engine::load`, mining.rs:321-322) and not on packet input, but the input is trusted server content, so this is not a defect.

Nothing in the window meets the defect criteria.
