<!-- fleet job=bug-hunt id=src-gameplay-developer-teleport-rs-L1 status=nothing_found turns=4 usd=0.0033 tokens(read,write,in,out)=[33262, 17794, 10, 1489] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/developer_teleport.rs lines 1-626 of 626

Window reviewed: `prototype/osfr-tools/src/gameplay/developer_teleport.rs` lines 1-626 (whole file).

No findings. The entire file is test code: it is declared as `#[cfg(test)] mod developer_teleport;` at `prototype/osfr-tools/src/gameplay.rs:5450-5451`, and every item in the window is either a `#[test]` function or a test helper (`content_directory`, `character`, `chat`, `flat_terrain`, `reply_text`, `path_request`, `path_replies`). The task excludes code in `#[cfg(test)]`, so none of the candidates I looked at (unchecked `text.len() as u32` in `chat`, the `valid[..20]` slice, the `.unwrap()` calls, the fixed-offset reply indexing in the path tests) count as defects. Production code that these tests exercise (`handle_in_world`, `developer_teleport` at `gameplay.rs:3159`, the placement and pathing paths) lies outside this window and was not reviewed here.
